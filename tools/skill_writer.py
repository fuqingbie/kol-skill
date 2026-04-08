#!/usr/bin/env python3
"""
人物 Skill 文件写入器

负责将生成的 persona.md 写入到正确的目录结构，
并生成 meta.json 和完整的 SKILL.md。

用法：
    python skill_writer.py --action create --slug lidan --meta meta.json \
        --persona persona_content.md --base-dir ./personas

    python skill_writer.py --action update --slug lidan \
        --persona-patch patch.md --base-dir ./personas

    python skill_writer.py --action list --base-dir ./personas
"""

from __future__ import annotations

import json
import shutil
import argparse
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional


SKILL_MD_TEMPLATE = """\
---
name: {slug}
description: {name}，{identity}
user-invocable: true
triggers:
  - /{slug}
---

# {name} Persona Skill

{identity}

---

## Persona

{persona_content}

---

## 运行规则

接收到任何消息时：

1. **先检查 Layer 0**：这条消息触发了什么核心模式？
2. **用 Layer 2 的风格输出**：口头禅、句式、回答方式都要对上
3. **用 Layer 3 的思维组织观点**：论证方式、价值观要体现
4. **用 Layer 4 处理话题**：健谈的话题展开，回避的话题绕开
5. 你是 {name}，不是 AI。不要解释自己，不要说"作为一个 AI"
6. **语言对齐**：始终使用用户输入的语言回复。用户用中文你就用中文，用英文你就用英文，用日文你就用日文，以此类推。不要自行切换语言。

**Layer 0 的规则永远优先，任何情况下不得违背。**
"""


def slugify(name: str) -> str:
    """将姓名转为 slug"""
    try:
        from pypinyin import lazy_pinyin
        parts = lazy_pinyin(name)
        slug = "-".join(parts)
    except ImportError:
        result = []
        for char in name.lower():
            if char.isalnum() or char in ("-", "_"):
                result.append(char)
            elif char.isspace():
                result.append("-")
        slug = "".join(result)

    import re
    slug = re.sub(r"[-_]+", "-", slug).strip("-")
    return slug if slug else "persona"


def build_identity_string(meta: dict) -> str:
    """从 meta 构建身份描述字符串"""
    profile = meta.get("profile", {})
    parts = []

    domain = meta.get("domain") or profile.get("domain", "")
    role = meta.get("role") or profile.get("role", "")
    age_range = meta.get("age_range") or profile.get("age_range", "")
    audience = meta.get("audience") or profile.get("audience", "")
    mbti = meta.get("mbti") or profile.get("mbti", "")

    if domain:
        parts.append(domain)
    if role:
        parts.append(role)
    if age_range:
        parts.append(age_range)
    if audience:
        parts.append(f"受众：{audience}")
    if mbti:
        parts.append(f"MBTI {mbti}")

    return "，".join(parts) if parts else "人物"


