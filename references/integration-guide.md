# 集成指南与排障

## 目录

- [依赖 Skills 清单](#依赖-skills-清单)
- [编排流程图](#编排流程图)
- [会话恢复协议](#会话恢复协议)
- [复杂度分级决策树](#复杂度分级决策树)
- [执行策略选择](#执行策略选择)
- [错误升级链](#错误升级链)
- [安装验证](#安装验证)
- [常见问题](#常见问题)

## 依赖 Skills 清单

| Skill | 职责 | 必需？ | 触发阶段 |
|-------|------|--------|---------|
| `using-superpowers` | 加载 Superpowers 方法论 | 是 | 阶段 4 |
| `brainstorming` | 设计探索（编码前，融合于 Spec 阶段） | 是 | 阶段 1 |
| `writing-plans` | 实施计划（bite-sized steps） | 是 | 阶段 2 |
| `test-driven-development` | TDD RED-GREEN-REFACTOR | 是 | 阶段 4 |
| `requesting-code-review` | 代码审查 | 是 | 阶段 4 |
| `verification-before-completion` | 完成前验证 | 是 | 阶段 4 (G4) |
| `planning-with-files` | 文件持久规划 + 会话恢复 | 是 | 阶段 0/2 |
| `ui-ux-pro-max` | UI/UX 设计系统 | 条件 | 阶段 3 |
| `systematic-debugging` | 4 阶段根因分析 | 按需 | 阶段 4 (错误) |
| `subagent-driven-development` | 子代理执行 + 两阶段审查 | 按需 | 阶段 4 |
| `executing-plans` | 批次执行 + 检查点 | 按需 | 阶段 4 |
| `finishing-a-development-branch` | 分支收尾 | 是 | 阶段 5 |
| `code-review-expert` | 深度代码审查 | 推荐 | 阶段 4 |

## 编排流程图

```
用户输入 /super-spec
        │
        ▼
   模式选择（决策树）
   ┌─────┴─────┐
   │           │
Spec-Kit    OpenSpec
   │           │
   ▼           ▼
   复杂度分级
   ┌──┬──┬──┐
   快速 标准 深度
   │   │   │
   │   │   └→ Agent Teams 评估
   │   │
   ▼   ▼
┌─────────────────────────────────────────┐
│ 阶段 0：上下文恢复                      │
│ task_plan.md 存在？→ 5-Question Test    │
│ → 断点续行                              │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│ 阶段 1：SDD 规范                        │
│ Spec-Kit / OpenSpec (快速用 ff)          │
│ ─── 闸门 G1: 用户确认 + 宪法对齐 ───── │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│ 阶段 2：持久规划                        │
│ planning-with-files + writing-plans     │
│ ─── 闸门 G2: 编号清单 + 测试点 ──────── │
└────────────────┬────────────────────────┘
                 ▼
         UI/UX 检测
         ┌──┴──┐
         是    否
         │     │
         ▼     │
┌────────────┐ │
│ 阶段 3     │ │
│ ui-ux-pro  │ │
│ --persist  │ │
│ ── G3 ──── │ │
└──────┬─────┘ │
       │       │
       ◄───────┘
       │
       ▼
┌─────────────────────────────────────────┐
│ 阶段 4：Superpowers 执行                │
│ 策略：Subagent-Driven / Executing-Plans │
│ TDD → 两阶段审查 → systematic-debugging │
│ ─── 闸门 G4: 测试+审查+验证证据 ─────── │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│ 阶段 5：归档                            │
│ finishing-a-development-branch          │
│ → task_plan.md + archive + progress.md  │
└─────────────────────────────────────────┘
```

## 会话恢复协议

当 AI 检测到 task_plan.md 已存在（说明有未完成任务）时，自动执行：

1. **读取全部规划文件**：task_plan.md + findings.md + progress.md
2. **5-Question Reboot Test**：
   - 我在哪个阶段？（task_plan.md 中最后一个 `[x]`）
   - 下一步是什么？（下一个 `[ ]`）
   - 总目标是什么？（task_plan.md 顶部目标声明）
   - 已发现什么？（findings.md 关键发现）
   - 已完成什么？（progress.md 最新条目）
3. **一致性检查**：`git diff --stat` 与 progress.md 对比
4. **断点定位**：从最后一个已完成步骤的下一步继续
5. **向用户汇报**：当前状态 + 下一步建议 → 确认后继续

触发方式：AI 在会话开始时检测到 `task_plan.md` 存在即自动执行，无需用户手动调用。此协议融合自 `planning-with-files` 的 session-catchup 机制。

## 复杂度分级决策树

```
收到任务描述
    │
    ├─ 单文件 bugfix/typo/配置？         → 快速
    ├─ 涉及 ≥ 3 个文件修改？             → 标准/深度
    ├─ 需要架构决策或技术选型？            → 深度
    ├─ 涉及 UI/UX 设计？                 → 标准（触发阶段 3）
    ├─ 可拆分为 ≥ 2 个独立并行子任务？     → 深度（+ Agent Teams）
    └─ 其他单功能变更                     → 标准
```

AI 判断后建议级别 → 用户确认或调整。

## 执行策略选择

阶段 4 提供两种执行策略（AI 根据任务特征推荐）：

| 维度 | Subagent-Driven | Executing-Plans |
|------|----------------|-----------------|
| 会话 | 当前会话 | 可并行会话 |
| 上下文 | 每任务 fresh subagent（零污染） | 同一会话累积上下文 |
| 审查 | 每任务两阶段审查（spec + quality） | 每批次(3 任务)检查点 |
| 适合 | 独立任务、高质量要求 | 紧耦合任务、快速迭代 |
| 成本 | 更多 subagent 调用 | 更少调用但上下文风险 |

推荐场景：
- 任务独立性高 + 质量要求高 → Subagent-Driven
- 任务紧耦合 + 快速迭代 → Executing-Plans
- 不确定 → Subagent-Driven（默认推荐）

## 错误升级链

```
错误发生
    ├─ 立即写入 progress.md（Error/Attempt/Resolution 表）
    │
    ▼
尝试 1: 诊断 → 针对性修复
    │
    ├─ 解决 → 继续
    │
    ▼
尝试 2: 换方法/换工具
    │
    ├─ 解决 → 继续
    │
    ▼
尝试 3: 质疑假设 → 搜索方案
    │
    ├─ 解决 → 继续
    │
    ▼
3 次失败 → 调用 systematic-debugging
    │  Phase 1: 根因调查
    │  Phase 2: 模式分析
    │  Phase 3: 假设验证
    │  Phase 4: 实现修复
    │
    ├─ 解决 → 继续
    │
    ▼
仍未解决 → 质疑架构 → 上报用户
```

## 安装验证

检查以下 Skills 是否已安装：

```
必需：
✓ using-superpowers
✓ brainstorming
✓ writing-plans
✓ test-driven-development
✓ requesting-code-review
✓ verification-before-completion
✓ planning-with-files
✓ finishing-a-development-branch

推荐：
✓ ui-ux-pro-max
✓ systematic-debugging
✓ subagent-driven-development
✓ executing-plans
✓ code-review-expert
```

缺少任何必需 Skill 时，通过 `npx skills find '<keyword>'` 搜索并安装。

## 常见问题

### Q: 模式判断错误？
`/super-spec reset` 删除 `.spec-mode`，重新触发自动判断。或使用 `force-spec-kit` / `force-openspec` 强制指定。

### Q: AI 跳过了规范阶段？
检查 `.cursor/rules/00-spec-first-superpowers.mdc` 是否存在且 `alwaysApply: true`。

### Q: UI/UX 设计系统未触发？
需求中明确使用界面相关关键词：UI、UX、页面、仪表盘、组件、交互、界面、设计、app、web、mobile。

### Q: 上下文丢失（长会话）？
检查 task_plan.md / progress.md 是否最新。执行 Read Before Decide 模式：每次重大决策前重读 task_plan.md。

### Q: 如何选择执行策略？
参见[执行策略选择](#执行策略选择)。默认推荐 Subagent-Driven。

### Q: 3 次修复同一错误仍失败？
参见[错误升级链](#错误升级链)。调用 `systematic-debugging` 做根因分析，仍失败则质疑架构。

### Q: Spec-Kit CLI 安装？
`curl -LsSf https://astral.sh/uv/install.sh | sh && uv tool install specify-cli`

### Q: OpenSpec CLI 安装？
`npm install -g @fission-ai/openspec@latest`

## 相关项目

| 项目 | GitHub | 说明 |
|------|--------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | GitHub 官方规范驱动框架 |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 轻量 OPSX 工作流 |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | TDD + 审查方法论 |
| planning-with-files | [othmanadi/planning-with-files](https://github.com/othmanadi/planning-with-files) | 文件持久规划 |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX 设计系统 |
