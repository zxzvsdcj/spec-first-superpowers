# OpenSpec（OPSX）工作流详解

OpenSpec 是轻量级规范驱动工作流，适用于存量项目的快速迭代开发。默认推荐模式。

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

逐步创建工件（每次一个，便于用户审阅）：

1. **spec.md** — 功能规范（What & Why）
2. **design.md** — 技术设计（How）
3. **tasks.md** — 可执行任务清单

每个工件创建后等待用户确认再继续。

### 3. 快速推进（可选）：`/opsx:ff`

一次性生成所有规划工件（proposal + spec + design + tasks），适用于需求已非常清晰的场景。

### 4. 应用变更：`/opsx:apply`

根据已确认的 tasks.md 开始实现。

### 5. 归档：`/opsx:archive`

完成后将变更文件移至归档目录，保留历史记录。

## 文件结构

```
.openspec/
├── config.yaml               # 项目配置（可选）
├── changes/                   # 活跃变更
│   └── [change-name]/
│       ├── proposal.md        # 变更提案
│       ├── spec.md            # 功能规范
│       ├── design.md          # 技术设计
│       └── tasks.md           # 任务清单
└── archive/                   # 已归档变更
```

## config.yaml 示例

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

## 与 Spec-Kit 的关键差异

| 维度 | OpenSpec | Spec-Kit |
|------|----------|----------|
| 流程权重 | 轻量、灵活 | 严格、分阶段 |
| 适用项目 | 存量/迭代 | 全新/复杂系统 |
| 宪法 | 可选（config.yaml） | 强制（constitution.md） |
| 工件粒度 | proposal→spec→design→tasks | spec→plan→tasks |
| 归档 | `/opsx:archive` 自动管理 | 手动维护 |
