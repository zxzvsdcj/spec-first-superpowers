# 跨项目协同模式

5 个开源项目并非独立工具，而是通过以下协同链形成闭环系统。

## 目录

- [链 1：宪法 → 闸门 → 审查](#链-1宪法--闸门--审查)
- [链 2：错误 → 日志 → 调试](#链-2错误--日志--调试)
- [链 3：设计 → 持久化 → 恢复](#链-3设计--持久化--恢复)
- [链 4：规范 → 计划 → 执行](#链-4规范--计划--执行)
- [链 5：验证 → 证据 → 归档](#链-5验证--证据--归档)

---

## 链 1：宪法 → 闸门 → 审查

**涉及项目**：Spec-Kit/OpenSpec × Superpowers

宪法(constitution)不是静态文档，而是**主动校验的检查清单**。

```
宪法定义约束 → G1 校验 spec 是否违反 → G4 审查校验代码是否违反
```

**实施方式**：
- 阶段 1 闸门：逐条检查 spec 与 constitution 对齐
  - Spec-Kit: plan.md 必须引用 constitution 检查点
  - OpenSpec: config.yaml 的 `context.constitution` 指向宪法文件
- 阶段 4 审查：code-review 时将 constitution 条款作为审查维度
  - 代码质量条款 → 审查 SOLID/命名/文档
  - 测试规范条款 → 审查覆盖率/TDD 循环
  - 性能基线条款 → 审查性能指标

---

## 链 2：错误 → 日志 → 调试

**涉及项目**：planning-with-files × Superpowers (systematic-debugging)

错误不静默吞掉，而是形成**可追溯的调试链**。

```
错误发生 → progress.md 记录(Error/Attempt/Resolution) → 3-Strike Protocol → systematic-debugging
```

**实施方式**：
- 每次错误立即写入 progress.md，格式：

```markdown
## 错误记录
| 错误 | 尝试 # | 操作 | 结果 |
|------|--------|------|------|
| ImportError: no module X | 1 | pip install X | 已解决 |
| TypeError: undefined | 1 | 检查参数类型 | 未解决 |
| TypeError: undefined | 2 | 添加空值检查 | 已解决 |
```

- 同一错误第 3 次未解决 → 自动切换到 `systematic-debugging` Skill
  - Phase 1: 根因调查（读错误/复现/检查变更/追踪数据流）
  - Phase 2: 模式分析（找到工作示例/对比差异）
  - Phase 3: 假设验证（最小改动/单一变量）
  - Phase 4: 实现修复（先写测试 → 修复 → 验证）
- 3 次修复同一问题失败 → 质疑架构 → 上报用户

---

## 链 3：设计 → 持久化 → 恢复

**涉及项目**：ui-ux-pro-max × planning-with-files

设计系统不是一次性产出，而是**跨会话持久化**的设计决策。

```
--design-system 生成 → --persist 写入 design-system/MASTER.md → 下次会话自动加载
```

**实施方式**：
- 阶段 3 生成设计系统时，始终使用 `--persist` 标志
- 产出 `design-system/MASTER.md`（全局设计规则）
- 特定页面有差异时，产出 `design-system/pages/<page-name>.md`（覆盖规则）
- 构建页面时的加载顺序：
  1. 检查 `design-system/pages/<page>.md` 是否存在
  2. 存在 → 页面规则优先于 MASTER
  3. 不存在 → 使用 MASTER 规则
- 阶段 0（上下文恢复）时，检测 `design-system/` 目录 → 自动加载设计上下文

---

## 链 4：规范 → 计划 → 执行

**涉及项目**：Spec-Kit/OpenSpec × planning-with-files × Superpowers (writing-plans)

规范工件**直接转化**为可执行的编号检查清单。

```
spec 验收标准 → task_plan.md 编号任务 → writing-plans bite-sized steps → TDD 执行
```

**实施方式**：
- 规范中的每个验收标准（Given-When-Then）映射为 task_plan.md 中的一个任务组
- 每个任务组按 `writing-plans` 格式拆分为 bite-sized steps：
  1. 写失败测试
  2. 运行确认失败
  3. 写最小实现
  4. 运行确认通过
  5. 提交
- Spec-Kit 的 tasks.md 与 task_plan.md 保持同步（Spec-Kit 管原子任务，task_plan.md 管进度状态）
- OpenSpec 的 tasks.md 同理
- 执行选择：
  - **Subagent-Driven**：每个 bite-sized step 由 fresh subagent 执行，两阶段审查
  - **Executing-Plans**：批次 3 个任务 + 检查点审查

---

## 链 5：验证 → 证据 → 归档

**涉及项目**：Superpowers (verification-before-completion) × planning-with-files

完成声明必须有**文件记录的验证证据**。

```
运行验证命令 → 读取完整输出 → 写入 progress.md(含 exit code + 时间戳) → 归档
```

**实施方式**：
- 闸门 G4 的验证步骤：
  1. IDENTIFY: 确定验证命令（pytest/npm test/build 等）
  2. RUN: 执行完整命令
  3. READ: 检查 exit code 和 failures 计数
  4. WRITE: 将输出写入 progress.md：
  ```markdown
  ## 验证证据
  - 时间：2026-03-02 14:30
  - 命令：`pytest tests/ -v`
  - 结果：34/34 passed, 0 failed
  - Exit code: 0
  ```
  5. CLAIM: 基于证据声明结果
- 归档阶段将 progress.md 中的证据作为完成记录的一部分
- `finishing-a-development-branch` 的选项（merge/PR/cleanup）也记录到 progress.md

---

## 协同矩阵速查

| 当你在... | 需要联动... | 通过... |
|----------|-----------|--------|
| 写 spec | 宪法条款 | 链 1: 宪法对齐检查 |
| 遇到错误 | 日志 + 调试 | 链 2: progress.md + 3-Strike |
| 做 UI 设计 | 设计持久化 | 链 3: --persist + MASTER.md |
| 拆分任务 | 验收标准 | 链 4: spec → plan → steps |
| 声明完成 | 验证证据 | 链 5: 运行 → 记录 → 归档 |
