# ClinicalRx Agent Instructions

## Mission
Build and maintain ClinicalRx as a trustworthy, free, static-first professional portfolio and clinical education resource.

## Non-negotiable boundaries
1. ClinicalRx is not MedCoverageIQ. Never merge their product scopes, branding, data, or roadmap.
2. Do not add PHI collection, accounts, authentication, analytics, or automatic draft persistence.
3. Never store clinical drafts in localStorage, sessionStorage, IndexedDB, cookies, or remote services.
4. Never send note text, medication lists from a patient case, or encounter details to external APIs.
5. Public drug lookups may send only the explicit drug search term/identifier needed for that lookup. Disclose this clearly.
6. Drug Intelligence and Medication Review/Reconciliation must remain separate workflows with separate state and tests.
7. No clinical recommendation without traceable source, date/version, scope, limitations, and appropriate professional review.
8. Do not claim source refresh is live or automatic unless retrieval, schema validation, provenance, publication, and UI display are all tested.
9. Never imply CPA authority, institutional privileges, payer enrollment, code eligibility, or reimbursement from a general reference.
10. Texas VDP, Texas Medicaid formulary/coverage, drug pricing/reimbursement, NDC-HCPCS ingestion and related pipelines are out of scope and must not be reintroduced.

## Engineering rules
- Keep the published site deployable as static files in `docs/`.
- Prefer vanilla JavaScript and browser-native capabilities unless a documented need justifies a build system.
- No secrets in browser code or Git history.
- Add tests for every workflow and privacy boundary.
- Preserve accessible labels, keyboard navigation, reduced-motion support, and responsive layouts.
- Keep dependencies minimal. Prefer Node built-in test runner.
- Never weaken or delete a failing test merely to make CI green. Fix the underlying defect or document why a test is obsolete and replace it with equivalent coverage.
- Keep source registries distinct from retrieved datasets and from UI claims.
- Require human review before publishing clinical content or changed source data.

## Required change report
For each meaningful change, report:
- files changed;
- behavior added/removed;
- tests run and results;
- data sources and whether they are references, live calls, or locally published snapshots;
- privacy/security impact;
- remaining clinical/legal/coding review.
