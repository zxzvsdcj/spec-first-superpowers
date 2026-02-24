# 集成指南与排障

## 目录

- [依赖 Skills 清单](#依赖-skills-清单)
- [编排流程图](#编排流程图)
- [安装验证](#安装验证)
- [常见问题](#常见问题)
- [相关项目](#相关项目)

## 依赖 Skills 清单

| Skill | 职责 | 必需？ |
|-------|------|--------|
| `using-superpowers` | 加载 Superpowers 方法论 | 是 |
| `brainstorming` | 设计探索（编码前） | 是 |
| `writing-plans` | 实施计划 | 是 |
| `test-driven-development` | TDD RED-GREEN-REFACTOR | 是 |
| `requesting-code-review` | 代码审查 | 是 |
| `verification-before-completion` | 完成前验证 | 是 |
| `planning-with-files` | 文件持久规划 | 是 |
| `ui-ux-pro-max` | UI/UX 设计系统 | 条件触发 |
| `systematic-debugging` | 错误排查 | 按需 |
| `finishing-a-development-branch` | 分支收尾 | 按需 |

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
  SDD 规范阶段
  （用户确认门控）
        │
        ▼
  planning-with-files
  task_plan.md / findings.md / progress.md
        │
        ▼
  UI/UX 检测 ──否──┐
   │是              │
   ▼               │
  ui-ux-pro-max    │
  （用户确认）      │
        │          │
        ◄──────────┘
        │
        ▼
  Superpowers 执行
  brainstorming → plans → TDD → review → verify
        │
        ▼
  归档 & 更新文件
```

## 安装验证

检查以下 Skills 是否已安装（在 Cursor 中确认 Skills 列表）：

```
必需：
✓ using-superpowers
✓ brainstorming
✓ writing-plans
✓ test-driven-development
✓ requesting-code-review
✓ verification-before-completion
✓ planning-with-files

推荐：
✓ ui-ux-pro-max
✓ systematic-debugging
✓ code-review-expert
```

缺少任何必需 Skill 时，通过 `npx skills find '<keyword>'` 搜索并安装。

## 常见问题

### Q: 模式判断错误？
`/super-spec reset` 删除 `.spec-mode`，重新触发自动判断。或使用 `force-spec-kit` / `force-openspec` 强制指定。

### Q: AI 跳过了规范阶段？
检查 `.cursor/rules/00-spec-first-superpowers.mdc` 是否存在且 `alwaysApply: true`。该规则文件是始终生效的守门员。

### Q: UI/UX 设计系统未触发？
在需求描述中明确使用界面相关关键词：UI、UX、页面、仪表盘、组件、交互、界面、设计、app、web、mobile 等。

### Q: 上下文丢失（长会话）？
检查 task_plan.md / progress.md 是否存在且最新。planning-with-files 的核心价值就是对抗上下文丢失。

### Q: Spec-Kit CLI 安装失败？
需要 Python + uv：`curl -LsSf https://astral.sh/uv/install.sh | sh && uv tool install specify-cli`

### Q: OpenSpec CLI 安装失败？
需要 Node.js：`npm install -g @fission-ai/openspec@latest`

## 相关项目

| 项目 | GitHub | 说明 |
|------|--------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | GitHub 官方规范驱动框架 |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 轻量 OPSX 工作流 |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | TDD + 审查方法论 |
| planning-with-files | [othmanadi/planning-with-files](https://github.com/othmanadi/planning-with-files) | 文件持久规划 |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX 设计系统 |
