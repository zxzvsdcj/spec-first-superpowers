#!/bin/bash
set -e

echo "=== Spec-First + Superpowers 依赖安装 ==="
echo ""

# 1. Spec-Kit CLI（新项目模式使用）
echo "[1/3] 安装 Spec-Kit CLI..."
if command -v uv >/dev/null 2>&1; then
  uv tool install specify-cli --from git+https://github.com/github/spec-kit.git || echo "  ⚠ Spec-Kit 安装失败，可稍后手动安装"
else
  echo "  安装 uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.cargo/bin:$PATH"
  uv tool install specify-cli --from git+https://github.com/github/spec-kit.git || echo "  ⚠ Spec-Kit 安装失败，可稍后手动安装"
fi

# 2. OpenSpec CLI（默认模式使用）
echo "[2/3] 安装 OpenSpec CLI..."
if command -v npm >/dev/null 2>&1; then
  npm install -g @fission-ai/openspec@latest || echo "  ⚠ OpenSpec 安装失败，请确认 Node.js 已安装"
else
  echo "  ⚠ npm 未找到，请先安装 Node.js: https://nodejs.org/"
fi

# 3. Cursor Skills（需在 Cursor 中手动安装）
echo "[3/3] Cursor Skills 安装提示..."
echo ""
echo "  以下 Skills 需在 Cursor 中通过 Skills 市场或 npx skills add 安装："
echo "  ─────────────────────────────────────"
echo "  必需："
echo "    • using-superpowers（含 brainstorming, writing-plans, TDD 等子 Skills）"
echo "    • planning-with-files"
echo "  推荐："
echo "    • ui-ux-pro-max"
echo "    • code-review-expert"
echo "    • systematic-debugging"
echo "  ─────────────────────────────────────"
echo ""

# 4. 放置提示
echo "=== 文件放置指南 ==="
echo ""
echo "  1. 将 SKILL.md + references/ + assets/ 复制到："
echo "     ~/.cursor/skills/spec-first-superpowers/"
echo ""
echo "  2. 将 .cursor/00-spec-first-superpowers.mdc 复制到项目："
echo "     <project>/.cursor/rules/00-spec-first-superpowers.mdc"
echo ""
echo "  3.（可选）将宪法模板复制到项目："
echo "     OpenSpec: assets/constitutions/openspec-constitution.md"
echo "     Spec-Kit: assets/constitutions/spec-kit-constitution.md"
echo ""
echo "=== 安装完成 ==="
echo "重启 Cursor，输入 /super-spec 测试。"
