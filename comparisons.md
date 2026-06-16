# 具身智能公司横向对比分析

> 将各公司的技术路线放在同一维度下对比，揭示不同选择的优劣势与适用场景。

---

## 一、VLA 架构对比

| 维度 | Figure AI (Helix) | Physical Intelligence (π0) | Tesla (Optimus) | Boston Dynamics (Atlas) | 1X Technologies (Redwood) | Google DeepMind (Gemini) | Agility (Digit) | Apptronik (Apollo) | NVIDIA (GR00T) | Enchanted (Miroki) | Genesis AI |
|------|-------------------|---------------------------|-----------------|------------------------|---------------------------|--------------------------|----------------|-------------------|------------------|-------------------|-----------|
| **架构类型** | 端到端 VLA | 端到端 VLA | 端到端神经网络 | 分层混合 (MPC+RL+VLA) | 端到端 VLA + World Model | 双模型 (VLA + ER) | 传统分层控制 | 硬件平台+Gemini VLA | Transformer VLA 参考设计 | 社交AI+传统控制 | 宣称全栈 VLA |
| **基础模型** | 自研 VLA | 3B VLM + Flow Matching | FSD 神经网络移植 | Diffusion Transformer (4.5亿) | Redwood VLA + 内置 LLM | Gemini 多模态大模型 | LIPM+ZMP+MPC | Gemini (合作伙伴) | GR00T Transformer | 第三方 LLM | 未公开 |
| **动作生成** | 双系统 (快/慢) | Flow Matching 50Hz | 端到端直接输出 | Flow Matching 30Hz | VLA 联合移动+操作 | VLA 输出动作 token | 预定义步态库 | Gemini 输出 | VLA 动作 token | 预定义轨迹 | 未公开 |
| **跨本体** | 否 | ✅ 是（8种） | 否 | 否 | 否 | ✅ 是（多种） | 否 | 部分（Gemini跨本体） | ✅ 是（参考设计） | 否 | 未验证 |
| **语言条件化** | ✅ | ✅ | Grok | ✅ | ✅ 内置LLM | ✅ Gemini | ❌ | ✅ (Gemini) | ✅ | ✅ (第三方LLM) | 未公开 |

### 关键洞察

**端到端派 vs 分层混合派**

| 派别 | 代表公司 | 核心信念 | 优势 | 风险 |
|------|---------|---------|------|------|
| **端到端** | Figure AI, PI, Tesla, 1X | "梯度从控制直接流向感知，全局最优" | 可扩展性强、长尾场景适应好、性能上限高 | 黑箱难调试、安全验证困难、需要海量数据 |
| **分层混合** | Boston Dynamics, Agility | "MPC/传统控制提供可信赖的物理基础，学习补充边缘案例" | 可解释、可调试、安全性高、数据需求低 | 各层接口可能次优、难以处理真正新颖的场景 |
| **平台+合作AI** | Apptronik, Enchanted | "硬件自研，AI 借力最强合作伙伴" | AI 能力起点高、专注硬件差异化 | 对合作伙伴依赖高、自主 AI 护城河浅 |
| **基础设施** | NVIDIA Isaac | "提供训练+仿真+部署全栈，不造机器人" | 生态绑定深、零机器人风险 | 不控制终端场景、GR00T 能力待验证 |

**Figure Helix 02 的三层架构 vs PI π0.7**

Figure 在 2026.01 发布的 Helix 02 将架构从两层升级为三层（S0+S1+S2）；PI π0.7 则走统一模型+丰富信号路线。详见独立分析文档 [`brain-architecture-notes.md`](./brain-architecture-notes.md)。

