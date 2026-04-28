# AGENTS.md — 项目上下文

> 本文件为 AI Agent 提供项目背景、结构和维护指南。

---

## 项目概述

**Soul2Humanoid** 是一个系统性调研全球主流机器人公司具身智能（Embodied AI）技术方案的仓库。

- **目标读者**：对具身智能/人形机器人感兴趣的研究者、工程师、投资者
- **核心关注点**："大脑"层面的算法架构（VLA、端到端神经网络、任务规划），而非纯硬件
- **语言**：中文为主，技术术语保留英文

---

## 目录结构规范

```
Soul2Humanoid/
├── README.md              # 项目门户，包含公司表格、资源索引
├── papers.md              # 核心论文索引
├── resources.md           # 开源资源汇总
├── comparisons.md         # 横向对比分析
├── people.md              # 关键人物追踪
├── .gitignore
│
├── reports/               # 公司调研报告（每个公司一个子目录）
│   └── {company}/
│       └── README.md      # 该公司的完整技术路线调研
│
├── assets/                # 图表资源
│   ├── {company}/         # 各公司专属图表
│   └── *.svg / *.png      # 横向对比图表
│
├── whiteboards/           # 飞书画板源文件
│
└── scripts/               # 图表生成脚本
    └── *.py
```

### 添加新公司报告的规范

1. 创建 `reports/{company-slug}/README.md`
2. 公司 slug 使用小写、连字符分隔（如 `boston-dynamics`）
3. 报告结构参考现有报告：公司概况 → 硬件 → AI 架构 → 数据策略 → 商业化 → 竞争格局
4. 如果有图表，放入 `assets/{company-slug}/`，并在报告中用相对路径引用
5. 在 `README.md` 的公司表格中添加一行
6. 在 `comparisons.md` 的相关对比表中补充该公司

---

## 内容风格指南

### Markdown 格式

- 使用 ATX 风格的标题（`#` 而非下划线）
- 表格用于对比和规格参数
- 代码块用于架构图（ASCII）或命令
- 图片引用格式：`![描述](../../assets/company/file.svg)`

### 信息来源标注

- 每份报告顶部标注调研日期和核心来源
- 引用具体数据时标注来源（如 "来源：CES 2026 新闻稿"）
- 推测性内容用斜体或明确标注"推测"

### 图表生成

- 优先使用 matplotlib 生成 SVG + PNG 双格式
- 图表脚本放入 `scripts/`，输出到 `assets/`
- 颜色参考现有脚本的调色板（PI_ORANGE, PI_BLUE 等）

---

## 维护检查清单

添加新公司调研后，检查：

- [ ] 报告文件已放入 `reports/{company}/README.md`
- [ ] 图表已放入 `assets/{company}/`（如有）
- [ ] README.md 公司表格已更新
- [ ] README.md 目录结构已更新
- [ ] comparisons.md 相关对比表已更新
- [ ] papers.md 如有相关论文已补充
- [ ] people.md 如有关键人物已补充
- [ ] 所有链接相对路径正确，GitHub 可正常渲染
- [ ] 已提交并推送到 GitHub

---

## 技术栈

- **图表生成**：Python 3.12 + matplotlib + numpy
- **画板**：飞书白板（导出 JSON/Mermaid/PNG）
- **版本控制**：Git + GitHub
- **文档格式**：Markdown (GitHub Flavored)
