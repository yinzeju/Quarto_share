# Quarto 工作流分享

分享用于科研写作与中文科研汇报的 Quarto 工作流：项目规则、两套 Codex 技能、参考资料及从材料整理到渲染交付的操作管线。

本仓库专注于可复用的技能、项目规范和制作流程，供读者应用到自己的 Quarto 项目中。

## 内容

| 路径 | 用途 |
|---|---|
| [AGENTS.md](AGENTS.md) | 通用项目规则 |
| [quarto-publication](.codex/skills/quarto-publication/SKILL.md) | 学术出版技能、语法示例和官方文档索引 |
| [create-scientific-slides-cn](.codex/skills/create-scientific-slides-cn/SKILL.md) | 中文科研 PPTX 内容、术语、视觉与验收规范 |
| [科研汇报规范](guidelines/research-reports/AGENTS.md) | 内容、数学、幻灯片视觉与引用规则，可合并到自己的汇报目录 |
| [操作管线](docs/pipeline.md) | 从材料到交付的制作流程 |

## 使用

1. 安装 [Quarto](https://quarto.org/docs/get-started/)，根据目标格式准备运行环境。
2. 将需要的技能目录复制到自己工作区的 `.codex/skills/`。
3. 阅读并合并项目规则，不直接覆盖已有的 `AGENTS.md`。制作科研幻灯片时，将 `guidelines/research-reports/AGENTS.md` 中适用的规则合并到自己的汇报目录；只复制技能不会自动应用这份规范。
4. 按 [操作管线](docs/pipeline.md) 在自己的具体 Quarto 项目内编写、预览和渲染。

此仓库没有 `_quarto.yml` 和出版源文件，不能直接作为出版项目运行 `quarto render`。

## 技能边界

- Quarto 出版使用 `quarto-publication`：公式保留在 `.qmd` 的 LaTeX 源码中，由 Quarto 正常渲染。
- Quarto 科研幻灯片使用 `quarto-publication`，同时遵守合并到项目中的 [科研汇报规范](guidelines/research-reports/AGENTS.md)。
- `create-scientific-slides-cn` 是专门制作 PPTX 的辅助技能，默认在可编辑文本框中保留原始 LaTeX 字符串；依赖使用者环境提供 `presentations` 技能及制作、渲染工具。本仓库不打包该外部技能。
- PPTX 辅助技能的固定分页、字号和公式文本框规则不自动套用到 Quarto、Reveal.js 或论文。以项目规则和用户明确要求为准。

## Quarto 科研幻灯片

- 忠于源材料，每页突出一个中心结论，以数学、数据、图表或文献支撑，区分理论结论、实验观察与推断。
- 默认中文，使用 16:9 画布、白色或极浅灰蓝背景、深海军蓝正文与蓝青强调，统一标题、字号层级和留白。
- 数学公式在 `.qmd` 中编写，由 Quarto 正常渲染；符号、变量定义和交叉引用保持一致。
- 所有文献引用放在对应页面左下角，统一为 `作者(年份)`，例如 `张三(2024)`、`Smith(2023)`；多篇用分号分隔，同页去重，并预留引用区域。
- 使用真实、可追溯的书目信息；完整参考文献附录不替代逐页引用。
- 渲染后逐页检查公式、图表、分页、可读性和引用位置，修复遮挡与溢出。