| 维度 | Figure Helix 02 | PI π0.7 |
|------|----------------|---------|
| **层数** | 3 层（S0/S1/S2） | 1 层（统一 VLM + 动作头） |
| **通信方式** | S2→latent vector→S1→joint targets→S0 | 文本+副目标图像+元数据→统一模型 |
| **频率** | 7Hz→200Hz→1kHz 频率分层 | 单一模型，无显式频率分层 |
| **底层控制** | S0 10M 运动先验（替代 10 万行 C++） | Flow Matching 直接生成 50 步动作块 |
| **可调试性** | 各层独立可调试、可替换 | 黑箱，难以单独调试某层 |
| **信息瓶颈** | S2→S1 的 latent vector 是瓶颈（~4096 维） | 文本+图像是瓶颈，但图像补空间信息 |
| **总参数** | ~7.1B（7B + 80M + 10M） | ~5B（4B + 860M） |

**核心哲学差异**：

- **Figure**：按频段拆——慢的想策略，快的做控制，最快的做物理。每层极致优化，层间连续向量通信。
- **PI**：不显式分层。给模型足够丰富的训练信号，让它自己学会在不同粒度上推理。

---

## 二、数据策略对比

| 公司 | 主要数据来源 | 数据规模 | 独特策略 | 数据飞轮 |
|------|------------|---------|---------|---------|
| **Figure AI** | BotQ 自主生成 + 真实部署 | 大规模（具体未公开） | **BotQ**：自主数据生成系统，合成+真实混合 | ✅ 强（部署→数据→训练→再部署） |
| **Physical Intelligence** | Open X-Embodiment + DROID + 自采 | 1600万+ 跨本体轨迹 | 跨本体数据融合，人类视频迁移 | ✅ 强（π* 在线 RL 自提升） |
| **Tesla** | 工厂部署 + FSD 数据迁移 | 数百万辆车 + 数千机器人 | **FSD 数据复用**：自动驾驶数据直接用于机器人 | ✅ 极强（全球最大数据飞轮） |
| **Boston Dynamics** | Spot 2000+ 部署 + 仿真 + 遥操作 | 工业级规模 | **Fleet 数据共享**：Spot 数据预训练 Atlas 感知 | ✅ 中（工业部署积累中） |
| **1X Technologies** | 真实家庭 + Expert 遥操作 + World Model | 增长中 | **Expert Mode**：人类专家远程遥控生成高质量数据 | ⚠️ 早期（家庭部署刚开始） |
| **Unitree** | 仿真 (RL) + 动作捕捉 + 遥操作 | 中等规模 | **开源生态**：全球开发者贡献数据和算法 | ⚠️ 弱（主要靠自研） |
| **Agility Robotics** | 真实部署 + 仿真 + 遥操作调试 | 小规模（试点阶段） | **传统控制为主**：数据主要用于监控而非训练 | ⚠️ 弱（控制方案不依赖数据驱动） |
| **Apptronik** | 仿真 + VR 遥操作 + Google 合作数据 | 中等规模 | **借力 Google**：借助 DeepMind 的跨本体数据集 | ⚠️ 中（依赖合作伙伴） |
| **NVIDIA Isaac** | Omniverse 合成数据 + 生态数据 | 无限（合成）+ 生态反馈 | **合成数据工厂**：Replicator 程序化生成无限标注数据 | ✅ 强（平台级飞轮） |
| **Enchanted Tools** | 试点现场 + 遥操作 + 第三方 LLM | 小规模 | **场景数据有限**：导航和对话数据积累中 | ⚠️ 弱（技术壁垒不在数据） |
| **Genesis AI** | 未公开 | 未知 | **未公开数据策略** | ❓ 完全未知 |

### 数据策略评价

**最独特的数据策略**：
1. **Tesla 的 FSD 迁移**：将数百万辆车的驾驶数据（视觉、决策、控制）迁移到人形机器人，这是任何竞争对手无法复制的数据壁垒。
2. **1X 的 Expert Mode**：用"专家远程遥控"解决家庭场景数据稀缺问题，避免了 Figure AI 的 BotQ 那种重资本投入。
3. **PI 的跨本体数据**：用其他机器人的数据训练自己的策略，实现了"数据杠杆"。

