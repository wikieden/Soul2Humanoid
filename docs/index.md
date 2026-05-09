# Soul2Humanoid — 具身大脑技术方案调研

> 系统性调研全球主流机器人公司的具身智能（Embodied AI）技术路线，聚焦「大脑」层面的算法架构、模型演进与工程实践。

[![Links](https://github.com/wikieden/Soul2Humanoid/actions/workflows/check-links.yml/badge.svg)](https://github.com/wikieden/Soul2Humanoid/actions/workflows/check-links.yml)
[![Last Updated](https://img.shields.io/badge/last%20updated-2026--05-blue)](./)
[![Companies](https://img.shields.io/badge/companies-11-orange)](./reports)
[![Papers](https://img.shields.io/badge/papers-12+-green)](./papers.md)

---

## 目录

- [最新动态](#最新动态)
- [项目简介](#项目简介)
- [调研覆盖公司](#调研覆盖公司)
- [横向对比概览](#横向对比概览)
- [目录结构](#目录结构)
- [参考资源](#参考资源)
- [技术关键词索引](#技术关键词索引)
- [使用方式](#使用方式)
- [贡献与更新](#贡献与更新)

---

## 最新动态

> 每次更新记录于此，详细动态见 [`latest-news.md`](./latest-news.md)

### 2026-05-08

| 公司 | 重大动态 |
|------|---------|
| **Figure AI** | BotQ 120 天 **24 倍**提速（1 台/小时）；**System 0** 零样本楼梯；**Never Fall** 协议；Helix 02 离线运行；$400-600/月租赁模型 |
| **1X Technologies** | **NEO Factory** 58K sqft 曝光；全垂直整合（Revo2 电机自产）；Jetson Thor；目标 100K/年 |
| **Unitree** | **双臂 R1 平台** $4,290 起；**$5.8 亿 IPO** 申请；20K 年出货目标 |
| **Boston Dynamics** | **CEO/C-Suite 大出走**（Playter 退休、Saunders→DeepMind、Kuindersma 离职）；Hyundai 要求 30K/年 |
| **Apptronik** | **$9.35 亿融资**；挖角 Waymo/BD/Amazon 组 Dream Team；下一代机器人将公布 |
| **Agility** | **Peggy Johnson** 新任 CEO；Unconstrained Humanoids 愿景 |
| **Meta** | 收购 **Assured Robot Intelligence**，正式进入人形机器人赛道 |

**行业趋势**：制造量产竞赛白热化 · 垂直整合成共识 · 家用市场提前布局 · BD 高管出走反映研究→商业转型阵痛

### 2026-04-29

| 动态 | 详情 |
|------|------|
| 新增 4 家公司报告 | Agility Robotics、Apptronik、NVIDIA Isaac、Enchanted Tools |
| 技术标签系统 | [`tags.md`](./tags.md) — 8 大维度，多标签交叉检索 |
| 中文媒体资源 | [`podcasts-videos.md`](./podcasts-videos.md) — 播客/B站/YouTube/会议 |
| 数据策略对比图 | 11 公司 5 维度柱状图 + 4 种飞轮模式图 |
| Twitter/X 监控 | [`people.md`](./people.md) — 12 个公司号 + 10 位关键人物 |

---

## 项目简介

本项目旨在追踪和梳理**人形机器人/具身智能领域**中，头部公司的技术方案与产品演进。核心关注维度包括：

- **感知架构**：视觉-语言-动作（VLA）融合、多模态输入处理
- **决策大脑**：端到端神经网络、任务规划、长程推理
- **动作生成**：Flow Matching / Diffusion、动作 Tokenization、高频控制
- **数据飞轮**：仿真到真实（Sim2Real）、人类视频迁移、自主数据生成
- **硬件协同**：AI-First 硬件设计、执行器与传感器选型

---

## 调研覆盖公司

| 公司 | 核心产品 | 技术路线关键词 | 报告 |
|------|---------|--------------|------|
| **Figure AI** | Figure 03 + Helix VLA | 人形通用机器人、VLA 端到端、BotQ 数据飞轮 | [`reports/figure-ai/`](./reports/figure-ai/) |
| **Physical Intelligence (π)** | π0.7 通用策略 | 跨本体 VLA 基础模型、Flow Matching、可组合泛化 | [`reports/physical-intelligence/`](./reports/physical-intelligence/) |
| **Tesla** | Optimus 人形机器人 | FSD 技术迁移、端到端神经网络、大规模数据闭环 | [`reports/tesla-optimus/`](./reports/tesla-optimus/) |
| **Boston Dynamics** | Atlas 电动版 | MPC+RL 混合控制、Hyundai 供应链、工业级可靠性 | [`reports/boston-dynamics/`](./reports/boston-dynamics/) |
| **1X Technologies** | NEO 家用机器人 | 肌腱驱动、World Model、Redwood VLA、OpenAI 合作 | [`reports/1x-technologies/`](./reports/1x-technologies/) |
| **Unitree 宇树科技** | H1/G1 人形机器人 | 极致性价比、开源生态、RL+模仿学习 | [`reports/unitree/`](./reports/unitree/) |
| **Google DeepMind** | Gemini Robotics / RT 系列 | VLA 奠基者、Open X-Embodiment、跨本体泛化 | [`reports/google-deepmind/`](./reports/google-deepmind/) |
| **Agility Robotics** | Digit 仓库机器人 | 仓储物流专用、传统控制、RaaS 商业模式 | [`reports/agility-robotics/`](./reports/agility-robotics/) |
| **Apptronik** | Apollo 通用人形 | 模块化硬件、NASA 执行器、Google Gemini 合作 | [`reports/apptronik/`](./reports/apptronik/) |
| **NVIDIA Isaac** | GR00T / Jetson / Isaac Sim | 具身智能基础设施、仿真平台、卖铲人 | [`reports/nvidia-isaac/`](./reports/nvidia-isaac/) |
| **Enchanted Tools** | Miroki 服务机器人 | 社交/康养场景、Pepper 团队、轮式服务 | [`reports/enchanted-tools/`](./reports/enchanted-tools/) |
| **Genesis AI** | GENE-26.5 全栈人形 | Human-Level 宣称、Wuji Tech 硬件合作、新兴公司 | [`reports/genesis-ai/`](./reports/genesis-ai/) ⚠️信息有限 |

> 持续更新中，后续计划覆盖：国内创业公司（智元、傅利叶、星动纪元等）深度跟进。

---

## 横向对比概览

![技术演进时间线总览](./assets/embodied-ai-timeline-overview.svg)

![公司能力雷达图](./assets/company-comparison-radar.svg)

![公司能力柱状图](./assets/company-comparison-bars.svg)

![数据策略对比图](./assets/data-strategy-comparison.svg)

> 评分基于公开信息的主观评估，维度包括：AI 成熟度、硬件成熟度、商业化进展、开源开放度、成本效率、数据策略。

---

## 目录结构

```
Soul2Humanoid/
├── README.md                          # 项目概述（本文档）
├── .gitignore                         # Git 忽略规则
│
├── reports/                           # 调研报告
│   ├── figure-ai/                     # Figure AI 技术路线
│   ├── physical-intelligence/         # Physical Intelligence (π) 技术路线
│   ├── tesla-optimus/                 # Tesla Optimus 深度调研
│   ├── boston-dynamics/               # Boston Dynamics Atlas 调研
│   ├── 1x-technologies/               # 1X Technologies NEO 调研
│   ├── unitree/                       # 宇树科技 H1/G1 调研
│   ├── google-deepmind/               # Google DeepMind RT/Gemini 调研
│   ├── agility-robotics/              # Agility Robotics Digit 调研
│   ├── apptronik/                     # Apptronik Apollo 调研
│   ├── nvidia-isaac/                  # NVIDIA Isaac / GR00T 调研
│   ├── enchanted-tools/               # Enchanted Tools Miroki 调研
│   └── genesis-ai/                    # Genesis AI GENE-26.5 调研（信息有限）
│
├── assets/                            # 图表与可视化资源
│   ├── figure-ai/                     # Figure AI 相关图表（SVG + PNG）
│   ├── physical-intelligence/         # PI 相关图表（SVG + PNG）
│   ├── company-comparison-radar.svg   # 公司能力雷达图
│   ├── company-comparison-radar.png
│   ├── company-comparison-bars.svg    # 公司能力柱状图
│   ├── company-comparison-bars.png
│   ├── data-strategy-comparison.svg   # 数据策略对比图
│   ├── data-strategy-comparison.png
│   ├── data-flywheel-patterns.svg     # 数据飞轮模式图
│   └── data-flywheel-patterns.png
│
├── whiteboards/                       # 飞书画板源文件
│   └── vla-arch.*
│
└── scripts/                           # 工具脚本
    ├── generate_diagrams.py           # PI 图表批量生成脚本（matplotlib）
    ├── generate_comparison_chart.py   # 公司对比图表生成脚本
    └── generate_data_flywheel_chart.py # 数据策略对比图生成脚本
```

---

## 参考资源

| 资源 | 说明 |
|------|------|
| [`comparisons.md`](./comparisons.md) | 横向对比分析 — 11 家公司在 VLA 架构、数据策略、安全机制、硬件设计、商业化路径的详细对比 |
| [`papers.md`](./papers.md) | 核心论文索引 — 按时间线整理的具身智能标志性论文，含 arXiv 链接、核心贡献和技术演进脉络 |
| [`tags.md`](./tags.md) | 技术标签索引 — 按架构范式、数据策略、应用场景等标签检索公司报告 |
| [`podcasts-videos.md`](./podcasts-videos.md) | 中文播客与视频资源汇总 — 播客、B站、YouTube、会议演讲等中文学习资源 |
| [`resources.md`](./resources.md) | 开源资源汇总 — 模型权重、数据集、仿真器、开发框架、硬件平台、评估基准 |
| [`people.md`](./people.md) | 关键人物追踪 — 各公司核心技术人员、研究负责人及其职业动向和技术观点 |
| [`funding.md`](./funding.md) | 投资与估值追踪 — 融资历程、估值分析、投资方格局和未来预测 |
| [`latest-news.md`](./latest-news.md) | 最新动态追踪 — 各公司近期重大事件、产品发布、融资、人事变动的实时记录 |
| [`CHANGELOG.md`](./CHANGELOG.md) | 更新日志 — 仓库文件变更历史 |

---

## 技术关键词索引

| 关键词 | 相关公司 | 说明 |
|--------|---------|------|
| **VLA (Vision-Language-Action)** | Figure AI, PI, DeepMind, 1X | 视觉-语言-动作统一模型，当前具身智能主流架构 |
| **Flow Matching** | PI, Boston Dynamics | 连续动作生成方法，相比自回归更平滑高频 |
| **End-to-End Neural Network** | Tesla, Figure AI | 端到端神经网络，替代传统感知-规划-控制分层架构 |
| **Cross-Embodiment** | PI, DeepMind | 跨机器人形态迁移，同一策略控制多种机器人 |
| **Data Flywheel** | Tesla, Figure AI | 数据闭环飞轮，自主采集→训练→部署→再采集 |
| **Sim2Real** | Figure AI, Unitree, BD | 仿真到真实的迁移学习，降低真实世界数据成本 |
| **BotQ** | Figure AI | 自主数据生成系统，大规模合成机器人操作数据 |
| **FSD Transfer** | Tesla | 自动驾驶全栈技术向人形机器人的直接迁移 |
| **Tendon-Driven** | 1X | 肌腱驱动执行器，高反向可驱动性，本质安全 |
| **World Model** | 1X, DeepMind | 基于物理的视频预测模型，用于动作结果仿真 |
| **MPC (Model Predictive Control)** | Boston Dynamics | 模型预测控制，传统但可靠的实时轨迹优化方法 |
| **Open X-Embodiment** | DeepMind, PI | 全球最大规模的跨机器人数据集 |
| **RL (Reinforcement Learning)** | Unitree, Boston Dynamics | 强化学习，用于运动控制和策略优化 |
| **Diffusion Transformer** | PI, Boston Dynamics | 扩散模型+Transformer，用于连续动作生成 |

---

## 使用方式

### 阅读报告
直接进入 `reports/` 目录下的各公司文件夹，查看 `README.md`。

### 重新生成图表
```bash
cd scripts
python3 generate_diagrams.py           # PI 技术图表
python3 generate_comparison_chart.py   # 公司对比图表
```
> 依赖：`matplotlib`, `numpy`

---

## 贡献与更新

- 调研时间：2026 年 4-5 月（持续更新）
- 信息来源：各公司官网、技术博客、学术论文、公开演讲、[Humanoids Daily](https://www.humanoidsdaily.com/)、X/Twitter
- 更新策略：重大动态即时记录到 [`latest-news.md`](./latest-news.md)，积累后更新各公司深度报告

---

## License

本仓库内容为技术研究笔记，仅供学习交流。各公司商标与技术归属各自所有者。