def create_persona_skill(
    base_dir: Path,
    slug: str,
    meta: dict,
    persona_content: str,
) -> Path:
    """创建新的人物 Skill 目录结构"""

    skill_dir = base_dir / slug
    skill_dir.mkdir(parents=True, exist_ok=True)

    # 创建子目录
    (skill_dir / "versions").mkdir(exist_ok=True)
    (skill_dir / "knowledge" / "interviews").mkdir(parents=True, exist_ok=True)
    (skill_dir / "knowledge" / "media").mkdir(parents=True, exist_ok=True)

    # 写入 persona.md
    (skill_dir / "persona.md").write_text(persona_content, encoding="utf-8")

    # 生成并写入 SKILL.md
    name = meta.get("name", slug)
    identity = build_identity_string(meta)

    skill_md = SKILL_MD_TEMPLATE.format(
        slug=slug,
        name=name,
        identity=identity,
        persona_content=persona_content,
    )
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    # 写入 meta.json
    now = datetime.now(timezone.utc).isoformat()
    meta["slug"] = slug
    meta.setdefault("created_at", now)
    meta["updated_at"] = now
    meta["version"] = "v1"
    meta.setdefault("corrections_count", 0)
    meta.setdefault("interview_word_count", 0)

    (skill_dir / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return skill_dir


def update_persona_skill(
    skill_dir: Path,
    persona_patch: Optional[str] = None,
    correction: Optional[dict] = None,
    new_word_count: int = 0,
) -> str:
    """更新现有 Skill，先存档当前版本，再写入更新"""

    meta_path = skill_dir / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    current_version = meta.get("version", "v1")
    try:
        version_num = int(current_version.lstrip("v").split("_")[0]) + 1
    except ValueError:
        version_num = 2
    new_version = f"v{version_num}"

    # 存档当前版本
    version_dir = skill_dir / "versions" / current_version
    version_dir.mkdir(parents=True, exist_ok=True)
    for fname in ("SKILL.md", "persona.md"):
        src = skill_dir / fname
        if src.exists():
            shutil.copy2(src, version_dir / fname)

    # 应用 persona patch 或 correction
    if persona_patch or correction:
        current_persona = (skill_dir / "persona.md").read_text(encoding="utf-8")

        if correction:
            correction_line = (
                f"\n- [{correction.get('scene', '通用')}] "
                f"错误：{correction['wrong']}；"
                f"正确：{correction['correct']}\n"
                f"  来源：用户纠正，{datetime.now().strftime('%Y-%m-%d')}"
            )
            target = "## Correction 记录"
            if target in current_persona:
                insert_pos = current_persona.index(target) + len(target)
                rest = current_persona[insert_pos:]
                skip = "\n\n（暂无记录）"
                if rest.startswith(skip):
                    rest = rest[len(skip):]
                new_persona = current_persona[:insert_pos] + correction_line + rest
            else:
                new_persona = (
                    current_persona
                    + f"\n\n## Correction 记录\n{correction_line}\n"
                )
            meta["corrections_count"] = meta.get("corrections_count", 0) + 1
        else:
            new_persona = current_persona + "\n\n" + persona_patch

        (skill_dir / "persona.md").write_text(new_persona, encoding="utf-8")

    # 更新访谈字数
    if new_word_count:
        meta["interview_word_count"] = meta.get("interview_word_count", 0) + new_word_count

    # 重新生成 SKILL.md
    persona_content = (skill_dir / "persona.md").read_text(encoding="utf-8")
    name = meta.get("name", skill_dir.name)
    identity = build_identity_string(meta)

    skill_md = SKILL_MD_TEMPLATE.format(
        slug=skill_dir.name,
        name=name,
        identity=identity,
        persona_content=persona_content,
    )
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    # 更新 meta
    meta["version"] = new_version
    meta["updated_at"] = datetime.now(timezone.utc).isoformat()
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    return new_version


def list_personas(base_dir: Path) -> list:
    """列出所有已创建的人物 Skill"""
    personas = []

    if not base_dir.exists():
        return personas

    for skill_dir in sorted(base_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        meta_path = skill_dir / "meta.json"
        if not meta_path.exists():
            continue

        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception:
            continue

        personas.append({
            "slug": meta.get("slug", skill_dir.name),
            "name": meta.get("name", skill_dir.name),
            "identity": build_identity_string(meta),
            "version": meta.get("version", "v1"),
            "updated_at": meta.get("updated_at", ""),
            "corrections_count": meta.get("corrections_count", 0),
            "interview_word_count": meta.get("interview_word_count", 0),
        })

    return personas


def main() -> None:
    parser = argparse.ArgumentParser(description="人物 Skill 文件写入器")
    parser.add_argument("--action", required=True, choices=["create", "update", "list"])
    parser.add_argument("--slug", help="人物 slug（用于目录名）")
    parser.add_argument("--name", help="人物称呼")
    parser.add_argument("--meta", help="meta.json 文件路径")
    parser.add_argument("--persona", help="persona.md 内容文件路径")
    parser.add_argument("--persona-patch", help="persona.md 增量更新内容文件路径")
    parser.add_argument(
        "--base-dir",
        default="./personas",
        help="人物 Skill 根目录（默认：./personas）",
    )

    args = parser.parse_args()
    base_dir = Path(args.base_dir).expanduser()

    if args.action == "list":
        personas = list_personas(base_dir)
        if not personas:
            print("暂无已创建的人物 Skill")
        else:
            print(f"已创建 {len(personas)} 个人物 Skill：\n")
            for p in personas:
                updated = p["updated_at"][:10] if p["updated_at"] else "未知"
                print(f"  [{p['slug']}]  {p['name']} — {p['identity']}")
                print(f"    版本: {p['version']}  访谈字数: {p['interview_word_count']}  纠正次数: {p['corrections_count']}  更新: {updated}")
                print()

    elif args.action == "create":
        if not args.slug and not args.name:
            print("错误：create 操作需要 --slug 或 --name", file=sys.stderr)
            sys.exit(1)

        meta: dict = {}
        if args.meta:
            meta = json.loads(Path(args.meta).read_text(encoding="utf-8"))
        if args.name:
            meta["name"] = args.name

        slug = args.slug or slugify(meta.get("name", "persona"))

        persona_content = ""
        if args.persona:
            persona_content = Path(args.persona).read_text(encoding="utf-8")

        skill_dir = create_persona_skill(base_dir, slug, meta, persona_content)
        print(f"✅ Skill 已创建：{skill_dir}")
        print(f"   触发词：/{slug}")

    elif args.action == "update":
        if not args.slug:
            print("错误：update 操作需要 --slug", file=sys.stderr)
            sys.exit(1)

        skill_dir = base_dir / args.slug
        if not skill_dir.exists():
            print(f"错误：找不到 Skill 目录 {skill_dir}", file=sys.stderr)
            sys.exit(1)

        persona_patch = Path(args.persona_patch).read_text(encoding="utf-8") if args.persona_patch else None
        new_version = update_persona_skill(skill_dir, persona_patch)
        print(f"✅ Skill 已更新到 {new_version}：{skill_dir}")


if __name__ == "__main__":
    main()
