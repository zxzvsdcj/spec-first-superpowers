# Cross-Tool Synergy Patterns

The five integrated projects aren't standalone tools — they form a closed-loop system through these synergy chains.

---

## Chain 1: Constitution → Gates → Review (with Review Loops)

**Projects**: Spec-Kit/OpenSpec × Superpowers

The constitution isn't a static document — it's an active checklist verified at every gate. Review loops add automated quality assurance before human review.

```
Constitution defines constraints
  → G1: Spec review loop (subagent) verifies spec alignment
    → User reviews written spec
  → G2: Plan review loop (subagent) verifies plan alignment
    → User reviews written plan
  → G4: Two-stage code review verifies code alignment
```

- At G1:
  - Spec-Kit: `plan.md` must reference constitution checkpoints; `/speckit.analyze` validates consistency
  - OpenSpec: `config.yaml` → `context` + `rules` inject project constraints
  - Spec-document-reviewer subagent checks completeness/clarity (max 3 iterations)
- At G2:
  - Plan-document-reviewer subagent checks file paths/test coverage (max 3 iterations)
  - File structure mapping locks in decomposition decisions
- At G4:
  - Code review uses constitution clauses as review dimensions
  - OpenSpec `/opsx:verify` validates Completeness × Correctness × Coherence

---

## Chain 2: Error → Log → Debug

**Projects**: planning-with-files × Superpowers (systematic-debugging)

Errors aren't silently swallowed — they form a traceable debugging chain.

```
Error occurs → progress.md logs it (Error/Attempt/Resolution)
  → 3-Strike → systematic-debugging
  → Implementer status handling (BLOCKED/NEEDS_CONTEXT)
```

- Every error is immediately logged in `progress.md`:

| Error | Attempt | Action | Result |
|-------|---------|--------|--------|
| ImportError: no module X | 1 | pip install X | Resolved |
| TypeError: undefined | 1 | Check param types | Unresolved |
| TypeError: undefined | 2 | Add null check | Resolved |

- Implementer subagent status integration:
  - **DONE_WITH_CONCERNS** → read concerns, address if about correctness
  - **NEEDS_CONTEXT** → provide context, re-dispatch
  - **BLOCKED** → escalate: more context / more capable model / break down task / rethink plan
- Same error unresolved 3 times → `systematic-debugging` activates:
  1. Root cause investigation (read errors, reproduce, check changes, trace data flow)
  2. Pattern analysis (find working examples, compare differences)
  3. Hypothesis testing (minimal change, single variable)
  4. Implement fix (write test first → fix → verify)
- Still failing after debugging → challenge architecture → escalate to user

---

## Chain 3: Design → Persist → Recover

**Projects**: ui-ux-pro-max (v2.0) × planning-with-files

Design decisions persist across sessions, not regenerated each time. v2.0 brings intelligent design system generation with 5 parallel reasoning searches.

```
v2.0 Design System Generator (5-domain search)
  → --design-system generates
  → --persist writes design-system/MASTER.md
  → next session auto-loads
```

- Phase 3 always uses `--persist` flag
- v2.0 generation pipeline:
  1. Product type matching (161 categories)
  2. Style recommendations (67 styles, BM25 ranking)
  3. Color palette selection (161 industry-specific palettes)
  4. Landing page patterns (24 patterns)
  5. Typography pairing (57 font combinations)
- Output: `design-system/MASTER.md` (global rules) + anti-patterns to avoid
- Page-specific overrides: `design-system/pages/<page-name>.md`
- Loading order when building a page:
  1. Check if `design-system/pages/<page>.md` exists
  2. If yes → page rules override MASTER
  3. If no → use MASTER rules
- Phase 0 (session recovery) detects `design-system/` → auto-loads design context
- 13 tech stacks supported: React, Next.js, Astro, Vue, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose

---

## Chain 4: Spec → Plan → Execute (with Scope Check)

**Projects**: Spec-Kit/OpenSpec × planning-with-files × Superpowers (writing-plans)

Spec artifacts transform directly into a numbered, executable checklist. Scope checks prevent overscoped specs.

```
Scope check (multiple subsystems?)
  → Spec acceptance criteria
  → File structure mapping
  → task_plan.md numbered tasks
  → writing-plans bite-sized steps
  → Model selection per task
  → TDD execution
```

- **Scope check** (early, at brainstorming): If request describes multiple independent subsystems, flag for decomposition into sub-projects before detailed spec work
- Each acceptance criterion (Given-When-Then) maps to a task group in `task_plan.md`
- **File structure mapping** (before tasks): Map out all files to be created/modified with responsibilities
- Each task group is broken into bite-sized steps (2-5 minutes each):
  1. Write failing test
  2. Run — confirm it fails
  3. Write minimal implementation
  4. Run — confirm it passes
  5. Commit
- Spec-Kit's `tasks.md` and `task_plan.md` stay in sync (tasks.md describes what; task_plan.md tracks status)
- **Model selection** for subagent execution:
  - Mechanical tasks (1-2 files, clear spec) → fast/cheap model
  - Integration tasks (multi-file coordination) → standard model
  - Architecture/design/review → most capable model
- Execution strategy selection:
  - **Subagent-Driven**: Fresh subagent per step, two-stage review (spec → quality)
  - **Executing-Plans**: Batch 3 tasks + checkpoint review
  - **Execution handoff**: After plan review loop, explicitly offer both options

---

## Chain 5: Verify → Evidence → Archive

**Projects**: Superpowers (verification-before-completion) × planning-with-files × OpenSpec

Completion claims require file-recorded verification evidence. Multi-dimensional validation available.

```
Run verification command → read full output
  → write to progress.md (exit code + timestamp)
  → /opsx:verify (Completeness × Correctness × Coherence)
  → archive
```

- At G4, the verification sequence:
  1. **IDENTIFY**: What command proves this? (pytest, npm test, build, etc.)
  2. **RUN**: Execute the full command
  3. **READ**: Check exit code and failure count
  4. **WRITE**: Record in `progress.md`:
     ```
     ## Verification Evidence
     - Time: 2026-03-19 14:30
     - Command: `pytest tests/ -v`
     - Result: 34/34 passed, 0 failed
     - Exit code: 0
     ```
  5. **VERIFY** (OpenSpec expanded): `/opsx:verify` checks 3 dimensions:
     - **Completeness**: All tasks done, all requirements implemented
     - **Correctness**: Implementation matches spec intent, edge cases handled
     - **Coherence**: Design decisions reflected in code, patterns consistent
  6. **CLAIM**: State the result based on evidence
- Archive phase:
  - `finishing-a-development-branch` options (merge/PR/keep/discard) also logged to `progress.md`
  - OpenSpec: `/opsx:archive` moves to `openspec/changes/archive/YYYY-MM-DD-<name>/`
  - Spec-Kit: Manual archive or via extension

---

## Quick Reference

| When you're... | You need... | Via... |
|----------------|-------------|--------|
| Writing a spec | Constitution alignment + spec review loop | Chain 1 |
| Hitting errors | Logging + implementer status + debugging | Chain 2 |
| Doing UI design | v2.0 design generation + persistence | Chain 3 |
| Breaking down tasks | Scope check + file mapping + model selection | Chain 4 |
| Claiming completion | Verification evidence + multi-dim validation | Chain 5 |
