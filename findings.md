# 五大核心工具官方更新调研报告

> 调研日期：2026-03-19
> 目标：全面审查五项核心工具的官方更新，指导 spec-first-superpowers v4 优化

## 1. Spec-Kit (github/spec-kit) — 重大更新

### 新增内容

| 变更 | 详情 | 对本项目影响 |
|------|------|-------------|
| **安装方式变更** | `uv tool install specify-cli --from git+...` (替代旧方式) | 需更新安装说明 |
| **新命令 `/speckit.implement`** | 直接执行所有任务并按计划构建功能 | 需纳入 spec-kit-workflow.md |
| **新命令 `/speckit.clarify`** | 澄清不明确区域（原 `/quizme`） | 已有但需确认名称同步 |
| **新命令 `/speckit.analyze`** | 跨工件一致性和覆盖率分析（建议在 `/speckit.tasks` 后、`/speckit.implement` 前运行） | **新增——应纳入闸门流程** |
| **新命令 `/speckit.checklist`** | 生成自定义质量检查清单（"unit tests for English"） | 可整合到 G1/G2 |
| **扩展 & 预设系统** | `.specify/extensions/` + `.specify/presets/` 实现工作流定制化 | 更新 workflow 文档 |
| **支持 20+ AI Agent** | Cursor, Claude Code, Gemini CLI, Codex, Windsurf, Kiro 等 | 更新兼容性说明 |
| **Plugin Marketplace** | Claude Code 官方市场支持 `/plugin install` | 更新安装指南 |
| **社区 Walkthrough** | 5 个示例（Greenfield/Brownfield/.NET/Java/Go） | 可链接参考 |
| **`--ai-skills` 标志** | 将 Prompt.MD 模板安装为 agent skills | 新功能支持 |

### 命令体系（最新完整版）

| 命令 | 类型 | 说明 |
|------|------|------|
| `/speckit.constitution` | 核心 | 创建/更新项目治理原则 |
| `/speckit.specify` | 核心 | 定义需求和用户故事 |
| `/speckit.plan` | 核心 | 创建技术实现计划 |
| `/speckit.tasks` | 核心 | 生成可执行任务列表 |
| `/speckit.implement` | **核心(新)** | 执行所有任务 |
| `/speckit.clarify` | 可选 | 澄清不明确区域 |
| `/speckit.analyze` | **可选(新)** | 跨工件一致性分析 |
| `/speckit.checklist` | **可选(新)** | 生成质量检查清单 |

---

## 2. OpenSpec (Fission-AI/OpenSpec) — 架构级重构

### 核心变更：OPSX 成为标准工作流

旧工作流 (`/openspec:proposal`) 已被 OPSX 替代。关键哲学转变：**"Actions, not phases"**。

### 双配置文件（Profile 系统）

| Profile | 默认命令 | 说明 |
|---------|---------|------|
| **core**（默认） | `propose`, `explore`, `apply`, `archive` | 快速路径 |
| **expanded** | 上述 + `new`, `continue`, `ff`, `verify`, `sync`, `bulk-archive`, `onboard` | 完整功能 |

### 新增命令

| 命令 | 说明 | 对本项目影响 |
|------|------|-------------|
| **`/opsx:propose`** | 一步创建变更+生成规划工件（替代 `/opsx:new` + `/opsx:ff` 组合） | **核心路径变更** |
| **`/opsx:explore`** | 探索想法、调查问题、澄清需求（无结构化要求） | **新增——可与 brainstorming 联动** |
| **`/opsx:verify`** | 验证实现是否匹配工件（Completeness/Correctness/Coherence 三维度） | **新增——应整合到 G4** |
| **`/opsx:sync`** | 将 delta specs 合并到主 specs | 新增 |
| **`/opsx:bulk-archive`** | 批量归档多个已完成变更 | 新增 |
| **`/opsx:onboard`** | 引导式端到端教程 | 新增 |

### 其他重要更新

- **安装**: `npm install -g @fission-ai/openspec@latest` + `openspec init`
- **项目配置**: `openspec/config.yaml` (schema, context, rules)
- **目录结构变更**: `openspec/changes/` (不再是 `.openspec/changes/`)
- **模型推荐**: "推荐 Opus 4.5 和 GPT 5.2"
- **多语言支持**: 国际化文档

---

## 3. Superpowers (obra/superpowers) — 显著增强

### brainstorming 重大升级

| 新特性 | 说明 | 对本项目影响 |
|--------|------|-------------|
| **Spec Review Loop** | 写完 spec 后分派 spec-document-reviewer subagent，最多 3 轮迭代 | **新质量关——应整合到 G1** |
| **Visual Companion** | 基于浏览器的伴侣工具，用于展示 mockup/图表 | 可选增强 |
| **Scope Check** | 如果需求涉及多个独立子系统，早期标记需要分解 | 重要增强 |
| **User Review Gate** | 用户必须审阅书面 spec 才能继续 | 强化 G1 |
| **Design Doc 存储** | `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` | 更新路径 |
| **HARD-GATE** | 即使"简单"项目也不跳过设计 | 强化哲学 |

### writing-plans 重大升级

| 新特性 | 说明 | 对本项目影响 |
|--------|------|-------------|
| **Plan Document Header** | 标准化头部，含必需 sub-skill 引用 | 更新模板 |
| **File Structure Mapping** | 定义任务前先映射所有文件 | 增强 G2 |
| **Plan Review Loop** | 分派 plan-document-reviewer subagent，最多 3 轮 | **新质量关——应整合到 G2** |
| **Execution Handoff** | 明确提供 Subagent-Driven vs Inline 选择 | 更新执行策略 |
| **Plans 存储** | `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md` | 更新路径 |
| **Scope Check** | 多独立子系统应拆分为独立计划 | 重要增强 |

