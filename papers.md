# 具身智能核心论文索引

> 按时间倒序排列，收录各公司/机构在具身智能领域的标志性论文。  
> 标注了 arXiv 链接、核心贡献及与当前技术路线的关联。

---

## Google DeepMind 系列

### RT-2: Vision-Language-Action Models (2023.07)

| 属性 | 内容 |
|------|------|
| **标题** | RT-2: Vision-Language-Action Models |
| **作者** | Google DeepMind Robotics Team |
| **arXiv** | [2307.15818](https://arxiv.org/abs/2307.15818) |
| **核心贡献** | 首次将大规模视觉-语言模型（VLM）直接输出为机器人动作标记（action tokens），开创了 **VLA（Vision-Language-Action）** 架构范式 |
| **技术细节** | 将机器人动作离散化为 256 个 token，与语言 token 统一在 PaLI-X/PaLM-E 的词汇表中训练；支持涌现能力（如识别材料、理解语义类别） |
| **影响** | 被引用 2000+ 次，成为具身智能领域最重要的奠基论文之一；Figure AI Helix、Physical Intelligence π0 等均受其架构启发 |

---

### Open X-Embodiment & RT-X (2023.10)

| 属性 | 内容 |
|------|------|
| **标题** | Open X-Embodiment: Robotic Learning Datasets and RT-X Models |
| **作者** | Google DeepMind + 全球 20+ 研究机构联合 |
| **arXiv** | [2310.08864](https://arxiv.org/abs/2310.08864) |
| **核心贡献** | 发布了**全球最大的跨机器人形态数据集**（Open X-Embodiment Dataset），并训练了 RT-X 模型证明跨本体泛化的可行性 |
| **技术细节** | 数据集涵盖 22 种机器人形态、527 项技能、1600 万+ 条轨迹；RT-X 在未见过的机器人上成功率比单一机器人训练高 50% |
| **影响** | 成为整个行业的数据基础设施；Physical Intelligence 的 π0 直接基于此数据集训练 |

---

### RT-H: Action Hierarchies (2024.03)

| 属性 | 内容 |
|------|------|
| **标题** | RT-H: Action Hierarchies Using Language |
| **作者** | Google DeepMind |
| **arXiv** | [2403.01823](https://arxiv.org/abs/2403.01823) |
| **核心贡献** | 使用**自然语言描述中间步骤**（如"靠近苹果"→"抓住苹果"→"拿起苹果"），显著提升长程任务的成功率 |
| **技术细节** | 高层策略输出语言指令，低层策略将语言转化为动作；利用语言作为中间表示，实现更好的泛化和组合性 |
| **影响** | 启发了 PI 的 π0.7 可组合泛化思路；与分层任务规划（HTN）形成有趣对比 |

---

### Gemini Robotics (2024.08 → 2025.03 → 2026.04)

| 属性 | 内容 |
|------|------|
| **标题** | Gemini Robotics: Multimodal Understanding for Embodied Agents |
| **作者** | Google DeepMind |
| **发布** | 博客/技术报告形式发布（非传统 arXiv 论文） |
| **核心贡献** | 将 Gemini 多模态大模型能力引入机器人控制，推出 **Gemini Robotics 1.5（VLA）** 和 **Gemini Robotics-ER 1.6（具身推理）** 双模型架构 |
| **技术细节** | VLA 模型处理视觉+语言→动作；ER 模型负责物理推理和任务规划；支持跨机器人形态（从双臂平台到人形）；可调用外部工具（Google Search） |
| **影响** | 与 Apptronik 合作构建下一代人形机器人；Boston Dynamics、Agility Robotics 等作为可信测试者集成 Gemini |

---

## Physical Intelligence (π) 系列

### π0: A Vision-Language-Action Flow Model (2024.10)

| 属性 | 内容 |
|------|------|
| **标题** | π0: A Vision-Language-Action Flow Model for General Robot Control |
| **作者** | Physical Intelligence |
| **arXiv** | [2410.24164](https://arxiv.org/abs/2410.24164) |
| **核心贡献** | 首个真正**跨本体的通用机器人策略**，使用 **Flow Matching** 生成连续动作，支持 50Hz 高频控制 |
| **技术细节** | 3B 参数 VLM 骨干 + Flow Matching 动作专家；在 Open X-Embodiment 数据上训练；同时控制 8 种截然不同的机器人形态；支持折叠衣物、收拾餐桌等复杂长程任务 |
| **影响** | 开源了权重和代码，成为学术界和工业界研究通用机器人策略的重要基准 |

---

### FAST: Efficient Action Tokenization (2025.01)

| 属性 | 内容 |
|------|------|
| **标题** | FAST: Efficient Action Tokenization for Vision-Language-Action Models |
| **作者** | Physical Intelligence |
| **arXiv** | [2501.12327](https://arxiv.org/abs/2501.12327) |
| **核心贡献** | 提出 **DCT + BPE** 的高效动作 tokenization 方法，实现 **10 倍压缩率** 和 **5 倍训练加速** |
| **技术细节** | 离散余弦变换（DCT）将动作轨迹压缩到频域 + BPE 对频率模式进行子词编码；使 VLA 模型能在更大数据集上高效训练 |
| **影响** | 与 π0 一并开源；成为后续 VLA 模型的标准动作编码方法之一 |

---

### π0.7: Compositional Generalization (2026.04)

| 属性 | 内容 |
|------|------|
| **标题** | π0.7: Steering and Recombining Robot Skills with Diverse Multimodal Prompts |
| **作者** | Physical Intelligence |
| **发布** | 技术博客 + 论文预印本 |
| **核心贡献** | 实现**可组合泛化**——通过语言指令、元数据、视觉子目标等多样化提示，将已学技能重新组合完成全新任务 |
| **技术细节** | 支持语言指令、控制模态标签、元数据条件、视觉子目标四种提示方式；展示涌现能力（零样本任务迁移） |
| **影响** | 代表了通用机器人策略从"单一任务执行"向"可操控的通用智能"的演进 |

---

## Figure AI 系列

### Helix VLA (2025.01)

| 属性 | 内容 |
|------|------|
| **标题** | Helix: A Vision-Language-Action Model for Generalist Humanoid Control |
| **作者** | Figure AI |
| **发布** | 技术博客 + 演示视频 |
| **核心贡献** | 首个在**全尺寸人形机器人**上实现端到端 VLA 控制的系统；Figure 02 机器人仅通过自然语言指令即可自主完成物流任务 |
| **技术细节** | 双系统架构："系统 1"（快速反应，200Hz）+ "系统 2"（慢速推理，7-9Hz）；全身控制（双臂+躯干+头部）；端到端训练 |
| **影响** | 验证了 VLA 架构在人形机器人上的工程可行性；推动 Figure AI 估值达到 $390 亿 |

---

## Boston Dynamics / TRI 合作

### Diffusion Transformer for Atlas Manipulation (2025.02)

| 属性 | 内容 |
|------|------|
| **标题** | Learning Dexterous Manipulation from Exemplar Videos via Differentiable Simulation and Reinforcement Learning |
| **作者** | Boston Dynamics + Toyota Research Institute (TRI) |
| **发布** | ICRA/CoRL 会议论文（具体会议待确认） |
| **核心贡献** | 展示了 Atlas 使用 **4.5 亿参数 Diffusion Transformer** 完成复杂长程操作任务；采用 **Flow Matching Loss** 训练 |
| **技术细节** | 单一策略控制双臂+双手+颈部+躯干+双脚的全 body pose；控制频率 30Hz；动作轨迹块长度 48（未来 1.6 秒）；任务涵盖系绳、铺桌布、翻凳子、搬运轮胎等 |
| **影响** | 标志着 Boston Dynamics 从纯 MPC 控制向"MPC + 学习"混合架构的战略转型 |

---

## 其他重要论文

### CLIPort / Transporter (Google, 2021)

| 属性 | 内容 |
|------|------|
| **标题** | CLIPort: What and Where Pathways for Robotic Manipulation |
| **作者** | Google Research |
| **arXiv** | [2109.12098](https://arxiv.org/abs/2109.12098) |
| **核心贡献** | 将 CLIP 视觉表征与机器人操作结合，开创了"视觉预训练 + 机器人微调"的先河 |

---

### ACT: Action Chunking with Transformers (2022)

| 属性 | 内容 |
|------|------|
| **标题** | Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware |
| **作者** | Stanford / Google |
| **arXiv** | [2304.13705](https://arxiv.org/abs/2304.13705) |
| **核心贡献** | 提出 **Action Chunking with Transformers (ACT)**，将动作序列分块预测，减少累积误差；ALOHA 双臂遥操作平台 |
| **影响** | 成为模仿学习和双臂操作领域的标准基线方法 |

---

### Diffusion Policy (2023)

| 属性 | 内容 |
|------|------|
| **标题** | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion |
| **作者** | Columbia / MIT |
| **arXiv** | [2303.04137](https://arxiv.org/abs/2303.04137) |
| **核心贡献** | 首次将 **扩散模型（Diffusion Model）** 用于机器人动作生成，证明其在多模态动作分布建模上的优势 |
| **影响** | 直接启发了 PI 的 Flow Matching 动作生成和 BD/TRI 的 Diffusion Transformer |

---

## 论文演进脉络图

```
2021  CLIPort / Transporter        → 视觉预训练 + 机器人操作
2022  ACT (Action Chunking)        → 动作分块预测
2023  Diffusion Policy              → 扩散模型生成动作
2023.07 RT-2                        → VLA 架构诞生
2023.10 Open X-Embodiment / RT-X    → 跨本体数据 + 泛化
2024.03 RT-H                        → 语言分层任务规划
2024.08 Gemini Robotics             → 多模态大模型 + 机器人
2024.10 π0                          → Flow Matching + 跨本体通用策略
2025.01 FAST                        → 高效动作 Tokenization
2025.01 Helix (Figure AI)           → 人形端到端 VLA
2025.02 BD+TRI Diffusion Transformer → Diffusion + 全身操作
2026.04 π0.7                        → 可组合泛化 + 涌现能力
```

---

## 按技术主题分类

### VLA 架构
- RT-2 (2023.07) — 奠基
- RT-X (2023.10) — 跨本体
- π0 (2024.10) — Flow Matching
- Helix (2025.01) — 人形端到端
- Gemini Robotics 1.5 (2024.08) — 多模态大模型

### 动作生成
- Diffusion Policy (2023) — 扩散模型
- π0 (2024.10) — Flow Matching
- FAST (2025.01) — 高效 Tokenization
- BD+TRI (2025.02) — Diffusion Transformer

### 数据与泛化
- Open X-Embodiment (2023.10) — 数据集
- RT-X (2023.10) — 跨本体泛化
- π0.7 (2026.04) — 可组合泛化

### 任务规划
- RT-H (2024.03) — 语言分层
- Gemini Robotics-ER 1.6 (2026.04) — 具身推理
