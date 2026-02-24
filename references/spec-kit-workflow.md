# Spec-Kit 工作流详解

Spec-Kit 是 GitHub 官方的规范驱动开发框架，适用于全新项目（Greenfield）或需要严格分阶段管理的复杂系统。

## 适用场景

- 全新项目从零搭建
- 大型系统（多模块、多团队协作）
- 需要严格阶段门控的企业级项目

## 完整命令流程

### 1. 项目宪法：`/speckit.constitution`

在 `.specify/memory/constitution.md` 中定义项目不可妥协原则：
- 代码质量标准（SOLID、DRY、KISS）
- 测试规范（覆盖率目标、TDD 要求）
- 性能基线
- 安全要求

模板参考：[assets/constitutions/spec-kit-constitution.md](../assets/constitutions/spec-kit-constitution.md)

### 2. 功能规范：`/speckit.specify`

生成 `.specify/specs/[feature-name]/spec.md`：
- **纯产品视角**（What & Why），禁止出现技术实现细节
- 包含：功能描述、用户故事、验收标准（Given-When-Then）、成功指标
- 必须引用宪法中的相关约束

### 3. 澄清歧义：`/speckit.clarify`

- 逐条审查 spec.md 中的模糊点
- 与用户逐轮确认（每次 1 个问题）
- 确保所有验收标准可测量、无歧义

### 4. 技术计划：`/speckit.plan`

生成 `.specify/specs/[feature-name]/plan.md`：
- **工程视角**（How），包含架构决策、技术选型
- 必须引用宪法检查点
- 包含风险评估与回滚策略

### 5. 任务分解：`/speckit.tasks`

生成 `.specify/specs/[feature-name]/tasks.md`：
- 原子化任务清单（每个任务可独立实现和测试）
- 带优先级和依赖关系
- 与 plan.md 中的架构模块对应

### 6. 用户确认门控

**spec.md + plan.md + tasks.md 三者全部经用户明确确认后**，才允许进入下一阶段。
确认信号："确认""OK""可以继续""Spec 没问题" 等明确语句。

## 初始化命令

```bash
specify init          # 初始化 .specify/ 目录
specify check         # 验证规范完整性
```

## 文件结构

```
.specify/
├── memory/
│   └── constitution.md    # 项目宪法
└── specs/
    └── [feature-name]/
        ├── spec.md        # 产品规范
        ├── plan.md        # 技术计划
        └── tasks.md       # 任务清单
```
