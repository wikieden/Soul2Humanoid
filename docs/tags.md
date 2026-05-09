# 技术标签索引

> 为每份调研报告打上技术标签，方便按主题快速检索和交叉对比。

---

## 标签体系

### 按架构范式

| 标签 | 说明 | 覆盖公司 |
|------|------|---------|
| `#端到端` | 单一神经网络直接输出动作，感知-规划-控制一体化 | Figure AI, Tesla, 1X, PI |
| `#分层混合` | 传统控制（MPC）+ 学习（RL/神经网络）分层架构 | Boston Dynamics, Agility Robotics |
| `#VLA` | Vision-Language-Action 视觉-语言-动作统一模型 | Figure AI, PI, 1X, DeepMind, Apptronik |
| `#MPC` | Model Predictive Control 模型预测控制 | Boston Dynamics |
| `#RL` | Reinforcement Learning 强化学习 | PI, Unitree, Boston Dynamics |
| `#模仿学习` | Imitation Learning 从人类演示中学习 | Unitree, Boston Dynamics, 1X |

### 按动作生成

| 标签 | 说明 | 覆盖公司 |
|------|------|---------|
| `#FlowMatching` | Flow Matching 连续动作生成 | PI, Boston Dynamics |
| `#Diffusion` | Diffusion Model / Diffusion Transformer 动作生成 | PI, Boston Dynamics, DeepMind |
| `#Transformer` | 基于 Transformer 的序列建模 | PI, DeepMind, Boston Dynamics |
| `#Tokenization` | 动作 Tokenization（离散/连续） | PI (FAST) |

### 按数据策略

| 标签 | 说明 | 覆盖公司 |
|------|------|---------|
| `#数据飞轮` | 部署→数据采集→训练→再部署的闭环 | Tesla, Figure AI, PI |
| `#跨本体` | Cross-Embodiment 跨机器人形态泛化 | PI, DeepMind |
| `#Sim2Real` | 仿真到真实的迁移学习 | Unitree, PI, Figure AI, Boston Dynamics |
| `#合成数据` | 自主生成/仿真生成训练数据 | Figure AI (BotQ), PI |
| `#遥操作` | Teleoperation 人类远程遥控生成数据 | 1X (Expert Mode), Boston Dynamics, Unitree |
| `#人类视频迁移` | 从人类视频学习迁移到机器人 | PI, Tesla |

### 按应用场景

| 标签 | 说明 | 覆盖公司 |
|------|------|---------|
| `#工业制造` | 工厂、仓储、物流场景 | Figure AI, Tesla, Boston Dynamics, PI, Agility Robotics, Apptronik |
| `#家用` | 家庭服务、个人助理场景 | 1X Technologies, Enchanted Tools, Genesis AI（推测） |
| `#教育研究` | 面向高校、研究机构的开发平台 | Unitree, DeepMind, NVIDIA Isaac |

### 按硬件特性

| 标签 | 说明 | 覆盖公司 |
|------|------|---------|
| `#肌腱驱动` | Tendon-Driven 柔性传动执行器 | 1X Technologies |
| `#高扭矩密度` | 关节电机高扭矩密度设计 | Unitree (189 N.m/Kg) |
| `#轻量化` | 极致轻量化设计 | Unitree (H1 47kg, G1 35kg) |
| `#低成本` | 成本优先/性价比策略 | Unitree ($13.5K) |
| `#模块化` | 硬件模块化设计，可拆卸/快换 | Apptronik |

### 按安全机制

| 标签 | 说明 | 覆盖公司 |
|------|------|---------|
| `#物理本质安全` | 从机械层面保证安全（高反向可驱动性、软体） | 1X Technologies |
| `#软件安全层` | Guardian Network、力限制器等软件安全 | Tesla, Figure AI, Apptronik |

### 按开源程度

| 标签 | 说明 | 覆盖公司 |
|------|------|---------|
| `#完全开源` | 模型权重+代码+数据全部开源 | PI (π0/FAST), DeepMind (数据集) |
| `#部分开源` | 开源部分模型/工具/数据集 | DeepMind, Unitree |
| `#闭源` | 核心技术/模型不公开 | Tesla, Figure AI, 1X, Boston Dynamics, Agility Robotics, Enchanted Tools |

### 按特殊能力

