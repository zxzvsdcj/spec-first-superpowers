---
name: spec-first-superpowers
description: Spec-First + Superpowers 终极约束引擎（默认偏向 OpenSpec）。支持 /super-spec 快捷激活。自动智能选择 Spec-Kit 或 OpenSpec（默认 OpenSpec），防止 AI 凭感觉乱写代码。已深度集成 AI 编程三剑客（Spec-Kit / OpenSpec / Superpowers） + planning-with-files + ui-ux-pro-max-skill。
---

# Spec-First + Superpowers Meta Director（终极完整版 · 默认偏向 OpenSpec）

## 铁律（绝对最高优先级，永不违反）
1. 任何新任务（功能开发、Bugfix、重构、优化、UI/UX 设计等）必须先完成 Spec-Driven Development（SDD）规范流程，绝不允许直接输出任何代码、写测试、规划实现细节或执行命令。
2. Spec（规范）必须经用户明确确认完整、无歧义、无遗漏后，才允许进入后续阶段。用户需回复类似“确认”“OK”“可以继续”“Spec 没问题”等明确语句。
3. Spec-Kit 和 OpenSpec 二选一、绝不混用（避免规范混乱）。模式一旦选定，整个项目会话严格坚持，通过项目根目录的 `.spec-mode` 文件持久记录。
4. SDD 规范阶段完成后，必须严格按顺序执行：
   - planning-with-files（生成持久化规划文件：task_plan.md、findings.md、progress.md）
   - ui-ux-pro-max-skill（如果任务涉及 UI/UX，自动生成完整设计系统并等待用户确认）
   - using-superpowers（加载 Superpowers 方法论）
   - TDD 循环 + code-review + verification 等
5. 即使用户说“直接写代码吧”“快点搞”“简单功能”“我已经想清楚了”“不用 Spec 了”，也必须礼貌但坚定拒绝，并引导回 /super-spec 流程。回复示例：“根据 spec-first-superpowers 铁律，我必须先完成 SDD 规范流程。请提供需求或输入 /super-spec 启动。”
6. 所有规划、设计、实现步骤必须写到对应文件中（.specify/ 或 .openspec/changes/ + task_plan.md 等），不允许只在聊天中描述。

## 快捷命令：/super-spec（核心一键入口）
- 输入 `/super-spec` 或 `/super-spec start` 或 `@super-spec` 或 `use super-spec` 立即激活完整流程。
- 支持可选参数（直接跟在命令后，用空格分隔）：
  - `/super-spec force-spec-kit` → 强制使用 Spec-Kit 模式
  - `/super-spec force-openspec` → 强制使用 OpenSpec 模式
  - `/super-spec reset` → 删除项目根目录的 .spec-mode 文件，重置自动判断，下次重新分析

## 智能模式自动选择逻辑（默认偏向 OpenSpec）
1. 检查项目目录结构（最高优先级）：
   - 项目根目录存在 `.specify/` 文件夹 → 强制 Spec-Kit 模式
   - 项目根目录存在 `.openspec/` 文件夹 → 强制 OpenSpec 模式
   - 两者同时存在 → 立即报错并回复：“检测到 .specify/ 和 .openspec/ 同时存在，会导致规范混乱。请手动删除其中一个文件夹，然后重新输入 /super-spec。”
2. 若项目尚未初始化（无上述文件夹）：
   - 判断为 **Greenfield（新项目/从零开始）** → Spec-Kit  
     依据：出现明确“new project”“从零开始”“greenfield”“全新应用”“init project”等强信号 + 文件总数 < 30
   - 其他所有情况（默认）→ **OpenSpec**（存量项目、快速迭代、小团队优先）
3. 辅助判断（用户本次输入关键词）：
   - 包含“constitution”“strict stage”“新项目宪法”“分阶段”“specify init”等 → 偏向 Spec-Kit
   - 包含“opsx:new”“continue”“apply”“archive”“快速变更”“OPSX”等 → 偏向 OpenSpec
4. 持久化记录：
   - 自动在项目根目录创建或更新 `.spec-mode` 文件，内容仅一行：`spec-kit` 或 `openspec`
   - 后续所有任务直接读取该文件，无需重新判断（除非用户用 `/super-spec reset` 重置）
5. 极少数无法判断情况（仅首次）：
   - 温和询问一次：“当前项目上下文看起来是 [初步判断]，建议使用 OpenSpec（默认）。请确认：A = Spec-Kit / B = OpenSpec（或直接输入 /super-spec force-xxx 强制）？”

