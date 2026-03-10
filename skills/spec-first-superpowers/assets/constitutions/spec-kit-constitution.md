# [Project Name] Constitution — Spec-Kit Mode

> **Version**: 2.1
> **Approved**: `[DATE]`
> **Scope**: All specs, plans, tasks, and code in this project must comply.
> **Enforcement**: This constitution is actively verified at gates G1–G4. `plan.md` must reference checkpoints.

## 1. Purpose

This constitution defines the project's non-negotiable principles. It's the highest-authority document in the SDD workflow. The AI must reference and obey these principles when generating `spec.md`, `plan.md`, and `tasks.md`.

## 2. Core Principles

### 2.1 Code Quality <!-- G4 check -->

- Readable, maintainable, testable (Clean Code)
- Complete docs for public APIs
- SOLID · DRY · KISS
- No magic numbers/strings
- Consistent naming
- Code style enforced (pre-commit hooks)
- No circular dependencies, clear layering
- All changes go through code review

### 2.2 Testing <!-- G4 check -->

- TDD / BDD preferred
- Coverage: critical paths ≥ `[YOUR_TARGET, e.g., 95%]`, overall ≥ `[YOUR_TARGET, e.g., 85%]`
- Tests are independent, repeatable, side-effect-free
- CI/CD test failure → blocks merge
- No committing untested code

### 2.3 User Experience <!-- G3 check -->

- Unified design system (Atomic Design)
- Responsive (mobile-first)
- WCAG 2.1 AA (ARIA, keyboard nav, contrast ≥ 4.5:1)
- Consistent interactions (buttons, navigation, loading, error states)
- i18n support
- Page load < `[YOUR_TARGET, e.g., 3s]`, interaction < `[YOUR_TARGET, e.g., 100ms]`

### 2.4 Performance <!-- G4 check -->

- First paint < `[YOUR_TARGET, e.g., 2s]` (P90)
- Main bundle < `[YOUR_TARGET, e.g., 500KB]` (gzip)
- No N+1 queries
- API response < `[YOUR_TARGET, e.g., 200ms]` (P95 < `[YOUR_TARGET, e.g., 500ms]`)
- Monitor LCP/FID/CLS

## 3. Architecture Governance <!-- G1 check -->

- Major architecture decisions recorded in `plan.md`, **referencing this constitution**
- Prefer mature, actively maintained, LTS technologies
- No high-risk dependencies
- Third-party license audit (MIT/Apache preferred)
- OWASP Top 10 protections

## 4. Document Separation <!-- G1 check -->

- `spec.md`: **Pure product perspective** (What & Why) — no frameworks, libraries, code structure
- `plan.md`: **Engineering perspective** (How) — must reference constitution checkpoints
- Violating separation = blocker

## 5. Gate ↔ Constitution Mapping

| Gate | Checks these sections |
|------|-----------------------|
| G1 | §3 (Architecture governance), §4 (Doc separation) |
| G2 | `plan.md` references constitution checkpoints? |
| G3 | §2.3 (User experience) |
| G4 | §2.1 (Code quality), §2.2 (Testing), §2.4 (Performance) |

## 6. Amendments

- Record version history + rationale for each change
- After amendment, AI self-checks whether existing spec/plan still complies
- Review quarterly or at major technical shifts

## 7. Quick Self-Check

- [ ] `spec.md` is pure product perspective, no technical details?
- [ ] `plan.md` references constitution checkpoints?
- [ ] Code passes linter + tests + coverage ≥ `[YOUR_TARGET]`?
- [ ] UI changes pass design system consistency + accessibility checks?
- [ ] Performance benchmarked before and after?
- [ ] Verification evidence written to `progress.md`?
