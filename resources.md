# 具身智能开源资源汇总

> 整理具身智能领域可获取的开源资源，包括模型权重、数据集、仿真器、开发工具等。  
> 标注了可用性状态（✅ 完全开源 / ⚠️ 部分开源 / 🔒 闭源但可申请）。

---

## 一、开源模型权重

### Physical Intelligence (π)

| 资源 | 类型 | 链接 | 状态 |
|------|------|------|------|
| **π0** | 通用机器人 VLA 策略 | [GitHub: physical-intelligence/pi0](https://github.com/physical-intelligence/pi0) | ✅ 完全开源（权重+代码） |
| **π0-FAST** | 带 FAST Tokenization 的 π0 | 同上 | ✅ 完全开源 |
| **π0.5 / π0.7** | 后续版本 | — | 🔒 闭源（仅技术报告） |

**说明**：PI 是目前开源程度最高的具身智能公司之一，π0 和 FAST 的权重与训练代码均已公开，学术界可基于此进行复现和改进。

---

### Google DeepMind

| 资源 | 类型 | 链接 | 状态 |
|------|------|------|------|
| **RT-1 / RT-2 架构参考** | VLA 模型架构 | [arXiv 论文](https://arxiv.org/abs/2307.15818) | ⚠️ 论文开源，权重未开源 |
| **RT-X 训练代码** | 训练框架 | [GitHub: google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment) | ✅ 训练代码开源 |
| **Gemini Robotics** | VLA 模型 | — | 🔒 闭源（通过 API/合作伙伴提供） |

**说明**：DeepMind 倾向于开源**方法和数据集**，而非直接开源模型权重。可通过 Google AI Studio 申请 Gemini Robotics 的早期访问。

---

### 其他开源模型

| 资源 | 类型 | 作者 | 链接 | 状态 |
|------|------|------|------|------|
| **OpenVLA** | 开源 VLA 模型 | Stanford / Berkeley | [GitHub: openvla/openvla](https://github.com/openvla/openvla) | ✅ 完全开源 |
| **Octo** | 开源通用机器人策略 | Berkeley / Stanford | [GitHub: octo-models/octo](https://github.com/octo-models/octo) | ✅ 完全开源 |
| **Diffusion Policy** | 扩散策略实现 | Columbia / MIT | [GitHub: real-stanford/diffusion_policy](https://github.com/real-stanford/diffusion_policy) | ✅ 完全开源 |
| **ACT (Action Chunking)** | 模仿学习框架 | Stanford | [GitHub: tonyzhaozh/act](https://github.com/tonyzhaozh/act) | ✅ 完全开源 |
| **RDT (Robotics Diffusion Transformer)** | 开源 Diffusion Transformer | 清华 / 上海 AI Lab | [GitHub: thu-ml/RDT](https://github.com/thu-ml/RDT) | ✅ 完全开源 |
| **SPOC** | 语义策略与对象中心表示 | AI2 | [GitHub: allenai/spoc](https://github.com/allenai/spoc) | ✅ 完全开源 |

---

## 二、开源数据集

### 跨本体数据集

| 数据集 | 规模 | 描述 | 链接 | 状态 |
|--------|------|------|------|------|
| **Open X-Embodiment** | 1600万+ 轨迹 | 全球最大跨机器人数据集，22 种形态 | [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/open_x_embodiment) | ✅ 完全开源 |
| **DROID** | 大规模真实世界数据 | Stanford 主导的真实机器人操作数据 | [GitHub: ailab-dvrk/droid](https://github.com/ailab-dvrk/droid) | ✅ 完全开源 |
| **BridgeData V2** | 6万+ 轨迹 | Berkeley 的厨房操作数据 | [GitHub](https://github.com/rail-berkeley/bridge_data_v2) | ✅ 完全开源 |
| **RoboSkills / RoboSkills-X** | 多任务数据集 | 多种技能的长程操作数据 | 各研究机构发布 | ⚠️ 部分开源 |

### 人形机器人专用数据

| 数据集 | 来源 | 描述 | 状态 |
|--------|------|------|------|
| **Figure BotQ 数据** | Figure AI | 大规模自主生成的合成+真实数据 | 🔒 闭源 |
| **Tesla Optimus 数据** | Tesla | 来自工厂部署的真实操作数据 | 🔒 闭源 |
| **Humanoid-Gym** | 社区 | 人形机器人仿真训练环境 | ✅ 开源 |

### 人类视频数据集

| 数据集 | 规模 | 描述 | 链接 | 状态 |
|--------|------|------|------|------|
| **Ego4D** | 3000+ 小时第一视角视频 | Meta 发布的日常活动视频 | [ego4d-data.org](https://ego4d-data.org/) | ✅ 完全开源 |
| **Something-Something V2** | 22万 视频片段 | 日常物体交互视频 | [TwentyBN](https://20bn.com/datasets/something-something) | ✅ 完全开源 |
| **Epic-Kitchens** | 100+ 小时厨房视频 | 第一视角厨房操作 | [epic-kitchens.github.io](https://epic-kitchens.github.io/) | ✅ 完全开源 |

---

## 三、仿真器与训练平台

| 平台 | 作者 | 描述 | 链接 | 状态 |
|------|------|------|------|------|
| **Isaac Sim / Isaac Gym** | NVIDIA | 基于 Omniverse 的高性能物理仿真，支持 GPU 并行 RL 训练 | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) | ✅ 免费（需注册） |
| **MuJoCo** | DeepMind | 经典物理引擎，机器人学标准仿真器 | [GitHub: deepmind/mujoco](https://github.com/deepmind/mujoco) | ✅ 完全开源 |
| **Genesis** | Genesis Embodied AI | 新兴的统一物理仿真平台，支持多种物理求解器 | [GitHub: Genesis-Embodied-AI/Genesis](https://github.com/Genesis-Embodied-AI/Genesis) | ✅ 完全开源 |
| **SAPIEN** | UCSD / 港中文 | 面向机器人学习的物理仿真平台，强调零件级交互 | [GitHub: sapien-sim/sapien](https://github.com/sapien-sim/sapien) | ✅ 完全开源 |
| **PyBullet** | Bullet Physics | 轻量级物理仿真，适合快速原型 | [GitHub: bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) | ✅ 完全开源 |
| **RoboSuite** | Stanford | 基于 MuJoCo 的模块化机器人仿真套件 | [GitHub: ARMLabRobosuite](https://github.com/ARMLabRobosuite) | ✅ 完全开源 |
| **Habitat** | Meta AI | 室内导航与具身 AI 仿真平台 | [GitHub: facebookresearch/habitat-sim](https://github.com/facebookresearch/habitat-sim) | ✅ 完全开源 |
| **AI2-THOR** | AI2 | 室内环境交互仿真，近真实感渲染 | [GitHub: allenai/ai2thor](https://github.com/allenai/ai2thor) | ✅ 完全开源 |

---

## 四、机器人开发框架与工具

| 工具 | 类型 | 描述 | 链接 | 状态 |
|------|------|------|------|------|
| **ROS 2** | 机器人中间件 | 机器人操作系统行业标准 | [ros.org](https://www.ros.org/) | ✅ 完全开源 |
| **LeRobot** | 训练框架 | Hugging Face 推出的机器人学习框架，支持模仿学习、VLA 训练 | [GitHub: huggingface/lerobot](https://github.com/huggingface/lerobot) | ✅ 完全开源 |
| **RoboSkills** | 数据集+框架 | 机器人技能学习框架 | 各研究组发布 | ⚠️ 部分开源 |
| **RoboHive** | 训练框架 | 从仿真到真实的迁移学习框架 | [GitHub:vikashplus/robohive](https://github.com/vikashplus/robohive) | ✅ 完全开源 |
| **DexPilot** | 遥操作框架 | 基于视觉的灵巧遥操作系统 | [GitHub](https://github.com//) | ⚠️ 部分开源 |

---

## 五、硬件平台与参考设计

| 平台 | 公司/机构 | 描述 | 价格 | 状态 |
|------|-----------|------|------|------|
| **Unitree G1** | 宇树科技 | 小型人形机器人，教育/研究定位 | **$13,500** | ✅ 可购买 |
| **Unitree G1 EDU** | 宇树科技 | G1 教育版，支持二次开发 | 联系销售 | ✅ 可购买 |
| **Unitree H1/H1-2** | 宇树科技 | 全尺寸人形机器人 | 联系销售 | ✅ 可购买 |
| **Trossen Robotics VX300 / WidowX** | Trossen | 低成本双臂/单臂研究平台 | $3K-$8K | ✅ 可购买 |
| **Franka Emika Panda** | Franka | 7 自由度协作机械臂（研究标准） | ~$30K | ✅ 可购买 |
| **ALOHA 2** | Stanford / Google | 低成本双臂遥操作平台 | ~$20K（自组更低） | ✅ 开源硬件设计 |
| **Mobile ALOHA** | Stanford | 移动版 ALOHA，轮式底座+双臂 | ~$30K（自组更低） | ✅ 开源硬件设计 |
| **Berkeley Humanoid** | Berkeley | 开源人形机器人设计 | 自组成本 ~$10K | ✅ 开源硬件设计 |

---

## 六、宇树科技开源资源

宇树是**人形机器人领域开源生态最活跃的公司**：

| 资源 | 链接 | 说明 |
|------|------|------|
| **GitHub 主页** | [github.com/unitreerobotics](https://github.com/unitreerobotics) | 官方代码仓库 |
| **Go2 SDK** | Go2 机器人 SDK | 四足机器人开发工具包 |
| **G1/H1 SDK** | 人形机器人 SDK | 控制接口和示例代码 |
| **仿真接口** | Isaac Sim / MuJoCo 接口 | 仿真环境适配 |
| **运动控制算法** | 部分开源 | RL 训练的控制策略 |
| **文档中心** | [support.unitree.com](https://support.unitree.com) | 中英文开发文档 |

---

## 七、评估基准与排行榜

| 基准 | 描述 | 链接 |
|------|------|------|
| **Open X-Embodiment Benchmark** | 跨本体通用能力评估 | 随数据集一起提供 |
| **LIBERO** | 长程机器人操作基准 | [GitHub](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| **CALVIN** | 语言条件化长程任务基准 | [GitHub](https://github.com/mees/calvin) |
| **RLBench** | 大规模机器人学习基准 | [GitHub](https://github.com/stepjam/RLBench) |
| **ManiSkill** | 大规模并行机器人操作基准 | [GitHub](https://github.com/haosulab/ManiSkill) |
| **SimplerEnv** | 真实到仿真的视觉操作评估 | [GitHub](https://github.com/simpler-conversation/SimplerEnv) |

---

## 八、学习资源

| 资源 | 类型 | 描述 | 链接 |
|------|------|------|------|
| **Hugging Face LeRobot 教程** | 教程 | 从零开始训练机器人策略 | [huggingface.co/lerobot](https://huggingface.co/lerobot) |
| **Stanford CS329R** | 课程 | Robotic Learning and Control | [课程页面](https://web.stanford.edu/class/cs329r/) |
| **Berkeley CS285** | 课程 | Deep Reinforcement Learning | [课程页面](http://rail.eecs.berkeley.edu/deeprlcourse/) |
| **The Robot Brains Podcast** | 播客 | 具身智能行业访谈 | [播客](https://www.therobotbrains.ai/) |
| **Two Minute Papers** | 视频 | AI 论文快速解读（含机器人） | [YouTube](https://www.youtube.com/c/K%C3%A1rolyZsolnai) |

---

## 使用建议

### 如果你想快速上手 VLA 训练

1. **硬件**：ALOHA 2 双臂平台（~$20K）或 Unitree G1 EDU（$13.5K）
2. **仿真**：Isaac Sim 或 Genesis 进行策略预训练
3. **框架**：LeRobot（Hugging Face）提供完整的训练 pipeline
4. **数据**：Open X-Embodiment + 自采数据
5. **模型**：从 OpenVLA 或 π0 开源权重开始微调

### 如果你只想做算法研究

1. **仿真**：MuJoCo + RoboSuite 或 Genesis
2. **数据**：Open X-Embodiment + BridgeData V2
3. **框架**：LeRobot 或自研 PyTorch 代码
4. **基准**：LIBERO 或 CALVIN 评估长程任务能力
