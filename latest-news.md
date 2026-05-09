# 2026 年 4-5 月最新动态追踪

> 基于 Humanoids Daily、公司官方博客、X/Twitter 等来源整理的最新行业动态。
> 更新日期：2026-05-08

---

## 快速导航

| 公司 | 核心动态 | 位置 |
|------|---------|------|
| **Figure AI** | 24x 制造提速、System 0、Never Fall、$400-600/月租赁 | [↓](#figure-ai--制造跃迁--ai-突破) |
| **1X Technologies** | NEO Factory 58K sqft、垂直整合、100K/年目标 | [↓](#1x-technologies--垂直整合工厂曝光) |
| **Unitree** | 双臂 R1 $4,290、$5.8亿 IPO | [↓](#unitree-宇树--双臂平台--ipo) |
| **Boston Dynamics** | C-Suite 大出走、Hyundai 30K/年压力 | [↓](#boston-dynamics--高管出走--量产压力) |
| **Apptronik** | $9.35 亿融资、Waymo/BD/Amazon Dream Team | [↓](#apptronik--935-亿融资--梦之队) |
| **Agility** | Peggy Johnson 新任 CEO | [↓](#agility-robotics--新-ceo-愿景) |
| **Meta** | 收购 Assured Robot Intelligence | [↓](#meta--收购入场) |
| **Genesis AI** | GENE-26.5 Human-Level 宣称 | [↓](#genesis-ai--新玩家) |

---

## Figure AI — 制造跃迁 + AI 突破

**2026.04.29** — BotQ 产线 120 天内制造吞吐量提升 **24 倍**：从 1 台/天 → 1 台/小时
- 已交付 **350+ 台 Figure 03**，本周目标制造 55 台
- 产线良率：终检通过率 80%，电池线良率 99.3%
- 已生产 9,000+ 台定制执行器（10 个 SKU）
- 每台机器人出厂前通过 80 项功能验证测试

**2026.04.29** — 发布 **System 0 (S0)** AI 模型
- 感知条件化全身控制器：将 RGB 图像集成到控制策略中
- 实现 **零样本 (zero-shot)** 楼梯/不平地面行走
- 完全在仿真中训练，无需真实世界微调即可部署

**2026.05.01** — 深度访谈披露更多细节
- **"Never Fall" 协议**：Vulcan AI 策略，即使腿部机械故障也能保持站立/跛行到维护区
- **Helix 02** 全部在板载 GPU 运行，**不需要网络连接**
- 2kW 无线感应充电（脚底），续航 4-5 小时，充电 1 小时
- 家用机器人租赁模型：**$400-600/月**（类似汽车租赁）
- 第 7 代灵巧手已展示
- Figure 4 设计中："iPhone 1 时刻"

来源：[Humanoids Daily](https://www.humanoidsdaily.com/news/24x-throughput-figure-scales-manufacturing-to-one-robot-per-hour), [Figure AI 官方](https://www.figure.ai/news/ramping-figure-03-production)

---

## 1X Technologies — 垂直整合工厂曝光

**2026.04.30** — 公开 **NEO Factory**（Hayward, CA）
- 58,000 平方英尺，200+ 员工，3 个月内建成
- **全垂直整合**：Revo2 电机、电池、肌腱、22-DoF 手全部自产
- 已生产 17,000 台 Revo2 电机
- 初始产能 10,000 台/年（预售 5 天售罄）
- **San Carlos 第二工厂**规划中：目标 2027 年底达 **100,000 台/年**

**NEO 硬件规格更新**
- **NEO Cortex**：NVIDIA Jetson Thor SoC
- 双 8.85MP 鱼眼立体相机，90Hz
- 波束成形麦克风 + 板载实时 AI 推理
- 当前产品优先用于**内部员工家庭测试**，消费版 2026 年交付
- NEO 已在工厂内自主执行物流和零件搬运任务

来源：[Humanoids Daily](https://www.humanoidsdaily.com/news/1x-goes-vertical-inside-the-hayward-factory-aiming-for-100-000-humanoids), [1X 官方](https://www.1x.tech/discover/neo-factory)

---

## Unitree 宇树 — 双臂平台 + IPO

**2026.04.30** — 发布 **Dual-Arm Humanoid Robot** 双臂平台
- 起售价 **$4,290**
- 4 种配置：R1-A5 / R1-A7（固定底座），R1-A5-D / R1-A7-D（轮式底座）
- 15-31 自由度，末端精度 ±0.1mm
- 基础算力 10 TOPS，可选 Jetson Orin（40-100 TOPS）
- 双目相机 + 深度图（544x448@10Hz）+ 4 阵列麦克风
- 轮式版续航约 1.5 小时

**IPO 动态**
- 据报道宇树已申请 **$5.8 亿 IPO**
- 2026 年出货目标 **20,000 台**
- CEO 王兴兴提出具身 AI 的"80/80"目标：80% 任务 80% 成功率

来源：[Humanoids Daily](https://www.humanoidsdaily.com/news/unitree-expands-r1-lineup-with-dual-arm-modular-platform-starting-at-4-290)

---

## Boston Dynamics — 高管出走 + 量产压力

**2026.05.05** — "C-Suite 大出走"
- CEO **Robert Playter** 2026 年 2 月退休（30+ 年生涯）
- CTO **Aaron Saunders** 离职加入 Google DeepMind
- VP 机器人研究 **Scott Kuindersma** 2026 年 1 月离职
- CSO、COO 也已离职

**Hyundai 量产压力**
- 董事会要求加速商业化，Hyundai 要求在汽车工厂部署"数万台"人形机器人
- 当前产能：约 **4 台 Atlas/月**
- 目标产能：**30,000 台/年**
- Kia 部署路线图：HMGMA 工厂 2028 年全面运营

**技术进展**
- 发布量产版 Atlas 首支视频：倒立、360° 执行器旋转
- 公司声明："平衡商业目标与机器人研究很困难，但 Atlas 让这一切可行"

来源：[Humanoids Daily](https://www.humanoidsdaily.com/news/the-production-pivot-leadership-exodus-and-internal-pressure-at-boston-dynamics), [Semafor](https://www.semafor.com/article/05/01/2026/c-suite-exodus-at-boston-dynamics)

---

## Apptronik — $9.35 亿融资 + 梦之队

**2026.04.29** — 高管团队大扩军
- **$9.35 亿总融资**（含 $5.2 亿 Series A-X 延伸）
- **Daniel Chu** 任 CPO：前 Waymo 首席产品官，自动驾驶→人形机器人
- **Kevin Garell** 任 SVP 服务与支持：前 Boston Dynamics
- **Chirag Shah** 任 VP 软件：前 Amazon Alexa/AI 多模态
- **Dave Perry** 任 VP 市场：前 Paramount+/Amazon

**路线图**
- 下一代人形机器人即将公布（"significant jump up"）
- 三阶段路线：物流 → 医疗保健 → 家庭
- CEO Cardenas：人形机器人是"我们时代的太空竞赛"，美国仅 <5 家公司有实力

来源：[Humanoids Daily](https://www.humanoidsdaily.com/news/apptronik-raids-tech-giants-for-executive-dream-team-ahead-of-new-robot-reveal)

---

## Agility Robotics — 新 CEO 愿景

**2026.05.07** — CEO Peggy Johnson 在 Abundance Summit 2026 演讲
- 提出"Unconstrained Humanoids"愿景：让 Digit 走出仓库围栏，进入更广泛场景
- *注：Peggy Johnson 为新任 CEO，接替创始人 Damion Shelton*

来源：[Humanoids Daily](https://www.humanoidsdaily.com/news/breaking-the-cage-agility-ceo-peggy-johnson-outlines-vision-for-unconstrained-humanoids-at-abundance-summit-2026)

---

## Meta — 收购入场

**2026.05.01** — 收购 **Assured Robot Intelligence**
- 目标：为人形机器人开发"操作系统"级基础软件
- 标志 Meta 正式进入人形机器人硬件领域
- 尽管近期 AI 研究部门领导层变动，仍大力推进

来源：[Humanoids Daily](https://www.humanoidsdaily.com/news/meta-acquires-assured-robot-intelligence-to-bolster-humanoid-ambitions)

---

## 行业趋势观察

1. **制造量产竞赛白热化**：Figure（1 台/小时）、1X（10K/年目标）、宇树（20K 出货目标）竞速量产
2. **高管离职潮**：BD 的 C-Suite 出走、人才流向 Figure/1X/DeepMind，反映行业从研究向商业转型的阵痛
3. **垂直整合成为共识**：1X 全自产电机+肌腱+手，Figure 自产执行器，供应链自主可控
4. **家用市场提前布局**：Figure 租赁模型 $400-600/月，1X 内部家庭测试，Apptronik 三阶段路线
5. **新玩家入场**：Meta 收购 Assured Robotics，宇树双臂平台 $4,290 拓展开发者生态；**Genesis AI** 发布 GENE-26.5 宣称 Human-Level（⚠️待验证）
6. **安全/可靠性成为核心指标**：Figure "Never Fall"、80 项出厂测试、OTA 更新+Fleet 管理

---

*数据来源：Humanoids Daily、公司官方博客、Semafor、X/Twitter*
*下次更新建议：2026 年 6 月初*
