"""spec-first-superpowers v3 Skill validation script"""
import sys, os, re

SKILL_DIR = os.environ.get(
    "SKILL_DIR",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills", "spec-first-superpowers"),
)
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


# 1. File existence
skill_md = os.path.join(SKILL_DIR, "SKILL.md")
check("SKILL.md exists", os.path.isfile(skill_md))

with open(skill_md, "r", encoding="utf-8") as f:
    content = f.read()

# 2. YAML frontmatter
fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
check("YAML frontmatter present", fm_match is not None)

fm = fm_match.group(1) if fm_match else ""
check("name field present", "name:" in fm)
check("description field present", "description:" in fm)
check("name = spec-first-superpowers", "spec-first-superpowers" in fm)

for t in ["/super-spec", "spec first"]:
    check(f'trigger "{t}" in description', t in fm, f"missing: {t}")

for field in ["license", "version", "author", "compatibility"]:
    check(f'no forbidden field "{field}"', f"{field}:" not in fm)

# 3. references/ directory and files
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

# 4. assets/ directory and files
assets_dir = os.path.join(SKILL_DIR, "assets", "constitutions")
check("assets/constitutions/ dir exists", os.path.isdir(assets_dir))

for af in ["openspec-constitution.md", "spec-kit-constitution.md"]:
    check(
        f"assets/constitutions/{af} exists",
        os.path.isfile(os.path.join(assets_dir, af)),
    )

# 5. Internal links resolve
links = re.findall(r"\]\(((?:references|assets)/[^)]+)\)", content)
for link in links:
    check(
        f'link "{link}" resolves',
        os.path.isfile(os.path.join(SKILL_DIR, link)),
        f"not found: {link}",
    )

# 6. SKILL.md key content
check("has /super-spec command", "/super-spec" in content)
check("has mode selection", "mode" in content.lower() or "Mode" in content)
check("has orchestration flow", "phase" in content.lower() or "pipeline" in content.lower())

# 7. Line count ≤ 120
lines = content.split("\n")
check(f"SKILL.md ≤ 120 lines (actual: {len(lines)})", len(lines) <= 120)

# 8. No redundant concepts (these are built into Claude / sub-skills)
for pat in ["TDD-First", "RED-GREEN-REFACTOR", "Clean Code", "SOLID", "DRY", "KISS"]:
    check(
        f'no redundant "{pat}"', pat not in content, "should delegate to sub-skills"
    )

# 9. v3 features present
check("has complexity triage", "complex" in content.lower() or "triage" in content.lower())
check("has session recovery", "session" in content.lower() or "recover" in content.lower())
check("has quality gates", "gate" in content.lower() or "G0" in content or "G1" in content)
check("has quality-gates.md reference", "quality-gates.md" in content)
check("has synergy-patterns.md reference", "synergy-patterns.md" in content)
check("has 5-Question Reboot Test", "5-Question" in content or "Reboot" in content)
check("has Subagent-Driven option", "ubagent" in content)
check("has finishing-a-development-branch", "finishing" in content.lower() or "archive" in content.lower())
check(
    "has verification evidence to progress.md",
    "verification" in content.lower() and "progress.md" in content,
)
check("has systematic-debugging", "systematic" in content.lower() or "3-Strike" in content)
check("has two-stage review", "two-stage" in content.lower() or "spec conformance" in content.lower())

# 10. Quality gates file content
qg_path = os.path.join(ref_dir, "quality-gates.md")
if os.path.isfile(qg_path):
    with open(qg_path, "r", encoding="utf-8") as f:
        qg = f.read()
    for gate in ["G0", "G1", "G2", "G3", "G4"]:
        check(f"quality-gates.md has {gate}", gate in qg, f"missing gate: {gate}")
    check(
        "quality-gates.md has error escalation",
        "3-Strike" in qg or "3 fail" in qg.lower() or "escalat" in qg.lower(),
    )
    check(
        "quality-gates.md has constitution reference",
        "constitution" in qg.lower(),
    )

# 11. Synergy patterns file content
sp_path = os.path.join(ref_dir, "synergy-patterns.md")
if os.path.isfile(sp_path):
    with open(sp_path, "r", encoding="utf-8") as f:
        sp = f.read()
    for chain in ["Chain 1", "Chain 2", "Chain 3", "Chain 4", "Chain 5"]:
        check(f"synergy-patterns.md has {chain}", chain in sp, f"missing: {chain}")

# 12. Dependency skills installed
skills_root = os.environ.get(
    "SKILLS_ROOT",
    os.path.join(os.path.expanduser("~"), ".cursor", "skills"),
)
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

# Report
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
