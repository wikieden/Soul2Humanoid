# WAM 世界动作模型落地全景（World Action Model Landscape）

> 调研日期：**2026-08-16**
> 核心来源：各公司官网 / 官方博客、arXiv、WAIC 2026 现场报道；仓库内交叉引用于 [`comparisons.md`](./comparisons.md)（第十节）与 [`latest-news.md`](./latest-news.md)。
> 一句话定位：**WAM（World Action Model，世界动作模型）把「预测世界如何演化」与「生成机器人动作」放进同一个模型**，区别于以 VLM 为骨干的 VLA——后者学「如何做」，WAM 学「世界会怎么变 + 该怎么动」。

---

## 一、概念与背景

**溯源**：2025 年底 NVIDIA GEAR 负责人 **Jim Fan** 在 *Robotics' End Game* 演讲中提出具身智能的下一前沿是 World Action Model（后被概括为「VLAs are dead, long live World Action Models」）；NVIDIA 于 **2026-06-15**（Seattle Robotics Lab，Moritz Reuss，《Pretrained to Imagine, Fine-Tuned to Act》）与 **2026-08-04**（*Beyond VLAs: How World Action Models Reshape Robot Manipulation*）两次以官方博客正式阐述该范式。

**VLA vs WAM 对比**：

| 维度 | VLA（Vision-Language-Action） | WAM（World Action Model） |
|------|------------------------------|--------------------------|
| 骨干 | 预训练 VLM（语言视觉） | 预训练视频 / 世界模型（物理动态） |
| 核心学习目标 | 观测 → 动作映射 | 世界状态演化 + 动作联合建模 |
| 数据依赖 | 大量近似同任务轨迹（遥操作） | 可利用异构数据（纯视频 / 无任务标签 / 多本体轨迹） |
| 泛化类型 | 语义泛化强，物理泛化弱 | 物理泛化强（未见过场景 / 本体 / 动作） |
| 代表 | Pi-0/0.5、GR00T N1 | Motubrain、Cosmos 3、Gravity 4D、LingBot-VA 等 |

**三条主流技术路线**：

1. **逆动力学（Inverse Dynamics）**：先生成 / 预测未来视频，再反推动作（UniPi 2023 提出，LingBot-VA 等放大）。
2. **联合预测（Joint video-action prediction）**：视频 + 动作在一个生成框架里统一建模，一次训练得到 VLA / 世界模型 / 视频生成 / 逆动力学 / 联合预测五种推理模式（生数 Motubrain、NVIDIA Cosmos 3）。
3. **4D latent 物理监督**：在 latent 空间同时监督 RGB 外观 + 三维空间结构（Pointmap）+ 三维运动（Scene Flow），训练「物理直觉」（极智嘉 Gravity 4D）。

---

## 二、已上真机（部署级）

> 截至 2026-08-16，能确认真机运行 / 商业部署的 WAM 玩家集中在**数据最易闭环**的场景：商用陪伴（越疆）、真实家庭（未来不远）、仓储物流（极智嘉）。

| 公司 | 模型 | 技术路线 | 真机落点 / 关键数据 | 来源 |
|------|------|---------|--------------------|------|
| **越疆 Dobot** | **空弈 DobotWAM** | VLA + WAM 融合，强调三维空间理解 + 数据闭环 | **LIBERO 基准 99.25% 成功率第一**；ATOM 电影院场景单日 14h、1,000+ 杯爆米花；LUMO 2026/8/5 发布，一脑多体（ATOM / LUMO / 四足共用底座） | [`comparisons.md`](./comparisons.md) |
| **未来不远 Futuring** | **Self-Evolving WAM**（自进化） | 执行前模拟后果、反事实推理 + Judge 挑选数据 | **F2 已进 500+ 真实家庭、5 万小时、10TB 数据**；WAIC 2026 首发；Pre-A 近 10 亿元（字节 / 汇川产投 / 纳爱斯） | [`comparisons.md`](./comparisons.md) |
| **极智嘉 Geek+** | **Gravity 4D WAM** | **4D latent 监督**（RGB + Pointmap + Scene Flow），4D-VAE 蒸馏 + WAM 推演 / IDM 反推动作两阶段 | **仓储场景首个落地模块**（WAIC 7/17）：Gino 1 真机拣选 / 抱箱 / 多机编队，全身并行控制单任务 -30%；LIBERO-Plus 零样本 73.73% → 78.62%（role-embedded 79.25%） | 新华网 2026/7/19、Geek+ 官网、机器人大讲堂 7/17 |
| **蚂蚁 Robbyant（灵波）** | **LingBot-VA 2.0** | 原生世界模型，逆动力学范式 | WAIC 2026 发布；同期开源 LingBot-VLA 2.0（60K 小时 / 20 形态） | [`latest-news.md`](./latest-news.md) |
| **智在无界** | **Being-H0.8** | **首个引入触觉模态**的隐式世界动作模型 | 触觉伪标签系统 TactoHand 将触觉信息扩展至 **50 万小时**；TopoHand 统一动作空间 | [`latest-news.md`](./latest-news.md) |