| 标签 | 说明 | 覆盖公司 |
|------|------|---------|
| `#世界模型` | 基于物理的视频预测/心理模拟 | 1X Technologies |
| `#语言条件化` | 自然语言指令直接驱动行为 | 所有 VLA 公司 |
| `#可组合泛化` | 将已学技能重新组合完成新任务 | PI (π0.7) |
| `#跨形态泛化` | 同一策略控制多种机器人形态 | PI, DeepMind |
| `#全身控制` | 双臂+躯干+头部+腿部的统一控制 | Figure AI, Boston Dynamics, PI |

---

## 按标签检索报告

### #端到端
- [`reports/figure-ai/`](reports/figure-ai/) — Helix VLA
- [`reports/tesla-optimus/`](reports/tesla-optimus/) — FSD 神经网络
- [`reports/1x-technologies/`](reports/1x-technologies/) — Redwood VLA
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π0/π0.7

### #VLA
- [`reports/figure-ai/`](reports/figure-ai/)
- [`reports/physical-intelligence/`](reports/physical-intelligence/)
- [`reports/1x-technologies/`](reports/1x-technologies/)
- [`reports/google-deepmind/`](reports/google-deepmind/)
- [`reports/apptronik/`](reports/apptronik/) — Gemini VLA 合作
- [`reports/nvidia-isaac/`](reports/nvidia-isaac/) — GR00T VLA 参考设计

### #数据飞轮
- [`reports/tesla-optimus/`](reports/tesla-optimus/)
- [`reports/figure-ai/`](reports/figure-ai/) — BotQ
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π* 在线 RL

### #跨本体
- [`reports/physical-intelligence/`](reports/physical-intelligence/)
- [`reports/google-deepmind/`](reports/google-deepmind/) — Open X-Embodiment

### #低成本
- [`reports/unitree/`](reports/unitree/) — G1 $13.5K

### #物理本质安全
- [`reports/1x-technologies/`](reports/1x-technologies/) — 肌腱驱动 95% 反向可驱动性

### #完全开源
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π0/FAST 权重+代码
- [`reports/google-deepmind/`](reports/google-deepmind/) — Open X-Embodiment 数据集

### #世界模型
- [`reports/1x-technologies/`](reports/1x-technologies/)

### #分层混合
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — MPC + RL + VLA
- [`reports/agility-robotics/`](reports/agility-robotics/) — 传统控制 + 有限学习

### #平台/基础设施
- [`reports/nvidia-isaac/`](reports/nvidia-isaac/) — Isaac Sim + Isaac Lab + GR00T

### #模块化
- [`reports/apptronik/`](reports/apptronik/) — Apollo 上半身可分离 + 末端快换


### #MPC
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — MPC 模型预测控制

### #RL
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π* 在线 RL
- [`reports/unitree/`](reports/unitree/) — RL 运动控制
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — MPC + RL

### #模仿学习
- [`reports/unitree/`](reports/unitree/) — 动作捕捉模仿
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — 遥操作演示
- [`reports/1x-technologies/`](reports/1x-technologies/) — Expert Mode 人类演示

### #FlowMatching
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π0 50Hz
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — Flow Matching 30Hz

### #Diffusion
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — Diffusion Transformer
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — BD+TRI Diffusion Transformer
- [`reports/google-deepmind/`](reports/google-deepmind/) — Gemini 生成模型

### #Transformer
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — 3B VLM 骨干
- [`reports/google-deepmind/`](reports/google-deepmind/) — Gemini Transformer
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — Diffusion Transformer

### #Tokenization
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — FAST: DCT+BPE

### #Sim2Real
- [`reports/unitree/`](reports/unitree/) — 仿真到真实迁移
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — 零样本楼梯迁移
- [`reports/figure-ai/`](reports/figure-ai/) — System 0 零样本部署
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — 仿真预训练

### #合成数据
- [`reports/figure-ai/`](reports/figure-ai/) — BotQ 自主数据生成
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — 合成+真实混合

### #遥操作
- [`reports/1x-technologies/`](reports/1x-technologies/) — Expert Mode
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — 遥操作调试
- [`reports/unitree/`](reports/unitree/) — 动作捕捉 + 遥操作

### #人类视频迁移
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — 人类视频到机器人迁移
- [`reports/tesla-optimus/`](reports/tesla-optimus/) — FSD 视频数据迁移

