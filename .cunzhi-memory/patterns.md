# 常用模式和最佳实践

- Cursor Skill 优化模式：遵循 skill-creator 的"精简至上 + 渐进式披露"原则。SKILL.md 控制在 ≤100 行，重型内容拆到 references/ 和 assets/ 子目录。冗余概念（TDD/SOLID/DRY 等 Claude 已内建的知识）不写入 Skill，委派给子 Skill。验证脚本覆盖：文件完整性 · Frontmatter · 内部链接 · 内容质量 · CLI 依赖 · Skill 依赖。
- v4→v5 升级关键经验：1) Superpowers v5.0.6 将 subagent review loops 替换为 inline self-review（~30s vs ~25min），这是架构级变更，必须第一时间适配。 2) MemPalace 集成设计为“可选增强”而非“强制依赖”，确保未配置时所有功能正常工作。 3) 全版本同步时，先写 findings.md 调研报告再动手，避免遗漏。 4) 验证脚本从 104→149 项，覆盖新特性至关重要。
