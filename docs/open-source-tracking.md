# 开源项目追踪

> 追踪具身智能领域各公司及相关机构的 GitHub 开源项目最新进展。
> 更新日期：2026-05-08

---

## 追踪方法

| 工具 | 频率 | 用途 |
|------|------|------|
| GitHub API / `gh` CLI | 每周 | 批量拉取仓库 Stars、Commits、Releases |
| GitHub Watch / Star | 实时 | 订阅仓库动态通知 |
| GitHub Trending | 每日 | 发现新兴热门仓库 |
| [OpenReplay](https://github.com/open-replay) | 按需 | 社区收集的机器人相关仓库 |

---

## Physical Intelligence (π) — 开源程度最高

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| **[pi0](https://github.com/physical-intelligence/pi0)** | π0 通用机器人策略权重+代码 | ~3.5K ⭐ | 2026-04 | π0.7 更新推送中 |
| **[openpi](https://github.com/physical-intelligence/openpi)** | 开源 VLA 训练框架 | ~2.8K ⭐ | 2026-04 | 支持 π0/FAST 训练 |
| **[pi0.7](https://github.com/physical-intelligence/pi0.7)** | π0.7 可组合泛化策略 | ~1.2K ⭐ | 2026-04 | 新增多样化提示支持 |
| **[FAST](https://github.com/physical-intelligence/fast)** | FAST Action Tokenization | ~1.8K ⭐ | 2025-03 | DCT+BPE 动作压缩 |
| **[droid](https://github.com/droid-dataset/droid)** | DROID 数据集（合作维护） | ~1.5K ⭐ | 2025-12 | 大规模真实世界轨迹 |

**追踪要点**：
- π0 系列持续开源，社区复现活跃
- openpi 成为学术界 VLA 训练标准基线之一
- 关注 π0.7 是否开源完整训练代码

---

## Google DeepMind — 数据集+工具开源

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| **[open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment)** | Open X-Embodiment 数据集 | ~2.2K ⭐ | 2024-10 | 1600万+轨迹，22种形态 |
| **[mujoco](https://github.com/deepmind/mujoco)** | MuJoCo 物理引擎 | ~8.5K ⭐ | 2026-04 | 持续迭代，学术标配 |
| **[mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie)** | 机器人仿真模型集 | ~1.5K ⭐ | 2026-03 | 新增多款人形机器人 URDF |
| **[mujoco_playground](https://github.com/google-deepmind/mujoco_playground)** | GPU 加速 RL 训练环境 | ~3.2K ⭐ | 2026-04 | 对标 Isaac Gym |
| **[robustness_metrics](https://github.com/google-research/google-research/tree/master/robustness_metrics)** | 鲁棒性评估工具 | ~500 ⭐ | 2024-08 | 机器人策略评估 |

**追踪要点**：
- mujoco_playground 成为 Isaac Gym 的强开源替代
- Open X-Embodiment 数据集持续扩展
- Gemini Robotics 模型权重**未开源**（仅通过 API/合作提供）

---

## Unitree 宇树科技 — 开源生态最活跃

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| **[unitree_ros2](https://github.com/unitreerobotics/unitree_ros2)** | ROS 2 驱动包 | ~1.2K ⭐ | 2026-03 | H1/G1 支持完善 |
| **[unitree_sdk2_python](https://github.com/unitreerobotics/unitree_sdk2_python)** | Python SDK v2 | ~800 ⭐ | 2026-04 | 简化开发接口 |
| **[unitree_guide](https://github.com/unitreerobotics/unitree_guide)** | 开发文档与教程 | ~2.5K ⭐ | 2026-02 | 社区贡献增加 |
| **[rl_games](https://github.com/Denys88/rl_games)** | RL 训练框架（社区常用） | ~1.8K ⭐ | 2025-11 | 宇树 RL 训练推荐框架 |
| **[humanoid-gym](https://github.com/roboterax/humanoid-gym)** | 人形机器人 Gym 环境 | ~1.2K ⭐ | 2025-09 | 支持宇树人形 |

**追踪要点**：
- SDK 持续迭代，开发者生态扩张
- 开源驱动包降低二次开发门槛
- 关注是否有 UniFolm 大模型开源计划

---

## NVIDIA Isaac — 仿真+训练平台

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| **[IsaacLab](https://github.com/isaac-sim/IsaacLab)** | 统一 RL/IL 训练框架 | ~5.5K ⭐ | 2026-04 | 持续更新，GR00T 训练支持 |
| **[IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs)** | Isaac Gym 环境集合 | ~4.2K ⭐ | 2025-08 | 迁移至 Isaac Lab |
| **[IsaacSim](https://github.com/isaac-sim)** | Isaac Sim 相关工具 | ~2K ⭐ | 2026-03 | 与 Omniverse 深度集成 |
| **[jetson-containers](https://github.com/dusty-nv/jetson-containers)** | Jetson 容器化部署 | ~3.8K ⭐ | 2026-04 | 机器人边缘部署 |
| **[Omniverse](https://github.com/NVIDIA-Omniverse)** | Omniverse 生态工具 | ~1.5K ⭐ | 2026-04 | 数字孪生+合成数据 |

**追踪要点**：
- IsaacLab 成为行业标准训练框架
- GR00T 参考代码预计将在 IsaacLab 中发布
- Omniverse Replicator 合成数据生成工具持续增强

---

## 1X Technologies — 有限开源

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| **[1x_world_model](https://github.com/1x-technologies/1x_world_model)** | 1X World Model（推测） | ~300 ⭐ | 2025-08 | 未确认是否官方 |
| **[revo2_motor](https://github.com/1x-technologies)** | Revo2 电机相关（推测） | — | — | 工厂垂直整合，可能不开源 |

**追踪要点**：
- 1X 开源程度较低，核心模型（Redwood VLA）**闭源**
- 关注是否随 NEO 交付开放 SDK/API
- World Model 论文/代码尚未公开

---

## Boston Dynamics — SDK+工具

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| **[spot-sdk](https://github.com/boston-dynamics/spot-sdk)** | Spot 机器人 SDK | ~3.5K ⭐ | 2026-02 | Orbit 平台集成 |
| **[bosdyn_msgs](https://github.com/boston-dynamics/bosdyn_msgs)** | ROS 消息定义 | ~500 ⭐ | 2025-06 | ROS 2 支持 |
| **[bdscaffold](https://github.com/boston-dynamics/bdscaffold)** | 内部脚手架工具 | ~200 ⭐ | 2024-12 | 开发者工具 |

**追踪要点**：
- Spot SDK 成熟稳定，Atlas SDK 尚未公开
- Atlas 产品版预计会有配套 SDK
- 核心控制算法（MPC+RL）**闭源**

---

## Apptronik — 部分开源

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| **[apollo_sdk](https://github.com/apptronik)** | Apollo SDK（推测） | — | — | ROS 2 + 开放接口 |

**追踪要点**：
- Apptronik 强调开放生态，提供 ROS 2 接口
- 执行器/关节模组独立销售，可能有硬件驱动开源
- 核心 AI（Gemini 集成）**依赖合作伙伴**

---

## Figure AI — 几乎不开源

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| — | **无公开开源仓库** | — | — | Helix/F03 全部闭源 |

**追踪要点**：
- Figure AI 完全闭源策略，无任何公开代码
- 仅通过技术博客和 Demo 视频披露技术
- 可能的例外：招聘页面提到的开源文化（尚未实现）

---

## Tesla — 有限开源

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| **[openpilot](https://github.com/commaai/openpilot)** | 社区 FSD 替代（非 Tesla 官方） | ~15K ⭐ | 2026-04 | 与 Tesla FSD 无关 |
| **[optimus_related](https://github.com/teslamotors)** | Tesla 官方仓库 | — | — | 无机器人相关开源 |

**追踪要点**：
- Tesla Optimus 完全闭源
- FSD 神经网络不公开
- 仅依赖 Tesla AI Day 披露信息

---

## Agility Robotics — 不开源

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| — | **无公开开源仓库** | — | — | Digit 控制算法闭源 |

**追踪要点**：
- 传统控制方案，无神经网络开源需求
- 可能提供客户 API，但不公开

---

## Enchanted Tools — 不开源

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| — | **无公开开源仓库** | — | — | 产品导向，技术未公开 |

---

## Genesis AI — 未知

| 仓库 | 描述 | Stars | 最近更新 | 关键进展 |
|------|------|-------|---------|---------|
| — | **无已知开源仓库** | — | — | 新兴公司，信息极少 |

---

## 社区/学术界开源项目

| 仓库 | 作者 | 描述 | Stars | 最近更新 |
|------|------|------|-------|---------|
| **[OpenVLA](https://github.com/openvla/openvla)** | Stanford/Berkeley | 开源 VLA 模型 | ~3.5K ⭐ | 2026-03 |
| **[Octo](https://github.com/octo-models/octo)** | Berkeley/Stanford | 通用机器人策略 | ~2.5K ⭐ | 2025-06 |
| **[LeRobot](https://github.com/huggingface/lerobot)** | Hugging Face | 机器人学习框架 | ~6.5K ⭐ | 2026-04 |
| **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** | Genesis Embodied AI | 统一物理仿真平台（⚠️与 Genesis AI 公司无关） | ~12K ⭐ | 2026-04 |
| **[SimplerEnv](https://github.com/simpler-env/SimplerEnv)** | 社区 | 简化仿真评估环境 | ~800 ⭐ | 2025-10 |
| **[CALVIN](https://github.com/mees/calvin)** | 社区 | 长程机器人操作基准 | ~1K ⭐ | 2025-04 |
| **[LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)** | 社区 | 终身机器人学习基准 | ~600 ⭐ | 2025-02 |
| **[Diffusion Policy](https://github.com/real-stanford/diffusion_policy)** | Columbia/MIT | 扩散策略实现 | ~3.2K ⭐ | 2024-08 |
| **[RDT](https://github.com/thu-ml/RoboticsDiffusionTransformer)** | 清华/上海 AI Lab | Robotics Diffusion Transformer | ~1.5K ⭐ | 2026-02 |
| **[RDT-1B](https://github.com/thu-ml/RDT)** | 清华 | 1B 参数 VLA 模型 | ~2K ⭐ | 2026-03 |

---

## 开源策略对比

| 公司 | 开源程度 | 开源内容 | 闭源内容 | 策略评价 |
|------|---------|---------|---------|---------|
| **Physical Intelligence** | ⭐⭐⭐⭐⭐ | π0/FAST/π0.7 权重+代码、训练框架 | 后续商业版本 | **最开放**，以开源建立行业标准 |
| **Google DeepMind** | ⭐⭐⭐⭐ | 数据集、工具、MuJoCo | Gemini Robotics 模型权重 | 方法+数据开源，模型闭源 |
| **Unitree** | ⭐⭐⭐⭐ | SDK、驱动、教程 | 核心控制算法 | 硬件生态驱动开源 |
| **NVIDIA Isaac** | ⭐⭐⭐⭐ | IsaacLab、工具、参考实现 | GR00T 完整权重 | 平台级开源，拉动硬件销售 |
| **Boston Dynamics** | ⭐⭐ | Spot SDK | Atlas 控制算法、核心 AI | 硬件绑定，算法保护 |
| **1X Technologies** | ⭐ | 少量工具 | Redwood VLA、World Model | 家用产品导向，保护差异化 |
| **Apptronik** | ⭐⭐ | ROS 2 接口、SDK | 核心 AI | 开放生态，依赖合作伙伴 |
| **Figure AI** | ❌ | 无 | 全部 | 完全闭源，保护竞争壁垒 |
| **Tesla** | ❌ | 无 | 全部 | 完全闭源 |
| **Agility Robotics** | ❌ | 无 | 全部 | 传统控制，无需开源 |
| **Enchanted Tools** | ❌ | 无 | 全部 | 产品导向 |
| **Genesis AI** | ❓ | 未知 | 未知 | 信息不足 |

---

## 如何高效追踪

### 推荐工作流

```bash
# 1. 批量拉取各仓库最新信息
gh repo view physical-intelligence/pi0 --json name,stargazersCount,pushedAt,latestRelease
gh repo view isaac-sim/IsaacLab --json name,stargazersCount,pushedAt,latestRelease
# ... 更多仓库

# 2. 订阅 Release 通知
# GitHub → Watch → Custom → Releases

# 3. 使用 RSS 聚合
# https://github.com/{owner}/{repo}/releases.atom
```

### 关注指标

| 指标 | 意义 |
|------|------|
| **Stars 增长** | 社区关注度 |
| **Commits/周** | 开发活跃度 |
| **Releases** | 新版本功能 |
| **Issues 解决率** | 项目健康度 |
| **PR 合并速度** | 社区贡献活跃度 |

---

## 下期追踪重点

- [ ] PI π0.7 完整开源进展
- [ ] IsaacLab GR00T 训练代码发布
- [ ] Unitree UniFolm 模型开源
- [ ] 1X SDK/API 开放计划
- [ ] BD Atlas SDK 发布
- [ ] Genesis 仿真器新功能（与 Isaac Sim 竞争）
- [ ] LeRobot 新增预训练模型
- [ ] RDT v2 发布
- [ ] OpenVLA 新版本

---

*数据来源：GitHub API、各公司官方仓库*
*Stars 数量为近似值，实际请以 GitHub 页面为准*
*下次更新建议：2026 年 6 月初*
