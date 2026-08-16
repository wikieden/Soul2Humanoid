# 更新日志

> 记录 Soul2Humanoid 仓库的演进历史，按时间倒序排列。

---

## 2026-08-16

### 新增

- **latest-news.md 新增 8/1–8/16 章节**：13 条新动态，覆盖宇树科技科创板 IPO 配售结果（发行价 150.8 元 / 发行市值约 610 亿 / 发行 PE 219 倍 / 网下超 5000 倍 / 95 家公募获配 18.2 亿 / 累计双足 1.8 万台）、**DeepSeek 1.41 亿元战配 + 36 个月《战略合作备忘录》**（互为优先采购）、WRC 2026 前瞻（国资委「中央企业机器人创新联合体」）、第二届世界人形机器人运动会备战（666 支队伍 / 2056 台）、央视财经 H1 具身智能融资 935 亿元（同比 5 倍）、LG × NVIDIA GR00T 双足人形 MOU、SAG H1 全球出货 1.91 万台（+272%）、Dyna-2（100 万小时人类视频）、Figure 肌腱灵巧手争议、X Square 1816 件/时直播分拣、San Mateo County 商用机器人条例、EAI 大会「能用化」评价标准之变、部件动态（Schaeffler / Sony）
- **快速导航表**：新增 8/6–8/16 共 6 行，时间线延伸至 8 月 16 日
- **comparisons.md 新增「十、家庭服务机器人赛道对比（2026 国内厂商）」**：10 家厂商横向对比（未来不远 / 乐享·元点 / 极佳拾光 S1 / 卧安 SwitchBot / 星尘智能 Astribot / 越疆 LUMO / 优必选 U1 / 松延动力 / 宇树 R1 / 追觅 Cyber 10 Ultra），覆盖产品形态、价格带、大脑模型、家庭数据策略、商业化进展 + 数据飞轮两派分析 + VLA→WAM 模型竞赛 + 与海外 1X / Weave 家庭线横评 + 风险与信息来源
- **新增 [`wam-landscape.md`](./wam-landscape.md)（WAM 世界动作模型落地全景）**：概念溯源（Jim Fan / NVIDIA 8/4 官方解读、VLA vs WAM 对比、三条技术路线）+ 已上真机部署（越疆空弈 99.25%、未来不远 500 家庭 / 5 万小时、极智嘉 Gravity 4D 仓储、LingBot-VA 2.0、Being-H0.8）+ 模型级发布（生数 Motubrain WorldArena / RoboTwin 2.0 双榜第一、Dyna-2 100 万小时、NVIDIA Cosmos 3、GigaBrain、GE-2、Qwen-Robot World、AWE 3.5、戴盟触觉 WM）+ 学术线（AHA-WAM 24.17/56.95 Hz、普渡 WAM sim-to-real）+ 四条关键观察 + 信息来源；外部新实体均经官网 / 新华网 / NVIDIA Blog / arXiv 核验

### 更新

- **README.md 最新动态**：新增 `2026-08-16` 表格（9 条事件）；Last Updated badge 更新为 `2026--08--16`
- **README.md 参考资源表**：`comparisons.md` 描述补充「2026 国内家庭服务机器人赛道对比（10 家厂商）」；2026-08-16 最新动态表新增家庭服务机器人赛道调研一行 + **WAM 落地全景**一行；参考资源表新增 `wam-landscape.md`
- **mkdocs.yml / sync_docs.py**：`wam-landscape.md` 注册进「横向分析」导航组与 docs 同步清单

### 关键事件汇总