---

## 三、控制方法演进路径

各公司的控制方法选择反映了其技术传承和战略优先级：

```
Boston Dynamics:    MPC ──→ MPC + RL ──→ MPC + RL + Diffusion Transformer
                    (30年)   (2024)        (2025+)
                    
Tesla:              FSD End-to-End ──→ Optimus End-to-End
                    (自动驾驶)          (人形机器人)
                    
Figure AI:          分层感知-规划-控制 ──→ Helix VLA End-to-End
                    (早期)               (2025)
                    
Physical Intelligence:  从零构建 VLA ──→ π0 ──→ π0.7
                        (2024)         (2024)  (2026)
                        
1X Technologies:    传统控制 ──→ Redwood VLA + World Model
                    (早期)      (2025+)
                    
Unitree:            传统控制 ──→ RL 运动 ──→ 模仿学习 ──→ UniFolm 大模型
                    (2016)      (2023)      (2024)      (2025+)

Genesis AI:         未公开 ──→ GENE-26.5 全栈方案
                    (? )        (2026)
```

---

## 四、安全机制对比

| 公司 | 安全层级 | 具体措施 | 独特之处 |
|------|---------|---------|---------|
| **Figure AI** | 软件层 | Guardian Network、力限制器、安全监控 | AI-First 硬件设计预留安全冗余 |
| **Tesla** | 软件层 | Guardian Network、力矩传感器、碰撞检测 | 借鉴自动驾驶安全系统 |
| **Boston Dynamics** | 软件+硬件 | Fenceless Guarding、IP67 防护、5分钟 limb 更换 | 工业级可靠性标准 |
| **1X Technologies** | **物理本质** | 肌腱驱动 95% 反向可驱动性、软体材料、无夹点设计 | **从机械层面保证人机共存安全** |
| **Unitree** | 软件层 | 紧急停止、碰撞检测 | 开发者自行 responsibility |
| **Agility Robotics** | 软件+硬件 | 摔倒检测、自我保护、低复杂度设计 | 简单夹爪降低夹伤风险 |
| **Apptronik** | 软件+硬件 | 多层安全监控、硬件急停、碰撞检测 | NASA 级可靠性标准 |
| **NVIDIA Isaac** | 平台层 | 提供安全仿真验证、数字孪生测试 | 在虚拟环境中预验证安全策略 |
| **Enchanted Tools** | 物理本质+软件 | 轻量小型化、软体材料、静音轮式 | 小巧体型本身降低伤害可能 |
| **Genesis AI** | 未公开 | 未公开 | 未公开 |

**1X 的物理本质安全是最独特的安全哲学**：不是用软件检测危险再响应，而是让机器人本身在物理上就无法产生危险（高反向可驱动性意味着遇到阻力自然"让开"）。

**Enchanted Tools** 采用类似思路：通过小型化和轻量化从物理层面降低风险。

---

## 五、硬件设计哲学对比

