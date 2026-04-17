# spec-first-superpowers v5 升级实施计划

> 状态：✅ 完成
> 创建时间：2026-04-17
> 方案：A（全面升级 v5 + MemPalace 集成）
> 调研报告：findings.md

## 目标

适配五大集成项目最新版本变更（重点：Superpowers v5.0.6 review loops 架构变更），
集成 MemPalace 作为第六大核心工具，全面升级至 v5。

## 阶段清单

### Phase 1：重写 quality-gates.md（🔴 最高优先级）
- [x] 1.1 G1 Spec Review Loop → Inline Self-Review Checklist
- [x] 1.2 G2 Plan Review Loop → Inline Self-Review Checklist
- [x] 1.3 Review Loops 专节 → 替换为 Inline Self-Review 说明
- [x] 1.4 G0 增加 MemPalace Session Recovery
- [x] 1.5 G3 更新 ui-ux-pro-max v2.5.0 数据
- [x] 1.6 更新所有版本引用

### Phase 2：重写 synergy-patterns.md
- [x] 2.1 Chain 1 审查循环 → Inline Self-Review
- [x] 2.2 Chain 3 ui-ux-pro-max v2.5.0 数据同步
- [x] 2.3 新增 Chain 6：MemPalace Memory Chain
- [x] 2.4 更新 Quick Reference 表

### Phase 3：更新 spec-kit-workflow.md
- [x] 3.1 安装方式 `--ai` → `--integration`
- [x] 3.2 新增 Workflow Engine + Catalog System 说明
- [x] 3.3 更新 Agent 支持列表

### Phase 4：更新 openspec-workflow.md
- [x] 4.1 Profile 术语修正 (expanded → custom)
- [x] 4.2 预适配 `/opsx:refine` 命令
- [x] 4.3 更新新 Agent 支持

### Phase 5：新增 mempalace-integration.md
- [x] 5.1 创建完整集成指南（5 个集成点）
- [x] 5.2 工具清单 + 配置说明

### Phase 6：更新 integration-guide.md
- [x] 6.1 新增 MemPalace 到依赖表
- [x] 6.2 新增 MemPalace 安装说明
- [x] 6.3 更新 Spec-Kit 安装命令
- [x] 6.4 更新 Session Recovery 增加 MemPalace
- [x] 6.5 更新所有版本引用
- [x] 6.6 更新 Related Projects 表

### Phase 7：更新 SKILL.md + constitutions
- [x] 7.1 SKILL.md v5 标题 + description 更新
- [x] 7.2 openspec-constitution.md v4.0 更新
- [x] 7.3 spec-kit-constitution.md v4.0 更新

### Phase 8：更新 README.md + 使用说明.md
- [x] 8.1 README.md v5 全面更新
- [x] 8.2 使用说明.md v5 全面更新

### Phase 9：验证
- [x] 9.1 增强 test_skill.py 至覆盖 v5 特性（149 项检查）
- [x] 9.2 运行验证：149/149 全部通过

### Phase 10：部署与交付
- [x] 10.1 部署到 ~/.cursor/skills/spec-first-superpowers/
- [x] 10.2 生成 SUMMARY.md
- [ ] 10.3 Git commit + push

## 错误记录

| 错误 | 尝试 | 解决 |
|------|------|------|
| planning-with-files 路径检测失败 | 1 | 该 skill 安装在 ~/.agents/skills/ 非 ~/.cursor/skills/，通过 SKILLS_ROOT 环境变量解决 |
