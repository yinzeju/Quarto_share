# Quarto 科研出版流程、技能与模板

本仓库整理了论文、科研汇报和周报的制作规则：先建立可追溯的证据与推导，再组织可编辑源稿，最后渲染、检查和交付。包含 `quarto-paper`、`quarto-report` 与 `weekly-report` 三套技能，以及可以直接渲染的论文和周报模板。

仓库地址：[yinzeju/Quarto_share](https://github.com/yinzeju/Quarto_share)。

## 从哪里开始

| 需要 | 入口 |
|---|---|
| 理解完整制作流程与质量标准 | [科研汇报流程与规则](docs/workflow.md) |
| 代理自动遵循的工作区规则 | [AGENTS.md](AGENTS.md) |
| 科研说明、汇报、Quarto 幻灯片、可编辑 PPTX | [quarto-report](.agents/skills/quarto-report/SKILL.md) |
| 周报的内容规划与连续推导 | [weekly-report](.agents/skills/weekly-report/SKILL.md) |
| 论文写作、期刊适配和 LaTeX/PDF 交付 | [quarto-paper](.agents/skills/quarto-paper/SKILL.md) |
| 查看内置的 Core 符号约定 | [Notation Core](.agents/skills/quarto-report/references/notation-core.md) |

## 包含什么

```text
Quarto_share/
├── README.md
├── AGENTS.md                     # 可复用的英文代理规则
├── .gitignore
├── .gitattributes                # 文本统一使用 LF
├── .agents/skills/
│   ├── quarto-report/            # 汇报制作规则与输出分支
│   ├── weekly-report/            # 复用 quarto-report，需一起保留
│   └── quarto-paper/             # 论文写作、期刊与源稿交付
├── Paper/Template/               # 复制作者现有的完整论文测试例
├── Report/Weekly/Template/       # 13 页周报、完整说明、GIF、图片、数据和脚本
└── docs/workflow.md              # 中文流程与质量要求
```

技能保留英文规则，科研汇报默认中文，论文语言跟随用户与目标期刊。作者原有的汇报偏好已直接写入技能：

| 项目 | 内置规则 |
|---|---|
| 制作顺序 | 先写详细汇报说明，再制作并同步 slides |
| 数学 | 使用作者的 Core 符号约定，保留可编辑 LaTeX 与必要的完整推导 |
| 视觉 | 浅色 16:9，蓝色/青色强调，清晰中文无衬线字体 |
| 引用 | 内容页左下角，作者、年份、期刊或真实载体、题目，每条独占一行 |
| 实验 | 真实数据表格与原图优先，明确指标、单位和比较条件 |
| 交付 | 保留源稿和使用的资源，渲染并检查版面，列出实际缺口 |

Core 原文已随 `quarto-report` 放在同一个技能目录内，使用时自动读取，不需要访问作者的笔记仓库或设置符号文件路径。

## 先看两个完整模板

| 分类目录 | 模板 | 具体内容 |
|---|---|---|
| [Paper](Paper/README.md) | [Paper/Template](Paper/Template/README.md) | 直接复制作者的 CMAME / Elsevier 管线测试：完整论文、真实背景文献、制造解数据、图表、期刊扩展与独立 LaTeX 编译脚本 |
| [Report/Weekly](Report/Weekly/README.md) | [Report/Weekly/Template](Report/Weekly/Template/README.md) | 参考作者 20261029 周报的表达方式；精确 DMD 的 13 页连续推导、完整说明、实际生成的合成数据、GIF、双图与三图排版 |

两个模板都附带已有的图表与数据，普通渲染不重新计算实验。论文模板保留虚构作者与合成测试标记；周报数字来自教学振子程序，不是作者真实实验。AI 应学习它们的组织与论证方式，用真实材料替换科学内容。

从仓库根目录可以直接运行：

```powershell
quarto render Paper/Template/manuscript.qmd --to html --no-execute
quarto render Report/Weekly/Template --no-execute
```

也可进入具体模板目录执行 `quarto preview`。进一步的期刊 PDF、数值重算和 LaTeX 验证命令写在各模板 README 中。

## 三步开始

克隆仓库：

```powershell
git clone https://github.com/yinzeju/Quarto_share.git
cd Quarto_share
```

1. 用 Codex 打开仓库根目录。保留 `.agents/skills/` 与 `AGENTS.md`；三套技能保持相邻。
2. 提供真实的笔记、论文 PDF/Markdown、实验报告或图表，可以放到工作区任意目录，也可以在任务中直接给出实际文件位置。
3. 让 AI 先读取相应模板，或复制下方完整任务，把主题、路径、日期和时长替换为自己的信息。代理按内置规则在 `Paper/` 或 `Report/` 中建立或修订项目。

本包采用 `.agents/skills/` 作为项目技能目录，这是当前 Codex 的本地技能发现位置；技能既可显式调用，也可按描述自动匹配。如果新技能未出现，可重启 Codex。[官方技能说明](https://learn.chatgpt.com/docs/build-skills)（核对日期：2026-11-12）。

分类目录组织与作者工作区一致；每个具体模板或项目都有自己的渲染入口：

```text
workspace/
├── AGENTS.md
├── .agents/skills/
├── materials/                    # 用户提供的材料，也可使用其他位置
├── Paper/
│   ├── Template/
│   └── Topic/                    # 按需复制模板后创建
└── Report/
    ├── Topic/
    └── Weekly/
        ├── Template/
        └── YYYYMMDD/             # 按需创建的新周报
```

有现成项目时保留原结构。默认从仓库根目录分派任务，代理在具体汇报目录内预览和渲染。Git 提交和推送按用户在实际会话中的授权处理。

实际构建需要安装 [Quarto](https://quarto.org/docs/get-started/)。HTML 使用 Quarto；LaTeX PDF 还需适配项目的 TeX 环境；执行代码时再配置对应的 Python、R 或 Julia 环境。PPTX 制作、浏览器和 PDF 页面检查工具由接收者自己的环境提供。

## 使用示例：从材料到成果

以下主题、文件名、日期和页数用于演示怎样提出任务，示例路径中的材料需由使用者提供。使用前把路径和需求替换为自己的真实信息。示例中的所有路径都相对于工作区根目录。

### 1. 准备材料并制作一次方法汇报

假设要向课题组介绍动态模态分解（DMD），并结合自己的振动系统实验。下面是一种材料摆放方式；也可以保持自己的目录，在任务中直接给出文件位置：

```text
sources/
├── notes/dmd-notes.md                     # 阅读笔记与希望重点解释的内容
├── literature/dmd/
│   ├── paper.pdf                         # 真实论文原文
│   └── paper.md                          # 同一论文的文本或 MinerU 导出
└── experiments/vibration/
    ├── report.md                         # 实验设置、指标定义、真实结论
    ├── metrics.csv                       # 已生成的定量结果
    └── figures/                          # 原始实验图
```

从工作区根目录打开 Codex，粘贴完整任务：

```text
使用 $quarto-report，制作一次面向课题组的中文方法汇报。

主题：动态模态分解（DMD）的方法与振动系统实验。
时长：20 分钟，约 12–16 页，使用浅色 16:9 布局。
目标项目：Report/DMD-method/。如该目录已有内容，先检查并沿用项目结构。

资料：
- 笔记：sources/notes/dmd-notes.md
- 论文：sources/literature/dmd/paper.pdf 和 paper.md
- 实验报告：sources/experiments/vibration/report.md
- 结果数据：sources/experiments/vibration/metrics.csv
- 实验图：sources/experiments/vibration/figures/

内容安排：
- 先讲研究问题和数据形式，再按论文与笔记说明方法的构造和推导。
- 精讲所需的假设、矩阵维度、关键中间步骤和结果用途。
- 用实验报告中已有的表格与原图展示证据，说明比较条件、指标和局限。
- 最后总结适用条件及仍需验证的问题。

先在项目中完成 汇报说明.qmd，写出总体主线、章节安排、材料清单，
以及每页内容、完整相关推导、图表来源和文献引用；随后制作 slides.qmd。
两份源稿保持一致，详细推导保留在说明中，投影内容按时长取舍。
引用按真实文献核对，每条在内容页左下角独占一行。
复用已有实验输出；缺少数据或证据时标记 TODO，不编造结果。

交付：详细汇报说明的 QMD 与 HTML、Reveal.js 幻灯片的 QMD 与 HTML，
以及实际使用的参考文献和图表资源。设置 slides.qmd 为默认演示目标，
使项目内运行 quarto preview 时打开幻灯片。
渲染后检查公式、逐页引用、资源链接和版面，报告实际输出位置及未完成项。
```

完成后应能在 `Report/DMD-method/` 中找到两份源稿、项目配置、文献和使用的图表。生成的 HTML 位置以项目配置和代理的实际交付说明为准。可以进入该项目再次预览：

```powershell
cd Report/DMD-method
quarto preview
```

### 2. 制作有文献、近期工作和实验的周报

下面以报告日 `2026-11-20` 为例。把具体材料范围、精讲对象和已完成工作写清楚，避免代理从整座资料库任意选题：

```text
使用 $weekly-report，制作 2026-11-20 的中文科研周报。
项目位置：Report/Weekly/20261120/；若同日已有报告，保留原项目，
为本次新报告选择独立的描述性子项目，不覆盖旧内容。
听众为课题组，汇报约 25 分钟、15–18 页。

读取以下真实材料：
- 本周工作笔记：sources/notes/weekly-20261120.md
- 精讲论文：sources/literature/main-paper/ 下对应的 PDF 和 Markdown
- 两篇相关方法：sources/literature/related-a/ 与 sources/literature/related-b/
- 本周实验：sources/experiments/week-20261120/report.md 及其结果图表

内容顺序：
1. 核心论文精讲：围绕本周工作需要的计算链展开，交代起点、构造、
   中间结果及其下一步用途，每个新符号和矩阵在首次使用时定义。
2. 相关方法概讲：分别说明问题、思想、工具、流程和输出，
   再比较三篇论文的创新、假设、证据局限及与当前工作的关系。
3. 本周工作：只讲笔记中已完成的内容，区分观察、解释和待验证想法。
4. 实验：用已有表格和原图展示，给出数据划分、预测时长、指标与单位，
   结论只覆盖当前比较条件。
5. 下一步：每项对应一个实际缺口、拟做动作和检验目标。

先写完整 汇报说明.qmd，再制作 slides.qmd，交付两者的源稿与 HTML。
长推导保持正常字号，必要时用整页垂直滚动。
完成渲染和版面检查后，更新 Report/Weekly/README.md：
写入日期、主题、实际内容摘要，以及能打开的相对项目链接。
资料不足的章节保留明确缺口，不把计划写成已完成结果。
```

### 3. 只修订现有汇报中的推导和实验页

已有报告不必每次重建。用页标题或内容定位需要修改的部分，并说明应同步的成果：

```text
使用 $quarto-report，修订 Report/DMD-method/ 中的现有汇报。
先读取项目 README、_quarto.yml、汇报说明.qmd、slides.qmd 和已有输出。

本次只修改两部分：
- “方法构造”相关页面：依据 sources/notes/dmd-notes-v2.md 补齐目前省略的
  中间推导，说明新矩阵如何得到、维度是什么、下一步用在哪里。
- “实验比较”页面：采用 sources/experiments/vibration-v2/report.md
  及其 metrics.csv 和 figures/ 中的已生成结果，保持原指标定义。

保留其他章节的顺序和现有主题，必要时为受影响内容增加页面。
同步更新详细汇报说明、对应的 slides、文献和图表资源。
如果新旧结果的比较条件不一致，说明原因，不直接写成性能提升。
重新渲染受影响输出，检查页序、引用、公式和图表；
最后简要列出修改内容、实际交付文件和仍缺的证据。
```

### 4. 需要可编辑 PPTX，或暂时只写说明

直接 PPTX 示例明确指定公式表示与原图处理方式，便于接收者判断是否适合自己的使用习惯：

```text
使用 $quarto-report，依据 Report/DMD-method/ 的详细汇报说明和真实图表，
制作 Report/DMD-method/dmd-talk.pptx，约 10 页、15 分钟、中文浅色 16:9。
按“问题—方法—实验—局限”组织，保留理解关键步骤所需的推导。
文本、表格、形状和连接线保持可编辑，公式使用可编辑文本框中的字面
LaTeX 源码，实验图片使用已有原图。同步记录 PPTX 的逐页安排和删减内容。
渲染并检查所有页面，验证公式源码、引用、图表与对象可编辑性。
缺少制作或渲染工具时，说明具体缺口和未执行的检查。
```

如果只想先理清内容，可以把交付阶段明确收窄：

```text
使用 $quarto-report，阅读 sources/notes/dmd-notes.md 和
sources/literature/dmd/ 的论文材料，在 Report/DMD-method/ 中
只完成 汇报说明.qmd：总体主线、章节规划、逐页内容、完整相关推导、
来源与符号映射。请标出证据缺口，本次不制作 slides 或 PPTX。
```

### 5. 从论文模板开始真实写作

```text
使用 $quarto-paper，先读取 Paper/Template 的论文、研究简报和输出配置，
将模板复制到 Paper/MyStudy/，保留原模板。
依据我提供的真实研究材料建立研究问题、主张与证据对应关系，再编写正文。
模板中的虚构作者、机构、声明和制造解数据不能沿用为真实投稿信息；
缺失信息用明确 TODO 标出。保留可编辑公式、真实文献与相对资源路径。
先渲染 HTML 检查内容，再按我明确选择的目标期刊核对官方要求与 PDF。
```
