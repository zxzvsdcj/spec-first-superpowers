---
name: spec-first-superpowers
description: >
  Spec-driven development orchestrator: enforces specification-before-code workflow
  with auto mode selection (Spec-Kit or OpenSpec, defaults OpenSpec).
  Triggers: "/super-spec", "@super-spec", "use super-spec", "spec first", "规范先行",
  or any new feature/bugfix/refactor in projects containing .spec-mode, .specify/, or .openspec/ directories.
  Orchestrates: Spec-Kit + OpenSpec + planning-with-files + ui-ux-pro-max + Superpowers (TDD/review/verification).
---

# Spec-First + Superpowers 编排器

## 核心规则

1. **Spec 先行**：任何任务必须先完成规范并获用户明确确认，才允许写代码
2. **模式互斥**：Spec-Kit 与 OpenSpec 二选一，不混用，通过 `.spec-mode` 文件持久记录
3. **文件持久化**：所有规划写入文件（task_plan.md 等），不依赖聊天记录
4. **抗催促**：用户要求跳过规范时，礼貌拒绝并引导回 `/super-spec`

## `/super-spec` 命令

| 命令 | 效果 |
|------|------|
| `/super-spec` | 激活完整流程（自动选择模式） |
| `/super-spec force-spec-kit` | 强制 Spec-Kit |
| `/super-spec force-openspec` | 强制 OpenSpec |
| `/super-spec reset` | 删除 `.spec-mode`，重新判断 |

## 模式选择（决策树）

```
1. 读取 .spec-mode → 有记录 → 使用该模式
2. 检查目录：
   .specify/ 存在 → Spec-Kit
   .openspec/ 存在 → OpenSpec
   两者共存 → 报错，要求删除一个
3. 无初始化目录：
   "new project/从零开始/greenfield" + 文件<30 → Spec-Kit
   其他 → OpenSpec（默认）
4. 写入 .spec-mode 持久化
```

## 编排流程（按顺序，不可跳过）

### 阶段 1：SDD 规范

按选定模式执行对应工作流：

- **Spec-Kit**：读取 [references/spec-kit-workflow.md](references/spec-kit-workflow.md) 并执行
- **OpenSpec**：读取 [references/openspec-workflow.md](references/openspec-workflow.md) 并执行

用户明确确认 Spec 完整无歧义后进入下一阶段。

### 阶段 2：持久规划

调用 `planning-with-files` skill 生成三文件：task_plan.md / findings.md / progress.md

### 阶段 3：UI/UX 设计（条件触发）

需求涉及界面关键词（UI/UX/页面/仪表盘/组件/交互/设计/app/web 等）时：
→ 调用 `ui-ux-pro-max` 生成完整设计系统，等待用户确认后继续。

### 阶段 4：Superpowers 执行

调用 `using-superpowers` 加载方法论，依次执行：
brainstorming → writing-plans → test-driven-development → requesting-code-review → verification-before-completion

### 阶段 5：归档

- 更新 task_plan.md 所有 checkbox
- OpenSpec 执行 `/opsx:archive` · Spec-Kit 更新 `.specify/` 文件

## 宪法模板（可选）

项目可选使用宪法文件定义不可妥协原则：

- [assets/constitutions/openspec-constitution.md](assets/constitutions/openspec-constitution.md)（通用/OpenSpec 项目）
- [assets/constitutions/spec-kit-constitution.md](assets/constitutions/spec-kit-constitution.md)（Spec-Kit 项目）

## 集成与排障

详见 [references/integration-guide.md](references/integration-guide.md)。
