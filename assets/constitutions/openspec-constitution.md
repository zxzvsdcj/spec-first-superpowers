# 项目宪法（Constitution） - Spec-First + Superpowers 终极约束版
# 默认偏向 OpenSpec 模式

版本：1.0  
创建日期：2026-02-23  
最后修订：2026-02-23  
适用范围：本项目所有 AI 生成的 spec、plan、tasks、代码、设计、规划文件均必须严格遵守此宪法。  
违反任何一条均为重大 blocker，必须立即停止当前流程并修正。

## 1. 核心使命与最高铁律
本项目的终极目标是：  
让 AI 完全按照**工程级最佳实践**工作，**杜绝凭感觉乱写代码**。

最高铁律（任何情况下不可违反）：
1. 必须先完成 SDD（规范驱动开发）全流程，才允许写任何一行代码。
2. 默认使用 **OpenSpec** 模式（OPSX 工作流），除非明确为全新项目且文件极少。
3. 所有规划必须持久化到文件（task_plan.md / findings.md / progress.md），聊天记录不可作为唯一记忆。
4. 任何涉及 UI/UX 的任务，必须先生成完整专业设计系统（ui-ux-pro-max-skill），并经用户确认后才允许实现。
5. 所有功能实现必须采用 **TDD-First** 方式（Superpowers 强制要求）。
6. 代码审查（requesting-code-review）是强制步骤，未通过审查不得合并。

## 2. 规范模式选择原则（与 meta-skill 对齐）
- 项目根目录存在 `.openspec/` → 强制 OpenSpec 模式
- 项目根目录存在 `.specify/` → 强制 Spec-Kit 模式
- 两者同时存在 → 报错并要求删除一个
- 无初始化文件夹时：
  - 明确关键词：new project / 从零开始 / greenfield / init → Spec-Kit
  - 其他所有情况（默认）→ OpenSpec
- 模式记录在项目根 `.spec-mode` 文件中，全局持久生效

## 3. 代码质量标准（Code Quality Rules）
- 严格遵循 Clean Code、SOLID、DRY、KISS 原则
- 所有公共接口/函数/类必须有完整文档（JSDoc / Docstring）
- 命名：camelCase（变量/函数）、PascalCase（类/组件）、kebab-case（文件/目录）
- 禁止魔法值，所有常量必须提取
- 代码风格强制工具：ESLint + Prettier / Ruff / Black / golangci-lint 等
- 禁止循环依赖，强制分层架构（presentation / application / domain / infrastructure）
- 每一次提交必须通过 linter + tests + coverage 检查

## 4. 测试规范（Testing Standards） - TDD-First 强制
- 所有新功能/修复必须**先写测试**（Superpowers TDD 要求）
- 单元测试覆盖率：关键路径 ≥ 95%，整体 ≥ 85%
- 测试必须独立、可重复、无副作用，使用 mock/stub/fake
- 关键业务逻辑必须有契约测试 / 属性测试 / 快照测试
- CI 管道中所有测试失败 → 阻塞合并
- 禁止提交“先实现后补测试”的代码

## 5. UI/UX 一致性与专业设计要求（强制 ui-ux-pro-max-skill）
- 所有界面相关任务必须先生成完整设计系统，包括：
  - Design Patterns（原子/分子/有机体）
  - Style Guide（颜色系统、排版系统、间距系统）
  - Color Palette（主色、辅助色、语义色、97+ 选项）
  - Typography（字体家族、大小、行高、字重、57+ 选项）
  - Effects（阴影、圆角、过渡、动画）
  - Anti-patterns 清单
  - Accessibility Checklist（WCAG 2.1 AA 级）
- 设计系统必须经用户确认后，才允许开始写 UI 代码
- 响应式优先：mobile-first，支持主流断点
- 国际化：所有文案提取到资源文件
- 一致性：按钮、表单、导航、反馈动画全局统一

## 6. 性能与安全基线
- 首屏加载 < 2.5s（90 分位）
- 交互响应 < 100ms
- Bundle size 主包 < 400KB（gzip 后）
- API 响应 < 200ms（P95 < 400ms）
- 禁止明文密钥、硬编码凭证
- 依赖安全扫描（npm audit / pip-audit / dependabot）
- OWASP Top 10 全防护（输入验证、CSRF、XSS 等）

## 7. 文件与规划持久化要求（planning-with-files 强制）
- 所有任务规划必须写入 task_plan.md（带 checkbox 状态）
- 研究、洞察、问题记录写入 findings.md
- 执行日志、测试结果、错误记录写入 progress.md
- 每一步行动前必须读取 task_plan.md
- 每一步完成后必须更新 progress.md
- 聊天记录不可替代文件，AI 必须以文件为唯一真相来源

## 8. 变更与修订流程
- 宪法修订需记录版本历史 + 理由
- 每次修订后，AI 应自检现有 spec/plan/tasks 是否仍符合
- 建议每 3 个月或重大技术栈变更时审视一次

## 9. 快速检查清单（AI 自检用）
- [ ] 当前模式已记录在 .spec-mode？
- [ ] SDD 规范是否完成并用户确认？
- [ ] task_plan.md / progress.md 是否已生成并更新？
- [ ] UI/UX 任务是否已生成完整设计系统并确认？
- [ ] 是否先写了测试（TDD）？
- [ ] 代码是否通过 linter / tests / coverage？
- [ ] 是否请求了 code-review？

**项目负责人签名**： __________________  
**日期**： __________________