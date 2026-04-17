# Upgrade Protocol

Standardized procedure for upgrading spec-first-superpowers when integrated projects release new versions. Triggered by `/super-spec upgrade`.

---

## Trigger

The user says `/super-spec upgrade`, "升级检查", "upgrade check", or requests a version sync of the integrated projects.

## Integrated Projects Registry

| # | Project | GitHub | Current Version | Package Manager |
|---|---------|--------|----------------|-----------------|
| 1 | Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | v0.7.1 | uv (Python) |
| 2 | OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | v1.2.0 | npm |
| 3 | Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | v5.0.7 | Plugin marketplace |
| 4 | planning-with-files | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | v2.30.0 | npx skills |
| 5 | ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | v2.5.0 | npx skills |
| 6 | MemPalace | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | v3.3.0 | pip (Python) |

## Execution Pipeline

### Phase 1: Reconnaissance (parallel)

For each project in the registry, **concurrently** gather:

1. **Latest release version** — via web search: `github.com/<org>/<repo> latest release <current-year>`
2. **Changelog / release notes** — key changes since current version
3. **Breaking changes** — API changes, renamed commands, deprecated features, architectural shifts
4. **New capabilities** — features this skill should integrate

Output: structured comparison table per project (current version → latest version → delta).

### Phase 2: Impact Analysis

For each project with version changes:

1. **Classify changes** by severity:
   - 🔴 **Breaking** — APIs removed/renamed, architecture changed, core assumptions invalidated
   - 🟡 **Important** — new features worth integrating, significant improvements
   - 🟢 **Minor** — bug fixes, new agent support, documentation improvements
2. **Map impact to skill files** — which reference files, constitutions, SKILL.md sections are affected
3. **Check for cross-project conflicts** — e.g., Superpowers changing review semantics affects quality-gates

Output: `findings.md` with full research report.

### Phase 3: Decision Gate

Present to user (via 寸止 or equivalent):
- Summary of all changes found
- Severity classification
- Recommended scope (full upgrade / partial / skip)
- Estimated files affected

**User must confirm** before proceeding to implementation.

### Phase 4: Implementation

Follow the numbered checklist pattern:

1. Update affected reference files (one file at a time, most critical first):
   - `quality-gates.md` — gate criteria changes
   - `synergy-patterns.md` — chain updates
   - `spec-kit-workflow.md` — Spec-Kit changes
   - `openspec-workflow.md` — OpenSpec changes
   - `mempalace-integration.md` — MemPalace changes
   - `integration-guide.md` — version sync + new features
2. Update `SKILL.md` — version numbers in description, new capabilities
3. Update constitutions — version references, new clauses
4. Update project docs — `README.md`, `使用说明.md`
5. Update version registry — this file's "Current Version" column
6. Update test script — add checks for new features

### Phase 5: Verification

1. Run `test_skill.py` — all tests must pass
2. Deploy to `~/.cursor/skills/spec-first-superpowers/`
3. Generate `SUMMARY.md` with change delta

### Phase 6: Commit & Archive

1. Git commit with message: `feat: upgrade to v<N> — <summary of key changes>`
2. Push to remote (if user requests)
3. Knowledge sedimentation (mem0 + 寸止)

## Quality Rules

- **No-skip rule**: Even if only one project changed, run the full reconnaissance on all 6 to catch cross-dependencies
- **Breaking-change-first rule**: Address 🔴 breaking changes before 🟡 important changes
- **Test-before-deploy rule**: `test_skill.py` must pass before deployment
- **Evidence-before-claim rule**: Show verification output, never say "should work"
- **Version-pin rule**: Always update the registry table in this file after successful upgrade

## History

| Date | From | To | Key Changes | Test Results |
|------|------|-----|-------------|-------------|
| 2026-03-19 | v3 | v4 | 5 tools updated, 17 gaps fixed | 104/104 |
| 2026-04-17 | v4 | v5 | Inline review, MemPalace, 6 tools updated, 11 gaps fixed | 149/149 |
