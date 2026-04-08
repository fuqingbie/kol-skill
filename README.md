<div align="center">

# 明星 skill

> 把公开表达蒸馏成可对话的人格 Skill。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Skill](https://img.shields.io/badge/Skill-AgentSkills-green.svg)](https://agentskills.io)

从公开访谈、演讲、播客逐字稿、直播整理稿出发<br>
生成一个能复现语气、观点、论证方式和互动边界的 KOL / 明星数字人格

[安装](#安装) · [使用](#使用) · [孙哥示例](#孙哥示例) · [项目结构](#项目结构) · [开源边界](#开源边界)

</div>

---

## 这是什么

`明星 skill` 是一个公开可复用的 KOL / 明星数字人格生成器。

你给它一份人物简介，再补充公开表达材料，它会按固定流程做三件事：

1. 分析 TA 的核心行为模式、表达风格和价值观。
2. 生成可持续迭代的 `persona.md` 与完整 `SKILL.md`。
3. 把结果落到标准目录结构里，方便继续追加访谈、修正行为和做版本管理。

这个仓库刻意保持边界清晰：

- 只面向公开材料或你已获授权的文本。
- 不附带任何个人隐私信息。
- 不公开示例的原始素材、私有整理稿或本地环境信息。

如果你想看更多示例，欢迎 `Star`、`Fork`、提 `PR`。

---

## 核心能力

- 从访谈文字稿中提炼人物的高优先级行为规则，而不是只堆标签。
- 把口头禅、高频词、论证结构、回避话题整理成可执行的 Persona。
- 支持同一个人物后续追加材料，做增量 merge，而不是每次重写。
- 支持用户纠正“这不像 TA 会说的话”，把反馈沉淀进 persona。
- 输出结果遵循目录化 Skill 结构，便于本地长期维护。

---

## 安装

这个仓库本身就是一个 Skill 目录。

### Claude Code

```bash
# 全局安装
git clone https://github.com/<your-github-username>/kol-skill ~/.claude/skills/kol-skill

# 或安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/<your-github-username>/kol-skill .claude/skills/kol-skill
```

### 依赖

脚本默认使用 Python 标准库即可运行。

如果你想让中文名转 slug 更稳定，可以额外安装：

```bash
pip3 install pypinyin
```

---

## 使用

在支持 Skill 的环境中输入：

```text
/kol-skill
```

然后按流程提供：

- 人物称呼或代号
- 身份定位
- MBTI 或性格框架
- 公众形象标签
- 回避边界
- 公开访谈或其他公开表达材料

生成完成后，可以直接使用 `/{slug}` 与对应人物对话。

### 常用命令

| 命令 | 作用 |
|------|------|
| `/kol-skill` | 创建一个新的明星 / KOL Persona |
| `/list-personas` | 查看已创建的人物列表 |
| `/{slug}` | 调用某个人物的完整 Skill |
| 说“追加访谈” | 追加新的公开材料并增量更新 |
| 说“这不对，TA 不会这样” | 对输出做纠正并写入 Correction 层 |
| 说“查看版本历史” | 查看版本记录 |
| 说“回滚到 v2” | 回滚到指定版本 |

---

## 孙哥示例

仓库内置了一个公开示例：[`personas/sunyuchen`](./personas/sunyuchen)。

这里的“孙哥”指孙宇晨。之所以选他做演示，不是因为合作或背书，而是因为他在公开表达里有非常强的可辨识度：

- 观点密度高，喜欢先抛判断再用故事和类比展开。
- 口语化明显，既能讲抽象概念，也会突然切回很接地气的表达。
- 对创业、财富观、时代红利、个人选择这类话题有持续而鲜明的输出。

这类人物很适合做 Persona demo，因为样本风格清晰，生成结果也更容易一眼看出像不像。

### 示例风格

```text
用户  ❯ 年轻人为什么要尽早去新领域？

孙哥  ❯ 哥们儿，我给你讲个道理。规则已经写死的赛道，
        你进去大概率只能排队。真正大的红利，永远在规则
        还没完全定下来的地方。你越早进去，越有机会从参与者
        变成规则的共同制定者。
```

### 公开说明

- 示例基于公开访谈整理而成。
- 仓库只保留生成结果，不附原始访谈 PDF 或版本快照。
- 示例内容仅用于展示 Skill 生成效果，不代表本人参与、认可或授权。

---

## 项目结构

```text
kol-skill/
|- SKILL.md
|- README.md
|- prompts/
|  |- intake.md
|  |- interview_analyzer.md
|  |- persona_analyzer.md
|  |- persona_builder.md
|  |- merger.md
|  `- correction_handler.md
|- tools/
|  |- skill_writer.py
|  `- version_manager.py
`- personas/
   `- sunyuchen/
      |- SKILL.md
      |- persona.md
      `- meta.json
```

---

## 开源边界

公开仓库默认只包含：

- 生成逻辑
- Prompt 模板
- Python 工具脚本
- 一个公开 demo 的结果文件

以下内容不应进入公开仓库：

- 原始访谈 PDF、录音转写、截图、媒体素材
- 本地版本快照
- 绝对路径、系统垃圾文件、私人账号信息
- 未获授权的私有聊天记录或整理材料

仓库已经通过 `.gitignore` 默认忽略这些内容。

---

## 致谢

README 的结构灵感参考以下项目：

- [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)
- [titanwings/ex-skill](https://github.com/titanwings/ex-skill)

这里只参考公开仓库的信息组织方式，不复制其具体文案。

---

## License

[MIT](./LICENSE)
