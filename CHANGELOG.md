# 更新日志

> 记录 Soul2Humanoid 仓库的演进历史，按时间倒序排列。

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
