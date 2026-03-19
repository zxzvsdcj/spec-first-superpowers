# Quality Gates (G0–G4)

Each gate is a hard stop between phases. If any check fails, go back, fix it, and re-evaluate.
When checking a gate, reference the relevant constitution clauses.

---

## G0 — Session Recovery

Triggered when `task_plan.md` already exists (meaning there's unfinished work).

| Check | Pass criteria |
|-------|--------------|
| Planning files present | `task_plan.md` + `findings.md` + `progress.md` all exist and are readable |
| 5-Question Reboot Test | Can answer: What phase am I in? / What's next? / What's the goal? / What did I learn? / What did I do? |
| Breakpoint located | Found last `[x]` in `task_plan.md`; next `[ ]` is the resume point |
| Context consistent | `git diff --stat` matches what `progress.md` reports |
| Design system check | If `design-system/` exists → auto-load design context |

**If it fails**: Fill in missing files → align state manually → re-evaluate.

---

## G1 — Spec Complete

Between Phase 1 (Specification) and Phase 2 (Planning).

| Check | Pass criteria | Constitution |
|-------|--------------|-------------|
| User confirmed | Explicit "yes", "OK", "confirmed", or equivalent | §1 Core mission |
| Spec complete | Spec-Kit: `spec.md` has user stories + acceptance criteria · OpenSpec: proposal + spec done | §4/§6 Doc separation |
| What vs How separated | Spec contains no implementation details | §4/§6 Doc separation |
| Constitution aligned | Spec content doesn't violate any constitution clause | §2 Core principles |
| Testable acceptance criteria | Each criterion maps to at least one test case | §2.2/§3 Testing |
| Scope check passed | If multiple independent subsystems detected, flagged for decomposition | brainstorming |
| Spec review loop passed | Spec-document-reviewer subagent approved (max 3 iterations) | Superpowers |
| User reviewed written spec | User explicitly reviewed the spec document file | brainstorming |

Spec-Kit extras: `specify check` returns no errors · `/speckit.analyze` passes (if run).

**If it fails**: Run `/speckit.clarify` or `/opsx:explore` to fill gaps → spec review loop → re-confirm.

---

## G2 — Plan Ready

Between Phase 2 (Planning) and Phase 3/4 (Design/Implementation).

| Check | Pass criteria |
|-------|--------------|
| Three files ready | `task_plan.md` + `findings.md` + `progress.md` created |
| Numbered checklist | Each atomic task has its own ID (e.g., 1.1, 1.2, 2.1) |
| File paths specified | Each task lists exact Create/Modify/Test file paths |
| File structure mapped | All files to be created/modified are mapped with responsibilities before tasks |
| TDD test points | Each task includes a test strategy or draft test cases |
| Acceptance traceability | Each task traces back to a confirmed acceptance criterion from G1 |
| Risk assessment | High-risk operations have rollback strategies noted |
| Plan review loop passed | Plan-document-reviewer subagent approved (max 3 iterations) | 
| User reviewed plan | User explicitly reviewed the plan document |

**If it fails**: Fill in missing items → plan review loop → user confirms plan → re-evaluate.

---

## G3 — Design Confirmed

Between Phase 3 (UI/UX Design) and Phase 4 (Implementation). Only for UI/UX tasks.

| Check | Pass criteria | Constitution |
|-------|--------------|-------------|
| Design system generated | `--design-system` output includes patterns, styles, colors, typography | §4/§2.3 UI/UX |
| Design persisted | `--persist` created `design-system/MASTER.md` | §7 File persistence |
| Pre-delivery checklist | All dimensions pass: Visual Quality · Interaction · Light/Dark · Accessibility | §4/§2.3 UI/UX |
| User confirmed | User explicitly approved the design | §1 Core mission |
| Accessibility | WCAG 2.1 AA · responsive · contrast ≥ 4.5:1 | §2.3 |

ui-ux-pro-max v2.0 capabilities: 67 UI styles · 161 color palettes · 57 font pairings · 13 tech stacks · 161 reasoning rules.

**If it fails**: Adjust design → regenerate → re-check.

---

## G4 — Implementation Verified

Between Phase 4 (Implementation) and Phase 5 (Archive). The strictest gate.

| Check | Pass criteria | Source skill |
|-------|--------------|-------------|
| TDD coverage | Every new feature/fix has tests with RED→GREEN cycle | test-driven-development |
| All tests pass | Test command output shows 0 failures (full output preserved) | verification-before-completion |
| Spec conformance review | Code matches confirmed spec (nothing missing, nothing extra) | requesting-code-review |
| Code quality review | No Critical/Important issues unfixed | requesting-code-review |
| Evidence archived | Verification output written to `progress.md` with exit code + timestamp | planning-with-files |
| Constitution compliant | Code quality, test coverage, performance, security meet constitution baselines | constitution |
| `/opsx:verify` passed | Completeness + Correctness + Coherence validated (OpenSpec expanded, if available) | OpenSpec |

**Two-stage review flow** (from Superpowers):
1. **Spec conformance** → Does the code match the confirmed spec?
   - Pass → proceed to step 2
   - Fail → fix → redo step 1
2. **Code quality** → SOLID, security, performance?
   - Pass → G4 passes
   - Fail → fix → redo step 2

**If it fails**: Fix based on review feedback → rerun tests → re-review → loop until it passes.

---

## Review Loops (New in v4)

### Spec Review Loop (integrated into G1)

After writing the spec document, dispatch a spec-document-reviewer subagent:
1. Reviewer examines spec for completeness, clarity, testability
2. If issues found → fix → re-dispatch reviewer
3. Max 3 iterations; if still failing → escalate to user
4. User reviews written spec before proceeding

### Plan Review Loop (integrated into G2)

After writing the implementation plan, dispatch a plan-document-reviewer subagent:
1. Reviewer examines plan for completeness, file paths, test coverage
2. If issues found → fix → re-dispatch reviewer
3. Max 3 iterations; if still failing → escalate to user
4. User reviews written plan before proceeding

---

## Implementer Status Handling (Phase 4)

When using subagent-driven-development, implementer subagents report one of four statuses:

| Status | Action |
|--------|--------|
| **DONE** | Proceed to spec compliance review |
| **DONE_WITH_CONCERNS** | Read concerns; address if about correctness/scope, note if observations |
| **NEEDS_CONTEXT** | Provide missing context, re-dispatch |
| **BLOCKED** | Assess: context problem → provide more; reasoning → use more capable model; task too large → break down; plan wrong → escalate |

---

## Error Escalation (applies to all gates)

```
Attempt 1: Diagnose → targeted fix → re-evaluate gate
Attempt 2: Different approach/tool → fix → re-evaluate
Attempt 3: Challenge assumptions → search for solutions → consider updating the plan
After 3 failures: → systematic-debugging (4-phase root cause analysis) → escalate to user
```

This merges `planning-with-files` 3-Strike Protocol with `systematic-debugging`.