| 维度 | Figure AI | Tesla | Boston Dynamics | 1X Technologies | Unitree | Agility | Apptronik | Enchanted | Genesis AI |
|------|-----------|-------|-----------------|-----------------|---------|---------|-----------|-----------|------------|
| **设计出发点** | AI-First | 制造-First | 可靠性-First | 安全-First | 成本-First | 场景-First | 模块化-First | 亲和-First | Human-Level（宣称） |
| **执行器类型** | 电动 | 电动 | 电动 | **肌腱驱动** | 电动 | 电动 | 线性+旋转混合 | 电动（小型） | Wuji Hand 1.0（合作） |
| **重量** | 61 kg | 未公开 | 90 kg | 30 kg | 35-47 kg | 65 kg | 73 kg | 30-40 kg | 未公开 |
| **自由度** | 未公开 | 50 | 56 | 未公开 | 23-43 | 16 | 30+ | 6-8（手臂） | 未公开 |
| **移动方式** | 双足 | 双足 | 双足 | 双足 | 双足 | 双足 | 双足 | **轮式** | 未公开 |
| **感知系统** | 高帧率多相机 | 8 个 Autopilot 相机 | HDR 立体相机 | 双 8.85MP 鱼眼 | 3D LiDAR | RealSense 深度相机 | 立体相机 | 深度相机 | 未公开 |
| **充电方式** | 2kW 无线充电 | 未公开 | 自主换电 <3min | 自主插电 | 可更换电池 | 热插拔电池 | 热插拔电池包 | 6-8h 续航 | 未公开 |
| **防护等级** | 未公开 | 未公开 | IP67 | IP68/IP44 | 未公开 | 未公开 | 未公开 | 未公开 | 未公开 |
| **供应链策略** | 全新搭建 | Tesla 超级工厂 | Hyundai 汽车级 | 未公开 | 中国制造自研 | 中等规模 | NASA 级高可靠 | 欧洲本地 | Wuji Tech 合作 |

---

## 六、商业化路径对比

| 公司 | 阶段 | 当前客户/部署 | 定价策略 | 收入模式 |
|------|------|--------------|---------|---------|
| **Figure AI** | 早期商业化 | BMW 工厂试点 | 未公开（预计 $10万+/年） | 机器人租赁/销售 + 服务 |
| **Physical Intelligence** | 技术授权 | 合作伙伴部署 | 技术授权费 | 模型授权 + 部署服务 |
| **Tesla** | 内部部署 | Tesla 工厂自用 | 目标 $2 万（远期） | 内部使用 → 对外销售 |
| **Boston Dynamics** | 产品发布 | Hyundai Metaplant 测试 | 未公开（预计 $20万+） | 硬件销售 + Orbit 平台订阅 |
| **1X Technologies** | 预售 | 消费者预购 | 未公开（$200 定金） | 硬件销售 + 订阅服务 |
| **Unitree** | 量产出货 | 高校、研究机构、开发者 | **$13,500 (G1)** | 硬件销售 |
| **Agility Robotics** | 早期试点 | Amazon、GXO 仓库 | RaaS (~$10-15/小时) | 机器人即服务 |
| **Apptronik** | 早期合作 | Jabil 制造试点 | 未公开 | 硬件销售 + 服务 |
| **NVIDIA Isaac** | 平台成熟 | 几乎所有机器人公司 | Jetson 硬件 + Omniverse 订阅 | 硬件 + 软件授权 |
| **Enchanted Tools** | 概念验证 | 医院/养老院试点 | 未公开 | 设备销售/租赁 |
| **Genesis AI** | 概念/原型 | 无 | 未公开 | 未公开 |

**商业化成熟度排序**：NVIDIA Isaac (平台已成熟) > Unitree (已量产) > Boston Dynamics (产品版发布) > Agility Robotics (试点中) > Figure AI (小批量试点) > Tesla (内部测试) > Apptronik (早期合作) > PI (技术授权) > 1X (预售) > Enchanted Tools (概念验证) > Genesis AI (概念/原型)

---

## 七、技术路线选择矩阵

如果你要：