| 维度 | 8/1–8/16 关键事件 |
|------|-------------------|
| **宇树 IPO** | 发行价 150.8 元 / 市值约 610 亿 / 网下超 5000 倍 / 公募获配 18.2 亿；「A 股人形机器人第一股」预计 8 月下旬敲钟（与 WRC 撞期） |
| **模型+本体绑定** | DeepSeek 1.41 亿战配（0.23%、36 个月锁定期）+ 双向优先采购备忘录：联合研发 AGI、DeepSeek 具身业务优先用宇树、宇树具身大模型优先用 DeepSeek |
| **出货量数据** | SAG：H1 全球 1.91 万台（同比 +272%）、前十全华系、前五全中国企业（智元 > 宇树 > 银河通用 > 优必选 > 乐聚）、智元+宇树占 70%+；2026 全年预计 6 万台 |
| **资本** | H1 国内具身智能融资 935 亿元（同比 5 倍）；投资逻辑从「讲概念」转向「看交付能力」 |
| **美国线** | LG × NVIDIA MOU（GR00T + Jetson Thor，2027 Q1 双足发布）；San Mateo County 首个商用机器人地方条例（遥操作模式承压）；Figure「肌腱是局部最优解」灵巧手路线之争 |
| **模型前沿** | Dyna-2（100 万小时人类视频、人→机迁移 scaling law）挑战 VLA 主流；世界动作模型「视频主导」与「机器人数据主导」两路线对峙 |
| **北京双会** | WRC 8/19–23 + 世界人形机器人运动会 8/22–26（冰丝带 666 队 / 2056 台）；国资委拟揭牌中央企业机器人创新联合体 |
| **家庭赛道** | 家庭机器人成为 2026 下半年新主战场：未来不远 Pre-A 近 10 亿元（500 真实家庭 / 5 万小时数据）、乐享·元点 M1 定价 7,000–9,000 元（3 万台订单、蚂蚁领投 Pre-A 5 亿）、优必选 U1 预售 1.3 万台（11.98 万–99 万元）、越疆 LUMO 1.3m 陪伴人形发布；入门价跌破万元（松延小布米 9,400 元） |

### 研究方向观察

- **估值锚切换**：宇树 610 亿发行市值 + DeepSeek 战配，本体企业定价逻辑从「硬件公司」向「AI 平台公司」迁移
- **数据闭环成护城河**：DeepSeek×宇树绑定实质是「模型—本体—真机数据」飞轮的制度安排，36 个月互锁是对其技术路线（VLA/端到端）的押注
- **「能演示 → 能使用」门槛**：EAI 大会评价标准之变 + 央视「进厂打工」报道印证，稳定性/一致性/成本/交付周期取代炫技成为核心 KPI
- **家庭赛道进入「进家元年」**：模型竞赛从 VLA 转向 WAM（未来不远 Self-Evolving WAM / 越疆空弈 WAM / 极佳 GigaBrain），「物理推演 / 执行前想象」成为家庭场景核心卖点；入门价下探至万元级（M1 7,000–9,000 元 / 小布米 <10,000 元），核心部件降价（关节 2,400→800 元）提供成本基础
- **家庭数据飞轮两派**：「真实家庭长时运行」（未来不远 / 乐享 / 卧安）vs「工业/单功能数据下放」（优必选 / 越疆 / 追觅）；资本开始为「可交付的家庭产品」付 Pre-A 溢价（5–10 亿/轮、产业资本集中入场）

---

## 2026-07-31

### 新增

- **latest-news.md 新增 7/18–7/31 章节**：~18 条新动态，覆盖 Google DeepMind Gemini Robotics 2（全身 VLA + 五指灵巧手 + ER 2 公开 API）、FCC 禁令（外国产人形机器人禁止进口美国）、Robros IGRIS-C 韩国后空翻、智在无界 Being-H0.8 隐式触觉世界模型（50 万小时数据）、中国首个具身智能国家标准、北京人形创新中心 TG-VLA 全身模型、新华网量产元年纪实（G2 2283 次零失误）、WAIC 2026 总结（208 企业、300 真机、年产 10 万目标）、国家人工智能中试基地（杭州）、行业范式转移分析
- **快速导航表**：新增 7/20–7/30 共 6 行，时间线延伸至 7 月 30 日

### 更新

