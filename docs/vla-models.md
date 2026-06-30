# VLA (Vision-Language-Action) 模型全景调研

> 调研时间：2026-06-11
> 核心来源：Google DeepMind RT 系列论文、Physical Intelligence π0 论文、Figure AI Helix 技术博客、OpenVLA / open-source 社区、arXiv 前沿预印本
> 作者：wikieden
> 联系：[wikieden@gmail.com](mailto:wikieden@gmail.com)

---

## 目录

- [1. VLA 定义与核心问题](#1-vla-定义与核心问题)
- [2. 架构演进时间线](#2-架构演进时间线)
- [3. 关键技术组件](#3-关键技术组件)
- [4. 主流模型深度解析](#4-主流模型深度解析)
- [5. 开源生态与可复现方案](#5-开源生态与可复现方案)
- [6. 技术挑战与瓶颈](#6-技术挑战与瓶颈)
- [7. 未来方向与产业预测](#7-未来方向与产业预测)
- [8. 参考资源](#8-参考资源)

---

## 1. VLA 定义与核心问题

### 1.1 什么是 VLA？

**VLA（Vision-Language-Action）** 是一种将视觉感知、自然语言理解和机器人动作生成统一在单一神经网络中的端到端架构。

> 给定一张（或多张）环境图像和一个自然语言指令，模型直接输出低层动作（关节角度、末端执行器位姿、夹爪开合等），无需显式的感知-规划-控制分层。

### 1.2 为什么 VLA 成为主流？

| 传统分层架构 | VLA 端到端架构 |
|------------|--------------|
| 感知模块提取物体位姿 | 视觉编码器直接处理原始像素 |
| 规划模块生成中间轨迹 | 隐式规划嵌入在模型内部 |
| 控制模块跟踪轨迹 | 动作头直接输出电机指令 |
| 各模块独立优化，误差累积 | 全局优化，梯度直达传感器层 |
| 难以利用互联网预训练知识 | 直接继承 VLM 的语义理解能力 |

**关键优势**：零样本泛化、多模态对齐、规模化潜力。

### 1.3 核心问题

1. **感知-语言对齐**：像素空间与语义空间的对齐
2. **语言-动作对齐**：抽象指令到精确连续动作的映射
3. **时间一致性**：长程任务中动作的时序连贯性

---

## 2. 架构演进时间线

### 2.1 三代演进

```
第一代（2022-2023）：独立训练 → RT-1, Gato
第二代（2023-2024）：VLM 微调 → RT-2, OpenVLA
第三代（2024-2026）：原生 VLA + 生成式动作 → π0, Helix, Gemini Robotics
```

### 2.2 里程碑模型时间线

| 时间 | 模型 | 机构 | 核心创新 |
|------|------|------|---------|
| 2022.12 | **RT-1** | Google DeepMind | 首个大规模机器人 Transformer |
| 2023.06 | **RT-2** | Google DeepMind | VLM 直接微调为 VLA，涌现泛化 |
| 2023.10 | **RT-X** | DeepMind + 33 机构 | Open X-Embodiment 跨机器人数据集 |
| 2024.01 | **Diffusion Policy** | Columbia + TRI | 扩散模型动作生成 |
| 2024.03 | **Octo** | Berkeley + Stanford | 开源通用 VLA |
| 2024.06 | **OpenVLA** | Stanford + Berkeley | 7B 开源可复现 VLA |
| 2024.10 | **π0** | Physical Intelligence | 原生 VLA + Flow Matching |
| 2025.02 | **Helix** | Figure AI | 双系统架构（S1+S2），50Hz |
| 2025.06 | **π0.5** | Physical Intelligence | 持续学习，在线适应 |
| 2025.08 | **Gemini Robotics** | Google DeepMind | 原生多模态 VLA |
| 2025.10 | **Helix 02** | Figure AI | 离线运行，边缘部署 |

### 2.3 架构范式演变

**范式一：VLM + 动作头（RT-2 / OpenVLA）**
- 预训练 VLM（PaLI-X, Llama 2）
- 冻结或微调骨干，新增动作预测头
- 动作离散化为 token，与文本 token 统一

**范式二：原生 VLA（π0 / Helix）**
- 从头设计的多模态架构，底层即融合
- 动作生成使用 Flow Matching / Diffusion
- 支持连续高频动作输出

**范式三：世界模型增强（1X / DeepMind）**
- VLA + 视频预测世界模型
- 动作前向仿真，提升安全性和长程规划

---

## 3. 关键技术组件

### 3.1 视觉编码器

| 模型 | 视觉骨干 | 特点 |
|------|---------|------|
| RT-2 | EfficientNet-B3 | 轻量，适合端侧 |
| OpenVLA | DINOv2 ViT-L | 自监督预训练，语义丰富 |
| π0 | SigLIP + DINOv2 | 多尺度特征融合 |
| Helix | 自研 CNN + Transformer | 针对机器人场景优化 |

**趋势**：ImageNet 监督 → 自监督（DINOv2）→ 对比学习（SigLIP, CLIP）

### 3.2 语言模型骨干

| 模型 | 语言骨干 | 参数量 |
|------|---------|--------|
| RT-2 | PaLI-X | 55B |
| OpenVLA | Llama 2 | 7B / 13B |
| π0 | 自研 Transformer | 3B (VLM) + 300M (动作) |
| Helix | 自研 | 未公开（推测 1-3B） |

**趋势**：超大参数（55B）→ 中小参数（3-7B）+ 高质量数据，追求实时推理

### 3.3 动作表示与生成

| 方法 | 代表模型 | 优点 | 缺点 |
|------|---------|------|------|
| **离散 Token（自回归）** | RT-2, OpenVLA | 与文本统一，实现简单 | 动作连续性差，低频 |
| **扩散模型（Diffusion）** | Diffusion Policy, Octo | 多模态分布建模，平滑 | 推理慢，需多步去噪 |
| **Flow Matching** | π0, Helix | 单步生成，连续平滑，高频 | 训练稳定性要求高 |

**动作 Tokenization**：连续动作离散化为 bin（如 256 个等级）或使用 VQ-VAE。Flow Matching 直接处理连续值，无需离散化。

### 3.4 动作输出频率

| 模型 | 控制频率 | 延迟 |
|------|---------|------|
| RT-2 | 1-3 Hz | 高 |
| OpenVLA | 1-5 Hz | 中等 |
| π0 | 50 Hz | 低（单步生成） |
| Helix | 50 Hz | 低（小模型 + 优化） |

**实时性要求**：人形机器人全身控制通常需要 20-50 Hz，因此 Flow Matching 和轻量模型成为趋势。

---

## 4. 主流模型深度解析

### 4.1 Google DeepMind RT 系列

#### RT-1（2022.12）

RT-1（Robotics Transformer 1）是首个大规模机器人 Transformer 模型，标志着 VLA 范式的开端。

**核心设计**：
- **架构**：基于 Transformer 的序列模型，接受历史图像和语言指令
- **动作表示**：离散化为 256 个 bin 的连续动作 Token
- **数据**：13 万条遥操作演示，覆盖 700+ 任务
- **控制频率**：1-3 Hz

**局限**：动作离散化带来精度损失，低频控制不适配精细操作；泛化能力有限，仅在训练场景内有效。

#### RT-2（2023.06）

RT-2 是 VLA 领域的里程碑：首次将大规模 VLM 直接微调为机器人策略模型。

**核心创新**：
- 从 **PaLI-X**（55B）或 **PaLM-E**（12B）VLM 出发，冻结视觉-语言骨干，新增动作预测头
- 动作被表示为与文本 token 相同的离散序列，实现「动作即语言」
- 训练数据包含互联网规模的视觉-语言数据 + 少量机器人演示（约 RT-1 级别的 1/4）

**涌现能力**：
- **符号理解**：根据"把可乐移到靠近德克萨斯的图片上"这种抽象指令执行
- **语义泛化**：从未见过的物体组合和场景
- **推理能力**：根据指令选择正确的工具（如"选一个能钉钉子的工具"→选择锤子）

**局限**：动作离散化导致 1-3 Hz 控制频率，不适合精细操作；55B 参数量推理速度慢；对未见过的任务类型泛化不稳定。

#### RT-X / Open X-Embodiment（2023.10）

DeepMind 联合 33 个学术机构构建了 **Open X-Embodiment** 数据集——全球最大的跨机器人数据集。

| 维度 | 数据 |
|------|------|
| 机器人形态 | 22 种（单臂、双臂、移动底盘、四足等） |
| 数据量 | 100 万+ episode |
| 任务数 | 500+ |
| 场景 | 实验室、厨房、仓库、家庭 |
| 数据格式 | 统一 action/observation 规范 |

RT-X 证明了**数据多样性比数据量更重要**——跨本体、跨场景的多样化数据使模型泛化能力显著提升。

---

### 4.2 Physical Intelligence π0 家族

#### π0（2024.10）

Physical Intelligence 的 π0 是首个从零设计的原生 VLA 架构，放弃「VLM 微调」范式，采用 **VLM 骨干 + Flow Matching 动作专家**的双组件设计。

**架构要点**：

| 组件 | 功能 | 参数量 |
|------|------|--------|
| **VLM 骨干** | 视觉-语言语义理解 | 3B |
| **Flow Matching 动作专家** | 高频连续动作生成 | 300M |
| **多模态融合器** | 图像 + 语言 + 动作历史融合 | — |

**Flow Matching 的核心优势**：
- **单步生成**：相比扩散模型（需 10-100 步去噪），Flow Matching 一步生成动作轨迹
- **连续平滑**：输出 50Hz 连续关节角度，无需离散化或插值
- **多模态分布**：能建模同一个任务的不同合理动作路径

**跨本体能力**：π0 同时训练控制 8 种不同机器人（单臂、双臂、移动等），使用规范化动作空间。

#### π0.5（2025.04）

π0.5 实现了**开放世界泛化**——在从未见过的厨房、卧室中零样本执行清洁任务。

**关键改进**：
- 训练数据扩展到 10,000+ 小时人类演示 + 机器人自主数据
- 引入**场景不变性训练**：模型学习忽略背景变化的特征
- 对光照变化、物体位置偏移、场景布局变化的鲁棒性显著提升

#### π0.7（2026.04）

π0.7 是 PI 至今最重大的版本——**可组合泛化的可操控模型**。

**四大核心突破**：
1. **组合泛化**：首次展现类似 LLM 的组合能力，能将不同技能（折叠、抓取、放置）重新组合解决新问题
2. **语言指令跟随**：能执行从未训练过的自然语言指令，性能与微调专家模型持平
3. **视觉子目标引导**：通过 World Model 生成的目标状态图像指导精确操作
4. **跨本体零样本**：无需目标机器人训练数据即可迁移——UR5e 双臂折叠衣物零样本迁移成功

---

### 4.3 Figure AI Helix 双系统架构

#### Helix（2025.02）

Helix 是 Figure AI 为其 Figure 02 人形机器人设计的 VLA 模型，采用独特的**双系统架构**——类似 Daniel Kahneman 的「快思考 vs 慢思考」框架。

| 系统 | 角色 | 模型规模 | 频率 | 功能 |
|------|------|---------|------|------|
| **S1（System 1）** | 快速反应 | 小（推测 <1B） | 50 Hz | 视觉运动反射、精细手指控制、平衡 |
| **S2（System 2）** | 慢速推理 | 大（推测 3-7B） | 按需 | 任务规划、语言理解、环境推理 |

**核心设计**：
- S1 直接处理视觉输入 → 输出 50Hz 电机指令，延迟低至 20ms
- S2 在更高层进行语义理解和任务分解，调用 S1 执行原子动作
- 无需预训练 VLM 微调，从头训练的 VLA 架构

**Helix 的关键创新**：将实时控制（S1）与高层推理（S2）显式分离，解决了传统 VLA 模型「要么快但不聪明，要么聪明但慢」的矛盾。

#### Helix 02（2025.10）

Helix 02 是 Helix 的升级版本，核心变化是从云端推理转向**边缘部署**。

**改进点**：
- 全部推理在 Figure 02 板载计算单元上运行（可能为 Jetson Thor 级别）
- 优化后 S1 频率维持在 50Hz，延迟进一步降低
- 去除了对云端的依赖，为商业化部署扫清障碍

---

### 4.4 OpenVLA（2024.06）

OpenVLA 是 Stanford 和 UC Berkeley 联合推出的 7B 参数开源 VLA，旨在解决 VLA 领域的「可复现性危机」。

**设计选择**：
- 语言骨干：Llama 2（7B / 13B）
- 视觉编码器：DINOv2 ViT-L（预训练，冻结）
- 投影层：Learned 视觉-语言投影 + MLP 动作预测头
- 训练：Open X-Embodiment 数据集 + 互联网预训练知识蒸馏

**重要性**：OpenVLA 是第一个完全开源、可复现的 VLA 模型，使全球研究社区能够在此基础上迭代和实验。

**局限**：7B 参数推理慢（1-5 Hz），不适合实时控制；基于 VLM 微调的范式限制了动作空间。

---

### 4.5 Gemini Robotics（2025.08）

Gemini Robotics 是 Google DeepMind 基于 Gemini 原生多模态能力构建的 VLA 模型。

**核心特点**：
- **原生多模态**：利用 Gemini 原生处理图像、视频、文本的能力，无需额外编码器
- **长上下文窗口**：支持多帧历史 + 长指令理解
- **视频理解**：能观看人类演示视频后直接模仿
- **世界模型集成**：使用与 Gemini Robotics 共享的 world model 进行动作前仿真

**定位**：Google 认为 VLA 的未来是「原生多模态模型 + 物理先验」，而非 VLM + 动作头的拼接。

---

### 4.6 其他重要模型

| 模型 | 时间 | 机构 | 核心贡献 |
|------|------|------|---------|
| **Diffusion Policy** | 2024.01 | Columbia + TRI | 首次将扩散模型用于机器人动作生成，多模态动作分布 |
| **Octo** | 2024.03 | Berkeley + Stanford | 开源通用 VLA，基于 Transformer 的多任务策略 |
| **GR-2** | 2024.08 | Microsoft | 视频预训练 + 动作微调的 VLA，视频预测能力 |
| **RDT-1** | 2024.12 | Tsinghua | 扩散 Transformer 统一动作头和语言头 |

**模型对比总览**：

| 模型 | 架构范式 | 参数量 | 控制频率 | 动作类型 | 开源 |
|------|---------|--------|---------|---------|------|
| RT-2 | VLM 微调 + 离散 Token | 55B | 1-3 Hz | 离散 | ❌ |
| OpenVLA | VLM 微调 + 离散 Token | 7B | 1-5 Hz | 离散 | ✅ |
| π0 | 原生 VLA + Flow Matching | 3.3B | 50 Hz | 连续 | ✅ |
| Helix | 双系统分离架构 | 1-7B（估计） | 50 Hz | 连续 | ❌ |
| Gemini Robotics | 原生多模态 VLA | 未公开 | 10-20 Hz（估计） | 连续 | ❌ |
| Octo | Transformer 多任务 | 300M-1B | 1-5 Hz | 离散 | ✅ |

---

## 5. 开源生态与可复现方案

### 5.1 开源 VLA 模型

| 模型 | 开源时间 | 许可证 | 权重可用 | 代码仓库 |
|------|---------|--------|---------|---------|
| **OpenVLA** | 2024.06 | MIT | ✅ | github.com/openvla/openvla |
| **Octo** | 2024.03 | Apache 2.0 | ✅ | github.com/octo-models/octo |
| **π0-FAST** | 2025.02 | 科研许可 | ✅ | github.com/Physical-Intelligence/openpi |
| **LeRobot** | 2024.01 | Apache 2.0 | — | github.com/huggingface/lerobot |

### 5.2 开源数据集

| 数据集 | 规模 | 机器人 | 任务 | 开放 |
|-------|------|--------|------|------|
| **Open X-Embodiment** | 100 万+ episode | 22 种 | 500+ | ✅ |
| **DROID** | 2.6 万 episode | 单臂 | 500+ | ✅ |
| **BridgeData v2** | 6 万 episode | WidowX | 100+ | ✅ |
| **RLBench** | 仿真 | Franka | 100+ | ✅ |
| **FurnitureBench** | 仿真 | Franka | 家具组装 | ✅ |

### 5.3 训练框架

- **LeRobot**（Hugging Face）：统一数据集格式 + 训练 Pipeline，降低入门门槛
- **robomimic**（Stanford）：模仿学习框架，支持 BC、HBC、IRL
- **rl_games**（NVIDIA）：GPU 加速 RL 训练，与 Isaac Lab 集成

---

## 6. 技术挑战与瓶颈

### 6.1 泛化鸿沟

| 维度 | 当前水平 | 理想目标 |
|------|---------|---------|
| 场景泛化 | 同类型场景 | 任意环境 |
| 物体泛化 | 已知物体 + 部分新物体 | 任意物体 |
| 任务泛化 | 训练过的任务类型 | 任意任务 |
| 跨本体泛化 | 部分成功 | 零样本 |

**核心瓶颈**：数据多样性不足。现有数据集远未覆盖真实世界的长尾分布。

### 6.2 数据效率

VLA 模型依赖海量数据，数据采集是当前最大的工程瓶颈。
- **人类遥操作**：成本高、速度慢、不可规模化
- **仿真数据**：Sim2Real 鸿沟依然存在
- **互联网视频**：缺乏动作标注，需复杂后处理
- **自主数据**：需要已有策略能力，存在冷启动问题

### 6.3 实时性约束

| 机器人类型 | 所需控制频率 | 当前 VLA 可达 |
|-----------|------------|--------------|
| 人形全身控制 | 20-50 Hz | 50 Hz（π0/Helix）|
| 灵巧手操作 | ≥100 Hz | 50 Hz（不足）|
| 高速运动 | ≥200 Hz | 远不足 |

**问题**：高频率 = 小模型，小模型 = 弱泛化。这是当前 VLA 的核心矛盾。

### 6.4 安全性与可解释性

- VLA 本质上是**黑盒**——无法解释为什么选择特定动作
- **幻觉问题**：在未见场景中可能产生完全错误的动作序列
- **安全性验证**：缺乏形式化验证方法，依赖大量真实世界测试
- **伦理问题**：人形机器人自主决策的伦理边界

---

## 7. 未来方向与产业预测

### 7.1 Scaling Law 探索

VLA 领域正处于类似 NLP 的「Scaling Law 探索期」：

- **数据 Scaling**：从当前 10^5-10^6 条数据 → 10^8-10^9 条（与互联网规模对齐）
- **模型 Scaling**：从 3-7B → 更大的基础模型，但保持推理效率
- **跨本体 Scaling**：更多机器人形态同时训练，涌现更强的泛化能力

### 7.2 世界模型与 VLA 融合

下一代 VLA 的核心趋势是**世界模型增强**：
- **Dreamer / MuZero 式**：在模型中预测动作结果
- **视频预测**：生成未来帧，验证动作安全性
- **1X 的 World Model Lab**：2026 年 6 月成立的专门实验室，探索 VLA + 世界模型融合

### 7.3 商业化路径

| 阶段 | 时间 | 应用场景 | 代表性公司 |
|------|------|---------|-----------|
| 早期部署 | 2025-2026 | 工业（质检、物流、装配） | Figure AI、Agility、Apptronik |
| 规模化推广 | 2027-2028 | 仓储、制造、实验室 | Tesla、1X |
| 家庭服务 | 2029+ | 家务、康养、陪伴 | 1X、Tesla、Enchanted Tools |

### 7.4 关键前沿方向

1. **动作 Tokenization**：FAST（DCT+BPE 压缩）→ 更高效的动作表示
2. **在线学习**：RL self-improvement loop（如 PI 的 Recap / RLT）
3. **长程记忆**：MEM 多尺度具身记忆 → 15 分钟+ 任务执行
4. **多模态融合**：视觉 + 触觉 + 听觉 + 本体感知
5. **边缘推理**：Helix 02 证明了车载运行的可行性
6. **开源生态**：OpenVLA / LeRobot / OpenPI 推动社区进步

---

## 8. 参考资源

### 8.1 开山之作
- [RT-1: Robotics Transformer for Real-World Control at Scale](https://robotics-transformer1.github.io/) (2022.12)
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://robotics-transformer2.github.io/) (2023.06)
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://open-x-embodiment.github.io/) (2023.10)

### 8.2 原生 VLA 与 Flow Matching
- [π0: A Vision-Language-Action Flow Model for General Robot Control](https://www.pi.website/blog/pi0) (2024.10)
- [π0.5: Open-World Generalization](https://www.pi.website/blog/pi05) (2025.04)
- [π0.7: Steerable Model with Emergent Capabilities](https://www.pi.website/blog/pi07) (2026.04)
- [FAST: Efficient Robot Action Tokenization](https://www.pi.website/research/fast) (2025.01)
- [MEM: Multi-Scale Embodied Memory](https://www.pi.website/research/memory) (2026.03)

### 8.3 开源 VLA
- [OpenVLA: An Open-Source Vision-Language-Action Model](https://openvla.github.io/) (2024.06)
- [Octo: An Open-Source Generalist Robot Policy](https://octo-models.github.io/) (2024.03)
- [OpenPI: Physical Intelligence Open-Source Release](https://www.pi.website/blog/openpi) (2025.02)

### 8.4 扩散与动作生成
- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://diffusion-policy.cs.columbia.edu/) (2024.01)
- [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) (2022)

### 8.5 行业应用
- [Helix: A Vision-Language-Action Model for Generalist Humanoid Control](https://www.figure.ai/helix) (2025.02)
- [Gemini Robotics: Bringing AI into the Physical World](https://deepmind.google/discover/blog/gemini-robotics/) (2025.08)
- [GR-2: A Video-Language-Action Model](https://gr-2.github.io/) (2024.08)

### 8.6 开源框架与数据集
- [LeRobot: State-of-the-art Machine Learning for Real-World Robotics](https://github.com/huggingface/lerobot)
- [DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset](https://droid-dataset.github.io/)
- [robomimic: A Framework for Robot Learning from Demonstration](https://robomimic.github.io/)
