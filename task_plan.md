# Task Plan: Skill 全面重构

## 目标
按 skill-creator 最佳实践重构 spec-first-superpowers，消除冗余、实现 progressive disclosure、修复所有配套文件。

## 状态：✅ 完成

### Phase 1: 核心重写
- [x] 重写 SKILL.md（118行 → 82行，精简 30%，progressive disclosure）
- [x] 创建 references/spec-kit-workflow.md
- [x] 创建 references/openspec-workflow.md
- [x] 创建 references/integration-guide.md

### Phase 2: 资源重组
- [x] 移动宪法模板到 assets/constitutions/
- [x] 删除旧 项目宪法/ 目录

### Phase 3: 配套文件修复
- [x] 重写 .mdc 规则（50行 → 16行，仅守门员职责）
- [x] 修复 README.md（去代码块包裹，更新结构说明）
- [x] 修复 install-all.sh（移除不存在命令，添加引导提示）
- [x] 更新 使用说明.md（精简去重）

### Phase 4: 验证
- [x] 检查所有文件引用路径（SKILL.md → references/ → assets/ 全部正确）
- [x] 生成总结文档

## 决策记录
- SKILL.md 仅保留编排逻辑，详细工作流拆到 references/
- .mdc 仅做 always-on 守门员，不重复 SKILL.md 内容
- 宪法模板作为 assets（供用户复制使用），从 项目宪法/ 移至 assets/constitutions/
