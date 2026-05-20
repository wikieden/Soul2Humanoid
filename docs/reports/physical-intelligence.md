# Physical Intelligence (π) 技术路线与重要研究方向梳理

> **文档生成时间**: 2026-04-26
> **信息来源**: https://www.pi.website
> **文档版本**: v1.0（对外版）

---

## 1. 摘要

Physical Intelligence（简称 PI 或 π）是一家致力于将通用人工智能（General-Purpose AI）引入物理世界的公司。其使命是构建能够控制**任意机器人**完成**任意任务**的通用机器人基础模型。自 2024 年 10 月发布 π0 以来，PI 在 18 个月内实现了从首个通用机器人策略到可组合泛化的 π0.7 的快速技术迭代，推动了 Vision-Language-Action（VLA）模型在机器人领域的全面落地。

本文档系统梳理 PI 的技术路线演进、六大核心研究方向以及关键性能基准，为理解通用机器人智能的发展提供参考。

---

## 2. 技术路线总览

PI 的核心技术架构围绕 **Vision-Language-Action（VLA）Foundation Model** 展开。该架构将互联网规模的视觉-语言预训练知识与机器人动作生成相结合，通过跨本体（Cross-Embodiment）数据训练，实现对多种机器人形态的统一控制。

### 2.1 核心架构组件

| 组件 | 功能 | 技术细节 |
|------|------|----------|
| **多模态输入** | 感知环境与任务指令 | 相机图像、自然语言指令、动作历史、视觉子目标 |
| **VLM 骨干网络** | 语义理解与知识迁移 | 3B 参数预训练视觉-语言模型，继承互联网规模知识 |
| **动作专家** | 生成高频连续动作 | Flow Matching / Diffusion，支持 50Hz 控制频率 |
| **训练数据** | 跨本体多源数据融合 | Open X-Embodiment、DROID、人类视频、自主 episode |

### 2.2 系统架构图

![VLA 系统架构图../assets/physical-intelligence/pi-vla-architecture.png)

**图 1** — Physical Intelligence VLA System Architecture

上图展示了 PI 的 VLA 系统架构：多模态输入经过预训练 VLM 骨干网络处理语义信息，再由动作专家生成高频连续动作输出，最终转化为机器人电机指令。整个模型在跨本体多源数据上进行训练，实现对不同机器人形态的统一控制。

---

## 3. 模型演进时间线

PI 的技术演进呈现出快速迭代、持续突破的特点。从 2024 年 10 月到 2026 年 4 月，共经历了 11 个关键里程碑：

| 时间 | 版本/技术 | 核心突破 |
|------|----------|---------|
| 2024.10 | π0 | 首个通用机器人策略，VLM + Flow Matching，支持 8 种机器人跨本体控制 |
| 2025.01 | FAST | 高效动作 tokenization（DCT + BPE），10x 压缩率，5x 训练加速 |
| 2025.02 | 开源 | π0 + π0-FAST 权重与代码开源 |
| 2025.04 | π0.5 | 开放世界泛化，可在全新厨房/卧室零样本执行清洁任务 |
| 2025.05 | Knowledge Insulation | 训练加速同时保留互联网规模知识 |
| 2025.06 | Real-Time Chunking | 高延迟环境下的高频实时动作执行 |
| 2025.11 | π*0.6 / Recap | 首个通过在线 RL 训练的通用策略，提升成功率与吞吐量 |
| 2025.12 | Human→Robot Transfer | 人类视频到机器人任务的迁移能力在规模上涌现 |
| 2026.02 | PI Layer | 真实世界部署，合作伙伴应用与规模化 |
| 2026.03 | MEM + RLT | 多尺度具身记忆（15 分钟长程任务）+ 高效 RL Token |
| 2026.04 | π0.7 | 可组合泛化的可操控模型，具备涌现能力 |

![技术演进时间线../assets/physical-intelligence/pi-timeline.png)

**图 2** — Physical Intelligence Technology Roadmap（2024.10 - 2026.04）

时间线清晰展示了 PI 从基础通用策略（π0）到可组合泛化模型（π0.7）的演进路径，每个里程碑都在泛化能力、训练效率或自主性上实现了关键突破。

---

## 4. 六大研究方向详解

### 4.1 通用机器人基础模型（VLA）

PI 的 VLA 模型是首个真正意义上跨本体的通用机器人策略。与传统方法不同，π0 不是针对单一机器人类型训练，而是同时学习控制 8 种截然不同的机器人形态（单臂、双臂、移动底盘等）。

**技术特点：**

