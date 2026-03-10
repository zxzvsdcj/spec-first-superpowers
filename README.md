# Spec-First + Superpowers v3

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cursor Compatible](https://img.shields.io/badge/Cursor-Compatible-brightgreen)](https://cursor.sh)
[![Default: OpenSpec](https://img.shields.io/badge/Default-OpenSpec-blue)](https://github.com/Fission-AI/OpenSpec)

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
- `ui-ux-pro-max` (recommended)
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
    → Specification (G1) → Persistent Planning (G2)
    → UI/UX Design (G3, conditional) → TDD Implementation (G4) → Archive
```

## What's in v3

- **Complexity triage**: Auto-classifies quick/standard/thorough; simple bugfixes take a fast path
- **Session recovery**: Detects existing `task_plan.md` and resumes from breakpoint
- **Quality gates G0-G4**: Clear pass criteria at every phase, with constitution verification
- **Two-stage review**: Spec conformance + code quality
- **Subagent-driven execution**: Fresh subagent per task, zero context pollution
- **Error escalation**: 3-Strike Protocol + systematic-debugging integration
- **Design persistence**: ui-ux-pro-max `--persist` for cross-session reuse
- **5 synergy chains**: Constitution→Gates→Review / Error→Log→Debug / Design→Persist→Recover / Spec→Plan→Execute / Verify→Evidence→Archive

## Project Structure

```
spec-first-superpowers/
├── skills/
│   └── spec-first-superpowers/             # ← npx skills add installs only this
│       ├── SKILL.md                        # Core orchestration logic (v3)
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
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | GitHub's spec-driven framework |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Lightweight OPSX workflow (default) |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | TDD + review methodology |
| planning-with-files | [othmanadi/planning-with-files](https://github.com/othmanadi/planning-with-files) | File-based persistent planning |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX design system |

---

Hades @Hades96444367 · Singapore · 2026
