# 中文术语与表达规范

## 翻译原则

- 优先使用学术界通行的中文译名，不进行生硬逐字翻译。
- 首次出现且英文缩写有助于识别时，写成“中文名称（缩写）”；后续只使用中文或统一缩写。
- 人名、算法名和模型名可以保留原文，例如 Koopman、Dreamer、TD-MPC2。
- 标题和图表标签不使用仅为装饰的英文大写词。
- LaTeX 命令、数学变量、单位、代码标识符不翻译。
- 同一份汇报中同一概念只使用一种中文写法。

## 常用术语

| 英文或缩写 | 推荐中文表达 |
|---|---|
| world model | 世界模型 |
| latent state | 潜状态；需要强调空间时用“潜空间状态” |
| latent dynamics | 潜空间动力学 |
| state representation | 状态表征 |
| rollout | 多步展开或多步推演 |
| long-horizon prediction | 长期预测 |
| trajectory | 轨迹 |
| encoder | 编码器 |
| decoder | 解码器 |
| actor | 策略网络；必要时首次写“策略网络（Actor）” |
| critic | 价值评价器；必要时首次写“价值评价器（Critic）” |
| planner | 规划器 |
| control input | 控制输入 |
| observation | 观测量 |
| foundation model | 基础模型 |
| pretrained model | 预训练模型 |
| black box | 黑盒 |
| semi-black-box | 半黑盒 |
| mode | 模态 |
| spectral decomposition | 谱分解 |
| eigenvalue | 特征值 |
| eigenfunction | 特征函数 |
| kernel | 核函数 |
| Gram matrix | 格拉姆矩阵 |
| reproducing kernel Hilbert space | 再生核希尔伯特空间（RKHS） |
| operator learning | 算子学习 |
| data-driven | 数据驱动 |
| physics-informed | 物理信息约束；按语境也可用“物理启发” |
| transfer learning | 迁移学习 |
| domain adaptation | 域适应 |
| cross-dataset | 跨数据集 |
| cross-machine | 跨装置或跨机器，按研究对象选择 |
| generalization | 泛化 |
| robustness | 鲁棒性 |
| uncertainty quantification | 不确定性量化 |
| closed-loop control | 闭环控制 |
| model predictive control | 模型预测控制（MPC） |
| linear quadratic regulator | 线性二次调节器（LQR） |
| reinforcement learning | 强化学习 |
| artificial intelligence for fusion | 人工智能赋能核聚变；标题中可简写为“核聚变人工智能” |
| plasma | 等离子体 |
| tokamak | 托卡马克 |
| disruption prediction | 破裂预测 |
| surrogate model | 代理模型 |
| digital twin | 数字孪生 |

## 专有词保留

- Koopman 算子通常保留人名，可写为“Koopman 算子”。
- 模型名、数据集名、装置名和软件名保持官方拼写，不强行翻译。
- LQR、MPC、RKHS 等标准缩写可以保留，但首次出现应给出中文全称。
- 若某英文词在特定研究社群中没有稳定中文译名，可保留原词，并在首次出现时给出简短中文解释。

## 禁止用法

- 不用 `RESEARCH REPORT`、`CHALLENGE`、`FRAMEWORK` 等英文充当页眉或装饰。
- 不把同一术语在“潜变量”“隐变量”“潜状态”之间随意切换。
- 不为显得科技化而堆叠英文缩写。
- 不翻译人名、模型名后导致读者无法检索原始工作。