- **互联网规模预训练**：利用 3B 参数 VLM 的语义理解能力，将互联网知识迁移到物理世界
- **Flow Matching 动作生成**：相比自回归或离散动作预测，Flow Matching 能生成更平滑、更高频的连续动作轨迹
- **统一动作空间**：通过规范化的动作表示，使同一策略能适配不同自由度的机器人

π0 已展示的能力包括：折叠衣物、收拾餐桌、组装纸箱、清洁厨房等复杂长程任务。在 π0 发布后，PI 持续通过开源（π0 + FAST 权重和代码）、扩大训练数据规模等方式，推动通用机器人基础模型的发展。

**π0.7 重大突破（2026.04）**：
- **组合泛化**：首次展现类似 LLM 的组合能力，能将不同技能重新组合解决新问题
- **零样本新设备操作**：能理解并操作训练集中从未出现过的厨房电器
- **跨本体零样本**：无洗衣折叠数据即可让新机器人学会折叠衣物
- **语言指令跟随**：能执行从未训练过的自然语言指令，性能与微调专家模型持平

### 4.2 动作表示与高效训练（FAST）

2025 年 1 月提出的 FAST（Efficient Robot Action Tokenization）是 PI 在动作表示上的重要创新。传统方法将动作序列直接输入模型，导致计算开销大、训练速度慢。FAST 通过离散余弦变换（DCT）+ 字节对编码（BPE）实现了动作数据的高效压缩。

![FAST 动作分词流程../assets/physical-intelligence/pi-fast-tokenization.png)

**图 4** — FAST: Efficient Robot Action Tokenization

**FAST 流程：**

1. **原始动作块**（Raw Action Chunk）：采集的高维连续动作序列
2. **离散余弦变换**（DCT）：将时域信号转换到频域，提取关键频率成分
3. **量化**：生成稀疏频率矩阵，保留主要信息
4. **展平**：将矩阵展平为一维向量
5. **BPE 压缩**：通过字节对编码构建紧凑的动作 Token 词汇表
6. **VLA 训练**：压缩后的 Token 直接用于自回归 Transformer 训练

**关键优势：**

- **10x 压缩率**：大幅降低序列长度，提升训练效率
- **5x 训练加速**：相比 Diffusion/Flow Matching 方法显著减少训练时间
- **自回归兼容**：使 VLA 模型可以采用与 LLM 类似的训练范式，便于利用现有训练基础设施
- **高精度保留**：DCT 的频域表示能有效保留动作信号的关键特征


### 4.3 跨本体迁移与组合泛化

π0.7（2026 年 4 月）是 PI 在泛化能力上的重大突破。通过**多样化多模态提示**（Diverse Multimodal Prompting），π0.7 实现了对模型的灵活操控和能力的组合重组。

![π0.7 多模态提示框架../assets/physical-intelligence/pi-pi07-prompting.png)

**图 3** — π0.7: Steerable Model with Diverse Multimodal Prompting

**四类输入提示：**

1. **语言指令**（Language Instructions）：如"pick up the oven mitt"、"open the drawer"
2. **元数据条件**（Metadata Conditioning）：质量要求（Quality: High）、速度偏好（Speed: Fast）等
3. **控制模态标签**（Control Modality Labels）：关节空间控制（Joint Control）/ 末端执行器控制（EEF Control）
4. **视觉子目标**（Visual Subgoal Images）：由 World Model 生成的目标状态图像，提供精确的空间布局信息

这些多样化的提示不仅让模型知道**做什么**（what），还知道**怎么做**（how），从而能够利用更广泛的数据源进行训练，包括不同质量的自主采集数据。

**涌现能力：**

- **技能组合**：将已学技能重新组合解决全新任务，如使用从未见过的厨房电器
- **语言跟随**：通过 step-by-step 语言指导（language coaching）学习新任务，然后自动执行
- **跨本体迁移**：无需目标机器人训练数据即可实现零样本迁移

![跨本体迁移示意../assets/physical-intelligence/pi-cross-embodiment.png)

**图 7** — Cross-Embodiment Transfer

**典型案例：UR5e 双臂折叠衣物**

π0.7 成功将 Bi-ARX 机器人上学到的折叠技能迁移到 UR5e 双臂机器人，而**从未在 UR5e 上收集过任何折叠数据**。由于两台机器人在尺寸、形态和控制方式上差异显著，π0.7 需要采用完全不同的操作策略。最终成功率达到专家人类操作员首次操作该机器人时的水平（这些专家平均拥有 375 小时遥操作经验）。

### 4.4 强化学习与自主提升

PI 构建了完整的 **RL 自提升闭环**（Self-Improvement Loop），使通用策略能够通过自主实践不断优化。

