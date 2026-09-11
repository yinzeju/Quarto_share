# Quarto 工作流分享

分享用于科研写作与中文科研汇报的 Quarto 工作流：项目规则、两套 Codex 技能、参考资料及从材料整理到渲染交付的操作管线。

这是一次独立快照，不包含原工作区的出版正文、论文、汇报、数据、素材、文献库、输出或 Git 历史，也不包含个人 Codex 配置和私人符号规范。

## 内容

| 路径 | 用途 |
|---|---|
| `AGENTS.md` | 通用项目规则 |
| `.codex/skills/quarto-publication/` | 学术出版技能、语法示例和官方文档索引 |
| `.codex/skills/create-scientific-slides-cn/` | 中文科研 PPT 内容、术语、视觉与验收规范 |
| `guidelines/research-reports/AGENTS.md` | 脱敏后的科研汇报规则，可合并到自己的汇报目录 |
| `docs/pipeline.md` | 从材料到交付的操作管线 |
| `docs/sharing-scope.md` | 分享范围和后续更新方法 |

## 使用

1. 安装 [Quarto](https://quarto.org/docs/get-started/)，根据目标格式准备运行环境。
2. 将需要的技能目录复制到自己工作区的 `.codex/skills/`。
3. 阅读并合并项目规则，不直接覆盖已有的 `AGENTS.md`。
4. 按 [操作管线](docs/pipeline.md) 在自己的具体 Quarto 项目内编写、预览和渲染。

此仓库没有 `_quarto.yml` 和出版源文件，不能直接作为出版项目运行 `quarto render`。

## 技能边界

- Quarto 出版使用 `quarto-publication`：公式保留在 `.qmd` 的 LaTeX 源码中，由 Quarto 正常渲染。
- `create-scientific-slides-cn` 是专门制作 PPTX 的辅助技能，默认在可编辑文本框中保留原始 LaTeX 字符串；依赖使用者环境提供 `presentations` 技能及制作、渲染工具。本仓库不打包该外部技能。
- PPTX 辅助技能的固定分页、字号和公式文本框规则不自动套用到 Quarto、Reveal.js 或论文。以项目规则和用户明确要求为准。

原有管线主要由技能和项目规则驱动；本次分享没有添加自动构建、部署或同步。由于没有出版源文件，本次不执行出版渲染；实际使用时须在自己的项目运行渲染并检查输出。
