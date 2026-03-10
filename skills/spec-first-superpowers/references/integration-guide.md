# Integration Guide

## Dependency Skills

| Skill | Role | Required? | Phase |
|-------|------|-----------|-------|
| `using-superpowers` | Loads Superpowers methodology | Yes | Phase 4 |
| `brainstorming` | Design exploration (merged into Spec phase) | Yes | Phase 1 |
| `writing-plans` | Implementation plans (bite-sized steps) | Yes | Phase 2 |
| `test-driven-development` | TDD RED-GREEN-REFACTOR | Yes | Phase 4 |
| `requesting-code-review` | Code review | Yes | Phase 4 |
| `verification-before-completion` | Pre-completion verification | Yes | Phase 4 (G4) |
| `planning-with-files` | File-based planning + session recovery | Yes | Phase 0/2 |
| `ui-ux-pro-max` | UI/UX design system | Conditional | Phase 3 |
| `systematic-debugging` | 4-phase root cause analysis | On demand | Phase 4 |
| `subagent-driven-development` | Subagent execution + two-stage review | On demand | Phase 4 |
| `executing-plans` | Batch execution + checkpoints | On demand | Phase 4 |
| `finishing-a-development-branch` | Branch wrap-up | Yes | Phase 5 |

Missing a required skill? Search and install: `npx skills find '<keyword>'`

## Session Recovery Protocol

When `task_plan.md` exists at session start (meaning there's unfinished work):

1. **Read all planning files**: `task_plan.md` + `findings.md` + `progress.md`
2. **5-Question Reboot Test**:
   - What phase am I in? (last `[x]` in `task_plan.md`)
   - What's next? (next `[ ]`)
   - What's the goal? (goal statement at top of `task_plan.md`)
   - What did I learn? (key findings from `findings.md`)
   - What did I do? (latest entry in `progress.md`)
3. **Consistency check**: `git diff --stat` vs. `progress.md` records
4. **Breakpoint**: Resume from the next unchecked step
5. **Report to user**: Current state + next step suggestion → confirm before continuing

This runs automatically at session start — no user action needed.

## Complexity Triage

```
Task received
    ├─ Single-file bugfix/typo/config?           → Quick
    ├─ Touches ≥ 3 files?                        → Standard or Thorough
    ├─ Requires architecture decisions?            → Thorough
    ├─ Involves UI/UX design?                     → Standard (triggers Phase 3)
    ├─ Can split into ≥ 2 independent subtasks?   → Thorough (+ Agent Teams)
    └─ Other single-feature changes               → Standard
```

The AI suggests a level; the user confirms or adjusts.

## Execution Strategy Selection

Phase 4 offers two strategies. The AI recommends based on task characteristics:

| Dimension | Subagent-Driven | Executing-Plans |
|-----------|----------------|-----------------|
| Context | Fresh subagent per task (zero pollution) | Same session, cumulative context |
| Review | Two-stage per task (spec + quality) | Checkpoint every 3 tasks |
| Best for | Independent tasks, high quality bar | Tightly coupled tasks, fast iteration |
| Trade-off | More subagent calls | Lower call count but context drift risk |

When in doubt → **Subagent-Driven** (default recommendation).

## Troubleshooting

**Mode seems wrong?**
Run `/super-spec reset` to delete `.spec-mode` and retrigger auto-detection. Or use `force-spec-kit` / `force-openspec`.

**AI skipped the spec phase?**
Check that `.cursor/rules/00-spec-first-superpowers.mdc` exists and has `alwaysApply: true`.

**UI/UX design didn't trigger?**
Include UI keywords in your request: UI, UX, page, dashboard, component, interaction, interface, design, app, web, mobile.

**Context drifting in long sessions?**
Check `task_plan.md` / `progress.md` are up to date. Use "Read Before Decide": re-read `task_plan.md` before any major decision.

**Same error 3 times?**
The 3-Strike protocol auto-escalates to `systematic-debugging`. If that also fails, the architecture may need rethinking — escalate to the user.

## Related Projects

| Project | GitHub | Role |
|---------|--------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | GitHub's spec-driven framework |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Lightweight OPSX workflow |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | TDD + review methodology |
| planning-with-files | [othmanadi/planning-with-files](https://github.com/othmanadi/planning-with-files) | File-based persistent planning |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX design system |
