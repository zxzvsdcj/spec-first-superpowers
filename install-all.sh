#!/bin/bash
set -e

echo "🚀 开始安装 Spec-First + Superpowers 终极约束全套工具（默认偏向 OpenSpec）"

# 1. Spec-Kit (GitHub 官方)
echo "📦 安装 Spec-Kit..."
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify check || echo "⚠️ Spec-Kit 验证完成（若报错请手动执行 specify init）"

# 2. OpenSpec (默认推荐模式)
echo "📦 安装 OpenSpec..."
npm install -g @fission-ai/openspec@latest || echo "⚠️ npm 未找到，请手动安装 Node.js"

# 3. Superpowers (方法论核心)
echo "📦 安装 Superpowers..."
if command -v cursor >/dev/null || command -v claude >/dev/null; then
  /plugin marketplace add obra/superpowers-marketplace
  /plugin install superpowers@superpowers-marketplace
else
  echo "⚠️ 请在 Cursor/Claude Code 中手动执行 Superpowers 安装命令"
fi

# 4. planning-with-files
echo "📦 安装 planning-with-files..."
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files

# 5. ui-ux-pro-max-skill
echo "📦 安装 ui-ux-pro-max-skill..."
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max-skill@ui-ux-pro-max-skill

# 6. 创建自定义 meta-skill（spec-first-superpowers）
echo "📦 创建自定义 meta-skill..."
mkdir -p ~/.cursor/skills/spec-first-superpowers
cat > ~/.cursor/skills/spec-first-superpowers/SKILL.md << 'EOF'
---
name: spec-first-superpowers
description: Spec-First + Superpowers 终极约束引擎（默认偏向 OpenSpec）。支持 /super-spec 快捷激活。自动智能选择 Spec-Kit 或 OpenSpec（默认 OpenSpec），防止 AI 凭感觉乱写代码。集成 AI 编程三剑客 + planning-with-files + ui-ux-pro-max-skill。
---

# Spec-First + Superpowers Meta Director（终极完整版 · 默认偏向 OpenSpec）

## 铁律（绝对最高优先级，永不违反）
1. 任何新任务必须先完成 SDD 规范流程，绝不允许直接输出代码。
2. Spec 未用户明确确认前，绝不进入实现阶段。
3. Spec-Kit 和 OpenSpec 二选一、绝不混用（默认偏向 OpenSpec）。
4. SDD 完成后必须依次执行：planning-with-files → ui-ux-pro-max-skill（若涉及 UI/UX）→ using-superpowers → TDD 全流程。
5. 用户催促时必须坚定引导回 /super-spec。

## 快捷命令：/super-spec
- 输入 /super-spec 或 /super-spec start 或 @super-spec 立即激活完整流程。
- 支持参数：force-spec-kit / force-openspec / reset

## 智能模式自动选择逻辑（默认偏向 OpenSpec）
1. 项目根有 .specify/ → Spec-Kit
2. 项目根有 .openspec/ → OpenSpec
3. 无初始化文件夹时：
   - 出现明确“new project / 从零开始 / greenfield / init project”等强信号 + 文件总数 < 30 → Spec-Kit
   - 其他所有情况（默认）→ OpenSpec（存量/迭代优先）
4. 创建/读取项目根 .spec-mode 文件持久化。

## 强制执行流程（/super-spec 后）
1. SDD 规范阶段（默认 OpenSpec）
2. planning-with-files：生成 task_plan.md / findings.md / progress.md
3. ui-ux-pro-max-skill：自动检测 UI/UX 关键词并生成完整设计系统
4. Superpowers：using-superpowers → TDD + review + verification

## 每次启动响应模板（必须先输出）
“我已激活 Spec-First + Superpowers 终极版（默认偏向 OpenSpec）。
当前模式：**[Spec-Kit / OpenSpec]**（记录在 .spec-mode）。
完整流程即将启动：SDD → 持久规划 → UI/UX 设计 → Superpowers TDD。

请提供需求，我立即开始。”

（完整 Red Flags、流程细节与之前一致，此处为简洁版，实际使用时 AI 会展开全部铁律）
EOF

echo "✅ 自定义 meta-skill 已创建（默认偏向 OpenSpec）"

# 7. 创建 Cursor rules（Standalone Prompt）
echo "📦 创建 .cursor/rules 全局强制规则..."
mkdir -p .cursor/rules
cat > .cursor/rules/00-spec-first-superpowers.mdc << 'EOF'
---
description: "Spec-First + Superpowers 终极 Standalone Prompt（默认偏向 OpenSpec）"
globs: "*"
alwaysApply: true
---

（以下为完整 Standalone Prompt 内容，见下一节）
EOF

echo "🎉 安装完成！"
echo "请重启 Cursor，然后输入 /super-spec 测试。"
echo "默认模式已偏向 OpenSpec，适合大多数迭代项目。"