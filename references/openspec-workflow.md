# OpenSpec（OPSX）工作流详解

OpenSpec 是轻量级规范驱动工作流，适用于存量项目的快速迭代开发。**默认推荐模式。**

## 适用场景

- 已有代码基础的存量项目
- 快速迭代、小团队开发
- 功能增强、Bugfix、重构等日常变更

## 核心命令流程

### 1. 新建变更：`/opsx:new [change-name]`

创建 `.openspec/changes/[change-name]/proposal.md`：
- 变更描述与动机
- 影响范围分析
- 初步方案概述

### 2. 逐步推进：`/opsx:continue`

逐步创建工件（每次一个，便于审阅）：

1. **spec.md** — 功能规范（What & Why）
2. **design.md** — 技术设计（How）
3. **tasks.md** — 可执行任务清单

每个工件创建后等待用户确认再继续。

### 3. 快速推进：`/opsx:ff`

**复杂度分级 = 快速 时的首选路径。**

一次性生成所有规划工件（proposal + spec + design + tasks）：
- 适用于需求已非常清晰的场景
- 单文件 bugfix/typo/配置变更
- 用户确认后直接进入执行阶段

### 4. 应用变更：`/opsx:apply`

根据已确认的 tasks.md 开始实现。

### 5. 归档：`/opsx:archive`

完成后将变更文件移至归档目录，保留历史记录。
**与 progress.md 同步**：归档时间和状态写入 progress.md 最终记录。

## 闸门 G1 检查清单

无论使用 `/opsx:continue` 还是 `/opsx:ff`，进入下一阶段前必须通过：

- [ ] 用户给出明确确认信号
- [ ] spec.md/proposal.md 不含技术实现细节
- [ ] design.md 的技术决策不违反宪法约束
- [ ] 每个验收标准可映射为测试用例
- [ ] tasks.md 任务与 task_plan.md 同步

## 宪法集成

通过 `config.yaml` 的 `context.constitution` 字段引用宪法：

```yaml
project:
  name: my-project
  stack: [TypeScript, React, Node.js]
rules:
  - 所有变更必须有对应测试
  - UI 变更需附设计稿或设计系统
context:
  constitution: ./constitution.md
```

闸门校验时读取此字段指向的宪法文件，逐条对齐。

## 文件结构

```
.openspec/
├── config.yaml               # 项目配置（含宪法引用）
├── changes/                   # 活跃变更
│   └── [change-name]/
│       ├── proposal.md        # 变更提案
│       ├── spec.md            # 功能规范
│       ├── design.md          # 技术设计
│       └── tasks.md           # 任务清单（与 task_plan.md 同步）
└── archive/                   # 已归档变更
```

## 与 Spec-Kit 的关键差异

| 维度 | OpenSpec | Spec-Kit |
|------|----------|----------|
| 流程权重 | 轻量、灵活 | 严格、分阶段 |
| 适用项目 | 存量/迭代 | 全新/复杂系统 |
| 宪法 | 可选（config.yaml） | 强制（constitution.md） |
| 工件粒度 | proposal→spec→design→tasks | spec→plan→tasks |
| 快速路径 | `/opsx:ff` 一键生成 | 无（必须逐步） |
| 归档 | `/opsx:archive` 自动 | 手动维护 |
