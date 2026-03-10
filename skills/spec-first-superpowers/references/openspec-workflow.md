# OpenSpec (OPSX) Workflow

OpenSpec is a lightweight spec-driven workflow for iterative development. This is the **default recommended mode**.

## When to Use

- Existing codebases with established patterns
- Fast iteration, small teams
- Feature enhancements, bugfixes, refactors

## Command Flow

### 1. New change: `/opsx:new [change-name]`

Create `.openspec/changes/[change-name]/proposal.md`:
- Change description and motivation
- Impact analysis
- Initial approach outline

### 2. Step-by-step: `/opsx:continue`

Create artifacts one at a time (pause for user review between each):

1. **spec.md** — Feature spec (What & Why)
2. **design.md** — Technical design (How)
3. **tasks.md** — Executable task list

### 3. Fast-forward: `/opsx:ff`

**The go-to path for Quick complexity.**

Generate all planning artifacts at once (proposal + spec + design + tasks):
- For clear, well-understood requirements
- Single-file bugfix/typo/config changes
- User confirms, then straight to implementation

### 4. Apply: `/opsx:apply`

Start implementing based on the confirmed `tasks.md`.

### 5. Archive: `/opsx:archive`

Move completed change files to archive. Timestamp and status written to `progress.md`.

## Gate G1 Checklist

Regardless of `/opsx:continue` or `/opsx:ff`, pass this before moving forward:

- [ ] User gave explicit confirmation
- [ ] `spec.md`/`proposal.md` contains no implementation details
- [ ] `design.md` decisions don't violate constitution
- [ ] Each acceptance criterion maps to test cases
- [ ] `tasks.md` synced with `task_plan.md`

## Constitution Integration

Reference the constitution via `config.yaml`:

```yaml
project:
  name: my-project
  stack: [TypeScript, React, Node.js]
rules:
  - All changes must have corresponding tests
  - UI changes require design system reference
context:
  constitution: ./constitution.md
```

Gate checks read this file and verify alignment clause by clause.

## File Structure

```
.openspec/
├── config.yaml
├── changes/
│   └── [change-name]/
│       ├── proposal.md   # Change proposal
│       ├── spec.md        # Feature spec
│       ├── design.md      # Technical design
│       └── tasks.md       # Task list (synced with task_plan.md)
└── archive/               # Completed changes
```

## OpenSpec vs. Spec-Kit

| Dimension | OpenSpec | Spec-Kit |
|-----------|---------|----------|
| Weight | Lightweight, flexible | Strict, phased |
| Best for | Existing/iterating | New/complex systems |
| Constitution | Optional (config.yaml) | Required (constitution.md) |
| Artifacts | proposal → spec → design → tasks | spec → plan → tasks |
| Fast path | `/opsx:ff` one-shot | None (always step-by-step) |
| Archiving | `/opsx:archive` auto | Manual |
