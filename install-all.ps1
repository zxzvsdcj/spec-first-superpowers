Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

Write-Host "=== Spec-First + Superpowers 快速安装（PowerShell） ==="
Write-Host ""

# 1. Spec-Kit CLI（新项目模式使用）
Write-Host "[1/4] 安装 Spec-Kit CLI..."
if (Get-Command uv -ErrorAction SilentlyContinue) {
    uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  [WARN] Spec-Kit 安装失败，可稍后手动安装"
    }
}
else {
    Write-Host "  [WARN] 未检测到 uv，请先安装后重试："
    Write-Host "        powershell -ExecutionPolicy ByPass -c `"irm https://astral.sh/uv/install.ps1 | iex`""
}

# 2. OpenSpec CLI（默认模式使用）
Write-Host "[2/4] 安装 OpenSpec CLI..."
if (Get-Command npm -ErrorAction SilentlyContinue) {
    npm install -g @fission-ai/openspec@latest
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  [WARN] OpenSpec 安装失败，请确认 Node.js 已安装"
    }
}
else {
    Write-Host "  [WARN] 未检测到 npm，请先安装 Node.js: https://nodejs.org/"
}

# 3. 安装本 Skill（GitHub 一键安装）
Write-Host "[3/4] 安装 spec-first-superpowers Skill..."
if (Get-Command npx -ErrorAction SilentlyContinue) {
    npx skills add zxzvsdcj/spec-first-superpowers --skill spec-first-superpowers --agent cursor --global --yes
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  [WARN] Skill 自动安装失败，可手动运行：npx skills add zxzvsdcj/spec-first-superpowers"
    }
}
else {
    Write-Host "  [WARN] 未检测到 npx，请先安装 Node.js: https://nodejs.org/"
}

# 4. 依赖 Skills 提示
Write-Host "[4/4] 依赖 Skills 检查提示..."
Write-Host ""
Write-Host "  在 Cursor 中请确保以下 Skills 可用："
Write-Host "  ─────────────────────────────────────"
Write-Host "  必需："
Write-Host "    • using-superpowers（含 brainstorming, writing-plans, TDD 等子 Skills）"
Write-Host "    • planning-with-files"
Write-Host "  推荐："
Write-Host "    • ui-ux-pro-max"
Write-Host "    • requesting-code-review"
Write-Host "    • systematic-debugging"
Write-Host "  ─────────────────────────────────────"
Write-Host ""
Write-Host "  可选规则文件："
Write-Host "    <project>/.cursor/rules/00-spec-first-superpowers.mdc"
Write-Host "  （从本仓库 .cursor/00-spec-first-superpowers.mdc 复制）"
Write-Host ""

Write-Host "=== 安装完成 ==="
Write-Host "重启 Cursor，输入 /super-spec 测试。"
