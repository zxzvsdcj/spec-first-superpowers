---
name: spec-first-superpowers
description: >
  Spec-driven development orchestrator: enforces specification-before-code workflow
  with auto mode selection (Spec-Kit or OpenSpec, defaults OpenSpec), complexity triage
  (quick/standard/thorough), session recovery, and quality gates at every stage.
  Triggers: "/super-spec", "@super-spec", "use super-spec", "spec first", "规范先行",
  or any new feature/bugfix/refactor in projects containing .spec-mode, .specify/, or .openspec/ directories.
  Orchestrates: Spec-Kit/OpenSpec (spec) + planning-with-files (persistence) +
  ui-ux-pro-max (design) + Superpowers (TDD/review/verification/debugging).
---

# Spec-First + Superpowers 编排器 v3

## 核心规则

1. **Spec 先行**：先规范后代码，用户确认后才允许实现
2. **模式互斥**：Spec-Kit 与 OpenSpec 二选一，`.spec-mode` 持久记录
3. **文件持久化**：规划写入文件(task_plan.md 等)，每次决策前重读计划
4. **会话恢复**：task_plan.md 已存在 → 自动恢复上下文 → 从断点续行
5. **质量闭环**：每阶段有质量闸门 (G0–G4)，不达标不前进；详见 [references/quality-gates.md](references/quality-gates.md)
6. **抗催促**：要求跳过规范 → 拒绝 → 引导 `/super-spec`

## 命令

| 命令 | 效果 |
|------|------|
| `/super-spec` | 完整流程（自动模式 + 自动分级） |
| `/super-spec force-spec-kit` | 强制 Spec-Kit |
| `/super-spec force-openspec` | 强制 OpenSpec |
| `/super-spec reset` | 重置模式判断 |

## 模式选择

```
.spec-mode 存在 → 使用记录
.specify/ → Spec-Kit · .openspec/ → OpenSpec · 两者共存 → 报错
全新项目 + 文件 < 30 → Spec-Kit · 其他 → OpenSpec（默认）
→ 写入 .spec-mode
```

## 复杂度分级（AI 判断 → 建议 → 用户确认）

| 级别 | 条件 | 流程 |
|------|------|------|
| **快速** | 单文件 bugfix/typo/配置 | 简化 Spec(`/opsx:ff`) → TDD → 归档 |
| **标准** | 单功能增改，范围清晰 | 全部阶段（阶段 3 条件触发） |
| **深度** | 多模块/架构级/技术选型 | 全部阶段 + Agent Teams 评估 |

## 编排流程（按序执行）

### 阶段 0：上下文恢复（自动）
task_plan.md 存在 → 读取全部规划文件 → 5-Question Reboot Test(我在哪/去哪/目标/发现/进度) → 从断点续行。不存在 → 正常启动。

### 阶段 1：SDD 规范
按模式执行：**Spec-Kit** → [spec-kit-workflow.md](references/spec-kit-workflow.md) · **OpenSpec** → [openspec-workflow.md](references/openspec-workflow.md)。
快速级别：用 `/opsx:ff` 或简化 spec，跳过 clarify。
**闸门 G1**：用户明确确认 + 宪法条款对齐检查。

### 阶段 2：持久规划
调用 `planning-with-files` + `writing-plans` 协同生成：task_plan.md（编号检查清单 + TDD 测试点）/ findings.md / progress.md。
**闸门 G2**：每个任务有文件路径 + 验收标准 + 测试用例草案。

### 阶段 3：UI/UX 设计（条件触发）
界面关键词 → `ui-ux-pro-max --design-system --persist` → design-system/MASTER.md 持久化。
**闸门 G3**：Pre-delivery Checklist 通过 + 用户确认设计方案。

### 阶段 4：Superpowers 执行
执行策略（AI 推荐，用户选择）：
- **Subagent-Driven**：每任务 fresh subagent + 两阶段审查（spec 符合 → 代码质量）
- **Executing-Plans**：批次执行 + 检查点审查

TDD 循环执行 · 错误 → `systematic-debugging`（3 次失败切换方案）。
**闸门 G4**：全部测试通过 + 审查通过 + `verification-before-completion` 证据 → 写入 progress.md。

### 阶段 5：归档
`finishing-a-development-branch` → 更新 task_plan.md 全部 checkbox → OpenSpec `/opsx:archive` / Spec-Kit `.specify/` → progress.md 最终记录。

## 补充资源

- 质量闸门详细标准：[references/quality-gates.md](references/quality-gates.md)
- 协同模式详解：[references/synergy-patterns.md](references/synergy-patterns.md)
- 宪法模板：[assets/constitutions/openspec-constitution.md](assets/constitutions/openspec-constitution.md) · [assets/constitutions/spec-kit-constitution.md](assets/constitutions/spec-kit-constitution.md)
- 集成与排障：[references/integration-guide.md](references/integration-guide.md)
