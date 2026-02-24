内容基于本次会话中构建的 **Spec-First + Superpowers 终极约束系统**（默认偏向 OpenSpec），并整合了你提供的《AI 编程三剑客》文章的核心信息。

文档采用标准的 GitHub README 风格，结构清晰、易读，包含安装、配置、使用、维护等完整说明，便于团队协作、后期维护或开源分享。

你可以直接复制到项目根目录的 `README.md` 文件中，然后根据实际项目名称、技术栈做少量调整。

```markdown
# Spec-First + Superpowers 终极约束开发模板

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cursor Compatible](https://img.shields.io/badge/Cursor-Compatible-brightgreen)](https://cursor.sh)
[![OpenSpec Default](https://img.shields.io/badge/Default-OpenSpec-blue)](https://github.com/Fission-AI/OpenSpec)

一个强制规范先行、TDD 驱动、文件持久规划 + 专业 UI/UX 设计系统的 AI 编程工作流模板。  
防止 AI “凭感觉乱写代码”，确保工程级质量与一致性。  
默认偏向 **OpenSpec**（轻量迭代友好），兼容 Spec-Kit，集成 Superpowers 方法论。

## 为什么需要这个模板？

2024–2026 年 AI 编程工具爆发式增长，但 AI 常出现“直接乱写”“跳阶段”“上下文丢失”“UI 风格不统一”等问题。  
本模板通过以下三剑客 + 两个增强 Skill 解决：

- **Spec-Kit**（GitHub 官方）→ 严格规范驱动（新项目/复杂系统）  
- **OpenSpec**（社区热门，默认）→ 轻量 OPSX 迭代工作流（存量项目/快速开发）  
- **Superpowers** → TDD-First + 代码审查 + 验证方法论  
- **planning-with-files** → 文件持久规划（永不丢上下文）  
- **ui-ux-pro-max-skill** → 自动生成专业多平台 UI/UX 设计系统

## 核心特性

- 强制 **Spec-First**：任何任务必须先完成 SDD 规范（默认 OpenSpec）
- 智能模式选择：自动判断 Greenfield / Brownfield，默认 OpenSpec
- 一键激活：输入 `/super-spec` 启动完整约束流程
- 持久规划：task_plan.md / findings.md / progress.md 作为唯一真相
- UI/UX 强制前置：涉及界面自动生成完整设计系统
- TDD + Review 强制：Superpowers 全流程执行
- 项目宪法约束：constitution.md 作为最高指导原则

## 项目结构（初始化后典型目录）

```
your-project/
├── .cursor/
│   ├── rules/
│   │   └── 00-spec-first-superpowers.mdc     # 强制规则（Standalone Prompt）
│   └── skills/
│       └── spec-first-superpowers/
│           └── SKILL.md                      # 自定义 meta-skill
├── .spec-mode                                    # 模式记录（spec-kit 或 openspec）
├── .specify/                                     # Spec-Kit 模式时生成（可选）
│   └── memory/
│       └── constitution.md                   # 项目宪法
├── .openspec/                                    # OpenSpec 模式时生成（默认）
│   ├── changes/                                  # 活跃变更
│   └── config.yaml                               # 项目配置（推荐）
├── task_plan.md                                  # 持久任务计划
├── findings.md                                   # 研究/洞察/问题记录
├── progress.md                                   # 执行日志/测试结果
├── design-system.md                              # UI/UX 设计系统（自动生成）
└── README.md                                     # 本文档
```

## 快速开始

### 1. 安装依赖（一键脚本）

在项目根目录创建 `install-all.sh`，复制以下内容并运行：

```bash
chmod +x install-all.sh && ./install-all.sh
```

（脚本完整内容见项目 docs/install-all.sh 或会话历史）

### 2. 放置核心文件

- 复制本项目的 `.cursor/rules/00-spec-first-superpowers.mdc`（强制规则）
- 复制 `.cursor/skills/spec-first-superpowers/SKILL.md`（meta-skill）
- 复制 constitution.md（项目宪法模板）到合适位置：
  - OpenSpec：参考写入 `.openspec/config.yaml` 的 `context` / `rules`
  - Spec-Kit：放入 `.specify/memory/constitution.md`

### 3. 在 Cursor 中激活

新建聊天或继续现有聊天，直接输入：

```
/super-spec
```

AI 将强制输出启动模板，并开始完整流程：
1. 智能判断模式（默认 OpenSpec）
2. SDD 规范（/opsx:new 等）
3. 生成持久规划文件
4. UI/UX 检测 → 设计系统（若涉及）
5. Superpowers TDD 执行

示例：

```
/super-spec force-openspec 添加用户仪表盘，支持拖拽小部件
```

## 常用命令

- `/super-spec` / `@super-spec` → 激活完整约束流程
- `/super-spec reset` → 重置模式判断
- `/super-spec force-spec-kit` → 强制 Spec-Kit
- `/super-spec force-openspec` → 强制 OpenSpec（默认已偏向）

## 推荐工作流示例

1. 输入：`/super-spec 新增登录页面，支持邮箱+密码 + Google 登录`
2. AI 输出启动模板 → 进入 OpenSpec /opsx:new
3. 生成 proposal/spec/design/tasks.md
4. 生成 task_plan.md 等持久文件
5. 检测 UI → 生成完整设计系统（颜色/字体/交互规范）
6. 用户确认后 → Superpowers TDD 循环
7. 每步更新 progress.md，最终归档 /opsx:archive

## 涉及开源项目（便于维护）

| 项目                  | GitHub 地址                                              | Stars（2026年2月） | 主要功能                              |
|-----------------------|----------------------------------------------------------|---------------------|---------------------------------------|
| Spec-Kit              | https://github.com/github/spec-kit                       | ~71.5k             | 官方规范驱动框架                      |
| OpenSpec              | https://github.com/Fission-AI/OpenSpec                   | ~25.3k             | 轻量 OPSX 迭代工具（默认模式）        |
| Superpowers           | https://github.com/obra/superpowers                      | ~59.3k             | TDD + 审查 方法论                     |
| planning-with-files   | https://github.com/othmanadi/planning-with-files         | -                  | 文件持久规划                          |
| ui-ux-pro-max-skill   | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill  | -                  | 专业 UI/UX 设计系统生成               |

## 维护与升级

- 更新工具：重新运行 `install-all.sh`
- 更新宪法：修改 constitution.md 并通知 AI 自检
- 模式切换：`/super-spec reset` 后重新激活
- 文档维护建议：将本 README + 所有 GitHub 链接放入 docs/ai-constraint-workflow.md

## 贡献与反馈

欢迎提交 Issue / PR：
- 优化 constitution 模板
- 添加更多技术栈适配（Next.js、Flutter、.NET 等）
- 改进 UI/UX 设计系统输出格式

感谢使用！  
让 AI 真正成为可靠的工程伙伴。

ades @Hades96444367  
Singapore · 2026
```
