# Integration Guide

## Dependency Skills

| Skill | Role | Required? | Phase |
|-------|------|-----------|-------|
| `using-superpowers` | Loads Superpowers methodology | Yes | Phase 4 |
| `brainstorming` | Design exploration + inline spec review | Yes | Phase 1 |
| `writing-plans` | Implementation plans + inline plan review | Yes | Phase 2 |
| `test-driven-development` | TDD RED-GREEN-REFACTOR | Yes | Phase 4 |
| `requesting-code-review` | Two-stage code review | Yes | Phase 4 |
| `verification-before-completion` | Pre-completion verification | Yes | Phase 4 (G4) |
| `planning-with-files` | File-based planning + session recovery | Yes | Phase 0/2 |
| `ui-ux-pro-max` | UI/UX design system (v2.5.0) | Conditional | Phase 3 |
| `systematic-debugging` | 4-phase root cause analysis | On demand | Phase 4 |
| `subagent-driven-development` | Subagent execution + two-stage review | On demand | Phase 4 |
| `executing-plans` | Batch execution + checkpoints | On demand | Phase 4 |
| `dispatching-parallel-agents` | Concurrent subagent workflows | On demand | Phase 4 |
| `finishing-a-development-branch` | Branch wrap-up | Yes | Phase 5 |

Missing a required skill? Search and install: `npx skills find '<keyword>'`

## External Tools

| Tool | Role | Required? |
|------|------|-----------|
| MemPalace | Cross-session memory + knowledge graph | Optional (recommended) |

## Installation

### Spec-Kit (v0.7.1+)

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init . --integration cursor
```

> Note: `--ai` flag is deprecated. Use `--integration` instead.

### OpenSpec (v1.2.0+)

```bash
npm install -g @fission-ai/openspec@latest
cd your-project && openspec init
```

### Superpowers (v5.0.7+)

**Cursor**: `/add-plugin superpowers` or search in plugin marketplace.

**Claude Code**: `/plugin install superpowers@claude-plugins-official`

**Gemini CLI**: `gemini extensions install https://github.com/obra/superpowers`

### ui-ux-pro-max (v2.5.0+)

Install via Cursor Skills or `npx skills add`:
```bash
npx skills add nextlevelbuilder/ui-ux-pro-max-skill
```

CLI tool available: `npm install -g uipro-cli`

### MemPalace (v3.3.0+, optional)

```bash
pip install mempalace
mempalace init ~/projects/your-project
```

Cursor MCP setup: see [references/mempalace-integration.md](mempalace-integration.md)

## Session Recovery Protocol

When `task_plan.md` exists at session start (meaning there's unfinished work):

1. **Read all planning files**: `task_plan.md` + `findings.md` + `progress.md`
2. **MemPalace context** (if configured):
   - `mempalace_status` → palace overview
   - `mempalace_search("project-name decisions")` → relevant history
   - `mempalace_diary_read(agent="spec-orchestrator")` → last workflow state
3. **5-Question Reboot Test**:
   - What phase am I in? (last `[x]` in `task_plan.md`)
   - What's next? (next `[ ]`)
   - What's the goal? (goal statement at top of `task_plan.md`)
   - What did I learn? (key findings from `findings.md`)
   - What did I do? (latest entry in `progress.md`)
4. **Consistency check**: `git diff --stat` vs. `progress.md` records
5. **Design system check**: If `design-system/` exists → auto-load design context
6. **Breakpoint**: Resume from the next unchecked step
7. **Report to user**: Current state + next step suggestion → confirm before continuing

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

### Model Selection for Subagent Execution

Use the least powerful model that can handle each role to conserve cost:

| Task type | Signal | Model |
|-----------|--------|-------|
| Mechanical implementation | 1-2 files, clear spec | Fast/cheap |
| Integration | Multi-file coordination, pattern matching | Standard |
| Architecture/design/review | Broad codebase understanding, design judgment | Most capable |

### Implementer Status Handling

| Status | Action |
|--------|--------|
| DONE | Proceed to spec compliance review |
| DONE_WITH_CONCERNS | Read concerns → address if correctness/scope |
| NEEDS_CONTEXT | Provide missing info, re-dispatch |
| BLOCKED | Escalate: more context / better model / break down / rethink |

## Troubleshooting

**Mode seems wrong?**
Run `/super-spec reset` to delete `.spec-mode` and retrigger auto-detection. Or use `force-spec-kit` / `force-openspec`.

**AI skipped the spec phase?**
Check that `.cursor/rules/00-spec-first-superpowers.mdc` exists and has `alwaysApply: true`.

**UI/UX design didn't trigger?**
Include UI keywords in your request: UI, UX, page, dashboard, component, interaction, interface, design, app, web, mobile.

**Context drifting in long sessions?**
Check `task_plan.md` / `progress.md` are up to date. Use "Read Before Decide": re-read `task_plan.md` before any major decision. Consider enabling MemPalace for persistent memory.

**Same error 3 times?**
The 3-Strike protocol auto-escalates to `systematic-debugging`. If that also fails, the architecture may need rethinking — escalate to the user.

**OpenSpec directory not found?**
OpenSpec now uses `openspec/` (not `.openspec/`). Run `openspec init` to initialize.

**OpenSpec profile confusion?**
"expanded" was renamed to "custom" in v1.2.0. Run `openspec config profile` to see current options.

## Related Projects

| Project | GitHub | Version | Role |
|---------|--------|---------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | v0.7.1 | GitHub's spec-driven framework |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | v1.2.0 | Lightweight OPSX workflow |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | v5.0.7 | TDD + inline review methodology |
| planning-with-files | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | v2.30.0 | File-based persistent planning |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | v2.5.0 | UI/UX design system |
| MemPalace | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | v3.3.0 | Cross-session memory + knowledge graph |
