# Spec-First + Superpowers v5

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
- `ui-ux-pro-max` (recommended, v2.5.0)
- `finishing-a-development-branch`

Optional external tools:

- **MemPalace** (`pip install mempalace`) — cross-session memory + knowledge graph

Helper scripts for external CLI tools:

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
/super-spec → Mode Selection → Complexity Triage → Session Recovery (auto + MemPalace)
    → Specification (G1, with inline spec review)
    → Persistent Planning (G2, with inline plan review + file structure mapping)
    → UI/UX Design (G3, conditional, v2.5.0 intelligent design system)
    → TDD Implementation (G4, with model selection + implementer status)
    → Archive (+ MemPalace persistence)
```

## What's in v5

- **Inline self-review**: Replaced subagent review loops with fast inline checklists (~30s vs ~25min, comparable quality, from Superpowers v5.0.6)
- **MemPalace integration**: Cross-session memory with 96.6% R@5 retrieval, knowledge graph for decision tracking, agent diary for workflow audit
- **Spec-Kit Workflow Engine**: Custom workflow registration and discovery via Catalog system (v0.7.0+)
- **OpenSpec `/opsx:refine`**: Targeted artifact review and refinement (custom profile)
- **OpenSpec profile rename**: "expanded" → "custom" (v1.2.0)
- **ui-ux-pro-max v2.5.0**: +6 specialist skills (banner-design, slides, ui-styling, design-system, design, brand), Three.js stack, 1923 Google Fonts DB
- **Updated all version references**: Spec-Kit v0.7.1, OpenSpec v1.2.0, Superpowers v5.0.7, planning-with-files v2.30.0

### Carried from v4

- Complexity triage (quick/standard/thorough)
- Session recovery with 5-Question Reboot Test
- Quality gates G0-G4 with constitution verification
- Two-stage review (spec conformance + code quality)
- Subagent-driven execution with zero context pollution
- Error escalation: 3-Strike Protocol + systematic-debugging
- Design persistence: `--persist` for cross-session reuse
- File structure mapping before task decomposition
- Model selection for subagent execution (fast → standard → capable)
- Implementer status handling (DONE/DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED)
- Scope check for early decomposition detection
- 6 synergy chains (updated with MemPalace chain)

## Project Structure

```
spec-first-superpowers/
├── skills/
│   └── spec-first-superpowers/             # ← npx skills add installs only this
│       ├── SKILL.md                        # Core orchestration logic (v5)
│       ├── references/
│       │   ├── spec-kit-workflow.md
│       │   ├── openspec-workflow.md
│       │   ├── integration-guide.md
│       │   ├── quality-gates.md
│       │   ├── synergy-patterns.md
│       │   └── mempalace-integration.md    # NEW in v5
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

| Project | GitHub | Version | Role |
|---------|--------|---------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | v0.7.1 | GitHub's spec-driven framework (uv tool install) |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | v1.2.0 | Lightweight OPSX workflow (default, npm) |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | v5.0.7 | TDD + inline review + subagent methodology |
| planning-with-files | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | v2.30.0 | File-based persistent planning |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | v2.5.0 | UI/UX design system |
| MemPalace | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | v3.3.0 | Cross-session memory + knowledge graph (optional) |

---

Hades @Hades96444367 · Singapore · 2026
