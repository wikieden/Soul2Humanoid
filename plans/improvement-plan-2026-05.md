# 项目完善实施计划

> 基于 2026-05-09 审计结果，系统性修复 HIGH + MEDIUM 优先级问题。
> 预计总耗时：~40 分钟

---

## 一、计划概要

| 阶段 | 任务 | 优先级 | 预计耗时 |
|------|------|--------|---------|
| **P1** | 修复失效链接（open-source-tracking.md） | HIGH | 8 min |
| **P2** | 补全 tags.md 23 个缺失检索区 | HIGH | 10 min |
| **P3** | 添加 CONTRIBUTING.md + Issue/PR 模板 | HIGH | 5 min |
| **P4** | 修复图表中文字体 + 补充架构图引用 | HIGH | 10 min |
| **P5** | 创建 docs/ 自动同步脚本 + Makefile 更新 | MEDIUM | 5 min |
| **P6** | 优化 latest-news.md 可读性 | MEDIUM | 5 min |
| **P7** | 添加 favicon + sitemap 插件 | LOW | 3 min |
| **P8** | 验证 + 提交 + Pages 部署 | — | 2 min |

**总预计：~48 分钟**

---

## 二、详细步骤

### P1：修复失效链接（8 min）

**目标**：open-source-tracking.md 中 9 个失效/推测 GitHub 链接

| 失效链接 | 问题 | 修复方案 |
|---------|------|---------|
| `github.com/open-replay` | 404，应为 `github.com/open-replay` 但实际不存在 | 替换为 GitHub Trending 或删除 |
| `github.com/physical-intelligence/pi0` | 404，仓库名可能是 `openpi` 或 `pi0.7` | 查正确 URL 或标注"仓库未公开" |
| `github.com/physical-intelligence/pi0.7` | 404 | 同上 |
| `github.com/physical-intelligence/fast` | 404 | 同上 |
| `github.com/google-research/.../robustness_metrics` | 路径可能已变 | 修正路径或删除 |
| `github.com/boston-dynamics/bdscaffold` | 404 | 删除 |
| `github.com/1x-technologies/1x_world_model` | 推测，未确认 | 标注"未公开" |
| `github.com/{owner}/{repo}/releases.atom` | 模板 URL | 替换为说明文字 |
| `github.com/thu-ml/RDT` | 404，实际仓库名为 `RoboticsDiffusionTransformer` | 修正 URL |

**验证**：运行 `python3 scripts/check_links.py` 确认 0 FAILED

---

### P2：补全 tags.md 检索区（10 min）

**目标**：为 23 个缺失检索区的标签补充公司链接列表

缺失标签清单：
`MPC`, `遥操作`, `语言条件化`, `人类视频迁移`, `闭源`, `RL`, `部分开源`, `Tokenization`, `FlowMatching`, `轻量化`, `家用`, `Diffusion`, `合成数据`, `教育研究`, `Transformer`, `软件安全层`, `工业制造`, `全身控制`, `可组合泛化`, `Sim2Real`, `模仿学习`, `肌腱驱动`, `跨形态泛化`, `高扭矩密度`

**策略**：
- 每个标签检索区格式：`### #标签名` + `- [reports/company/](...)` 列表
- 基于标签定义表中的"覆盖公司"列直接生成
- 如果标签覆盖公司太多，只列前 5 家 + "更多..."

---

### P3：CONTRIBUTING.md + 模板（5 min）

**目标**：降低外部贡献门槛

文件清单：
- `CONTRIBUTING.md` — 贡献指南（报告格式、提交流程、PR 规范）
- `.github/ISSUE_TEMPLATE/bug_report.md` — Bug 报告模板
- `.github/ISSUE_TEMPLATE/feature_request.md` — 功能请求模板
- `.github/pull_request_template.md` — PR 模板

**内容要点**：
- 报告格式参考 AGENTS.md
- 新增公司报告的检查清单
- 图表生成规范
- 链接检查要求

---

### P4：图表字体 + 架构图引用（10 min）

**4a. 中文字体修复**
- 问题：macOS matplotlib 使用 DejaVu Sans，不支持中文
- 方案：在生成脚本中设置 `matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']`
- 或者：所有图表标题/标签改为英文，避免中文

**4b. 架构图引用**
- 在 `reports/tesla-optimus/README.md` 等缺失架构图引用的报告中添加 `![架构图](../assets/xxx.svg)`
- 涉及报告：tesla, 1x, agility, boston-dynamics, figure-ai, google-deepmind, unitree

---

### P5：自动同步脚本 + Makefile（5 min）

**目标**：消除手动 cp 容易遗漏的问题

**5a. 创建 `scripts/sync_docs.py`**
- 扫描根目录 `*.md` → 复制到 `docs/`
- 扫描 `reports/*/README.md` → 复制到 `docs/reports/{company}.md`
- 扫描 `assets/` → 复制到 `docs/assets/`
- 自动修复图片路径

**5b. 更新 `Makefile`**
- `make sync` — 运行同步脚本
- `make build` — 同步 + mkdocs build
- `make serve` — 同步 + mkdocs serve
- `make deploy` — 同步 + git add + commit + push

---

### P6：latest-news.md 可读性优化（5 min）

**目标**：改为"按公司分类"的折叠表格视图

**方案**：
- 每个公司一个折叠块（`<details>`）
- 内部用表格：日期 | 动态 | 来源
- 保留行业趋势观察部分

---

### P7：favicon + sitemap（3 min）

**目标**：SEO 和视觉体验

- 创建 `docs/assets/favicon.ico`（用 emoji 🤖 生成）
- `mkdocs.yml` 添加 `site_favicon: assets/favicon.ico`
- 添加 `mkdocs-sitemap-plugin`（可选，非必须）

---

### P8：验证 + 提交（2 min）

1. `python3 scripts/check_links.py` → 确认 0 FAILED
2. `make build` → mkdocs build 成功
3. `git add -A && git commit && git push`
4. 确认 Pages 部署成功

---

## 三、验收标准

| 检查项 | 通过标准 |
|--------|---------|
| 链接检查 | `scripts/check_links.py` → 0 FAILED |
| MkDocs 构建 | `mkdocs build` 成功，无 ERROR |
| tags.md 覆盖率 | 34/34 标签均有检索区 |
| 贡献文件 | CONTRIBUTING.md + 3 个 GitHub 模板存在 |
| 同步脚本 | `make sync` 可正确同步所有文件 |
| Pages 部署 | GitHub Actions 成功，站点可访问 |

---

*计划制定：2026-05-09*
*执行方式：按 P1→P8 顺序逐阶段完成，每阶段后立即验证*