### subagent-driven-development 重大升级

| 新特性 | 说明 |
|--------|------|
| **Model Selection** | 按角色使用最低成本模型（机械任务用 fast，架构用 capable） |
| **Implementer Status** | DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED 四种状态 |
| **Prompt Templates** | `implementer-prompt.md`, `spec-reviewer-prompt.md`, `code-quality-reviewer-prompt.md` |
| **详细流程图** | Graphviz 流程图描述完整流程 |
| **Red Flags** | 明确列出禁止行为（不跳过审查、不并行实现等） |

### 新增 Skills

| Skill | 说明 |
|-------|------|
| `dispatching-parallel-agents` | 并发 subagent 工作流 |
| `writing-skills` | 创建新 skills（含测试方法论） |

### 安装方式

- **Claude Code**: `/plugin install superpowers@claude-plugins-official`
- **Cursor**: `/add-plugin superpowers`
- **Gemini CLI**: `gemini extensions install https://github.com/obra/superpowers`

---

## 4. planning-with-files (OthmanAdi/planning-with-files) — 稳定迭代

- 默认分支为 `master`（非 `main`）
- 最近推送：2026-03-15
- 支持多平台：`.cursor/`, `.claude-plugin/`, `.codex/`, `.gemini/` 等
- 核心功能稳定：三文件体系 + 会话恢复 + 3-Strike + 5-Question Reboot
- 无重大架构变更

---

## 5. ui-ux-pro-max (nextlevelbuilder/ui-ux-pro-max-skill) — v2.0 发布

### 数量级提升

| 维度 | v1 (项目引用) | v2.0 (官方最新) | 增幅 |
|------|--------------|----------------|------|
| UI Styles | 50 | **67** | +34% |
| Color Palettes | 21 | **161** | +667% |
| Font Pairings | 50 | **57** | +14% |
| Chart Types | 20 | **25** | +25% |
| Tech Stacks | 9 | **13** | +44% |
| Reasoning Rules | — | **161** | 全新 |
| UX Guidelines | — | **99** | 全新 |

### 新增 Tech Stacks

Astro, Nuxt.js, Nuxt UI, Jetpack Compose

### v2.0 旗舰功能：智能设计系统生成器

5 路并行搜索：产品类型匹配(161类) → 风格推荐(67种) → 色彩选择(161色) → 着陆页模式(24种) → 排版配对(57组)

### 新增 Style 类别

- Landing Page Styles (8 种)
- BI/Analytics Dashboard Styles (10 种)

### CLI 工具

`uipro-cli` (npm 包)

---

## 6. 当前项目 v3 与官方最新的差距汇总

| # | 差距 | 影响级别 | 涉及文件 |
|---|------|---------|---------|
| 1 | Spec-Kit 缺少 `/speckit.implement`, `/speckit.analyze`, `/speckit.checklist` | 高 | spec-kit-workflow.md |
| 2 | Spec-Kit 安装方式过时 | 中 | integration-guide.md, install-all.* |
| 3 | OpenSpec 未反映 `/opsx:propose` 核心路径 + `/opsx:explore` | **高** | openspec-workflow.md |
| 4 | OpenSpec 缺少 `/opsx:verify` 三维度验证 | 高 | openspec-workflow.md, quality-gates.md |
| 5 | OpenSpec Profile 系统 (core vs expanded) 未体现 | 中 | openspec-workflow.md |
| 6 | OpenSpec 目录结构变更 (`openspec/` 替代 `.openspec/`) | **高** | openspec-workflow.md, constitution |
| 7 | brainstorming Spec Review Loop 未整合到 G1 | 高 | quality-gates.md, SKILL.md |
| 8 | brainstorming Visual Companion 未提及 | 低 | synergy-patterns.md |
| 9 | writing-plans Plan Review Loop 未整合到 G2 | 高 | quality-gates.md |
| 10 | writing-plans File Structure Mapping 未要求 | 中 | quality-gates.md |
| 11 | subagent-driven-development Model Selection 未引导 | 中 | integration-guide.md |
| 12 | subagent-driven-development Implementer Status 处理未文档化 | 中 | synergy-patterns.md |
| 13 | ui-ux-pro-max 数据量过时（50→67 styles, 21→161 palettes 等） | 高 | SKILL.md description, README |
| 14 | ui-ux-pro-max 新增 Tech Stacks 未列出 | 中 | integration-guide.md |
| 15 | 安装脚本未反映各工具最新安装方式 | 中 | install-all.sh/ps1 |
| 16 | Superpowers 安装方式未更新（Plugin Marketplace） | 中 | integration-guide.md |
| 17 | 协同链缺少新能力整合（verify + review loops） | 高 | synergy-patterns.md |

---

## 7. 来源

- Spec-Kit: https://github.com/github/spec-kit (README + CLI Reference + Extensions/Presets)
- OpenSpec: https://github.com/Fission-AI/OpenSpec (README + docs/opsx.md + docs/commands.md)
- Superpowers: https://github.com/obra/superpowers (README + skills/brainstorming/SKILL.md + skills/writing-plans/SKILL.md + skills/subagent-driven-development/SKILL.md)
- planning-with-files: https://github.com/OthmanAdi/planning-with-files (API metadata)
- ui-ux-pro-max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (README v2.0)
