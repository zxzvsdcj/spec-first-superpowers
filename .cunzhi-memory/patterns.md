# 常用模式和最佳实践

- Cursor Skill 优化模式：遵循 skill-creator 的"精简至上 + 渐进式披露"原则。SKILL.md 控制在 ≤100 行，重型内容拆到 references/ 和 assets/ 子目录。冗余概念（TDD/SOLID/DRY 等 Claude 已内建的知识）不写入 Skill，委派给子 Skill。验证脚本覆盖：文件完整性 · Frontmatter · 内部链接 · 内容质量 · CLI 依赖 · Skill 依赖。
