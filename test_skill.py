"""spec-first-superpowers v3 Skill 完整性验证脚本"""
import sys, os, re

SKILL_DIR = r"C:\Users\Hades\.cursor\skills\spec-first-superpowers"
results = []
passed = 0
failed = 0


def check(name, condition, detail=""):
    global passed, failed
    if condition:
        results.append(f"  PASS: {name}")
        passed += 1
    else:
        results.append(f"  FAIL: {name} -- {detail}")
        failed += 1


# ── 1. 文件存在性 ────────────────────────────────────
skill_md = os.path.join(SKILL_DIR, "SKILL.md")
check("SKILL.md exists", os.path.isfile(skill_md))

with open(skill_md, "r", encoding="utf-8") as f:
    content = f.read()

# ── 2. YAML frontmatter ────────────────────────────────
fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
check("YAML frontmatter present", fm_match is not None)

fm = fm_match.group(1) if fm_match else ""
check("name field present", "name:" in fm)
check("description field present", "description:" in fm)
check("name = spec-first-superpowers", "spec-first-superpowers" in fm)

for t in ["/super-spec", "@super-spec", "use super-spec", "spec first"]:
    check(f'trigger "{t}" in description', t in fm, f"missing: {t}")

for field in ["license", "version", "author", "compatibility"]:
    check(f'no forbidden field "{field}"', f"{field}:" not in fm)

# ── 3. references/ 目录与文件 ─────────────────────────
ref_dir = os.path.join(SKILL_DIR, "references")
check("references/ dir exists", os.path.isdir(ref_dir))

for rf in [
    "spec-kit-workflow.md",
    "openspec-workflow.md",
    "integration-guide.md",
    "quality-gates.md",
    "synergy-patterns.md",
]:
    path = os.path.join(ref_dir, rf)
    exists = os.path.isfile(path)
    check(f"references/{rf} exists", exists)
    if exists:
        size = os.path.getsize(path)
        check(f"references/{rf} not empty ({size}B)", size > 100)

# ── 4. assets/ 目录与文件 ─────────────────────────────
assets_dir = os.path.join(SKILL_DIR, "assets", "constitutions")
check("assets/constitutions/ dir exists", os.path.isdir(assets_dir))

for af in ["openspec-constitution.md", "spec-kit-constitution.md"]:
    check(
        f"assets/constitutions/{af} exists",
        os.path.isfile(os.path.join(assets_dir, af)),
    )

# ── 5. 内部链接可解析 ─────────────────────────────────
links = re.findall(r"\]\(((?:references|assets)/[^)]+)\)", content)
for link in links:
    check(
        f'link "{link}" resolves',
        os.path.isfile(os.path.join(SKILL_DIR, link)),
        f"not found: {link}",
    )

# ── 6. SKILL.md 关键内容段 ────────────────────────────
check("has /super-spec command", "/super-spec" in content)
check(
    "has mode selection logic", "模式选择" in content or "mode" in content.lower()
)
check(
    "has orchestration flow", "编排" in content or "orchestrat" in content.lower()
)

# ── 7. 行数控制 ≤ 100 行 ──────────────────────────────
lines = content.split("\n")
check(f"SKILL.md ≤ 100 lines (actual: {len(lines)})", len(lines) <= 100)

# ── 8. 无冗余内容（Claude 已内建的概念不重复）────────
for pat in ["TDD-First", "RED-GREEN-REFACTOR", "Clean Code", "SOLID", "DRY", "KISS"]:
    check(
        f'no redundant "{pat}"', pat not in content, "should delegate to sub-skills"
    )

# ── 9. v3 新功能检查 ──────────────────────────────────
check("has complexity triage (复杂度分级)", "复杂度分级" in content)
check("has session recovery (会话恢复)", "会话恢复" in content or "上下文恢复" in content)
check(
    "has quality gates (质量闸门)",
    "闸门" in content or "quality gate" in content.lower(),
)
check(
    "has quality-gates.md reference",
    "quality-gates.md" in content,
)
check(
    "has synergy-patterns.md reference",
    "synergy-patterns.md" in content,
)
check(
    "has 5-Question Reboot Test",
    "5-Question" in content or "Reboot" in content,
)
check(
    "has Subagent-Driven option",
    "Subagent" in content or "subagent" in content,
)
check(
    "has finishing-a-development-branch",
    "finishing" in content,
)
check(
    "has verification evidence to progress.md",
    "verification" in content.lower() and "progress.md" in content,
)
check(
    "has systematic-debugging integration",
    "systematic-debugging" in content or "systematic" in content.lower(),
)
check(
    "has two-stage review (两阶段审查)",
    "两阶段" in content or "two-stage" in content.lower() or "spec 符合" in content,
)

# ── 10. 质量闸门文件内容检查 ──────────────────────────
qg_path = os.path.join(ref_dir, "quality-gates.md")
if os.path.isfile(qg_path):
    with open(qg_path, "r", encoding="utf-8") as f:
        qg = f.read()
    for gate in ["G0", "G1", "G2", "G3", "G4"]:
        check(f"quality-gates.md has {gate}", gate in qg, f"missing gate: {gate}")
    check(
        "quality-gates.md has error escalation",
        "3-Strike" in qg or "3 次" in qg or "升级" in qg,
    )
    check(
        "quality-gates.md has constitution reference",
        "宪法" in qg or "constitution" in qg.lower(),
    )

# ── 11. 协同模式文件内容检查 ──────────────────────────
sp_path = os.path.join(ref_dir, "synergy-patterns.md")
if os.path.isfile(sp_path):
    with open(sp_path, "r", encoding="utf-8") as f:
        sp = f.read()
    for chain in ["链 1", "链 2", "链 3", "链 4", "链 5"]:
        check(f"synergy-patterns.md has {chain}", chain in sp, f"missing: {chain}")

# ── 12. 依赖 Skill 已安装 ─────────────────────────────
skills_root = r"C:\Users\Hades\.cursor\skills"
for skill in [
    "using-superpowers",
    "planning-with-files",
    "ui-ux-pro-max",
    "brainstorming",
    "test-driven-development",
    "writing-plans",
    "verification-before-completion",
    "requesting-code-review",
    "systematic-debugging",
]:
    skill_path = os.path.join(skills_root, skill, "SKILL.md")
    check(
        f"dependency skill '{skill}' installed",
        os.path.isfile(skill_path),
        f"not found: {skill_path}",
    )

# ── 13. 依赖工具可用性 ───────────────────────────────
import shutil

for cmd, label in [("specify", "Spec-Kit CLI"), ("openspec", "OpenSpec CLI")]:
    check(
        f"{label} ({cmd}) on PATH",
        shutil.which(cmd) is not None,
        f"run: pip install specify-cli / npm i -g @fission-ai/openspec",
    )

# ── 报告 ─────────────────────────────────────────────
print("=" * 60)
print("  spec-first-superpowers v3 Skill Validation Report")
print("=" * 60)
for r in results:
    print(r)
print("-" * 60)
print(f"  Total: {passed + failed}  |  Passed: {passed}  |  Failed: {failed}")
if failed == 0:
    print("  >>> ALL TESTS PASSED <<<")
else:
    print(f"  >>> {failed} TEST(S) FAILED <<<")
print("=" * 60)
sys.exit(0 if failed == 0 else 1)
