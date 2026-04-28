# Soul2Humanoid — 具身大脑技术方案调研

> 系统性调研全球主流机器人公司的具身智能（Embodied AI）技术路线，聚焦「大脑」层面的算法架构、模型演进与工程实践。

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

> 持续更新中，后续计划覆盖：1X Technologies、Apptronik、Boston Dynamics、Agility Robotics 等。

---

## 目录结构

```
Soul2Humanoid/
├── README.md                          # 项目概述（本文档）
├── .gitignore                         # Git 忽略规则
│
├── reports/                           # 调研报告
│   ├── figure-ai/                     # Figure AI 技术路线
│   │   └── README.md
│   ├── physical-intelligence/         # Physical Intelligence (π) 技术路线
│   │   └── README.md
│   └── tesla-optimus/                 # Tesla Optimus 深度调研
│       └── README.md
│
├── assets/                            # 图表与可视化资源
│   ├── figure-ai/                     # Figure AI 相关图表（SVG + PNG）
│   │   ├── botq-manufacturing.svg
│   │   ├── data-flywheel.svg
│   │   ├── helix-architecture.svg
│   │   ├── hw-sw-co-design.svg
│   │   └── scenario-progression.svg
│   └── physical-intelligence/         # PI 相关图表（SVG + PNG）
│       ├── pi-benchmark.svg
│       ├── pi-cross-embodiment.svg
│       ├── pi-fast-tokenization.svg
│       ├── pi-mem-memory.svg
│       ├── pi-pi07-prompting.svg
│       ├── pi-rl-loop.svg
│       ├── pi-timeline.svg
│       └── pi-vla-architecture.svg
│
├── whiteboards/                       # 飞书画板源文件
│   ├── vla-arch.json
│   ├── vla-arch.mmd
│   └── vla-arch.png
│
└── scripts/                           # 工具脚本
    └── generate_diagrams.py           # PI 图表批量生成脚本（matplotlib）
```

---

## 技术关键词索引

| 关键词 | 相关公司 | 说明 |
|--------|---------|------|
| **VLA (Vision-Language-Action)** | Figure AI, PI | 视觉-语言-动作统一模型，当前具身智能主流架构 |
| **Flow Matching** | PI | 连续动作生成方法，相比自回归更平滑高频 |
| **End-to-End Neural Network** | Tesla | 端到端神经网络，替代传统感知-规划-控制分层架构 |
| **Cross-Embodiment** | PI | 跨机器人形态迁移，同一策略控制多种机器人 |
| **Data Flywheel** | Tesla, Figure AI | 数据闭环飞轮，自主采集→训练→部署→再采集 |
| **Sim2Real** | Figure AI | 仿真到真实的迁移学习，降低真实世界数据成本 |
| **BotQ** | Figure AI | 自主数据生成系统，大规模合成机器人操作数据 |
| **FSD Transfer** | Tesla | 自动驾驶全栈技术向人形机器人的直接迁移 |

---

## 使用方式

### 阅读报告
直接进入 `reports/` 目录下的各公司文件夹，查看 `README.md`。

### 重新生成图表
```bash
cd scripts
python3 generate_diagrams.py
```
> 依赖：`matplotlib`, `numpy`

---

## 贡献与更新

- 调研时间：2026年4月
- 信息来源：各公司官网、技术博客、学术论文、公开演讲
- 更新策略：跟随各公司重大技术发布（新模型、新产品、新论文）进行增量更新

---

## License

本仓库内容为技术研究笔记，仅供学习交流。各公司商标与技术归属各自所有者。
