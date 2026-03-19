# Spec-First + Superpowers v4

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cursor Compatible](https://img.shields.io/badge/Cursor-Compatible-brightgreen)](https://cursor.sh)
[![Default: OpenSpec](https://img.shields.io/badge/Default-OpenSpec_OPSX-blue)](https://github.com/Fission-AI/OpenSpec)

A Cursor Agent Skill that enforces spec-before-code workflow. Prevents the AI from skipping design and jumping straight to implementation.

## Install

```bash
npx skills add zxzvsdcj/spec-first-superpowers
```

Non-interactive install (for scripts/CI):

```bash
npx skills add zxzvsdcj/spec-first-superpowers --skill spec-first-superpowers --agent cursor --global --yes
```

Verify installation:

```bash
npx skills ls -g -a cursor
```

> Install command follows the [vercel-labs/skills](https://github.com/vercel-labs/skills) convention.

## Dependency Skills

These should be installed via Cursor Skills marketplace or `npx skills add`:

- `using-superpowers` + sub-skills (brainstorming, writing-plans, TDD, code-review, etc.)
- `planning-with-files`
- `ui-ux-pro-max` (recommended, v2.0)
- `finishing-a-development-branch`

Optional helper scripts for external CLI tools:

```bash
# Linux / macOS
chmod +x install-all.sh && ./install-all.sh
```

```powershell
# Windows PowerShell
.\install-all.ps1
```

## Usage

In any Cursor chat:

```
/super-spec
```

| Command | Effect |
|---------|--------|
| `/super-spec` | Full workflow (auto mode + auto complexity) |
| `/super-spec force-spec-kit` | Force Spec-Kit mode |
| `/super-spec force-openspec` | Force OpenSpec mode |
| `/super-spec reset` | Reset mode selection |

## How It Works

```
/super-spec → Mode Selection → Complexity Triage → Session Recovery (auto)
    → Specification (G1, with spec review loop)
    → Persistent Planning (G2, with plan review loop + file structure mapping)
    → UI/UX Design (G3, conditional, v2.0 intelligent design system)
    → TDD Implementation (G4, with model selection + implementer status)
    → Archive
```

## What's in v4

- **Updated OpenSpec OPSX workflow**: `/opsx:propose` as default quick path, `/opsx:explore` for ideation, `/opsx:verify` for 3-dimension validation (Completeness × Correctness × Coherence), Profile system (core vs expanded)
- **Updated Spec-Kit commands**: `/speckit.implement` for execution, `/speckit.analyze` for cross-artifact consistency, `/speckit.checklist` for quality validation, Extensions & Presets system
- **Automated review loops**: Spec-document-reviewer + plan-document-reviewer subagents (max 3 iterations each) integrated into G1/G2
- **File structure mapping**: Required before task decomposition (G2 enhancement)
- **Model selection for subagents**: Cost-optimized per-task model selection (fast → standard → capable)
- **Implementer status handling**: DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED with clear escalation paths
- **ui-ux-pro-max v2.0**: 67 UI styles, 161 color palettes, 57 font pairings, 13 tech stacks, 161 reasoning rules, intelligent design system generator
- **Scope check**: Early detection of overscoped requirements for decomposition

### Carried from v3

- Complexity triage (quick/standard/thorough)
- Session recovery with 5-Question Reboot Test
- Quality gates G0-G4 with constitution verification
- Two-stage review (spec conformance + code quality)
- Subagent-driven execution with zero context pollution
- Error escalation: 3-Strike Protocol + systematic-debugging
- Design persistence: `--persist` for cross-session reuse
- 5 synergy chains (updated with new capabilities)

## Project Structure

```
spec-first-superpowers/
├── skills/
│   └── spec-first-superpowers/             # ← npx skills add installs only this
│       ├── SKILL.md                        # Core orchestration logic (v4)
│       ├── references/
│       │   ├── spec-kit-workflow.md
│       │   ├── openspec-workflow.md
│       │   ├── integration-guide.md
│       │   ├── quality-gates.md
│       │   └── synergy-patterns.md
│       └── assets/
│           └── constitutions/
│               ├── openspec-constitution.md
│               └── spec-kit-constitution.md
├── .cursor/
│   └── 00-spec-first-superpowers.mdc       # Always-on gatekeeper rule
├── test_skill.py                           # Validation script
├── install-all.sh / install-all.ps1        # Helper install scripts
└── README.md
```

> `npx skills add` discovers the `skills/` subdirectory and installs only its contents. Dev files in the repo root are not included.

## Integrated Projects

| Project | GitHub | Role |
|---------|--------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | GitHub's spec-driven framework (uv tool install) |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Lightweight OPSX workflow (default, npm) |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | TDD + review + subagent methodology |
| planning-with-files | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | File-based persistent planning |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX design system (v2.0) |

---

Hades @Hades96444367 · Singapore · 2026