![RL 自提升闭环../assets/physical-intelligence/pi-rl-loop.png)

**图 6** — RL Self-Improvement Loop

**闭环流程：**

1. **通用策略（π0）**：作为基础模型生成初始行为，覆盖广泛任务
2. **Recap / RLT 训练**：通过在线 RL 优化特定任务的专用策略，提升成功率和吞吐量
3. **经验生成**：自主执行大量 episode，收集带元数据的执行经验
4. **蒸馏（Distillation）**：将 RL 优化后的经验蒸馏回通用策略，附加策略元数据（如质量、速度标注）
5. **增强通用策略（π0.7）**：获得策略性知识和更高成功率，同时保持通用性

**关键成果：**

- **π*0.6 / Recap**（2025 年 11 月）：首个通过在线 RL 训练获得显著提升的通用策略
- **RLT**（2026 年 3 月）：从 VLA 模型中提取 RL Token，实现高效的在线强化学习，大幅降低 RL 训练计算开销
- **性能匹配**：通过蒸馏，单一通用模型 π0.7 在特定任务上的性能与专用 RL 策略相当甚至超越

### 4.5 记忆与长程推理（MEM）

MEM（Multi-Scale Embodied Memory）是 PI 解决长程任务和部分可观测环境挑战的关键技术，于 2026 年 3 月发布。

![MEM 多尺度记忆架构../assets/physical-intelligence/pi-mem-memory.png)

**图 5** — MEM: Multi-Scale Embodied Memory Architecture

**双尺度记忆架构：**

- **短期记忆（Short-Term Memory）**：基于高效视频编码器的帧级历史，保留近期原始观测细节。适用于需要精细动作回顾的场景。
- **长期记忆（Long-Term Memory）**：基于自然语言的记忆，存储抽象概念和任务知识。以文本形式记录关键事件和状态，如"已将锅盖放在灶台左侧"。
- **主动推理机制**：动态选择需要记忆的内容，同时进行高层子任务规划。模型不仅决定"做什么"，还决定"记住什么"。

**核心能力：**

- 支持长达 **15 分钟** 的连续任务执行
- 处理**部分可观测环境**（Partial Observability）：物体不在视野中时仍能记住其位置
- **上下文自适应**（In-Context Adaptation）：根据历史经验动态调整操作策略，避免重复错误

**应用场景**：准备完整餐食（如烤奶酪三明治）、清理整个厨房、按食谱准备食材等需要多步骤协调的长程任务。

### 4.6 实时性与系统效率

PI 在实时控制方面进行了多项关键技术优化，确保模型在真实机器人硬件上的高效部署：

**Real-Time Action Chunking（2025.06）**

- 在高延迟通信环境下维持动作精度和执行速度
- 通过动作块缓存和插值保证 50Hz 高频控制不间断
- 解决了大 VLA 模型推理延迟与实时控制需求之间的矛盾

**Knowledge Insulation（2025.05）**

- 解决 VLA 模型在机器人数据微调时的**知识遗忘**问题
- 在加速机器人任务训练的同时，保留互联网规模的视觉-语言知识
- 使模型既能快速适应新任务，又不失通用语义理解能力

**RLT（RL Token，2026.03）**

- 从 VLA 模型中提取专用 RL Token，实现高效的在线强化学习
- 仅需数小时的额外数据即可显著提升精确操作任务的成功率
- 大幅降低 RL 训练的计算开销和数据需求


---

## 5. 性能基准对比

PI 在多个高难度真实世界任务上进行了系统性的基准测试。下图展示了 π0 与 OpenVLA、Octo 等开源/学术模型在 5 个任务上的归一化成功率对比。

![性能基准对比../assets/physical-intelligence/pi-benchmark.png)

**图 8** — Performance Benchmark: π0 vs OpenVLA vs Octo

**测试任务说明：**

| 任务 | 机器人平台 | 难度说明 |
|------|-----------|---------|
| **Bussing Easy** | UR5e | 基础餐桌收拾，分类放置餐具和垃圾 |
| **Bussing Hard** | UR5e | 困难版餐桌收拾，更多干扰物和复杂抓取姿态 |
| **Shirt Folding** | Bi-ARX | 双臂衬衫折叠，需要精确协调两个机械臂 |
| **Grocery Bagging** | UR5e | 杂货装袋，涉及多种形状物体的顺序放置 |
| **Toast out of Toaster** | Bi-Trossen | 从烤面包机中取出吐司，考验精细操作和时机把握 |

**关键结果：**

