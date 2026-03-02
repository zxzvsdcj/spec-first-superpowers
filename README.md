# Spec-First + Superpowers v3

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cursor Compatible](https://img.shields.io/badge/Cursor-Compatible-brightgreen)](https://cursor.sh)
[![Default: OpenSpec](https://img.shields.io/badge/Default-OpenSpec-blue)](https://github.com/Fission-AI/OpenSpec)

强制规范先行的 AI 编程工作流 Skill。防止 AI 跳过设计直接写代码，确保工程级质量。

## v3 新特性

- **复杂度分级**：自动判断快速/标准/深度，简单 bugfix 走快速路径
- **会话恢复**：检测已有 task_plan.md 自动恢复上下文
- **质量闸门 G0-G4**：每阶段有明确通过标准，宪法主动校验
- **两阶段审查**：spec 符合 + 代码质量双重审查
- **Subagent-Driven 执行**：每任务 fresh subagent，零上下文污染
- **错误升级链**：3-Strike Protocol + systematic-debugging 联动
- **设计系统持久化**：ui-ux-pro-max `--persist` 跨会话复用
- **5 条协同链**：宪法→闸门→审查 / 错误→日志→调试 / 设计→持久化→恢复 / 规范→计划→执行 / 验证→证据→归档

## 快速开始

### 1. 安装依赖 Skills

确保以下 Skills 已安装（通过 Cursor Skills 市场或 `npx skills add`）：

- `using-superpowers` + 子 Skills（brainstorming, writing-plans, TDD, code-review 等）
- `planning-with-files`
- `ui-ux-pro-max`（推荐）
- `finishing-a-development-branch`

外部 CLI 工具（按需）：

```bash
# Spec-Kit CLI（新项目使用）
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# OpenSpec CLI（默认模式）
npm install -g @fission-ai/openspec@latest
```

### 2. 放置 Skill 文件

将本项目的 `SKILL.md`（含 `references/` 和 `assets/`）复制到：

```
~/.cursor/skills/spec-first-superpowers/     # 全局
```

将 `.cursor/00-spec-first-superpowers.mdc` 复制到项目的 `.cursor/rules/` 目录。

### 3. 激活

在 Cursor 聊天中输入：

```
/super-spec
```

## 项目结构

```
spec-first-superpowers/
├── SKILL.md                              # 核心编排逻辑 (v3)
├── references/
│   ├── spec-kit-workflow.md              # Spec-Kit 工作流 + 闸门标准
│   ├── openspec-workflow.md              # OpenSpec 工作流 + 快速路径
│   ├── integration-guide.md             # 集成指南 + 会话恢复 + 错误链
│   ├── quality-gates.md                 # G0-G4 质量闸门详细标准
│   └── synergy-patterns.md              # 5 条跨项目协同链
├── assets/
│   └── constitutions/
│       ├── openspec-constitution.md      # OpenSpec 宪法模板 + 闸门检查点
│       └── spec-kit-constitution.md      # Spec-Kit 宪法模板 + 闸门检查点
├── .cursor/
│   └── 00-spec-first-superpowers.mdc     # Always-on 守门规则
├── test_skill.py                        # 验证脚本
├── install-all.sh                       # 依赖安装脚本
├── README.md
└── 使用说明.md
```

## 常用命令

| 命令 | 效果 |
|------|------|
| `/super-spec` | 激活完整流程（自动分级） |
| `/super-spec force-spec-kit` | 强制 Spec-Kit 模式 |
| `/super-spec force-openspec` | 强制 OpenSpec 模式 |
| `/super-spec reset` | 重置模式判断 |

## 工作流概览

```
/super-spec → 模式选择 → 复杂度分级 → 会话恢复(自动) → SDD 规范(G1) → 持久规划(G2) → UI/UX 设计(G3,条件) → TDD 执行(G4) → 归档
```

## 集成的开源项目

| 项目 | GitHub | 说明 |
|------|--------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | GitHub 官方规范驱动框架 |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 轻量 OPSX 工作流（默认） |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | TDD + 审查方法论 |
| planning-with-files | [othmanadi/planning-with-files](https://github.com/othmanadi/planning-with-files) | 文件持久规划 |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX 设计系统 |

---

Hades @Hades96444367 · Singapore · 2026
