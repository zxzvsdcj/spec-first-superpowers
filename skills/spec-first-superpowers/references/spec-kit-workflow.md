# Spec-Kit Workflow

Spec-Kit is GitHub's spec-driven development framework. Best for brand-new projects or complex systems that need strict phase gating.

## When to Use

- Building from scratch (greenfield)
- Large systems (multi-module, multi-team)
- Enterprise projects requiring strict phase control
- Projects needing extensions, presets, or custom workflows

## Installation

```bash
# Persistent installation (recommended)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Initialize in existing project
specify init . --integration cursor
# or
specify init --here --integration cursor

# Upgrade
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git

# Check installed tools
specify check
```

Also supports: `--integration claude`, `--integration copilot`, `--integration gemini`, `--integration windsurf`, `--integration codex`, `--integration kiro-cli`, `--integration goose`, and [20+ more agents](https://github.com/github/spec-kit#-supported-ai-agents).

> Note: The `--ai` flag is deprecated as of v0.7.1. Use `--integration` instead.

## Command Flow

### 1. Constitution: `/speckit.constitution`

Define non-negotiable principles in `.specify/memory/constitution.md`.
Template: [assets/constitutions/spec-kit-constitution.md](../assets/constitutions/spec-kit-constitution.md)

The constitution is actively verified at every gate — not just referenced passively.

### 2. Specification: `/speckit.specify`

Generate `.specify/specs/[feature-name]/spec.md`:
- Pure product perspective (What & Why) — no implementation details
- Includes: feature description, user stories, acceptance criteria (Given-When-Then), success metrics
- Each acceptance criterion must map to at least one test case
- Must reference relevant constitution constraints

### 3. Clarify: `/speckit.clarify`

- Review ambiguities in `spec.md` one by one
- Confirm with user in rounds (one question at a time)
- Ensure all acceptance criteria are measurable and unambiguous
- Skippable at Quick complexity level

### 4. Plan: `/speckit.plan`

Generate `.specify/specs/[feature-name]/plan.md`:
- Engineering perspective (How) — architecture decisions, tech choices
- Must reference constitution checkpoints for each decision
- Includes risk assessment and rollback strategies

### 5. Tasks: `/speckit.tasks`

Generate `.specify/specs/[feature-name]/tasks.md`:
- Atomic task list (each independently implementable and testable)
- With priority and dependency info
- Maps to architecture modules in `plan.md`
- Synced with `task_plan.md` (tasks.md describes; task_plan.md tracks status)

### 6. Analyze: `/speckit.analyze` (optional, recommended)

Cross-artifact consistency and coverage analysis. Run after `/speckit.tasks`, before `/speckit.implement`:
- Validates spec ↔ plan ↔ tasks alignment
- Catches missing coverage, contradictions, ambiguities
- Surfaces gaps before implementation begins

### 7. Checklist: `/speckit.checklist` (optional)

Generate custom quality checklists that validate requirements completeness, clarity, and consistency — described as "unit tests for English". Useful for complex specs.

### 8. Implement: `/speckit.implement`

Execute all tasks and build the feature according to the plan:
- Works through tasks sequentially
- Follows TDD patterns
- Commits incrementally

### 9. Gate G1

All artifacts must be explicitly confirmed by the user before proceeding to implementation.

Checklist:
- [ ] User gave explicit confirmation
- [ ] `spec.md` contains no implementation details
- [ ] `plan.md` references constitution checkpoints
- [ ] Each acceptance criterion maps to test cases
- [ ] `specify check` returns no errors
- [ ] Spec doesn't violate any constitution clause
- [ ] `/speckit.analyze` passes (if run)

## Workflow Engine & Catalog (v0.7.0+)

Spec-Kit v0.7.0 introduced a Workflow Engine with a Catalog system, enabling custom workflow registration and discovery.

### Catalog System

```bash
# Browse available workflows
specify catalog list

# Install a workflow from the catalog
specify catalog add <workflow-name>
```

Workflows registered in the community catalog can be discovered and composed with Spec-Kit's core commands, enabling project-specific execution patterns (e.g., `architect-preview`).

## Extensions & Presets

Spec-Kit supports workflow customization through two systems:

### Extensions — Add New Capabilities

Add functionality beyond Spec-Kit's core (new commands, templates, integrations).

```bash
specify extension search
specify extension add <extension-name>
```

### Presets — Customize Existing Workflows

Override templates and commands to match your methodology (Agile, Kanban, DDD, etc.).

```bash
specify preset search
specify preset add <preset-name>
```

### Priority Resolution

```
Project-Local Overrides (.specify/templates/overrides/)  ← highest
Presets (.specify/presets/<id>/templates/)
Extensions (.specify/extensions/<id>/templates/)
Spec Kit Core (.specify/templates/)                      ← lowest
```

## File Structure

```
.specify/
├── memory/
│   └── constitution.md
├── specs/
│   └── [feature-name]/
│       ├── spec.md     # Product spec (What & Why)
│       ├── plan.md     # Technical plan (How, refs constitution)
│       └── tasks.md    # Task list (synced with task_plan.md)
├── templates/
│   └── overrides/      # Project-local template overrides
├── extensions/         # Installed extensions
└── presets/            # Installed presets
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `specify init` | Initialize `.specify/` directory |
| `specify check` | Validate spec completeness (integrated into G1) |
| `specify extension search/add` | Manage extensions |
| `specify preset search/add` | Manage presets |
| `specify catalog list/add` | Browse and install community workflows |
