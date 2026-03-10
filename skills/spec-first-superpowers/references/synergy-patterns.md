# Cross-Tool Synergy Patterns

The five integrated projects aren't standalone tools — they form a closed-loop system through these synergy chains.

---

## Chain 1: Constitution → Gates → Review

**Projects**: Spec-Kit/OpenSpec × Superpowers

The constitution isn't a static document — it's an active checklist verified at every gate.

```
Constitution defines constraints → G1 verifies spec alignment → G4 review verifies code alignment
```

- At G1: Check each spec item against constitution clauses
  - Spec-Kit: `plan.md` must reference constitution checkpoints
  - OpenSpec: `config.yaml` → `context.constitution` points to constitution file
- At G4: Code review uses constitution clauses as review dimensions
  - Code quality clauses → review SOLID, naming, docs
  - Testing clauses → review coverage, TDD cycle
  - Performance clauses → review benchmarks

---

## Chain 2: Error → Log → Debug

**Projects**: planning-with-files × Superpowers (systematic-debugging)

Errors aren't silently swallowed — they form a traceable debugging chain.

```
Error occurs → progress.md logs it (Error/Attempt/Resolution) → 3-Strike → systematic-debugging
```

- Every error is immediately logged in `progress.md`:

| Error | Attempt | Action | Result |
|-------|---------|--------|--------|
| ImportError: no module X | 1 | pip install X | Resolved |
| TypeError: undefined | 1 | Check param types | Unresolved |
| TypeError: undefined | 2 | Add null check | Resolved |

- Same error unresolved 3 times → `systematic-debugging` activates:
  1. Root cause investigation (read errors, reproduce, check changes, trace data flow)
  2. Pattern analysis (find working examples, compare differences)
  3. Hypothesis testing (minimal change, single variable)
  4. Implement fix (write test first → fix → verify)
- Still failing after debugging → challenge architecture → escalate to user

---

## Chain 3: Design → Persist → Recover

**Projects**: ui-ux-pro-max × planning-with-files

Design decisions persist across sessions, not regenerated each time.

```
--design-system generates → --persist writes design-system/MASTER.md → next session auto-loads
```

- Phase 3 always uses `--persist` flag
- Output: `design-system/MASTER.md` (global rules)
- Page-specific overrides: `design-system/pages/<page-name>.md`
- Loading order when building a page:
  1. Check if `design-system/pages/<page>.md` exists
  2. If yes → page rules override MASTER
  3. If no → use MASTER rules
- Phase 0 (session recovery) detects `design-system/` → auto-loads design context

---

## Chain 4: Spec → Plan → Execute

**Projects**: Spec-Kit/OpenSpec × planning-with-files × Superpowers (writing-plans)

Spec artifacts transform directly into a numbered, executable checklist.

```
Spec acceptance criteria → task_plan.md numbered tasks → writing-plans bite-sized steps → TDD execution
```

- Each acceptance criterion (Given-When-Then) maps to a task group in `task_plan.md`
- Each task group is broken into bite-sized steps:
  1. Write failing test
  2. Run — confirm it fails
  3. Write minimal implementation
  4. Run — confirm it passes
  5. Commit
- Spec-Kit's `tasks.md` and `task_plan.md` stay in sync (tasks.md describes what; task_plan.md tracks status)
- Execution strategy selection:
  - **Subagent-Driven**: Fresh subagent per step, two-stage review
  - **Executing-Plans**: Batch 3 tasks + checkpoint review

---

## Chain 5: Verify → Evidence → Archive

**Projects**: Superpowers (verification-before-completion) × planning-with-files

Completion claims require file-recorded verification evidence.

```
Run verification command → read full output → write to progress.md (exit code + timestamp) → archive
```

- At G4, the verification sequence:
  1. **IDENTIFY**: What command proves this? (pytest, npm test, build, etc.)
  2. **RUN**: Execute the full command
  3. **READ**: Check exit code and failure count
  4. **WRITE**: Record in `progress.md`:
     ```
     ## Verification Evidence
     - Time: 2026-03-02 14:30
     - Command: `pytest tests/ -v`
     - Result: 34/34 passed, 0 failed
     - Exit code: 0
     ```
  5. **CLAIM**: State the result based on evidence
- Archive phase includes `progress.md` evidence as part of the completion record
- `finishing-a-development-branch` options (merge/PR/cleanup) also logged to `progress.md`

---

## Quick Reference

| When you're... | You need... | Via... |
|----------------|-------------|--------|
| Writing a spec | Constitution alignment | Chain 1 |
| Hitting errors | Logging + debugging | Chain 2 |
| Doing UI design | Design persistence | Chain 3 |
| Breaking down tasks | Acceptance criteria mapping | Chain 4 |
| Claiming completion | Verification evidence | Chain 5 |
