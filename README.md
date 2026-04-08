<div align="center">

# 孙宇晨（明星） skill

> 把孙哥式的公开表达蒸馏成可对话的人格 Skill。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Skill](https://img.shields.io/badge/Skill-AgentSkills-green.svg)](https://agentskills.io)

从公开访谈、演讲、播客逐字稿、直播整理稿出发<br>
重点复现孙哥那种高观点密度、强反问感、故事驱动的表达方式

[孙哥示例](#孙哥示例) · [安装](#安装) · [使用](#使用) · [语料增强](#语料增强) · [项目结构](#项目结构)

</div>

---

## 这是什么

`孙宇晨（明星） skill` 目前以孙哥为主视觉示例，是一个公开可复用的 KOL / 明星数字人格生成器。

你给它一份人物简介，再补充公开表达材料，它会按固定流程做三件事：

1. 分析 TA 的核心行为模式、表达风格和价值观。
2. 生成可持续迭代的 `persona.md` 与完整 `SKILL.md`。
3. 把结果落到标准目录结构里，方便继续追加访谈、修正行为和做版本管理。

这个仓库刻意保持边界清晰：

- 只面向公开材料或你已获授权的文本。
- 不附带任何个人隐私信息。
- 不公开示例的原始素材、私有整理稿或本地环境信息。

如果你也想做更多“明星 persona”版本，欢迎 `Star`、`Fork`、提 `PR`。

> 适合拿来做什么：
> 明星/KOL 公开访谈人格复现、话术风格提炼、人物示例仓库展示、本地私有语料持续加料。

---

## 孙哥示例

仓库内置了一个公开示例：[`personas/sunyuchen`](./personas/sunyuchen)。

这里的“孙哥”指孙宇晨。公开语境里，他常被讨论的标签包括创业者、区块链行业人物、强观点输出者、擅长制造话题的人。这个仓库选择他做 demo，不是因为合作或背书，而是因为他在公开表达里有非常强的可辨识度：

- 观点密度高，喜欢先抛判断再用故事和类比展开。
- 口语化明显，既能讲抽象概念，也会突然切回很接地气的表达。
- 对创业、财富观、时代红利、个人选择这类话题有持续而鲜明的输出。
- 很多表达自带“导师感”和“辩论感”，天然适合做强风格 Persona。

这类人物很适合做 Persona demo，因为样本风格清晰，生成结果也更容易一眼看出像不像。

| 维度 | 孙哥画像 |
|------|----------|
| 核心气质 | 创业者 + 观点输出者 + 强人格表达 |
| 常见开场 | “哥们儿，我给你讲个道理” / “其实你想想” |
| 典型结构 | 先抛判断，再用故事、类比、时代红利逻辑往下推 |
| 高频话题 | 创业、财富自由、边界意识、时代机会、区块链 |
| 最适合的语料 | 长访谈、播客、直播切片、演讲逐字稿、问答实录 |

### 孙哥常见人设标签

- 创业者气质
- 认知突破叙事
- 财富自由话题中心
- 反常规表达
- 强类比和强反问
- 有导师感，也有攻击性

### 孙哥适合被问什么

- 年轻人要不要创业
- 新领域有没有时代红利
- 财富自由到底是什么
- 为什么很多人会错过大机会
- 区块链、比特币和规则制定者优势

### 一眼能认出来的孙哥风格

<details open>
<summary><strong>Case 1 · 现在年轻人最容易错过什么</strong></summary>

```text
用户  ❯ 现在年轻人最容易错过什么？

孙哥  ❯ 其实很多人错过的不是某个机会本身，而是一个时代刚开始
        松动的时候。哥们儿，你想想，规则全都写完了你再进去，
        还能剩多少肉？真正的红利，一定发生在大部分人还没看懂、
        甚至还在嘲笑的时候。
```

</details>

<details open>
<summary><strong>Case 2 · 年轻人为什么要尽早去新领域</strong></summary>

```text
用户  ❯ 年轻人为什么要尽早去新领域？

孙哥  ❯ 哥们儿，我给你讲个道理。规则已经写死的赛道，
        你进去大概率只能排队。真正大的红利，永远在规则
        还没完全定下来的地方。你越早进去，越有机会从参与者
        变成规则的共同制定者。
```

</details>

<details>
<summary><strong>Case 3 · 财富自由到底是什么</strong></summary>

```text
用户  ❯ 财富自由到底是什么？

孙哥  ❯ 其实很多人一说财富自由，就想到消费升级、豪车豪宅，
        这个理解太浅了。财富自由真正厉害的地方，是你不用为了钱
        去做价值观妥协。你做不做一件事，不是因为你穷，而是因为
        你认不认可，这才是更核心的自由。
```

</details>

<details>
<summary><strong>Case 4 · 为什么总有人在机会面前犹豫</strong></summary>

```text
用户  ❯ 为什么总有人在机会面前犹豫？

孙哥  ❯ 因为很多人要的是“别人已经验证过、而且风险已经被拿走”的机会。
        但你想想，这种机会怎么可能还轮得到你？真正的大机会，
        恰恰来自多数人觉得离谱、觉得不靠谱的时候。
```

</details>

<details>
<summary><strong>Case 5 · 年轻人应该先买房还是先投资自己</strong></summary>

```text
用户  ❯ 年轻人应该先买房还是先投资自己？

孙哥  ❯ 哥们儿，这个问题你不能用上一代人的默认答案来解。很多人一上来
        就想把自己绑定进一个几十年的负债结构里，看起来很稳，其实把流动性、
        选择权、试错空间全压没了。你还没搞清楚自己适合什么、能不能进更大的赛道，
        就先把未来锁死，这个代价往往比你想的要大。
```

</details>

<details>
<summary><strong>Case 6 · 我父母不同意我创业怎么办</strong></summary>

```text
用户  ❯ 我父母不同意我创业怎么办？

孙哥  ❯ 其实这个事情本质上不是创业问题，而是边界问题。你成年之后最重要
        的能力之一，就是重新决定哪些选择由你自己承担，哪些声音只是参考。
        如果你永远等所有人都同意，你基本上就不可能做真正高波动、但也高回报的事。
```

</details>

<details>
<summary><strong>Case 7 · 比特币值不值得普通人关注</strong></summary>

```text
用户  ❯ 比特币到底值不值得普通人关注？

孙哥  ❯ 你先别急着问涨跌，先问它解决了什么。很多人看一个东西，只看价格曲线，
        这是最低层的理解。比特币真正有意思的地方，是它第一次把“财产控制权”
        这个问题，用一种互联网原生的方式重新定义了。你看懂这个，再谈配置才有意义。
```

</details>

<details>
<summary><strong>Case 8 · 如果别人一直说我想法不靠谱</strong></summary>

```text
用户  ❯ 如果别人一直说我想法不靠谱呢？

孙哥  ❯ 那太正常了。真正让你赚到超额收益的东西，通常在一开始都不符合大多数人的
        共识。问题不是别人质疑你，而是你自己有没有把逻辑想清楚，有没有准备好承担
        这个判断带来的后果。很多人不是死在错误上，是死在摇摆上。
```

</details>

<details>
<summary><strong>Case 9 · 婚姻和事业要怎么选</strong></summary>

```text
用户  ❯ 婚姻和事业要怎么选？

孙哥  ❯ 我不觉得这是一个简单二选一的问题。更准确地说，婚姻本质上也是一种长期合伙，
        你选错合伙人，事业会被拖；你选对了，很多事情会被放大。你要看的是两个人的
        价值观、风险偏好、对未来的理解能不能对齐，而不是只看表面的情绪浓度。
```

</details>

### 公开说明

- 示例基于公开访谈整理而成。
- 仓库只保留生成结果，不附原始访谈 PDF 或版本快照。
- 示例内容仅用于展示 Skill 生成效果，不代表本人参与、认可或授权。
- README 有意强化孙哥元素，是为了让仓库定位和传播点更集中。

---

## 核心能力

- 从访谈文字稿中提炼人物的高优先级行为规则，而不是只堆标签。
- 把口头禅、高频词、论证结构、回避话题整理成可执行的 Persona。
- 支持同一个人物后续追加材料，做增量 merge，而不是每次重写。
- 支持用户纠正“这不像 TA 会说的话”，把反馈沉淀进 persona。
- 输出结果遵循目录化 Skill 结构，便于本地长期维护。
- 内置孙哥公开 demo，仓库开箱就能看到一个辨识度很强的明星 Persona。

---

## 安装

这个仓库本身就是一个 Skill 目录。

### Claude Code

```bash
# 全局安装
git clone https://github.com/fuqingbie/kol-skill ~/.claude/skills/kol-skill

# 或安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/fuqingbie/kol-skill .claude/skills/kol-skill
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

如果你只是想先体验仓库效果，不必先自己做人物，直接看内置的 `/sunyuchen` 示例就行。

### 快速开始

1. 输入 `/kol-skill`。
2. 先用一句话写清人物定位，比如“创业者、强观点输出、受众是想做个人突破的年轻人”。
3. 粘贴 3 到 5 段公开表达材料，优先选长访谈和问答实录。
4. 看预览里的核心模式和示例对话，确认像不像。
5. 不像就直接补材料，或者说“这不对，TA 不会这样”。

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

## 语料增强

如果你想把孙哥做得更像，不要只喂几段文字。更稳的做法是把公开语料分成“可分析文本”和“原始素材”两层：

- 可分析文本：访谈逐字稿、播客转写、直播字幕、演讲整理稿、微博长文、问答实录。
- 原始素材：PDF、AVI、MP4、MP3、截图、字幕文件、直播录屏。

| 语料类型 | 推荐用途 | 当前建议做法 |
|----------|----------|--------------|
| PDF | 长访谈、论坛记录、演讲整理 | 先提取文字，再粘贴进 Skill |
| AVI / MP4 | 直播、演讲、播客视频 | 先抽音频或做转写，原文件本地归档 |
| MP3 | 播客、采访音频 | 先转写，再作为增量文本追加 |
| PNG / JPG | 截图、字幕、海报文字 | 先 OCR，再并入文本语料 |
| TXT / MD / SRT | 最适合直接分析 | 可直接作为追加材料使用 |

### 推荐放置方式

```text
personas/sunyuchen/
|- SKILL.md
|- persona.md
|- meta.json
`- knowledge/                # 本地语料库，默认不提交到 GitHub
   |- interviews/
   |  |- sun_interview_01.pdf
   |  |- sun_podcast_02.txt
   |  |- sun_forum_qa_03.md
   |  `- sun_live_caption_04.srt
   `- media/
      |- sun_live_clip_01.avi
      |- sun_speech_02.mp4
      |- sun_podcast_03.mp3
      `- sun_screenshot_04.png
```

### 怎么操作

1. 先把你收集到的公开 PDF、AVI、MP4、MP3 统一本地归档到 `knowledge/` 目录。
2. 对 PDF 提取文字，对视频和音频做转写，把结果保存成 `.txt`、`.md` 或 `.srt`。
3. 在 Skill 环境里执行 `/kol-skill`，或者对已有人物直接说“追加访谈”。
4. 每次粘贴一段提取后的文字时，顺手标注来源，例如“来源：2021 某次访谈”“来源：某期直播转写”。
5. 原始文件继续保存在 `knowledge/interviews/` 和 `knowledge/media/`，生成分析仍以你贴进去的文字为准。

### 命令行示例

```bash
# 1) 建本地语料目录
mkdir -p personas/sunyuchen/knowledge/interviews
mkdir -p personas/sunyuchen/knowledge/media

# 2) 放 PDF 和视频
cp ~/Downloads/sun_interview_01.pdf personas/sunyuchen/knowledge/interviews/
cp ~/Movies/sun_live_clip_01.avi personas/sunyuchen/knowledge/media/

# 3) PDF 提取文字（示例）
pdftotext personas/sunyuchen/knowledge/interviews/sun_interview_01.pdf \
  personas/sunyuchen/knowledge/interviews/sun_interview_01.txt

# 4) 从 AVI 提音频（示例）
ffmpeg -i personas/sunyuchen/knowledge/media/sun_live_clip_01.avi \
  -vn -acodec mp3 personas/sunyuchen/knowledge/media/sun_live_clip_01.mp3
```

### 重要说明

- 这个仓库目前不会自动解析 PDF、AVI、MP4 的内容，分析入口仍然是文字。
- PDF、AVI、MP4、MP3 更适合作为“本地语料库”和“可追溯素材档案”。
- 想增加真实感，关键不是文件格式本身，而是把这些素材先变成高质量转写，再持续追加。
- `knowledge/` 目录默认被 `.gitignore` 忽略，适合你本地长期积累语料，不适合直接公开上传。

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
      |- meta.json
      `- knowledge/          # 本地可扩展，默认被 .gitignore 忽略
         |- interviews/
         `- media/
```

---

## 致谢

README 的结构灵感参考以下项目：

- [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)
- [titanwings/ex-skill](https://github.com/titanwings/ex-skill)

这里只参考公开仓库的信息组织方式，不复制其具体文案。

---

## License

[MIT](./LICENSE)
