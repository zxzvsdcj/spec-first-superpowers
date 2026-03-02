# 质量闸门详细标准 (G0–G4)

每个闸门是**阶段间的硬门控**。不满足全部条件 → 回退修复 → 重新评估。
闸门检查时必须引用宪法(constitution)中的对应条款。

## 目录

- [G0 上下文恢复闸门](#g0-上下文恢复闸门)
- [G1 规范完成闸门](#g1-规范完成闸门)
- [G2 规划完备闸门](#g2-规划完备闸门)
- [G3 设计确认闸门](#g3-设计确认闸门)
- [G4 执行验证闸门](#g4-执行验证闸门)

---

## G0 上下文恢复闸门

**触发条件**：task_plan.md 已存在（说明有未完成任务）。

| 检查项 | 通过标准 |
|--------|---------|
| 规划文件完整性 | task_plan.md + findings.md + progress.md 均存在且可读 |
| 5-Question Reboot Test | 能回答：我在哪个阶段 / 下一步是什么 / 总目标 / 已发现什么 / 已完成什么 |
| 断点定位 | 在 task_plan.md 中找到最后一个 `[x]` 标记，下一个 `[ ]` 即为断点 |
| 上下文一致 | git diff --stat 与 progress.md 记录一致，无未记录的变更 |

**不通过时**：补充缺失文件 → 手动对齐状态 → 重新评估。

---

## G1 规范完成闸门

**触发位置**：阶段 1（SDD 规范）→ 阶段 2（持久规划）

| 检查项 | 通过标准 | 宪法映射 |
|--------|---------|---------|
| 用户明确确认 | 用户给出"确认/OK/可以/没问题"等明确信号 | §1 核心使命 |
| 规范完整性 | Spec-Kit: spec.md 含用户故事+验收标准 · OpenSpec: proposal+spec 完整 | §4 文档分离 |
| What vs How 分离 | spec/proposal 中无技术实现细节 | §4 文档分离 |
| 宪法对齐 | 规范内容不违反 constitution 中任何一级约束 | §2 核心原则 |
| 验收标准可测 | 每个验收标准可映射为至少一个测试用例 | §2.2 测试规范 |

**Spec-Kit 额外检查**：`specify check` 返回无错误。

**不通过时**：执行 `/speckit.clarify` 或 `/opsx:continue` 补充 → 重新确认。

---

## G2 规划完备闸门

**触发位置**：阶段 2（持久规划）→ 阶段 3/4（设计/执行）

| 检查项 | 通过标准 |
|--------|---------|
| 三文件就绪 | task_plan.md + findings.md + progress.md 均已创建 |
| 编号检查清单 | task_plan.md 中每个原子操作独立编号（如 1.1, 1.2, 2.1...） |
| 文件路径明确 | 每个任务列出 Create/Modify/Test 的精确文件路径 |
| TDD 测试点 | 每个任务包含测试用例草案或测试策略 |
| 验收标准映射 | 每个任务可追溯到 G1 中已确认的验收标准 |
| 风险评估 | 高风险操作标注回滚策略 |

**不通过时**：补充缺失项 → 用户确认计划 → 重新评估。

---

## G3 设计确认闸门

**触发位置**：阶段 3（UI/UX 设计）→ 阶段 4（执行）。仅 UI/UX 任务触发。

| 检查项 | 通过标准 | 宪法映射 |
|--------|---------|---------|
| 设计系统生成 | `--design-system` 输出包含 pattern + style + colors + typography | §5 UI/UX |
| 设计持久化 | `--persist` 产出 design-system/MASTER.md | §7 文件持久化 |
| Pre-delivery Checklist | 4 维度全部检查：Visual Quality · Interaction · Light/Dark · Accessibility | §5 UI/UX |
| 用户确认 | 用户明确确认设计方案 | §1 核心使命 |
| 宪法 UI 条款 | 满足 WCAG 2.1 AA · 响应式 · 对比度 ≥ 4.5:1 | §2.3 用户体验 |

**不通过时**：调整设计参数 → 重新生成 → 重新检查。

---

## G4 执行验证闸门

**触发位置**：阶段 4（执行）→ 阶段 5（归档）。这是最严格的闸门。

| 检查项 | 通过标准 | 来源 Skill |
|--------|---------|-----------|
| TDD 覆盖 | 每个新功能/修复有对应测试，且经历 RED→GREEN 循环 | test-driven-development |
| 全部测试通过 | 运行命令输出 0 failures，保留完整输出 | verification-before-completion |
| Spec 符合审查 | 代码实现与已确认规范一致（无遗漏/无超范围） | requesting-code-review (spec) |
| 代码质量审查 | 无 Critical/Important 未修复问题 | requesting-code-review (quality) |
| 验证证据归档 | verification 输出写入 progress.md，含 exit code + 时间戳 | planning-with-files |
| 宪法合规 | 代码质量/测试覆盖/性能/安全满足 constitution 基线 | constitution |

**两阶段审查流程**（来自 Superpowers subagent-driven-development）：
```
Step 1: Spec 符合审查 → 代码是否匹配已确认规范？
  ✅ 通过 → Step 2
  ❌ 不通过 → 修复 → 重新 Step 1

Step 2: 代码质量审查 → SOLID/安全/性能？
  ✅ 通过 → G4 通过
  ❌ 不通过 → 修复 → 重新 Step 2
```

**不通过时**：根据审查反馈修复 → 重跑测试 → 重新审查 → 循环直到通过。

---

## 错误升级协议（贯穿全部闸门）

```
尝试 1: 诊断 → 针对性修复 → 重新评估闸门
尝试 2: 换方法/工具 → 修复 → 重新评估
尝试 3: 质疑假设 → 搜索方案 → 考虑更新计划
3 次失败后: → systematic-debugging（4 阶段根因分析）→ 上报用户
```

此协议来自 planning-with-files 的 3-Strike Error Protocol 与 Superpowers systematic-debugging 的融合。