- **README.md 最新动态**：新增 `2026-07-30` 表格（7 条事件）；Last Updated badge 更新为 `2026--07--31`

### 关键事件汇总

| 维度 | 7/18–7/31 关键事件 |
|------|-------------------|
| **Google DeepMind Gemini Robotics 2** | 全身 VLA 控制（脚到指尖）+ 五指灵巧手（22-DoF）+ 多机器人协作；ER 2 通过 Gemini API 公开预览；Apptronik Apollo 2 演示 |
| **FCC 禁令** | 外国产人形机器人禁止进口美国；中国制造商占 85% 全球市场，市场真空显现 |
| **触觉 + 世界模型新赛道** | 智在无界 Being-H0.8 首次在预训练引入触觉（50 万小时）；蚂蚁灵波「具身原生」理念 |
| **韩国全栈自研** | Robros IGRIS-C 后空翻，硬件+软件+AI 全栈自研，工业 PoC 已启动 |
| **中国量产元年纪实** | 普智 G2 8h/2283次零失误；工信部数据：2026 年人形机器人整机产量有望突破 10 万台 |
| **标准化与基础设施** | 首个具身智能国家标准发布；北京人形 100 万小时训练基地目标；杭州国家中试基地 140 台机器人 |
| **WAIC 2026 总结** | 208 家企业、300 台真机、三条主线（成本下探、大脑竞赛、数据基础设施）|

---

## 2026-07-17

### 新增

- **latest-news.md 新增 7/13–7/17 章节**：12 条新动态，覆盖 WAIC 2026 开幕、Robbyant LingBot-VLA 2.0 开源（60K 小时、20 形态）、NVIDIA GR00T 1.7 Apache 2.0 开源、小米 Robotics-U0 38B 模型、小鹏 Iron 量产加速、1X NEO Hands 25-DoF 灵巧手、Georgia Tech Learn to Teach 框架、ergoCub 共享具身智能论文
- **快速导航表**：新增 7/13–7/17 共 4 行，时间线延伸至 7 月 17 日

### 更新

- **README.md 最新动态**：新增 `2026-07-17` 表格（9 条事件）；Last Updated badge 更新为 `2026--07--17`
- **公司表格**：新增 Weave Robotics 一行（16 家公司）；badge 更新为 companies-16

### 新增文件

