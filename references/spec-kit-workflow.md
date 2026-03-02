# Spec-Kit 工作流详解

Spec-Kit 是 GitHub 官方的规范驱动开发框架，适用于全新项目或需要严格分阶段管理的复杂系统。

## 适用场景

- 全新项目从零搭建
- 大型系统（多模块、多团队协作）
- 需要严格阶段门控的企业级项目

## 完整命令流程

### 1. 项目宪法：`/speckit.constitution`

在 `.specify/memory/constitution.md` 中定义不可妥协原则。
模板参考：[assets/constitutions/spec-kit-constitution.md](../assets/constitutions/spec-kit-constitution.md)

**宪法条款将在后续每个闸门中被主动校验，而非仅被被动引用。**

### 2. 功能规范：`/speckit.specify`

生成 `.specify/specs/[feature-name]/spec.md`：
- **纯产品视角**（What & Why），禁止技术实现细节
- 包含：功能描述、用户故事、验收标准（Given-When-Then）、成功指标
- 每个验收标准必须可映射为至少一个测试用例
- **必须引用宪法中的相关约束**

### 3. 澄清歧义：`/speckit.clarify`

- 逐条审查 spec.md 中的模糊点
- 与用户逐轮确认（每次 1 个问题）
- 确保所有验收标准可测量、无歧义

**快速级别可跳过此步**（复杂度分级 = 快速 时）。

### 4. 技术计划：`/speckit.plan`

生成 `.specify/specs/[feature-name]/plan.md`：
- **工程视角**（How），包含架构决策、技术选型
- **必须引用宪法检查点**（对每个决策标注对应的 constitution 条款）
- 包含风险评估与回滚策略

### 5. 任务分解：`/speckit.tasks`

生成 `.specify/specs/[feature-name]/tasks.md`：
- 原子化任务清单（每个任务可独立实现和测试）
- 带优先级和依赖关系
- 与 plan.md 中的架构模块对应
- **与 task_plan.md 同步**：tasks.md 管原子任务描述，task_plan.md 管进度状态

### 6. 用户确认门控（闸门 G1）

**spec.md + plan.md + tasks.md 三者全部经用户明确确认后**，才允许进入下一阶段。

G1 检查清单（必须全部通过）：
- [ ] 用户给出明确确认信号
- [ ] spec.md 不含技术实现细节
- [ ] plan.md 引用了 constitution 检查点
- [ ] 每个验收标准可映射为测试用例
- [ ] `specify check` 返回无错误
- [ ] 规范内容不违反 constitution 任何一级约束

## 初始化命令

```bash
specify init          # 初始化 .specify/ 目录
specify check         # 验证规范完整性（集成到 G1 闸门）
```

## 文件结构

```
.specify/
├── memory/
│   └── constitution.md    # 项目宪法（闸门校验依据）
└── specs/
    └── [feature-name]/
        ├── spec.md        # 产品规范 (What & Why)
        ├── plan.md        # 技术计划 (How, 引用 constitution)
        └── tasks.md       # 任务清单 (与 task_plan.md 同步)
```