- **π0 全面领先**：在所有 5 个任务上均取得最高性能
- **极端任务满分**：在 Shirt Folding 任务上达到 **100%** 成功率
- **跨本体优势明显**：OpenVLA 和 Octo 在跨本体场景下几乎无法完成任务（0% 或接近 0%）
- **架构设计的价值**：即使是 π0-small（轻量版，无 VLM 预训练），性能也远超其他方法，证明了 Flow Matching + VLM 预训练架构的有效性

---

## 6. 未来展望

PI 的技术路线展现了从通用基础模型到可组合智能的清晰演进路径：

### 6.1 已实现的关键跨越

1. **π0 → π0.7 的飞跃**：18 个月内完成 7 次重大版本迭代，每次都在泛化、效率或自主性上取得突破
2. **开源生态建设**：π0 和 FAST 的开源为学术界和工业界提供了重要基线，推动了整个领域的进步
3. **真实世界落地**：PI Layer 的推出标志着技术从实验室走向实际应用场景，与合作伙伴共同解决真实问题
4. **AGI 通向物理世界**：通过 VLA + Memory + RL 的闭环架构，PI 正在构建能够持续学习和适应的物理智能体

### 6.2 值得关注的发展方向

- **更长程任务**：支持超过 30 分钟的复杂任务规划与执行
- **多机器人协作**：分布式具身智能，多机器人协同完成任务
- **更深层次的认知融合**：与大型语言模型更深度的结合，实现真正的物理世界推理
- **世界模型**：构建能预测物理交互结果的世界模型，用于规划和学习
- **安全与对齐**：确保通用物理智能的行为符合人类意图和安全规范

---

## 7. 附录

### 7.1 术语表

| 术语 | 英文 | 说明 |
|------|------|------|
| VLA | Vision-Language-Action | 视觉-语言-动作模型，将视觉感知、语言理解和动作生成统一在一个框架中 |
| Flow Matching | Flow Matching | 一种连续时间生成模型，用于生成平滑、高频的连续动作轨迹 |
| DCT | Discrete Cosine Transform | 离散余弦变换，用于动作信号的频域压缩，是 JPEG 等图像压缩的核心技术 |
| BPE | Byte Pair Encoding | 字节对编码，用于构建紧凑的词汇表，广泛应用于 NLP 领域 |
| Cross-Embodiment | Cross-Embodiment | 跨本体，指同一策略能够适配不同形态（单臂、双臂、移动等）的机器人 |
| RL | Reinforcement Learning | 强化学习，通过试错和奖励反馈优化策略 |
| MEM | Multi-Scale Embodied Memory | 多尺度具身记忆，结合短期视觉记忆和长期语言记忆 |
| RLT | RL Token | 强化学习 Token，从 VLA 模型中提取用于高效在线 RL |
| VLM | Vision-Language Model | 视觉-语言模型，具备图像理解和语言生成能力 |
| EEF | End-Effector | 末端执行器，机器人的"手"或工具端 |

### 7.2 关键论文与博客链接

| 时间 | 标题 | 类型 | 链接 |
|------|------|------|------|
| 2024.10 | π0: Our First Generalist Policy | Blog | https://www.pi.website/blog/pi0 |
| 2025.01 | FAST: Efficient Robot Action Tokenization | Paper | https://www.pi.website/research/fast |
| 2025.02 | Open Sourcing π0 | Blog | https://www.pi.website/blog/openpi |
| 2025.04 | π0.5: a VLA with Open-World Generalization | Blog | https://www.pi.website/blog/pi05 |
| 2025.05 | VLAs that Train Fast, Run Fast, and Generalize Better | Paper | https://www.pi.website/research/knowledge_insulation |
| 2025.06 | Real-Time Action Chunking with Large Models | Paper | https://www.pi.website/research/real_time_chunking |
| 2025.11 | π*0.6: a VLA that Learns from Experience | Blog | https://www.pi.website/blog/pistar06 |
| 2025.12 | Emergence of Human to Robot Transfer in VLAs | Paper | https://www.pi.website/research/human_to_robot |
| 2026.02 | The Physical Intelligence Layer | Blog | https://www.pi.website/blog/partner |
| 2026.03 | VLAs with Long and Short-Term Memory | Paper | https://www.pi.website/research/memory |
| 2026.03 | Precise Manipulation with Efficient Online RL | Paper | https://www.pi.website/research/rlt |
| 2026.04 | π0.7: a Steerable Model with Emergent Capabilities | Blog | https://www.pi.website/blog/pi07 |

---

*本文档由 AI 助手基于 PI 官网公开信息整理生成，仅供学习交流使用。*