### #工业制造
- [`reports/figure-ai/`](reports/figure-ai/)
- [`reports/tesla-optimus/`](reports/tesla-optimus/)
- [`reports/boston-dynamics/`](reports/boston-dynamics/)
- [`reports/physical-intelligence/`](reports/physical-intelligence/)
- [`reports/agility-robotics/`](reports/agility-robotics/)
- [`reports/apptronik/`](reports/apptronik/)

### #家用
- [`reports/1x-technologies/`](reports/1x-technologies/) — NEO 家用机器人
- [`reports/enchanted-tools/`](reports/enchanted-tools/) — Miroki 康养
- [`reports/genesis-ai/`](reports/genesis-ai/) — 推测家用场景

### #教育研究
- [`reports/unitree/`](reports/unitree/) — G1 EDU 平台
- [`reports/google-deepmind/`](reports/google-deepmind/) — 学术研究
- [`reports/nvidia-isaac/`](reports/nvidia-isaac/) — Isaac Lab 教学

### #软件安全层
- [`reports/tesla-optimus/`](reports/tesla-optimus/) — Guardian Network
- [`reports/figure-ai/`](reports/figure-ai/) — 力限制器
- [`reports/apptronik/`](reports/apptronik/) — 多层安全监控

### #全身控制
- [`reports/figure-ai/`](reports/figure-ai/) — 双臂+躯干+头部+腿部
- [`reports/boston-dynamics/`](reports/boston-dynamics/) — Atlas 全身 pose
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π0 全身关节

### #可组合泛化
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π0.7 多样化提示

### #跨形态泛化
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π0 跨8种机器人
- [`reports/google-deepmind/`](reports/google-deepmind/) — Open X-Embodiment

### #闭源
- [`reports/tesla-optimus/`](reports/tesla-optimus/)
- [`reports/figure-ai/`](reports/figure-ai/)
- [`reports/1x-technologies/`](reports/1x-technologies/)
- [`reports/boston-dynamics/`](reports/boston-dynamics/)
- [`reports/agility-robotics/`](reports/agility-robotics/)
- [`reports/enchanted-tools/`](reports/enchanted-tools/)

### #部分开源
- [`reports/google-deepmind/`](reports/google-deepmind/) — 数据集+工具
- [`reports/unitree/`](reports/unitree/) — SDK + 驱动

### #语言条件化
- [`reports/figure-ai/`](reports/figure-ai/) — Helix 自然语言指令
- [`reports/physical-intelligence/`](reports/physical-intelligence/) — π0 自然语言
- [`reports/1x-technologies/`](reports/1x-technologies/) — Redwood VLA
- [`reports/google-deepmind/`](reports/google-deepmind/) — Gemini 原生支持
- [`reports/apptronik/`](reports/apptronik/) — Gemini 对话
- [`reports/nvidia-isaac/`](reports/nvidia-isaac/) — GR00T 语言条件化

### #肌腱驱动
- [`reports/1x-technologies/`](reports/1x-technologies/) — 肌腱驱动 95% 反向可驱动性

### #轻量化
- [`reports/unitree/`](reports/unitree/) — H1 47kg, G1 35kg

### #高扭矩密度
- [`reports/unitree/`](reports/unitree/) — 189 N.m/Kg
---

## 多标签交叉检索示例

| 检索需求 | 标签组合 | 结果 |
|---------|---------|------|
| "想找一个开源的、做 VLA 的、支持跨本体的公司" | `#VLA` + `#完全开源` + `#跨本体` | Physical Intelligence |
| "家用场景、物理安全的机器人" | `#家用` + `#物理本质安全` | 1X Technologies |
| "工业级、高可靠性、MPC 控制" | `#工业制造` + `#MPC` + `#分层混合` | Boston Dynamics |
| "低成本、教育研究、开源生态" | `#低成本` + `#教育研究` + `#部分开源` | Unitree |
| "端到端、数据飞轮最强" | `#端到端` + `#数据飞轮` | Tesla |
| "仓储物流专用、RaaS 模式" | `#工业制造` + `#分层混合` + `#数据飞轮` | Agility Robotics |
| "模块化硬件、Google AI 加持" | `#VLA` + `#模块化` + `#工业制造` | Apptronik |
| "仿真平台、基础设施" | `#平台/基础设施` + `#Sim2Real` + `#合成数据` | NVIDIA Isaac |
| "服务康养、小巧亲和" | `#家用` + `#物理本质安全` | Enchanted Tools |
| "Human-Level 宣称、全栈方案" | `#VLA` + `#灵巧手` | Genesis AI |