> ⚠️ 越疆 / 未来不远 / 极智嘉为明确真机 / 商业部署；LingBot-VA 2.0、Being-H0.8 为「模型已发布、真机规模化部署在途」，此处按发布口径归入部署级以保留上下文，实际落地进度以官方为准。

---

## 三、已发布 / 在途（模型级，真机规模化在路上）

| 公司 | 模型 | 亮点 | 时间 / 来源 |
|------|------|------|------------|
| **生数科技** | **Motubrain**（通用世界动作模型） | **UniDiffuser 统一建模视频 + 动作**，三流 MoT（视频 / 动作 / 语言）架构；一次训练即可推理 VLA / 世界模型 / 视频生成 / 逆动力学 / 联合预测五种模式；**WorldArena + RoboTwin 2.0 双榜第一**（50 任务平均 96.0，随机环境唯一 >95 的模型）；50–100 条同样本数据快速适配新本体；前代 **Motus** 2025/12 开源（官方称超 Pi0.5 40%） | 2026/4/29；[生数官网](https://www.shengshu.com/zh/news/motubrain-world-action-model/)、[arXiv 2604.27792](https://arxiv.org/html/2604.27792v3) |
| **Dyna Robotics** | **Dyna-2** | **100 万小时人类视频**世界动作模型；提出人 → 机迁移 scaling law；未知任务零样本灵巧操作，挑战 VLA 主流 | 2026/8/10；[`latest-news.md`](./latest-news.md) |
| **NVIDIA** | **Cosmos 3** | 开源**全模态世界基础模型**（MoT 架构），原生动作生成（关节角度 / 夹爪 / 轨迹），支持正动力学 / 逆动力学 / 联合预测三种模式；官方定位「WAM 的强骨干」；GEAR 团队基于其开发视频动作模型 | 2026-08-04；[NVIDIA Developer Blog](https://developer.nvidia.com/blog/beyond-vlas-how-world-action-models-reshape-robot-manipulation/)、[Cosmos 3 技术报告](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf) |
| **极佳视界** | **GigaBrain 1** | 家庭场景具身大模型（拾光 S1 配套），2026 Q3 推出 | [`comparisons.md`](./comparisons.md) |
| **智元 AGIBOT** | **GE-2 世界模型** | 「三智合一」架构：GO-2（VLA）+ GE-2（世界模型）+ BFM-2（运动基座） | README 公司表 |
| **阿里巴巴** | **Qwen-Robot World** | Manip（VLA）+ Nav（VLN）+ World 三件套，开源数据训练 | [`latest-news.md`](./latest-news.md) |
| **它石智航** | **AWE 3.5** | WAIC 2026「大脑成为主战场」主线之一；近百台已在客户现场投入作业，下半年继续交付 | [`latest-news.md`](./latest-news.md) |
| **戴盟机器人** | **触觉世界模型** | 原生触觉 WM，完成「水果装盒、笔袋收纳」等长时序操作 | [`latest-news.md`](./latest-news.md) |
| **1X Technologies**（美国） | World Model + NEO | 2026/6 成立 **World Model Lab**（Luma AI 研究员加盟），NEO 家用机器人 + $499/月 RaaS | [`latest-news.md`](./latest-news.md) |

---

## 四、学术线（解决落地硬伤：实时延迟与 sim-to-real）

> WAM 的头号工程瓶颈是**视频生成拖慢控制频率**——同步式 WAM 真机不可用（论文对比：Motus 单步延迟 1866ms / 0.54Hz）。以下工作正面打这个痛点。

| 团队 | 工作 | 关键结果 | 时间 / 来源 |
|------|------|---------|------------|
| **上交 ScaleLab × 上海 AI Lab × 百度百舸** | **AHA-WAM**（异步视野自适应世界动作模型） | 「慢世界规划 + 快动作执行」双 DiT 异步解耦；无机器人数据预训练在 RoboTwin 2.0 达 **92.80%**、真机 4 任务 **78.3%**；闭环控制 **24.17 Hz**（AHA-WAM-Flash **56.95 Hz**，比 Fast-WAM 快 4.59×）；单步推理 415ms → **41ms**（10×） | arXiv [2606.09811](https://arxiv.org/html/2606.09811v1)（2026/6/8）；[百度智能云技术站](https://juejin.cn/post/7651183007398838335) |
| **普渡大学** | WAM sim-to-real（Cosmos Policy） | **800 条纯仿真示教、零真实数据**上 Franka 真机，4 任务平均 35%（优于 50 条真实示教的 Diffusion Policy 25%）——首次证明 WAM 跨过 sim-to-real | arXiv [2606.31101](https://arxiv.org/abs/2606.31101)（2026/6/30） |
| **NVIDIA** | *World Action Models are Zero-shot Policies* | 联合预测视频 + 动作即获得零样本策略性质（数据利用 / 开放世界泛化 / 少样本适配新本体） | 引用于 2026-08-04 官方博客 |

---

## 五、关键观察

1. **真机部署目前就三家，且各选「数据最易闭环」的场景**：越疆（商用陪伴，电影院单日 14h）、未来不远（真实家庭，500 户 / 5 万小时）、极智嘉（仓储，百万 SKU 拣选）——符合「数据在哪、WAM 先落地在哪」的规律。
2. **路线已细分，无单一收敛架构**：逆动力学（LingBot-VA / UniPi 系）、联合预测 / MoT（Motubrain、Cosmos 3）、4D latent 物理监督（Gravity 4D）、触觉双模态（Being-H0.8 / 戴盟）、人类视频预训练（Dyna-2）、自进化（未来不远）。
3. **WAM 落地最大硬伤是实时延迟**：视频生成与高频控制的节奏错配。两条解法并行——**异步架构**（AHA-WAM「想得慢、动得快」）与**推理加速**（Motubrain 端到端 >50× 提速、FP8 / DiT 缓存 / 去噪步压缩）。
4. **VLA 没死，正在合流**：Motubrain「一次训练覆盖 VLA」、越疆 VLA + WAM 融合、阿里 / 智元把世界模型做成 VLA 组件；NVIDIA 判断「最终赢家很可能是 VLA + WAM 的混合体」——「动作头 + 物理先验」而非二选一。

---

## 六、信息来源

| 来源 | 时间 | 覆盖 |
|------|------|------|
| 生数科技官网（Motubrain 发布页 / motubrain.com）/ arXiv 2604.27792 | 2026/4/29 | 生数 Motubrain（UniDiffuser、三流 MoT、双榜第一、Motus 前代） |
| 新华网 / Geek+ 官网 / 腾讯新闻 / 机器人大讲堂 | 2026/7/17–7/20 | 极智嘉 Gravity 4D WAM（4D latent、两阶段推理、Gino 1 真机、LIBERO-Plus 数字） |
| NVIDIA Developer Blog（*Beyond VLAs*） / Cosmos 3 技术报告 | 2026/8/4 | WAM 概念定义、VLA vs WAM、Cosmos 3 开源全模态世界模型 |
| 百度智能云技术站 / arXiv 2606.09811 | 2026/6/15 | AHA-WAM（异步双 DiT、24.17/56.95 Hz、415→41ms） |
| arXiv 2606.31101（普渡） | 2026/6/30 | WAM 纯仿真 sim-to-real（800 条 / 零真实数据 / 35%） |
| [`latest-news.md`](./latest-news.md) | 2026/6–8 | Dyna-2、Being-H0.8、LingBot-VA 2.0、它石 AWE 3.5、戴盟、1X World Model Lab、阿里 Qwen-Robot |
| [`comparisons.md`](./comparisons.md) | 2026/8/16 | 越疆空弈 WAM、未来不远 Self-Evolving WAM、极佳 GigaBrain |

> 注意：各家「部署户数 / 订单 / 成功率」多为公司自述或官方发布口径，未经第三方审计；技术参数以各论文 / 官网为准。