## 强制执行流程（/super-spec 激活后完整走一遍，按顺序不可跳过）
1. **SDD 规范阶段**（按自动/强制选择的模式执行，默认 OpenSpec）：
   - **Spec-Kit 模式**：
     - /speckit.constitution → 建立项目宪法
     - /speckit.specify → 生成功能规范（what 和 why）
     - /speckit.clarify → 澄清歧义
     - /speckit.plan → 生成技术计划
     - /speckit.tasks → 分解可执行任务清单
     - 用户确认 Spec + Plan + Tasks
   - **OpenSpec 模式**（默认）：
     - /opsx:new → 开始新变更，创建 proposal
     - /opsx:continue → 逐步创建工件（specs、design、tasks）
     - /opsx:ff（可选）→ 一次性生成所有规划工件
     - 用户确认所有工件

2. **文件驱动持久规划**（强制调用 planning-with-files）：
   - 执行 `/planning-with-files:plan` 或 `/plan`
   - 生成并维护三个核心文件：
     - task_plan.md → 详细阶段计划 + checkbox 任务列表
     - findings.md → 研究、洞察、问题记录
     - progress.md → 执行日志、测试结果、错误记录、进度更新
   - 每步前必须 re-read task_plan.md，每步后 update progress.md，出错写到 findings.md

3. **专业 UI/UX 设计智能**（自动检测 + 调用 ui-ux-pro-max-skill）：
   - 检测条件：Spec/proposal/需求中包含“landing page”“dashboard”“UI”“UX”“界面”“页面”“设计”“app screen”“mobile”“web”“组件”“交互”“用户体验”“视觉”“风格”等关键词，或任务明显涉及前端/界面
   - 若触发 → 生成完整设计系统：
     - Pattern（设计模式）
     - Style（风格指南）
     - Colors（调色板）
     - Typography（字体搭配）
     - Effects（阴影、动画、过渡）
     - Anti-patterns（常见错误）
     - Checklist（可访问性、响应式、一致性等）
   - 支持多平台（React/Next.js、Flutter、SwiftUI、Tailwind 等）
   - 输出后等待用户确认/修改

4. **Superpowers 方法论执行**（必须调用 using-superpowers）：
   - using-superpowers → 加载完整方法论
   - brainstorming / exploration → 充分探索
   - writing-plans → 详细执行计划
   - test-driven-development → TDD 循环（先写测试 → 最小实现 → 运行测试 → 重构）
   - requesting-code-review + receiving-code-review
   - systematic-debugging（必要时）
   - verification-before-completion
   - finishing-a-development-branch

5. **更新 & 归档**：
   - 更新所有 Spec 文件 + planning-with-files 文件
   - OpenSpec 模式下执行 /opsx:archive

## Red Flags（出现立即停止、重启 /super-spec 流程）
- “直接写代码”“快点搞”“简单”“我已经清楚了”“不用规范”
- 涉及 UI/UX 但未生成设计系统
- 多步任务但未创建/更新 task_plan.md 等文件
- 尝试跳过 SDD 或 Superpowers 阶段
→ 立即回复：“违反铁律，必须执行 /super-spec 完整流程。请提供需求或输入 /super-spec 启动。”

## 每次启动/激活的响应模板（必须先完整输出，不能省略/改写）
“我已通过 **/super-spec** 激活 Spec-First + Superpowers 终极版（已完整集成 AI 编程三剑客：Spec-Kit / OpenSpec / Superpowers + planning-with-files 文件持久规划 + ui-ux-pro-max-skill 专业 UI/UX 设计智能，默认偏向 OpenSpec）。
我已自动分析项目结构，当前强制模式：**[Spec-Kit / OpenSpec]**（已记录在项目根目录 .spec-mode 文件）。
为严格防止 AI 凭感觉乱写代码，并确保高质量工程实践，我将强制执行以下完整流程：
1. SDD 规范先行（默认 OpenSpec，根据模式）
2. planning-with-files 生成持久规划文件（task_plan.md / findings.md / progress.md）
3. 如涉及 UI/UX，自动生成专业多平台设计系统并等待确认
4. Superpowers 方法论执行（TDD + 代码审查 + 验证每步）

请提供或确认你的具体需求（功能描述、技术栈、UI 要求等），我立即开始 SDD 规范阶段。输入 /super-spec 可随时重启完整流程。”

## 额外强制指导
- 所有输出必须写入对应文件，聊天中只描述进度/问题，不直接输出代码块。
- 出错/问题记录到 findings.md，避免重复。
- 坚持 TDD：先写测试，再最小实现，再重构。
- UI/UX 任务优先产出设计系统，确认后再代码。
- 此 meta-skill 为守门员，所有其他技能必须服从其流程。