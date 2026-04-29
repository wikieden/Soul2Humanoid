# 更新日志

> 记录 Soul2Humanoid 仓库的演进历史，按时间倒序排列。

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
