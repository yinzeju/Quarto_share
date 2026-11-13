# 论文模板：CMAME / Elsevier 管线测试

本项目直接复制自作者的 Paper/cmame-pipeline-test，保留原论文源稿、实际计算的制造解数据与图、文献、Elsevier 扩展 0.4.5、投稿格式 profile 和复现脚本。这里的作者、机构与论文均带有明确的**合成测试**标记，不用于实际投稿。科学内容没有被替换为新的研究结果。

为直接分享，只补入作者周报中使用的本地数学运行时，并让同一图路径按输出格式选择 PNG 或 PDF；正文与数值证据保持原例的科学含义。HTML 不需要在打开时再下载数学脚本。

## 直接渲染

进入本目录：

~~~powershell
quarto render manuscript.qmd --to html --no-execute
quarto render manuscript.qmd --profile submission --to elsevier-pdf --no-execute
~~~

HTML 和 PDF 分别生成在 _output/manuscript.html、_output/manuscript.pdf，保留的 manuscript.tex 位于源稿旁。默认 HTML 只需 Quarto；期刊式 PDF 还需 pdflatex 与 bibtex。已附带例子的图表与数据，普通渲染不会重新计算数值实验。

## 从论文到可复现证据

| 文件或目录 | 用途 |
|---|---|
| [manuscript.qmd](manuscript.qmd) | 完整论文示例，包含模型、弱式、离散、结果和边界 |
| [_quarto.yml](_quarto.yml)、[_quarto-submission.yml](_quarto-submission.yml) | 审阅与 Elsevier 输出设置 |
| [references.bib](references.bib) | 原示例使用的真实背景文献 |
| [research-brief.md](notes/research-brief.md) | 问题、证据、作者测试标记与结论边界 |
| [generate-demo.py](scripts/generate-demo.py) | 实际求解一维线性有限元制造解算例 |
| [convergence.csv](results/convergence.csv) | 数值误差与收敛数据 |
| [verification.png](figures/verification.png) | 与矢量 PDF 对应的示例图 |
| [_extensions/elsevier](_extensions/elsevier/LICENSE) | 已固定版本的期刊扩展及原许可 |

重新生成例子需要 NumPy 与 Matplotlib：

~~~powershell
python scripts/generate-demo.py
~~~

## 导出与独立编译

先生成期刊 PDF，再创建一个新的源码快照：

~~~powershell
python ../../.agents/skills/quarto-paper/scripts/package_latex.py --tex manuscript.tex --root . --output _output/latex-source-demo --resource _extensions/elsevier/elsarticle.cls --resource highlights.txt
python scripts/verify-export.py --archive _output/latex-source-demo.zip --output _output/independent-build-demo
~~~

打包器拒绝覆盖旧快照。再次打包时换一个输出名称。验证脚本在项目外的新目录校验哈希、运行 pdflatex / BibTeX 并检查资源独立性；它不会执行实际投稿。

原项目的[期刊要求记录](notes/journal-requirements.md)来自 2026-10-28 的测试，保留其历史核验边界；不是当前期刊全部要求的认证。用于真实论文时，使用 quarto-paper 核对当前官方要求，替换虚构身份、声明、研究问题与数值证据。

当前分享副本的实际检查见[模板验证记录](notes/validation.md)。