- **reports/weave-robotics/README.md**：Weave Robotics Isaac 1 家用轮式机器人完整调研报告（含 4 张产品参考图 + 系统架构图）
- **assets/weave-robotics/**：4 张产品参考图（isaac1-at-home、laundry、tidyup、sage）
- **assets/weave-robotics-architecture.svg**：Isaac 1 系统架构图
- **assets/agibot-architecture.svg**：智元「一体三智」AI 架构图
- **assets/fourier-architecture.svg**：傅利叶 GR-2 系统架构图
- **assets/star-dynamics-architecture.svg**：星动纪元 ERA-42 VLA 架构图

### 关键事件汇总

| 维度 | 7/13–7/17 关键事件 |
|------|-------------------|
| **WAIC 2026** | 上海开幕，10 万㎡、1,100+ 企业，具身智能成最大亮点；普渡 Physical Agent + PUDU D7 首展；腾讯「小六」首秀；人形机器人现场烹饪 |
| **VLA 模型开源潮** | Robbyant LingBot-VLA 2.0（Ant Group）和 NVIDIA GR00T 1.7（Apache 2.0）相继开源 |
| **世界模型路线** | Robbyant LingBot-VA 2.0 从零构建原生具身世界模型（非视频生成微调），150Hz 单 GPU |
| **小米入局** | 发布 Robotics-U0 380 亿参数多模态具身基础模型，四大能力统一 |
| **小鹏量产加速** | Iron 月产千台目标（2026 年底），2027 全球发售 |
| **灵巧手突破** | 1X NEO Hands 25-DoF 肌腱驱动，面向家用场景 |
| **学术前沿** | Georgia Tech「Learn to Teach」RL 框架；ergoCub 共享具身智能 Nature 论文 |

### 研究方向观察

- **VLA 基础模型全面开源化**：NVIDIA GR00T 1.7（Apache 2.0）+ Robbyant LingBot-VLA 2.0，行业正从独家模型走向开放生态竞争
- **从 EV 到机器人**：小鹏加速转型，成为继 BYD、Seres 后第三家明确进军具身智能的中国车企
- **WAIC 成为具身智能主舞台**：从 AI 软件到实体机器人，具身智能正在定义 AI 的下一个十年

---

## 2026-07-05

### 新增

- **latest-news.md 新增 7/4–7/5 章节**：5 条新动态，覆盖 AI2 Robotics 融资、新华财经量产窗口期报道、两协会情感陪伴倡议、亚布力论坛、Tesla Optimus 量产产线
- **快速导航表**：新增 7/5 一行，时间线延伸至 7 月 5 日

### 更新

- **README.md 最新动态**：新增 `2026-07-05` 表格；Last Updated badge 更新为 `2026--07--05`

### 关键事件汇总

| 维度 | 7/4–7/5 关键事件 |
|------|------------------|
| **资本** | AI2 Robotics 完成近 7.35 亿美元融资，投后估值约 200 亿元 |
| **量产** | Tesla Optimus 弗里蒙特工厂首条量产产线落地，7 月底启动小批量量产 |
| **政策/伦理** | 两协会发布情感陪伴人形机器人发展倡议，强调科技向善与隐私保护 |
| **行业判断** | 新华财经：全球具身智能产业迈入量产交付关键窗口期 |
| **商业化** | 亚布力论坛：无界动力获近 1 亿美元订单，宇树陈立判断 2-5 年突破 |

### 研究方向观察

- **量产交付窗口期开启**：Optimus 量产产线落地 + 智元万台交付 + 宇树 6,500 台下线，行业进入真实产能竞争
- **资本持续涌入**：AI2 Robotics 7.35 亿美元融资，轮式人形机器人赛道升温
- **伦理规范前置**：情感陪伴人形机器人倡议发布，行业开始重视安全与隐私
- **To B 场景率先突破**：亚布力论坛共识，工业等 To B 场景将先于家庭场景商业化

---

## 2026-07-04

### 新增

- **latest-news.md 新增 6/27–7/4 章节**：5 条新动态，覆盖上海 CIEI 2026 博览会、宇树 IPO 注册获批、8 台人形机器人工厂 99.987% 成功率、工信部/国资委专项行动、中国移动 5G-A 训练场
- **快速导航表**：新增 6/28、7/4 两行，时间线延伸至 7 月初

### 更新

- **README.md 最新动态**：新增 `2026-07-04` 表格；Last Updated badge 更新为 `2026--07--04`

### 关键事件汇总

| 维度 | 6/27–7/4 关键事件 |
|------|------------------|
| **资本化** | 宇树科技科创板 IPO 注册获批，104 天创纪录，A 股「具身智能第一股」将至 |
| **商业化** | 8 台人形机器人工厂 6 天×10 小时装配，集群成功率 99.987% |
| **政策** | 工信部、国资委专项行动：2026 年底常态部署、百个以上场景、万台级规模 |
| **展会** | 上海 CIEI 2026 国际具身智能产业博览会开幕，60+ 企业参展 |
| **基础设施** | 中国移动发布首个 5G-A 具身智能人形机器人训练场（苏州）+ 消防救援示范 |

### 研究方向观察

- **从 Demo 到作业模式**：99.987% 工厂成功率证明人形机器人开始进入真实产能竞争
- **A 股具身智能元年**：宇树 IPO 获批，资本化窗口正式打开
- **政策明确时间表**：2026 年底万台级常态部署成为行业共同目标
- **通信基础设施赋能**：5G-A 训练场可能成为降低数据采集成本的新路径

---

## 2026-06-26

### 新增

- **latest-news.md 新增 6/20–6/26 章节**：7 条新动态，覆盖 Figure AI 机器人 > 员工里程碑、智元 1.5 万台下线、1X NEO 商业化交付等
- **快速导航表**：新增 6/20、6/26 两行，时间线延伸至 6 月 26 日

### 更新

- **README.md 最新动态**：新增 `2026-06-26` 表格，覆盖 7 个公司/事件条目；Last Updated badge 更新为 `2026--06--26`
- **README.md 公司表格**：公司数量更新至 **15 家**（含智元/星动/傅利叶等新报告）

### 关键事件汇总

| 维度 | 6/20–6/26 关键事件 |
|------|------------------|
| **里程碑** | Figure AI 机器人（~740 台）首超人类员工（~660 人），业界首例 |
| **量产加速** | 智元第 15,000 台 G2 下线（距 1 万台不到 3 个月）；8 台 G2 南昌工厂 6 天并线直播 |
| **C 端落地** | 1X NEO 全规模生产启动，首批 $20,000 交付美国消费者 |
| **入华** | Tesla Optimus Gen 3 CES Asia 首秀，台系供应链就绪，中国预售将至 |
| **产品矩阵** | 优必选 U1 系列 50+ 款首发；越疆预告家庭陪伴机器人 |

### 研究方向观察

- **「机器人员工时代」开启**：Figure AI 机器人 > 人类员工，从象征到实质
- **家用人形机器人 C 端验证**：1X NEO $20,000 交付，定价和场景将接受真实市场检验
- **中国量产竞赛白热化**：智元 5 个月从首批发货到 1.5 万台，优必选/越疆/千寻密集发布
- **Optimus 正式入华**：特斯拉 Gen 3 中国预售在即，全球最大人形市场迎来最强竞争者

---

## 2026-06-19

### 新增

- **latest-news.md 新增 6/17–6/19 月下旬章节**：13+ 条新动态，覆盖 VivaTech 2026 Paris、Automate 2026、IPO 窗口、车企入局等主题
- **快速导航表**：新增 6/17、6/18、6/19 三行，时间线延伸至 6 月下旬

### 更新

- **README.md 最新动态**：新增 `2026-06-19` 表格，覆盖 12 个公司/事件条目；Last Updated badge 更新为 `2026--06--19`
- **行业趋势观察**：6/19 Türkiye Today 行业分析（机器人尚未大规模自主工作）加入 latest-news.md

### 关键事件汇总

| 维度 | 6/17–6/19 关键事件 |
|------|------------------|
| **海外部署** | Figure 02 BMW Spartanburg 新里程碑、1X NEO Beta 家用试用、Agility Digit 扩展亚马逊 |
| **中国 IPO 窗口** | 宇树招股书披露 2025 净利 6 亿、六小龙集体冲刺 IPO、宇树 H2 发布 + 优必选亿元大单 |
| **VivaTech Paris** | 智元「三智合一」展示、Foxconn 闭环物理 AI 栈欧洲首秀 |
| **车企入局** | Seres 发布 Xiaosai、Faraday Future 全形态 EAI Robot World |
| **新公司/新形态** | Genesis AI Eno（非人形）、Alibaba Qwen-Robot 系列（Manip+Nav+World） |
| **Automate 2026** | Kawasaki 8 轴 RL030N、Autonomique 实产、Curr-0、MINT-4B、Sanctuary AI 99.5% |
| **出海/海外** | 傅利叶 GR-3 千万级订单落地马来西亚 PERKESO 康复中心 |

### 研究方向观察

- **人形 vs 非人形路线分歧开始显性化**：Genesis AI Eno 明确「不需看起来像人」，挑战全人形共识
- **车企集体入场**：BYD（尧舜禹）+ Seres（Xiaosai）+ Faraday Future（EAI Robot World）+ 小鹏（IRON）+ 广汽（GoMate）+ 奇瑞（Aimoga）+ Tesla（Optimus）
- **资本化窗口开启**：中国六小龙集体冲刺 IPO，2026 年具身智能「上市大年」
- **VLA 从单点模型走向全栈套件**：Alibaba Qwen-Robot 三个模型分工又协同

---

## 2026-06-16

### 新增

- **3 家中国公司调研报告**：智元 (AGIBOT)、星动纪元 (StarDynamics)、傅利叶智能 (Fourier)，覆盖公司概况/AI 架构/数据策略/商业化进展
- **latest-news.md 全面更新**：新增 5-6 月行业动态（Figure×Catalyst Brands、1X World Model Lab、NVIDIA GR00T、BYD 入局、星动纪元 A+ 轮、智元 A3 打乒乓等）
- **papers.md 新增论文章节**：2026 年 5-6 月 10+ 篇重要新论文（Qwen-VLA、LeVERB、SENTINEL、UniT、WLA-0、UniVLA 等）

### 更新

- **README.md**：公司表格扩展至 **15 家**（新增智元/星动/傅利叶），最新动态更新至 2026-06-16，目录结构同步
- **latest-news.md**：重写为完整的时间线格式（4 月→5 月→6 月），新增 7 条行业趋势总结
- **papers.md**：新增 2026 年 5-6 月重要论文（ICLR/CVPR 2026、arXiv 新预印本）
- **README.md 使用方式**：新增 MkDocs 本地预览指南和 make check 链接检查

### 研究方向扩展

- 覆盖公司从 **12 家 → 15 家**，增加中国具身智能公司阵营
- 新增跟踪：BYD 人形机器人项目、NEURA Robotics、北京天工 3.0、中国机器人数字身份证政策
- README 中移除「后续计划覆盖中国公司」的待办标记

---

## 2026-05-08

### 新增

- **`latest-news.md`** — 2026 年 4-5 月最新行业动态追踪（Figure/1X/Unitree/BD/Apptronik/Agility/Meta）
- **Twitter/X 监控列表**：12 个公司官方账号 + 10 位关键人物个人账号（people.md）
- **`dexterous-hand-ego-data.md`** — 灵巧手 × Ego 数据深度调研：10+ 产品对比、8 核心算法框架、5 大数据集、Scaling Law、商业格局与未来预测

### 更新

- **Figure AI**：BotQ 产线 24 倍提速（1 台/小时）、350+ 台 F03 交付、System 0 零样本楼梯、Never Fall 协议、Helix 02 离线运行、$400-600/月租赁模型
- **1X Technologies**：NEO Factory 曝光（58K sqft）、垂直整合生产、Jetson Thor+、10K→100K/年产能路线、内部家庭测试中
- **Unitree**：双臂 R1 平台 $4,290 起、$5.8 亿 IPO 申请、20K 年出货目标
- **Boston Dynamics**：CEO/C-Suite 大出走、Hyundai 量产压力（4 台/月→30K/年）、量产版 Atlas 视频发布
- **Apptronik**：$9.35 亿融资、挖角 Waymo/BD/Amazon 高管组成"Dream Team"、下一代机器人将公布
- **Agility**：Peggy Johnson 新任 CEO、Unconstrained Humanoids 愿景
- **people.md**：更新 CEO 变更、离职记录、新增人才流动（BD→DeepMind/Apptronik，Waymo→Apptronik）
- **funding.md**：Apptronik 融资额更新至 $9.35 亿

### 行业趋势

- Meta 收购 Assured Robot Intelligence，正式进入人形机器人赛道
- 制造量产竞赛白热化：Figure/1X/Unitree 竞速
- 垂直整合成共识、家用市场提前布局

---

## 2026-04-29

### 新增

- **4 家公司调研报告**：Agility Robotics (Digit)、Apptronik (Apollo)、NVIDIA Isaac (GR00T/Isaac Sim/Jetson)、Enchanted Tools (Miroki)
- **技术标签索引**：`tags.md` — 8 大标签维度，支持多标签交叉检索
- **中文播客/视频资源汇总**：`podcasts-videos.md` — 播客、B站、YouTube、会议演讲、微信公众号
- **数据策略对比图**：
  - `assets/data-strategy-comparison.svg/png` — 11 公司 5 维度柱状对比
  - `assets/data-flywheel-patterns.svg/png` — 4 种数据飞轮模式环形图
- **4 家新公司架构图**：
  - `assets/agility-digit-architecture.svg/png`
  - `assets/apptronik-apollo-architecture.svg/png`
  - `assets/nvidia-isaac-architecture.svg/png`
  - `assets/enchanted-tools-architecture.svg/png`
- `scripts/generate_data_flywheel_chart.py` — 数据飞轮图表生成脚本

### 更新

- **对比图表扩展至 11 家公司**：雷达图和柱状图新增 DeepMind、Agility、Apptronik、NVIDIA、Enchanted
- **comparisons.md**：VLA 架构对比表扩展至 10 列，新增"平台+合作AI"和"基础设施"派别，数据策略/安全/硬件/商业化/观察点/风险表全部补充新公司
- **people.md**：新增 Agility、Apptronik、NVIDIA、Enchanted 关键人物，补充人才流动图
- **funding.md**：新增 NVIDIA Isaac、Enchanted Tools 融资条目，补充预测表
- **papers.md**：新增 GR00T 技术报告，更新论文演进脉络图
- **README.md**：公司表格扩展至 11 家，目录结构更新，新增数据策略图引用
- **tags.md**：补充 Apptronik VLA 检索链接、NVIDIA Isaac Sim2Real 标签
- 所有图表切换为 GitHub Dark 主题配色

### 修复

- `scripts/check_links.py` 修复嵌套 markdown 链接提取正则，解决 badge URL 误匹配

---

## 2026-04-28

### 新增

- **7 家公司调研报告**：Figure AI、Physical Intelligence (π)、Tesla、Boston Dynamics、1X Technologies、Unitree、Google DeepMind
- **5 份索引/对比文档**：
  - `comparisons.md` — 横向对比分析（VLA 架构、数据策略、安全机制、硬件设计、商业化）
  - `papers.md` — 核心论文索引（12+ 篇标志性论文，按时间线和技术主题分类）
  - `resources.md` — 开源资源汇总（模型、数据集、仿真器、框架、硬件平台）
  - `people.md` — 关键人物追踪（各公司核心技术人员、人才流动趋势）
  - `funding.md` — 投资与估值追踪（融资历程、估值分析、投资方格局）
- **14 张可视化图表**：
  - 公司能力雷达图 + 柱状图
  - 技术演进时间线总图（2023-2026，7 家公司 30+ 里程碑）
  - Tesla 端到端架构图、BD 分层混合架构图、1X NEO 系统架构图
  - DeepMind Gemini 双模型架构图、Unitree RL Pipeline 图
  - PI 8 张技术图表、Figure AI 5 张图表
- **工程化改进**：
  - `Makefile` — 一键生成图表、检查链接
  - `scripts/check_links.py` — 多线程外部链接检查器
  - `.github/workflows/check-links.yml` — 每周自动链接检查 CI
  - `AGENTS.md` — AI Agent 项目上下文和维护指南
  - README badges + 目录（TOC）

### 修复

- 修复 `resources.md` 中 9 个失效的外部链接

---

## 2026-04-26

### 新增

- 初始提交：Figure AI、Physical Intelligence (π)、Tesla 三家公司的调研报告
- PI 技术图表生成脚本（`scripts/generate_diagrams.py`）
- Figure AI 相关图表（SVG + PNG）

---

## 更新策略

- **内容更新**：跟随各公司重大技术发布（新模型、新产品、新论文）进行增量更新
- **链接检查**：每周自动运行 CI，手动修复失效链接
- **版本标记**：重大内容更新在 CHANGELOG 中记录，日常小幅修正不单独记录
