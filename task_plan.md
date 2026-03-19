# spec-first-superpowers v4 升级实施计划

> 状态：✅ 完成
> 创建时间：2026-03-19
> 方案：A（全面升级 v4）

## 目标

适配五项核心工具的官方更新，解决 17 项差距，全面升级至 v4。

## 阶段清单

### Phase 1：重写 openspec-workflow.md
- [x] 1.1 OPSX 标准化工作流（propose/explore/verify）
- [x] 1.2 Profile 系统（core vs expanded）
- [x] 1.3 目录结构变更（openspec/ 替代 .openspec/）
- [x] 1.4 config.yaml 项目配置

### Phase 2：更新 spec-kit-workflow.md
- [x] 2.1 新增 /speckit.implement、/speckit.analyze、/speckit.checklist
- [x] 2.2 Extensions & Presets 系统
- [x] 2.3 安装方式变更（uv tool install）

### Phase 3：升级 quality-gates.md
- [x] 3.1 G1 整合 Spec Review Loop
- [x] 3.2 G2 整合 Plan Review Loop + 文件结构映射
- [x] 3.3 G4 整合 /opsx:verify 三维度验证
- [x] 3.4 Implementer Status Handling
- [x] 3.5 Review Loops 专节

### Phase 4：更新 synergy-patterns.md
- [x] 4.1 Chain 1 增加审查循环
- [x] 4.2 Chain 2 增加实现者状态
- [x] 4.3 Chain 3 更新至 v2.0
- [x] 4.4 Chain 4 增加范围检查 + 模型选择
- [x] 4.5 Chain 5 增加三维度验证

### Phase 5：更新 integration-guide.md
- [x] 5.1 安装方式全面更新
- [x] 5.2 新增 dispatching-parallel-agents skill
- [x] 5.3 模型选择指南
- [x] 5.4 实现者状态处理

### Phase 6：更新 SKILL.md + constitutions
- [x] 6.1 SKILL.md description + v4 标题 + 新特性
- [x] 6.2 openspec-constitution.md v3.0
- [x] 6.3 spec-kit-constitution.md v3.0

### Phase 7：配套更新
- [x] 7.1 README.md v4
- [x] 7.2 使用说明.md v4

### Phase 8：验证
- [x] 8.1 test_skill.py 增强至 104 项检查
- [x] 8.2 运行验证：104/104 全部通过

### Phase 9：部署与交付
- [x] 9.1 部署到 ~/.cursor/skills/spec-first-superpowers/
- [x] 9.2 生成 SUMMARY.md
- [ ] 9.3 Git commit + push

## 错误记录

| 错误 | 尝试 | 解决 |
|------|------|------|
| SKILL.md 缺少 implementer status 关键词 | 1 | 在 Subagent-Driven 描述中补充 |