| 目标 | 最佳选择 | 理由 |
|------|---------|------|
| **快速进入研究领域** | Unitree G1 EDU + LeRobot | 最低成本、最开放生态 |
| **工业级可靠性** | Boston Dynamics Atlas | 20+ 年控制积累、Hyundai 供应链 |
| **最大数据飞轮** | Tesla Optimus | FSD 数百万辆车数据迁移 |
| **最先进的 VLA 算法** | Physical Intelligence π0 | 开源可复现、跨本体泛化 |
| **家用场景安全** | 1X Technologies NEO | 物理本质安全、OpenAI 语言理解 |
| **端到端人形控制** | Figure AI Helix | 首个全尺寸人形 VLA 部署 |
| **平台化赋能** | Google DeepMind Gemini | 不造硬件，赋能所有机器人公司 |
| **仓储物流专用** | Agility Robotics Digit | 场景聚焦、传统控制可靠、RaaS 模式 |
| **模块化硬件平台** | Apptronik Apollo | NASA 级执行器、上半身可分离、Google AI 加持 |
| **基础设施全栈** | NVIDIA Isaac | 仿真+训练+芯片+部署，行业卖铲人 |
| **服务/康养场景** | Enchanted Tools Miroki | 小巧亲和、轮式可靠、Pepper 团队经验 |
| **Human-Level 宣称** | Genesis AI GENE-26.5 | 全栈方案、Wuji Hand 合作、待验证 |

---

## 八、未来 12 个月关键观察点

| 公司 | 值得观察的里程碑 |
|------|-----------------|
| **Figure AI** | Helix 在 BMW 工厂的规模化部署效果；Figure 03 量产进度 |
| **Physical Intelligence** | π0.7 的实际部署表现；是否开源更多模型 |
| **Tesla** | Optimus 在 Tesla 工厂的实际生产效率数据 |
| **Boston Dynamics** | Atlas 产品版的客户交付；与 DeepMind 合作的成果 |
| **1X Technologies** | NEO 首批家庭用户反馈；World Model 的实际泛化能力 |
| **Unitree** | G1/H1 在开发者社区的采用率；UniFolm 大模型进展 |
| **Google DeepMind** | Gemini Robotics 的合作伙伴部署规模；是否开源更多模型 |
| **Agility Robotics** | Amazon/GXO 试点的实际运营数据（每小时搬运量、故障率） |
| **Apptronik** | Google Gemini 集成 Apollo 后的实际能力表现；关节模组独立销售进展 |
| **NVIDIA Isaac** | GR00T 基础模型的实际效果；Jetson Thor 的量产和客户采用率 |
| **Enchanted Tools** | 医院/养老院试点的用户满意度、任务完成率、故障率 |
| **Genesis AI** | 独立第三方验证（非公司控制场景）；团队背景公开；融资与估值确认 |

---

## 九、关键假设与风险

| 公司 | 核心假设 | 如果假设失败 |
|------|---------|-------------|
| **Figure AI** | VLA 端到端可以快速迭代并达到工业级可靠性 | 可能需要回归分层架构，时间和资金成本巨大 |
| **Physical Intelligence** | 跨本体通用策略可以覆盖绝大多数任务 | 可能发现某些任务必须针对特定机器人定制 |
| **Tesla** | FSD 技术可以无缝迁移到人形机器人 | 驾驶与操作的本质差异可能导致移植失败 |
| **Boston Dynamics** | MPC+学习的混合架构比纯端到端更可靠 | 可能在复杂长尾场景上被端到端超越 |
| **1X Technologies** | 家用市场愿意为机器人支付溢价 | 可能发现家用场景需求不足或价格敏感 |
| **Unitree** | 低成本+开源可以快速占领开发者市场 | 可能在高端工业市场缺乏竞争力 |
| **Agility Robotics** | 仓储 tote 搬运是一个足够大的单一市场 | 被更通用的机器人（Figure/Tesla）降本后替代 |
| **Apptronik** | Google Gemini 的 VLA 能力可以快速集成到硬件上 | 若 Google 合作生变，AI 能力需从零重建 |
| **NVIDIA Isaac** | 机器人行业将持续依赖 NVIDIA 的 GPU+仿真生态 | 开源仿真器（Genesis）或自研芯片可能削弱垄断 |
| **Enchanted Tools** | 医疗/康养场景愿意为服务机器人付费 | Pepper 的前车之鉴：社交机器人可能再次遭遇商业化困境 |
| **Genesis AI** | 宣称的 Human-Level 能力真实可达 | 可能是过度营销，缺乏可验证的技术基础 |
