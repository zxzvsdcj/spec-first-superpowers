# Spec-First + Superpowers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cursor Compatible](https://img.shields.io/badge/Cursor-Compatible-brightgreen)](https://cursor.sh)
[![Default: OpenSpec](https://img.shields.io/badge/Default-OpenSpec-blue)](https://github.com/Fission-AI/OpenSpec)

强制规范先行的 AI 编程工作流 Skill。防止 AI 跳过设计直接写代码，确保工程级质量。

## 核心特性

- **Spec 先行**：任何任务必须先完成规范并获用户确认
- **智能模式选择**：自动判断 Spec-Kit（新项目）或 OpenSpec（默认，存量项目）
- **一键激活**：`/super-spec` 启动完整约束流程
- **文件持久化**：task_plan.md / findings.md / progress.md 防止上下文丢失
- **UI/UX 前置**：涉及界面时自动生成设计系统
- **TDD 强制**：Superpowers 方法论全流程执行

## 快速开始

### 1. 安装依赖 Skills

确保以下 Skills 已安装（通过 Cursor Skills 市场或 `npx skills add`）：

- `using-superpowers` + 子 Skills（brainstorming, writing-plans, test-driven-development 等）
- `planning-with-files`
- `ui-ux-pro-max`（推荐）

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
# 或
<project>/.cursor/skills/spec-first-superpowers/   # 项目级
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
├── SKILL.md                              # 核心编排逻辑
├── references/
│   ├── spec-kit-workflow.md              # Spec-Kit 详细工作流
│   ├── openspec-workflow.md              # OpenSpec 详细工作流
│   └── integration-guide.md             # 集成指南与排障
├── assets/
│   └── constitutions/
│       ├── openspec-constitution.md      # OpenSpec 宪法模板
│       └── spec-kit-constitution.md      # Spec-Kit 宪法模板
├── .cursor/
│   └── 00-spec-first-superpowers.mdc     # Always-on 守门规则
├── README.md
├── install-all.sh                        # 依赖安装脚本
└── 使用说明.md                            # 详细使用说明
```

## 常用命令

| 命令 | 效果 |
|------|------|
| `/super-spec` | 激活完整流程 |
| `/super-spec force-spec-kit` | 强制 Spec-Kit 模式 |
| `/super-spec force-openspec` | 强制 OpenSpec 模式 |
| `/super-spec reset` | 重置模式判断 |

## 工作流概览

```
/super-spec → 模式选择 → SDD 规范（用户确认）→ 持久规划 → UI/UX 设计（条件）→ TDD 执行 → 归档
```

## 集成的开源项目

| 项目 | GitHub | 说明 |
|------|--------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | GitHub 官方规范驱动框架 |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 轻量 OPSX 工作流（默认） |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | TDD + 审查方法论 |
| planning-with-files | [othmanadi/planning-with-files](https://github.com/othmanadi/planning-with-files) | 文件持久规划 |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX 设计系统 |

## 贡献

欢迎提交 Issue / PR：优化宪法模板、添加技术栈适配、改进工作流。

---

Hades @Hades96444367 · Singapore · 2026
