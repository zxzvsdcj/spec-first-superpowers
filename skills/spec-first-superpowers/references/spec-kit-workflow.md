# Spec-Kit Workflow

Spec-Kit is GitHub's spec-driven development framework. Best for brand-new projects or complex systems that need strict phase gating.

## When to Use

- Building from scratch
- Large systems (multi-module, multi-team)
- Enterprise projects requiring strict phase control

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

Skippable at Quick complexity level.

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

### 6. Gate G1

All three artifacts must be explicitly confirmed by the user before proceeding.

Checklist:
- [ ] User gave explicit confirmation
- [ ] `spec.md` contains no implementation details
- [ ] `plan.md` references constitution checkpoints
- [ ] Each acceptance criterion maps to test cases
- [ ] `specify check` returns no errors
- [ ] Spec doesn't violate any constitution clause

## File Structure

```
.specify/
├── memory/
│   └── constitution.md
└── specs/
    └── [feature-name]/
        ├── spec.md     # Product spec (What & Why)
        ├── plan.md     # Technical plan (How, refs constitution)
        └── tasks.md    # Task list (synced with task_plan.md)
```

## CLI Commands

```bash
specify init    # Initialize .specify/ directory
specify check   # Validate spec completeness (integrated into G1)
```
