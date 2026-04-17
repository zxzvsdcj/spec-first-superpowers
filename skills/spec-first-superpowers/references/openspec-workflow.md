# OpenSpec (OPSX) Workflow

OpenSpec is a lightweight, fluid spec-driven workflow for iterative development. This is the **default recommended mode**.

The OPSX workflow follows the philosophy: **"Actions, not phases"** — you can create, implement, update, and archive at any time, without rigid phase gates.

## When to Use

- Existing codebases with established patterns
- Fast iteration, small teams
- Feature enhancements, bugfixes, refactors

## Profile System

OpenSpec offers two workflow profiles. Configure with `openspec config profile`, apply with `openspec update`.

| Profile | Commands | Best for |
|---------|----------|----------|
| **core** (default) | `propose`, `explore`, `apply`, `archive` | Quick, streamlined workflow |
| **custom** | Above + `new`, `continue`, `ff`, `refine`, `verify`, `sync`, `bulk-archive`, `onboard` | Full control, large changes |

> Note: The "expanded" profile was renamed to "custom" in v1.2.0. Both terms may appear in older documentation.

## Command Flow

### Core Profile (Default Quick Path)

#### 1. Explore: `/opsx:explore [topic]`

Think through ideas, investigate problems, compare options. No artifacts created — just a thinking partner. When insights crystallize, transition to `/opsx:propose`.

#### 2. Propose: `/opsx:propose [change-name]`

**The default start command.** Creates a change and generates all planning artifacts in one step:
- Creates `openspec/changes/<change-name>/`
- Generates: `proposal.md` → `specs/` → `design.md` → `tasks.md`
- Stops when ready for `/opsx:apply`

#### 3. Apply: `/opsx:apply [change-name]`

Implement tasks from the change. Works through the task list, writing code and checking off items. Can resume where you left off if interrupted.

#### 4. Archive: `/opsx:archive [change-name]`

Move completed change to `openspec/changes/archive/YYYY-MM-DD-<name>/`. Offers to sync delta specs if needed. Preserves all artifacts for audit trail.

### Custom Profile (Additional Commands)

| Command | Purpose |
|---------|---------|
| `/opsx:new [name]` | Start a new change scaffold only |
| `/opsx:continue [name]` | Create next artifact one at a time |
| `/opsx:ff [name]` | Fast-forward: create all planning artifacts at once |
| `/opsx:refine [name]` | Review and refine existing artifacts with targeted feedback |
| `/opsx:verify [name]` | Validate implementation matches artifacts (3 dimensions) |
| `/opsx:sync [name]` | Merge delta specs into main specs |
| `/opsx:bulk-archive` | Archive multiple completed changes |
| `/opsx:onboard` | Guided tutorial through complete workflow |

### `/opsx:refine` — Artifact Review (new)

Enables targeted review and refinement of existing spec artifacts:
- Accepts feedback on specific sections or dimensions
- Supports sub-agent spec discovery for proposals
- Useful when specs need iteration after initial `/opsx:propose`

### `/opsx:verify` — Three-Dimension Validation

When available (custom profile), this command validates implementation quality:

| Dimension | What it validates |
|-----------|-------------------|
| **Completeness** | All tasks done, all requirements implemented, scenarios covered |
| **Correctness** | Implementation matches spec intent, edge cases handled |
| **Coherence** | Design decisions reflected in code, patterns consistent |

Reports issues as CRITICAL / WARNING / SUGGESTION.

## Gate G1 Checklist

Regardless of command path, pass this before moving to implementation:

- [ ] User gave explicit confirmation
- [ ] `spec.md`/`proposal.md` contains no implementation details
- [ ] `design.md` decisions don't violate constitution
- [ ] Each acceptance criterion maps to test cases
- [ ] `tasks.md` synced with `task_plan.md`
- [ ] Inline spec review passed (brainstorming skill)

## Constitution Integration

Reference the constitution via `config.yaml`:

```yaml
# openspec/config.yaml
schema: spec-driven
context: |
  Tech stack: [your stack]
  Testing: [your test framework]
rules:
  proposal:
    - Include rollback plan
  specs:
    - Use Given/When/Then format for scenarios
  design:
    - Include sequence diagrams for complex flows
```

| Config Field | Type | Description |
|-------------|------|-------------|
| `schema` | string | Default schema for new changes (e.g., `spec-driven`) |
| `context` | string | Project context injected into all artifact instructions |
| `rules` | object | Per-artifact rules (keyed by artifact ID: `proposal`, `specs`, `design`, `tasks`) |

Gate checks read this file and verify alignment clause by clause.

## File Structure

```
openspec/
├── config.yaml               # Project config (schema, context, rules)
├── changes/
│   ├── [change-name]/
│   │   ├── .openspec.yaml    # Change metadata
│   │   ├── proposal.md       # Change proposal
│   │   ├── specs/            # Feature specs
│   │   │   └── [domain]/spec.md
│   │   ├── design.md         # Technical design
│   │   └── tasks.md          # Task list (synced with task_plan.md)
│   └── archive/              # Completed changes
│       └── YYYY-MM-DD-[name]/
└── specs/                    # Main specs (synced from changes via /opsx:sync)
```

## Installation

```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init
```

To enable custom workflow: `openspec config profile` → select workflows → `openspec update`.

Supports: Cursor, Claude Code, Gemini CLI, Codex, Windsurf, Kiro, Pi, and [more](https://github.com/Fission-AI/OpenSpec#supported-tools).

## OpenSpec vs. Spec-Kit

| Dimension | OpenSpec | Spec-Kit |
|-----------|---------|----------|
| Weight | Lightweight, fluid | Strict, phased |
| Best for | Existing/iterating | New/complex systems |
| Philosophy | Actions, not phases | Phase-gated progression |
| Constitution | Optional (config.yaml) | Required (constitution.md) |
| Artifacts | proposal → specs → design → tasks | spec → plan → tasks |
| Quick path | `/opsx:propose` one-shot | `/speckit.implement` after full flow |
| Verification | `/opsx:verify` + `/opsx:refine` (custom) | `/speckit.analyze` + `/speckit.checklist` |
| Archiving | `/opsx:archive` / `/opsx:bulk-archive` | Manual |
| Customization | Schema-driven, per-artifact rules | Extensions, Presets & Workflow Engine |
