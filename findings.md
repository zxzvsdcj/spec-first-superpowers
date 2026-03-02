# 深度分析报告：5 个开源项目精华提取与协同优化

> 分析日期：2026-03-02
> 目标：极致优化 spec-first-superpowers Skill，最大化 5 个开源项目的协同价值

## 1. 各项目精华提取

### 1.1 Spec-Kit (github/spec-kit)

| 精华能力 | 当前利用度 | 优化空间 |
|----------|-----------|---------|
| 宪法(Constitution)作为不可妥协原则 | 中 — 仅在开头提及 | 应在**每个质量闸门**主动校验宪法条款 |
| spec/plan/tasks 三文档分离 (What vs How) | 高 | 保持 |
| `specify check` 完整性验证 | 未利用 | 应整合到闸门 G1 |
| 用户确认门控 | 高 | 保持 |
| `.specify/` 结构化工件管理 | 中 | 与 planning-with-files 统一管理 |

### 1.2 OpenSpec (Fission-AI/OpenSpec)

| 精华能力 | 当前利用度 | 优化空间 |
|----------|-----------|---------|
| 变更驱动(Change-based)轻量流程 | 高 | 保持 |
| `/opsx:ff` 快速推进（需求已清晰时） | 未利用 | **作为复杂度分级的快速路径** |
| config.yaml 项目规则声明 | 低 | 可与宪法交叉引用 |
| `/opsx:archive` 归档管理 | 中 | 与 progress.md 同步 |
| 逐步 `/opsx:continue` 增量创建 | 中 | 保持 |

### 1.3 Superpowers (obra/superpowers)

| 精华能力 | 当前利用度 | 优化空间 |
|----------|-----------|---------|
| 技能优先级体系 (Process → Implementation) | 低 | 应在编排中强制执行 |
| brainstorming 硬门控 (设计先于编码) | 中 | 与 Spec 阶段融合而非串行重复 |
| TDD RED-GREEN-REFACTOR 铁律 | 中 | 保持 |
| **两阶段审查** (spec 符合 + 代码质量) | **未利用** | **应纳入执行阶段闸门** |
| **Subagent-Driven Development** | **未利用** | **作为执行阶段的可选策略** |
| systematic-debugging 4 阶段 + 3 次切换 | 低 — 仅"按需" | 应集成到错误处理链 |
| verification-before-completion 证据铁律 | 中 | 应绑定到 progress.md |
| finishing-a-development-branch 收尾 | **未利用** | **应纳入归档阶段** |
| executing-plans 批次检查点 | **未利用** | 作为执行选项之一 |

### 1.4 planning-with-files (othmanadi/planning-with-files)

| 精华能力 | 当前利用度 | 优化空间 |
|----------|-----------|---------|
| 文件即记忆 (Context Window=RAM, File=Disk) | 高 | 保持 |
| **session-catchup.py 会话恢复** | **未利用** | **应集成到阶段 0** |
| 2-Action Rule (每 2 次搜索保存) | 低 | 应在全流程强制 |
| **Read Before Decide 模式** | **未利用** | **每个阶段转换前必须重读** |
| 3-Strike Error Protocol | 低 | 应与 systematic-debugging 联动 |
| 5-Question Reboot Test | **未利用** | 作为上下文恢复的验证 |
| 错误日志表 (Error/Attempt/Resolution) | 低 | 标准化到 progress.md |
| 模板系统 (templates/) | 中 | 保持 |

### 1.5 ui-ux-pro-max (nextlevelbuilder/ui-ux-pro-max-skill)

| 精华能力 | 当前利用度 | 优化空间 |
|----------|-----------|---------|
| `--design-system` 一键设计系统生成 | 中 | 保持 |
| **`--persist` Master + Page overrides** | **未利用** | **设计持久化跨会话** |
| Pre-delivery Checklist (4 维度 20+ 项) | 低 | 应纳入闸门 G3 和 G4 |
| 9 技术栈专属指南 | 低 | 自动识别项目栈后推荐 |
| 推理规则 (ui-reasoning.csv) | 中 | 保持 |
| 常见专业 UI 规则 (no emoji/cursor-pointer) | 低 | 纳入审查清单 |

## 2. 当前 v1 的 12 个关键缺失

| # | 缺失 | 影响 | 涉及项目 |
|---|------|------|---------|
| 1 | 无会话恢复 | 长任务中断后丢失上下文 | planning-with-files |
| 2 | 无复杂度分级 | 简单 bugfix 被迫走完整流程 | OpenSpec `/opsx:ff` |
| 3 | 无 Read Before Decide | 长上下文中决策偏差 | planning-with-files |
| 4 | 无两阶段审查 | 代码可能偏离规范却通过审查 | Superpowers |
| 5 | 无 Subagent-Driven 选项 | 缺少高效执行路径 | Superpowers |
| 6 | 无 finishing-a-development-branch | 归档不完整 | Superpowers |
| 7 | 宪法仅被动引用 | 不同阶段可能违反宪法约束 | Spec-Kit |
| 8 | 无设计系统持久化 | 每次会话重新生成 | ui-ux-pro-max |
| 9 | 3-Strike 未联动 debugging | 失败处理碎片化 | planning + Superpowers |
| 10 | 验证证据未写入 progress.md | 完成声明无文件记录 | Superpowers + planning |
| 11 | 无质量闸门文档 | 闸门标准隐含在流程中 | 所有 |
| 12 | brainstorming 与 Spec 串行重复 | 浪费上下文和时间 | Superpowers + Spec |

## 3. 协同优化矩阵 (Cross-Project Synergies)

```
          Spec-Kit    OpenSpec    Superpowers    Planning    UI/UX
Spec-Kit     —        模式互斥     宪法×审查      工件统一     设计×规范
OpenSpec   模式互斥      —         ff×复杂度     归档×日志     config×设计
Superpowers 宪法×审查  ff×复杂度      —          错误×恢复     检查清单
Planning   工件统一    归档×日志    错误×恢复        —         持久化设计
UI/UX      设计×规范   config×设计  检查清单      持久化设计      —
```

关键协同链：
1. **宪法 → 闸门 → 审查**：宪法条款在每个闸门校验，审查时引用宪法
2. **错误 → 日志 → 调试**：progress.md 记录错误 → 3-Strike → systematic-debugging
3. **设计 → 持久化 → 恢复**：design-system/MASTER.md → 跨会话持久 → 自动恢复
4. **规范 → 计划 → 执行**：spec 工件直接转化为 task_plan.md 的编号清单
5. **验证 → 证据 → 归档**：verification 输出写入 progress.md → 归档

## 4. 来源

- Spec-Kit: 已安装 Skill + references/spec-kit-workflow.md
- OpenSpec: 已安装 Skill + references/openspec-workflow.md
- Superpowers: using-superpowers + 8 个子 Skill (brainstorming, writing-plans, TDD, etc.)
- planning-with-files: 已安装 Skill v2.10.0
- ui-ux-pro-max: 已安装 Skill + scripts/search.py
