"""spec-first-superpowers v5 Skill validation script"""
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
    "mempalace-integration.md",
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

# 9. v5 features present
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

# 10. v5 NEW features (replacing v4 checks)
check("has inline self-review mention", "inline" in content.lower() and "review" in content.lower())
check("has file structure mapping", "file structure" in content.lower() or "structure mapping" in content.lower())
check("has model selection", "model selection" in content.lower())
check("has implementer status", "implementer status" in content.lower() or "DONE_WITH_CONCERNS" in content or "NEEDS_CONTEXT" in content or "BLOCKED" in content)
check("has scope check", "scope check" in content.lower() or "scope" in content.lower())
check("has /opsx:propose reference", "/opsx:propose" in content or "opsx:propose" in content)
check("has MemPalace mention", "mempalace" in content.lower() or "MemPalace" in content)
check("has mempalace-integration.md reference", "mempalace-integration.md" in content)
check("has v5 in title", "v5" in content.lower())
check("has 6 synergy chains", "6 chain" in content.lower() or "6 chains" in content.lower())
check("has knowledge graph mention", "knowledge graph" in content.lower())

# 11. Quality gates file content (v5)
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
        "quality-gates.md has inline self-review",
        "inline" in qg.lower() and "review" in qg.lower(),
    )
    check(
        "quality-gates.md no subagent reviewer reference",
        "spec-document-reviewer subagent" not in qg,
        "should use inline self-review, not subagent",
    )
    check(
        "quality-gates.md has inline spec review checklist",
        "spec inline review" in qg.lower() or "inline spec review" in qg.lower(),
    )
    check(
        "quality-gates.md has inline plan review checklist",
        "plan inline review" in qg.lower() or "inline plan review" in qg.lower(),
    )
    check(
        "quality-gates.md has implementer status",
        "DONE_WITH_CONCERNS" in qg or "NEEDS_CONTEXT" in qg or "BLOCKED" in qg,
    )
    check(
        "quality-gates.md has /opsx:verify",
        "opsx:verify" in qg.lower() or "completeness" in qg.lower(),
    )
    check(
        "quality-gates.md has MemPalace reference",
        "mempalace" in qg.lower() or "MemPalace" in qg,
    )
    check(
        "quality-gates.md has v2.5.0 reference",
        "v2.5.0" in qg,
    )

# 12. Synergy patterns file content (v5)
sp_path = os.path.join(ref_dir, "synergy-patterns.md")
if os.path.isfile(sp_path):
    with open(sp_path, "r", encoding="utf-8") as f:
        sp = f.read()
    for chain in ["Chain 1", "Chain 2", "Chain 3", "Chain 4", "Chain 5", "Chain 6"]:
        check(f"synergy-patterns.md has {chain}", chain in sp, f"missing: {chain}")
    check(
        "synergy-patterns.md has inline review (not subagent)",
        "inline" in sp.lower() and "review" in sp.lower(),
    )
    check(
        "synergy-patterns.md has v2.5.0 mention",
        "v2.5.0" in sp,
    )
    check(
        "synergy-patterns.md has model selection",
        "model selection" in sp.lower() or "fast" in sp.lower(),
    )
    check(
        "synergy-patterns.md has MemPalace chain",
        "mempalace" in sp.lower() or "MemPalace" in sp,
    )
    check(
        "synergy-patterns.md has knowledge graph",
        "knowledge graph" in sp.lower() or "mempalace_kg" in sp,
    )

# 13. OpenSpec workflow v5 content
os_path = os.path.join(ref_dir, "openspec-workflow.md")
if os.path.isfile(os_path):
    with open(os_path, "r", encoding="utf-8") as f:
        os_content = f.read()
    check("openspec has /opsx:propose", "/opsx:propose" in os_content)
    check("openspec has /opsx:explore", "/opsx:explore" in os_content)
    check("openspec has /opsx:verify", "/opsx:verify" in os_content)
    check("openspec has /opsx:refine", "/opsx:refine" in os_content)
    check("openspec has profile system", "profile" in os_content.lower() or "core" in os_content.lower())
    check("openspec has 'custom' profile", "custom" in os_content.lower())
    check("openspec has openspec/ directory", "openspec/" in os_content)
    check("openspec has config.yaml", "config.yaml" in os_content)
    check("openspec has inline review reference", "inline" in os_content.lower())

# 14. Spec-Kit workflow v5 content
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
    check("speckit has --integration flag", "--integration" in sk_content)
    check("speckit has --ai deprecated note", "deprecated" in sk_content.lower() or "--ai" in sk_content)
    check("speckit has Workflow Engine", "workflow engine" in sk_content.lower() or "catalog" in sk_content.lower())

# 15. MemPalace integration file content
mp_path = os.path.join(ref_dir, "mempalace-integration.md")
if os.path.isfile(mp_path):
    with open(mp_path, "r", encoding="utf-8") as f:
        mp_content = f.read()
    check("mempalace has installation guide", "pip install mempalace" in mp_content)
    check("mempalace has MCP configuration", "mcp" in mp_content.lower())
    check("mempalace has 5 integration points", "integration point" in mp_content.lower() or "five integration" in mp_content.lower())
    check("mempalace has knowledge graph", "knowledge graph" in mp_content.lower())
    check("mempalace has agent diary", "agent diary" in mp_content.lower() or "diary" in mp_content.lower())
    check("mempalace has session recovery", "session recovery" in mp_content.lower())
    check("mempalace has cross-project", "cross-project" in mp_content.lower())
    check("mempalace has tool reference", "mempalace_search" in mp_content or "mempalace_status" in mp_content)

# 16. Constitution files v4.0 content
for const_name, const_file in [
    ("openspec", "openspec-constitution.md"),
    ("spec-kit", "spec-kit-constitution.md"),
]:
    const_path = os.path.join(assets_dir, const_file)
    if os.path.isfile(const_path):
        with open(const_path, "r", encoding="utf-8") as f:
            const_content = f.read()
        check(f"{const_name} constitution has v4.0", "4.0" in const_content)
        check(f"{const_name} constitution has inline review", "inline" in const_content.lower())
        check(f"{const_name} constitution has v2.5.0", "v2.5.0" in const_content)
        check(f"{const_name} constitution has MemPalace", "mempalace" in const_content.lower() or "MemPalace" in const_content)
        check(
            f"{const_name} constitution no subagent reviewer",
            "spec-document-reviewer subagent" not in const_content,
            "should reference inline review, not subagent",
        )

# 17. Integration guide v5 content
ig_path = os.path.join(ref_dir, "integration-guide.md")
if os.path.isfile(ig_path):
    with open(ig_path, "r", encoding="utf-8") as f:
        ig_content = f.read()
    check("integration-guide has MemPalace", "mempalace" in ig_content.lower() or "MemPalace" in ig_content)
    check("integration-guide has v0.7.1", "v0.7.1" in ig_content or "0.7.1" in ig_content)
    check("integration-guide has v5.0.7", "v5.0.7" in ig_content or "5.0.7" in ig_content)
    check("integration-guide has v2.5.0", "v2.5.0" in ig_content or "2.5.0" in ig_content)
    check("integration-guide has v2.30.0", "v2.30.0" in ig_content or "2.30.0" in ig_content)
    check("integration-guide has v3.3.0", "v3.3.0" in ig_content or "3.3.0" in ig_content)
    check("integration-guide has --integration flag", "--integration" in ig_content)
    check("integration-guide has inline review", "inline" in ig_content.lower())

# 18. Dependency skills installed
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
print("  spec-first-superpowers v5 Skill Validation Report")
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
