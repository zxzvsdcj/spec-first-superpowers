# [项目名称] Constitution（项目宪法）

**版本**：1.0  
**批准日期**：YYYY-MM-DD  
**最后修订**：YYYY-MM-DD  
**适用范围**：本项目所有规范、计划、任务、代码实现均必须遵守此宪法。任何违反均视为重大问题，需要立即修正。

## 1. 前言与目的
本宪法定义了项目的**不可妥协原则**（immutable principles），是所有 Spec-Driven Development（SDD）流程的最高指导文件。  
AI 代理在生成 spec.md、plan.md、tasks.md 时必须引用并遵守这些原则。  
目的：确保项目一致性、可维护性、高质量、可扩展性，并避免技术债务积累。

## 2. 核心原则（Core Principles）
以下原则为**一级优先级**，所有技术决策必须与之对齐。违反需在 plan.md 中明确说明权衡理由并获得人工批准。

### 2.1 代码质量（Code Quality）
- 代码必须**可读、可维护、可测试**（Clean Code 原则）。
- 所有公共 API/类/方法必须包含完整文档（JSDoc / Docstring / XML 注释）。
- 遵循单一职责原则（SRP）、DRY（Don't Repeat Yourself）、KISS（Keep It Simple Stupid）。
- 禁止魔法数字/字符串，必须提取为常量或配置。
- 命名规范：camelCase / PascalCase 一致，变量名有意义，避免缩写。
- 代码风格强制使用 ESLint / Prettier / Black / Ruff 等工具，并在 pre-commit 钩子中运行。
- 禁止循环依赖，架构层级必须清晰（分层/模块化）。
- 所有变更必须通过代码审查（至少 1 人 approve）。

### 2.2 测试规范（Testing Standards）
- 采用 **TDD / BDD** 优先（先写测试，再写实现）。
- 单元测试覆盖率目标：**≥ 85%**（关键路径 ≥ 95%）。
- 所有新功能/修复必须包含对应测试（单元 + 集成 + E2E）。
- 测试必须独立、可重复、无副作用，使用 mock/stub。
- 关键业务逻辑必须有契约测试 / 属性测试。
- CI/CD 管道中必须运行所有测试，失败即阻塞合并。
- 禁止提交未测试代码（coverage report 必须通过）。

### 2.3 用户体验一致性（User Experience Consistency）
- 所有 UI 组件必须遵循**统一设计系统**（Design System / Atomic Design）。
- 支持响应式设计（mobile-first，适配桌面/平板/手机）。
- 符合 **WCAG 2.1 AA** 无障碍标准（ARIA、键盘导航、对比度 ≥ 4.5:1）。
- 交互一致：按钮风格、加载动画、错误提示、导航模式统一。
- 国际化/本地化支持：所有硬编码字符串提取到资源文件。
- 性能感知：页面加载 < 3s，交互响应 < 100ms。
- 用户故事必须包含验收标准（Given-When-Then 格式）。

### 2.4 性能要求（Performance Requirements）
- 核心页面首屏加载时间 < 2s（90 分位）。
- 避免阻塞渲染（defer/async 脚本、懒加载图片/组件）。
- Bundle size 控制：主包 < 500KB（gzip 后）。
- 数据库查询优化：避免 N+1，添加索引，使用缓存。
- API 响应时间 < 200ms（P95 < 500ms）。
- 监控性能指标（LCP、FID、CLS），集成 Sentry / New Relic 等。
- 移动端优先优化（低带宽场景下仍流畅）。

## 3. 架构与技术决策治理（Governance）
- 所有重大架构决策必须记录在 plan.md 中，并引用宪法原则。
- 技术栈变更需在 constitution.md 中记录理由和影响评估。
- 优先选择**成熟、社区活跃、长期支持**的技术（LTS 版本）。
- 禁止引入高风险依赖（已弃用包、star < 1k 的实验项目）。
- 所有第三方库必须有许可证审查（MIT/Apache 优先）。
- 安全原则：OWASP Top 10 防护、依赖扫描、秘密管理（no .env in git）。
- 文档分离原则：spec.md 只写 WHAT & WHY，plan.md 写 HOW。

## 4. 文档与规范分离（Documentation Separation of Concerns）
- spec.md：**纯产品视角**（What & Why），技术无关。
  - 禁止出现框架、库、代码结构、实现细节。
  - 焦点：用户故事、验收标准、成功指标。
- plan.md：**工程视角**（How），包含所有技术决策。
  - 必须引用 constitution 检查点。
- 违反分离视为 blocker，必须修正。

## 5. 变更与修订流程
- 宪法修订需人工批准 + 记录版本历史。
- 每次修订后，AI 应检查现有 spec/plan 是否仍符合。
- 建议每季度审视一次，或重大技术变更时触发。

## 6. 附录：快速检查清单
- 代码提交前：运行 linter、tests、coverage ≥ 85%。
- 新功能前：spec.md 技术无关？plan.md 引用宪法？
- UI 变更前：设计系统一致？无障碍检查？
- 性能变更前：基准测试前后对比？

**签名/批准**  
项目负责人：__________________ 日期：__________