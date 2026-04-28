# Google DeepMind 机器人技术路线深度调研

> **调研日期**：2026年4月  
> **核心来源**：Google DeepMind 官网、Gemini Robotics 页面、RT-2/RT-X 论文  
> **核心产品**：Gemini Robotics 1.5、Gemini Robotics-ER 1.6、RT-2/RT-X 系列

---

## 1. 组织概况

Google DeepMind 不是机器人公司，而是**具身智能领域最重要的技术赋能者**。其研发的 VLA（Vision-Language-Action）模型被全球大多数头部机器人公司采用或参考。

| 项目 | 内容 |
|------|------|
| **机构** | Google DeepMind |
| **前身** | DeepMind（2010，伦敦）+ Google Brain（2011，硅谷） |
| **合并** | 2023 年合并为 Google DeepMind |
| **领导人** | Demis Hassabis（CEO，2024 诺贝尔化学奖） |
| **机器人团队** | 由资深研究员主导，与 Google Research 紧密合作 |
| **使命** | "Solve intelligence, and then use that to solve everything else" |

---

## 2. 技术演进时间线

| 时间 | 技术/产品 | 核心突破 |
|------|----------|---------|
| 2023.07 | **RT-2** | 首个大规模 VLA 模型，将视觉-语言模型直接输出机器人动作 |
| 2023.10 | **RT-X** | 跨机器人形态的泛化，Open X-Embodiment 数据集 |
| 2024.03 | **RT-H** | 用语言描述中间步骤，提升长程任务成功率 |
| 2024.08 | **Gemini Robotics** | 基于 Gemini 多模态模型的 VLA 系统 |
| 2025.03 | **Gemini Robotics 1.5** | 更强大的 VLA 模型，支持更复杂的物理交互 |
| 2026.04 | **Gemini Robotics-ER 1.6** | 增强具身推理模型，支持复杂任务规划 |

---

## 3. 核心技术架构

### 3.1 双模型架构

Google DeepMind 采用 **VLA + ER（Embodied Reasoning）双模型架构**：

| 模型 | 角色 | 功能 |
|------|------|------|
| **Gemini Robotics 1.5** | VLA 模型 | "看"（视觉）+ "理解"（语言）+ "动"（动作） |
| **Gemini Robotics-ER 1.6** | 具身推理模型 | 物理世界推理、复杂任务规划、逻辑决策 |

**工作流程**：
1. ER 模型分析任务，制定步骤计划
2. VLA 模型将视觉输入和指令转化为具体动作
3. 两者协作完成长程、复杂任务

### 3.2 Gemini Robotics 1.5（VLA）

- **输入**：视觉图像 + 自然语言指令
- **输出**：机器人电机命令
- **能力**：
  - 跨机器人形态泛化（双臂静态平台、人形机器人等）
  - 精细操作（折纸、打包午餐盒、准备沙拉）
  - 多步骤任务自主执行
  - 自然语言交互

### 3.3 Gemini Robotics-ER 1.6（具身推理）

- **核心能力**：在物理世界中以空前精度进行推理
- **功能**：
  - 复杂任务规划
  - 逻辑决策
  - 工具使用（如调用 Google Search 查找信息）
  - 动态环境适应

### 3.4 Gemini Robotics On-Device

- **定位**：可在机器人设备上本地运行的 VLA 模型
- **意义**：降低延迟、保护隐私、支持离线运行
- **目标**：让开发者可以针对自己的应用微调模型

---

## 4. 开源与生态贡献

### 4.1 Open X-Embodiment 数据集

- **规模最大的机器人数据集**
- 汇集全球 20+ 研究机构的机器人数据
- 覆盖数百种机器人形态和数千种任务
- 为 PI 的 π0、Figure AI 的 Helix 等模型提供训练数据基础

### 4.2 RT-X / RT-2 论文与代码

- 公开发表了 RT-2、RT-X、RT-H 等技术论文
- 推动了整个行业的 VLA 研究热潮
- 被引用数千次，成为具身智能领域的基石文献

### 4.3 合作伙伴生态

DeepMind 与全球主要机器人公司建立了合作关系：

| 公司 | 合作类型 | 说明 |
|------|---------|------|
| **Apptronik** | 合作伙伴 | 共建下一代人形机器人 |
| **Boston Dynamics** | 可信测试者 | Atlas 集成 Gemini Robotics |
| **Agility Robotics** | 可信测试者 | Digit 集成 Gemini |
| **Figure AI** | 间接（技术参考） | Helix VLA 参考了 RT 系列架构 |
| **Physical Intelligence** | 间接（数据集） | π0 使用 Open X-Embodiment 数据 |
| **宇树科技** | 间接 | 使用 Isaac Sim 进行训练 |

---

## 5. 与 Physical Intelligence 的对比

| 维度 | Google DeepMind | Physical Intelligence (π) |
|------|----------------|---------------------------|
| **定位** | 技术平台/赋能者 | 垂直整合的机器人 AI 公司 |
| **产品形态** | 模型 + SDK | 通用机器人策略 + 部署服务 |
| **开源程度** | 论文 + 部分数据集开源 | 开源 π0 + FAST 权重和代码 |
| **商业化** | 通过 Gemini API 和合作伙伴 | 直接面向客户部署 |
| **硬件** | 不造硬件，纯软件 | 不造硬件，提供 AI 能力 |
| **核心优势** | 庞大的研究资源、Gemini 多模态能力 | 专注、快速迭代、工程落地 |

---

## 6. 关键影响

Google DeepMind 对具身智能领域的贡献是**奠基性的**：

1. **定义了 VLA 架构**：RT-2 首次证明视觉-语言模型可以直接控制机器人
2. **构建了数据基础设施**：Open X-Embodiment 成为行业标准数据集
3. **推动了跨本体泛化**：证明单一策略可以控制多种机器人
4. **建立了安全框架**：与政策制定者、专家合作制定机器人 AI 安全标准
5. **赋能整个行业**：几乎所有主流机器人公司都在使用或参考 DeepMind 的技术
