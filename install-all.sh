#!/bin/bash
set -e

echo "=== Spec-First + Superpowers 快速安装 ==="
echo ""

# 1. Spec-Kit CLI（新项目模式使用）
echo "[1/4] 安装 Spec-Kit CLI..."
if command -v uv >/dev/null 2>&1; then
  uv tool install specify-cli --from git+https://github.com/github/spec-kit.git || echo "  ⚠ Spec-Kit 安装失败，可稍后手动安装"
else
  echo "  安装 uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.cargo/bin:$PATH"
  uv tool install specify-cli --from git+https://github.com/github/spec-kit.git || echo "  ⚠ Spec-Kit 安装失败，可稍后手动安装"
fi

# 2. OpenSpec CLI（默认模式使用）
echo "[2/4] 安装 OpenSpec CLI..."
if command -v npm >/dev/null 2>&1; then
  npm install -g @fission-ai/openspec@latest || echo "  ⚠ OpenSpec 安装失败，请确认 Node.js 已安装"
else
  echo "  ⚠ npm 未找到，请先安装 Node.js: https://nodejs.org/"
fi

# 3. 安装本 Skill（GitHub 一键安装）
echo "[3/4] 安装 spec-first-superpowers Skill..."
if command -v npx >/dev/null 2>&1; then
  npx skills add zxzvsdcj/spec-first-superpowers --skill spec-first-superpowers --agent cursor --global --yes || echo "  ⚠ Skill 自动安装失败，可手动运行：npx skills add zxzvsdcj/spec-first-superpowers"
else
  echo "  ⚠ npx 未找到，请先安装 Node.js: https://nodejs.org/"
fi

# 4. 依赖 Skills 提示
echo "[4/4] 依赖 Skills 检查提示..."
echo ""
echo "  在 Cursor 中请确保以下 Skills 可用："
echo "  ─────────────────────────────────────"
echo "  必需："
echo "    • using-superpowers（含 brainstorming, writing-plans, TDD 等子 Skills）"
echo "    • planning-with-files"
echo "  推荐："
echo "    • ui-ux-pro-max"
echo "    • requesting-code-review"
echo "    • systematic-debugging"
echo "  ─────────────────────────────────────"
echo ""
echo "  可选规则文件："
echo "    <project>/.cursor/rules/00-spec-first-superpowers.mdc"
echo "  （从本仓库 .cursor/00-spec-first-superpowers.mdc 复制）"
echo ""
echo "=== 安装完成 ==="
echo "重启 Cursor，输入 /super-spec 测试。"
