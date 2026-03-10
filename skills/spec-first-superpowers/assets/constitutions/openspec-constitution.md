# Project Constitution — OpenSpec Mode

> **Version**: 2.1
> **Scope**: All AI-generated specs, designs, tasks, and code in this project must comply.
> **Enforcement**: This constitution is actively verified at gates G1–G4.

## 1. Core Mission

The AI works by engineering best practices — no coding by vibes.

Iron rules:
1. Complete the SDD workflow before writing any code.
2. Default to OpenSpec mode unless the project is brand new with very few files.
3. All plans persist to files — chat history is not a reliable memory.
4. UI/UX tasks require a design system approved by the user before implementation.
5. All implementation follows TDD-First (write tests before code).
6. Code review is mandatory (two-stage: spec conformance + code quality).

## 2. Code Quality <!-- G4 check -->

- Clean Code · SOLID · DRY · KISS
- Complete docs for public interfaces
- Consistent naming conventions
- No magic values
- Code style enforced by tooling
- No circular dependencies
- Every commit passes linter + tests

## 3. Testing <!-- G4 check -->

- TDD-First: tests before implementation
- Coverage: critical paths ≥ `[YOUR_TARGET, e.g., 90%]`, overall ≥ `[YOUR_TARGET, e.g., 80%]`
- Tests are independent, repeatable, side-effect-free
- CI test failure → blocks merge
- No "implement first, test later"

## 4. UI/UX Consistency <!-- G3 check -->

- Unified design system (Atomic Design)
- Responsive-first (mobile-first)
- WCAG 2.1 AA (contrast ≥ 4.5:1, keyboard navigation, ARIA)
- Consistent interactions (buttons, navigation, feedback patterns)
- i18n support

## 5. Performance & Security <!-- G4 check -->

- First paint < `[YOUR_TARGET, e.g., 2.5s]` (P90)
- Interaction < `[YOUR_TARGET, e.g., 100ms]`
- Main bundle < `[YOUR_TARGET, e.g., 400KB]` (gzip)
- API response < `[YOUR_TARGET, e.g., 200ms]` (P95 < `[YOUR_TARGET, e.g., 400ms]`)
- No plaintext secrets/credentials
- OWASP Top 10 protections

## 6. Document Separation <!-- G1 check -->

- `spec.md`: Pure product perspective (What & Why) — no technical details
- `design.md`: Engineering perspective (How) — references this constitution
- Violating separation = blocker

## 7. File Persistence <!-- G2 check -->

- `task_plan.md` (numbered checklist + status)
- `findings.md` (discoveries + research)
- `progress.md` (logs + test results + verification evidence)
- Re-read `task_plan.md` before every action
- Update `progress.md` after every action

## 8. Gate ↔ Constitution Mapping

| Gate | Checks these sections |
|------|-----------------------|
| G1 | §1 (Mission), §6 (Doc separation) |
| G2 | §7 (File persistence) |
| G3 | §4 (UI/UX) |
| G4 | §2 (Code quality), §3 (Testing), §5 (Performance & security) |

## 9. Quick Self-Check

- [ ] SDD spec completed and user confirmed?
- [ ] `task_plan.md` generated and current?
- [ ] UI task has design system generated and confirmed?
- [ ] TDD: tests written first?
- [ ] Code passes linter + tests?
- [ ] Two-stage review (spec + quality) passed?
- [ ] Verification evidence written to `progress.md`?
