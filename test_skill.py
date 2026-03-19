"""spec-first-superpowers v4 Skill validation script"""
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

# 9. v4 features present
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

# 10. v4 NEW features
check("has review loop mention", "review loop" in content.lower())
check("has file structure mapping", "file structure" in content.lower() or "structure mapping" in content.lower())
check("has model selection", "model selection" in content.lower())
check("has implementer status", "implementer status" in content.lower() or "DONE_WITH_CONCERNS" in content or "NEEDS_CONTEXT" in content or "BLOCKED" in content)
check("has scope check", "scope check" in content.lower() or "scope" in content.lower())
check("has /opsx:propose reference", "/opsx:propose" in content or "opsx:propose" in content)
check("has v2.0 ui-ux-pro-max mention", "v2.0" in content or "67 styles" in content or "161 palettes" in content)
check("has v4 in title", "v4" in content.lower())

# 11. Quality gates file content
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
    check(
        "quality-gates.md has spec review loop",
        "spec review loop" in qg.lower() or "spec-document-reviewer" in qg.lower(),
    )
    check(
        "quality-gates.md has plan review loop",
        "plan review loop" in qg.lower() or "plan-document-reviewer" in qg.lower(),
    )
    check(
        "quality-gates.md has implementer status",
        "DONE_WITH_CONCERNS" in qg or "NEEDS_CONTEXT" in qg or "BLOCKED" in qg,
    )
    check(
        "quality-gates.md has /opsx:verify",
        "opsx:verify" in qg.lower() or "completeness" in qg.lower(),
    )

# 12. Synergy patterns file content
sp_path = os.path.join(ref_dir, "synergy-patterns.md")
if os.path.isfile(sp_path):
    with open(sp_path, "r", encoding="utf-8") as f:
        sp = f.read()
    for chain in ["Chain 1", "Chain 2", "Chain 3", "Chain 4", "Chain 5"]:
        check(f"synergy-patterns.md has {chain}", chain in sp, f"missing: {chain}")
    check(
        "synergy-patterns.md has review loops",
        "review loop" in sp.lower(),
    )
    check(
        "synergy-patterns.md has v2.0 mention",
        "v2.0" in sp or "67 styles" in sp or "161" in sp,
    )
    check(
        "synergy-patterns.md has model selection",
        "model selection" in sp.lower() or "fast" in sp.lower(),
    )

# 13. OpenSpec workflow v4 content
os_path = os.path.join(ref_dir, "openspec-workflow.md")
if os.path.isfile(os_path):
    with open(os_path, "r", encoding="utf-8") as f:
        os_content = f.read()
    check("openspec has /opsx:propose", "/opsx:propose" in os_content)
    check("openspec has /opsx:explore", "/opsx:explore" in os_content)
    check("openspec has /opsx:verify", "/opsx:verify" in os_content)
    check("openspec has profile system", "profile" in os_content.lower() or "core" in os_content.lower())
    check("openspec has openspec/ directory", "openspec/" in os_content)
    check("openspec has config.yaml", "config.yaml" in os_content)

# 14. Spec-Kit workflow v4 content
sk_path = os.path.join(ref_dir, "spec-kit-workflow.md")
if os.path.isfile(sk_path):
    with open(sk_path, "r", encoding="utf-8") as f:
        sk_content = f.read()
    check("speckit has /speckit.implement", "/speckit.implement" in sk_content)
    check("speckit has /speckit.analyze", "/speckit.analyze" in sk_content)
    check("speckit has /speckit.checklist", "/speckit.checklist" in sk_content)
    check("speckit has extensions", "extension" in sk_content.lower())
    check("speckit has presets", "preset" in sk_content.lower())
    check("speckit has uv tool install", "uv tool install" in sk_content)

# 15. Dependency skills installed
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
print("  spec-first-superpowers v4 Skill Validation Report")
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
