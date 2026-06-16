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

### Hi Robot: Hierarchical Interactive Robot (2025.02)

| 属性 | 内容 |
|------|------|
| **标题** | Teaching Robots to Listen and Think Harder |
| **作者** | Physical Intelligence |
| **arXiv** | [2502.19417](https://arxiv.org/abs/2502.19417) |
| **核心贡献** | **System 1/2 分层推理架构**，VLA 作为直觉"System 1"，VLM 作为 deliberative"System 2"进行任务分解和人机交互 |
| **技术细节** | 高层 VLM 将复杂任务分解为子步骤，"whisper"给 π0 执行；支持实时人类反馈和上下文纠正 |
| **影响** | 为 VLA 模型引入类人推理能力，支持复杂长程任务和人机协作 |

---

### Knowledge Insulation (2025.05)

| 属性 | 内容 |
|------|------|
| **标题** | VLAs that Train Fast, Run Fast, and Generalize Better |
| **作者** | Physical Intelligence |
| **发布** | 技术博客 + 论文 |
| **核心贡献** | 解决 VLA 微调时的**知识遗忘**问题，在加速训练的同时保留互联网规模预训练知识 |
| **技术细节** | 通过架构隔离 VLM 推理层和动作生成层，避免机器人数据微调破坏预训练语义理解 |
| **影响** | 使 π0.5 能在保持开放世界泛化的同时快速适应新任务 |

---

### Real-Time Action Chunking (2025.06)

| 属性 | 内容 |
|------|------|
| **标题** | Real-Time Action Chunking with Large Models |
| **作者** | Physical Intelligence |
| **arXiv** | [2506.07339](https://arxiv.org/abs/2506.07339) |
| **核心贡献** | 解决大 VLA 模型推理延迟与实时控制需求的矛盾，实现**50Hz 高频实时控制** |
| **技术细节** | 动作块缓存 + 异步推理 + 平滑过渡，避免 chunk 切换时的不连续和危险加速度 |
| **影响** | 使 π0 系列模型能在边缘设备和移动机器人上实时运行 |

---

### π*0.6 / Recap: RL with Experience (2025.11)

| 属性 | 内容 |
|------|------|
| **标题** | π*0.6: a VLA that Learns from Experience |
| **作者** | Physical Intelligence |
| **发布** | 技术博客 + 论文 |
| **核心贡献** | 首个通过**在线 RL** 训练的通用策略，实现演示→纠正→自主练习的三步学习闭环 |
| **技术细节** | Recap 算法（RL with Experience & Corrections via Advantage-conditioned Policies）；自主 episode 收集 + 优势条件策略蒸馏 |
| **影响** | 最困难任务吞吐量提升 2×+，失败率降低 2×+，实现商业级鲁棒性（连续制作浓缩咖啡） |

---

### Human→Robot Transfer (2025.12)

| 属性 | 内容 |
|------|------|
| **标题** | Emergence of Human to Robot Transfer in VLAs |
| **作者** | Physical Intelligence |
| **发布** | 技术博客 + 论文 |
| **核心贡献** | 发现**人类视频到机器人任务的迁移能力**在大规模 VLA 中涌现，提供约 2× 数据效率提升 |
| **技术细节** | 利用第一人称人类视频（ego-centric data）作为额外训练数据源，解决机器人数据稀缺问题 |
| **影响** | 为机器人学习开辟海量人类视频数据源，降低数据收集成本 |

---

### MEM: Multi-Scale Embodied Memory (2026.03)

| 属性 | 内容 |
|------|------|
| **标题** | VLAs with Long and Short-Term Memory |
| **作者** | Physical Intelligence |
| **发布** | 技术博客 + 论文 |
| **核心贡献** | 为 VLA 引入**长短时记忆**，支持长达 **15 分钟** 的长程任务执行 |
| **技术细节** | 短期记忆存储原始观测，长期记忆存储自然语言抽象；模型主动选择记忆内容，避免因果混淆 |
| **影响** | 突破 VLA 短程任务限制，实现打扫整个厨房、制作完整餐食等复杂场景 |

---

### RLT: RL Token (2026.03)

| 属性 | 内容 |
|------|------|
| **标题** | Precise Manipulation with Efficient Online RL |
| **作者** | Physical Intelligence |
| **发布** | 技术博客 + 论文 |
| **核心贡献** | 从 VLA 提取**专用 RL Token**，实现高效的在线强化学习，精细操作速度提升 **3×** |
| **技术细节** | RL Token 提供 VLA 与轻量 RL 策略之间的紧凑接口，只需几分钟到几小时真实数据即可微调 |
| **影响** | 大幅降低 RL 训练计算开销，支持部署时实时优化精确操作任务 |

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

### NVIDIA GR00T: Humanoid Foundation Model (2024.03)

| 属性 | 内容 |
|------|------|
| **标题** | Project GR00T: Generalist Robot 00 Technology |
| **作者** | NVIDIA |
| **发布** | GTC 2024 主题演讲 + 技术博客 |
| **核心贡献** | 面向人形机器人的**通用基础模型参考设计**，基于 Transformer VLA 架构，支持多模态输入（视觉+语言+状态） |
| **技术细节** | 利用 Omniverse 生成合成数据训练；通过 Jetson Thor 在边缘部署；为 Figure AI、1X、Agility、Apptronik 等合作伙伴提供参考实现 |
| **影响** | NVIDIA 作为"卖铲人"推动人形机器人生态标准化；GR00T 与 Isaac Lab/Sim 形成训练-仿真-部署闭环 |

---

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
2024.03 GR00T (NVIDIA)               → 人形基础模型 + 仿真数据闭环
2024.10 π0                          → Flow Matching + 跨本体通用策略
2025.01 FAST                        → 高效动作 Tokenization
2025.01 Helix (Figure AI)           → 人形端到端 VLA
2025.02 BD+TRI Diffusion Transformer → Diffusion + 全身操作
2026.04 π0.7                        → 可组合泛化 + 涌现能力
```

---

## 2026 年 5-6 月新增重要论文

### Qwen-VLA (2026.05)
| 属性 | 内容 |
|------|------|
| **标题** | Qwen-VLA: Unifying VLA across Tasks, Environments, and Robot Embodiments |
| **作者** | 阿里 Qwen 团队 |
| **arXiv** | [2605.30280](https://arxiv.org/abs/2605.30280) |
| **核心贡献** | 基于 Qwen3.5-4B 的统一 VLA，DiT Flow Matching，LIBERO 97.9%，跨本体泛化 |

### LeVERB / SENTINEL / UniT / StarVLA-α (ICLR/CVPR 2026)
- **LeVERB** (ICLR 2026): 首个面向人形全身控制的 VLA 分层架构，零样本 sim-to-real
- **SENTINEL** (CVPR 2026): 全端到端语言→动作 Flow Matching 模型
- **UniT** ([2604.19734](https://arxiv.org/abs/2604.19734)): 跨本体人类→人形策略迁移
- **StarVLA-α** ([2604.11757](https://arxiv.org/abs/2604.11757)): 证明强 VLM 骨干即可强性能，超越 π0.5 20%

### WLA-0 / UniVLA (2026.06 / ICLR 2026)
- **WLA-0** ([2606.05979](https://arxiv.org/abs/2606.05979)): 新 WLA 范式，AR Transformer，40ms 推理，RoboTwin2.0 92.94%
- **UniVLA** (ICLR 2026): 视觉/语言/动作统一离散 token 自回归建模，LIBERO 95.5% SOTA
- **EgoActor** / **Humanoid-LLA** (ICLR 2026): 端到端指令→动作 / 开放词汇人形全身控制
- **CReF** ([2603.29452](https://arxiv.org/abs/2603.29452)): 深度条件人形行走，零样本迁移

---

## 按技术主题分类

### VLA 架构
- RT-2 (2023.07) — 奠基
- RT-X (2023.10) — 跨本体
- π0 (2024.10) — Flow Matching
- Helix (2025.01) — 人形端到端
- Gemini Robotics 1.5 (2024.08) — 多模态大模型
- GR00T (2024.03) — 人形基础模型 + 仿真

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

---

## 热门论文持续跟踪

> 基于 Semantic Scholar / Google Scholar 引用趋势和社区关注度，追踪具身智能领域高影响力论文。
> 标注 🔥 引用 >500 / ⭐ 引用 >200 / 📈 近期快速上升

### VLA 与通用策略

| 论文 | 年份 | 引用趋势 | 关键词 | 状态 |
|------|------|---------|--------|------|
| RT-2: Vision-Language-Action Models | 2023.07 | 🔥 2000+ | VLA 奠基 | 持续影响 |
| Open X-Embodiment / RT-X | 2023.10 | 🔥 1500+ | 跨本体数据 | 行业数据基础设施 |
| π0: VLA Flow Model | 2024.10 | ⭐ 300+ 📈 | Flow Matching | 开源，快速上升 |
| FAST: Action Tokenization | 2025.01 | ⭐ 200+ 📈 | DCT+BPE | 开源，VLA 训练加速 |
| Helix (Figure AI) | 2025.01 | 📈 | 人形 VLA | 技术博客，闭源 |
| Gemini Robotics | 2024.08→2026 | ⭐ 400+ | 多模态 VLA | 持续迭代 |
| GR00T (NVIDIA) | 2024.03 | 📈 | 人形基础模型 | 参考设计，生态绑定 |

### 动作生成与控制

| 论文 | 年份 | 引用趋势 | 关键词 | 状态 |
|------|------|---------|--------|------|
| Diffusion Policy | 2023.03 | 🔥 1500+ | 扩散动作生成 | 经典基线 |
| ACT: Action Chunking | 2023.04 | 🔥 1000+ | 动作分块 | 模仿学习标配 |
| BD+TRI Diffusion Transformer | 2025.02 | 📈 | 全身操作 | MPC+学习融合标杆 |
| RDT: Robotics Diffusion Transformer | 2024.10 | ⭐ 200+ | Diffusion Transformer | 清华，开源 |

### 数据、泛化与学习

| 论文 | 年份 | 引用趋势 | 关键词 | 状态 |
|------|------|---------|--------|------|
| RT-H: Action Hierarchies | 2024.03 | ⭐ 300+ | 语言分层 | 启发可组合泛化 |
| DROID: Large-Scale Real-World Data | 2024 | ⭐ 200+ | 真实世界数据 | Stanford 主导 |
| BridgeData V2 | 2023 | 🔥 600+ | 厨房操作数据 | 经典数据集 |
| π0.7: Compositional Generalization | 2026.04 | 📈 | 可组合泛化 | 最新，零样本迁移 |

### 基础模型与架构

| 论文 | 年份 | 引用趋势 | 关键词 | 状态 |
|------|------|---------|--------|------|
| Octo: Generalist Robot Policy | 2024 | ⭐ 300+ | 开源通用策略 | Berkeley/Stanford |
| OpenVLA | 2024 | ⭐ 400+ | 开源 VLA | Stanford/Berkeley |
| CLIPort | 2021 | 🔥 800+ | 视觉+操作 | 先驱工作 |

### 仿真与 Sim2Real

| 论文 | 年份 | 引用趋势 | 关键词 | 状态 |
|------|------|---------|--------|------|
| Isaac Gym / Isaac Lab | 2022-2024 | 🔥 1000+ | GPU 并行 RL | NVIDIA 生态核心 |
| Genesis | 2024 | 📈 | 统一物理仿真 | 新兴开源替代 |
| MuJoCo (DeepMind) | 2021→ | 🔥 3000+ | 标准物理引擎 | 开源，学术标配 |

---

### 跟踪方法

| 来源 | 频率 | 用途 |
|------|------|------|
| [arXiv cs.RO](https://arxiv.org/list/cs.RO/recent) | 每日 | 机器人学新论文 |
| [Semantic Scholar](https://www.semanticscholar.org/) | 每周 | 引用趋势追踪 |
| [Papers With Code - Robotics](https://paperswithcode.com/task/robotics) | 每周 | SOTA 排行榜 |
| [Google Scholar Alerts](https://scholar.google.com/) | 每周 | 关键词订阅（VLA, humanoid robot, embodied AI） |
| X/Twitter #arXiv | 实时 | 学者自行推广 |
| CoRL / RSS / ICRA / ICRA proceedings | 季度 | 顶会论文集 |

### 下期重点跟踪

- [ ] π0.7 开源进展与社区复现
- [ ] Gemini Robotics-ER 独立论文发布
- [ ] Figure Helix 02 技术报告
- [ ] GR00T 首篇正式论文
- [ ] BD+TRI 全文发表（当前仅为会议摘要）
- [ ] RDT v2 / Diffusion Transformer 新版本
- [ ] DROID 扩展数据集发布
