# 极致优化 spec-first-superpowers v3 实施计划

> 状态：✅ 完成
> 创建时间：2026-03-02
> 方案：A（协同深度整合）

## 目标

补齐 12 个关键缺失 + 实现 5 条协同优化链，使 5 个开源项目的价值最大化。

## 阶段清单

### Phase 1：核心编排 (SKILL.md v3)
- [x] 1.1 重写 SKILL.md（85 行，含 6 条核心规则 + 复杂度分级 + 会话恢复 + 质量闸门）

### Phase 2：新增 references
- [x] 2.1 创建 references/quality-gates.md（G0-G4 详细标准 + 错误升级协议）
- [x] 2.2 创建 references/synergy-patterns.md（5 条协同链详解）

### Phase 3：增强现有 references
- [x] 3.1 增强 references/spec-kit-workflow.md（宪法主动校验 + G1 闸门清单）
- [x] 3.2 增强 references/openspec-workflow.md（ff 快速路径 + 宪法集成 + G1 清单）
- [x] 3.3 增强 references/integration-guide.md（会话恢复 + 复杂度分级 + 执行策略 + 错误链 + Subagent）

### Phase 4：增强 assets
- [x] 4.1 重写 assets/constitutions/openspec-constitution.md（v2.0 + 闸门检查点标记）
- [x] 4.2 重写 assets/constitutions/spec-kit-constitution.md（v2.0 + 闸门检查点标记）

### Phase 5：配套更新
- [x] 5.1 更新 test_skill.py（79 项检查，含 v3 新功能验证）
- [x] 5.2 更新 README.md（反映 v3 变更 + 新特性列表）
- [x] 5.3 更新 使用说明.md（反映 v3 变更）

### Phase 6：验证与交付
- [x] 6.1 运行 test_skill.py: 79/79 全部通过
- [x] 6.2 部署到 ~/.cursor/skills/spec-first-superpowers/
- [ ] 6.3 Git commit + push

## 错误记录

| 错误 | 尝试 | 解决 |
|------|------|------|
| link "assets/constitutions/" resolves | 1 | 改为具体文件链接（openspec + spec-kit） |
| no redundant "RED-GREEN-REFACTOR" | 1 | 替换为"TDD 循环执行" |
