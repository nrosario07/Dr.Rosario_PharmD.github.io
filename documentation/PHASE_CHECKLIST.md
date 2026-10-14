# ClinicalRx phase checklist — v0.8.0

Statuses describe actual delivered scope, not clinical certification. Generic calculator development is retired under the link-first policy; PREVENT licensing is no longer a blocker.

| Phase | Completed | Remaining / blockers |
|---|---|---|
| Professional brand | 11 professional pages, four pillars, free Pages, LinkedIn-only contact | Mobile/accessibility refinement; new-release browser regression |
| CMM / MTP continuity | Guided SOAP/MTP, reviewed patient plan, external-result transfer; v0.7 explicit local save/preview/restore with review resets | Structured reporting; governed EHR mappings; standalone quality/adherence form persistence |
| Medication intelligence | RxNorm identities, selected label, source dates, cabinet and explicit SOAP sync; stale-label/duplicate fixes | Comprehensive validated DDI and pricing sources; pediatric/organ normalization; literature appraisal |
| Calculator references | Reviewed external directory and local result recorder; PREVENT external-only | Ongoing destination checks; new custom calculator only after documenting no suitable validated online option |
| Clinical pathways | Bounded anticoagulation calendar, inhaler review, adult T2D prompts | Interval-aware bridge orders and reviewed exports; full prescribing pathways require validated rules and fixtures |
| Practice development | Business outline, payer/economic review, staffing/capacity planner; local draft continuity | Denials, payment-delay and working-capital model; dated contract evidence; governed CPA authoring |
| Education | SOAP-derived agreed-action patient plans and inhaler teaching links | Reviewed Spanish, device-specific handouts, quizzes and teaching studio |
| Quality / adherence | Educational organizers, recorded VAS and gap actions | Authorized measure specifications, denominator/exclusions, validated prediction calibration; no certified HEDIS/Stars output |
| Residency | Scope retained | Current ASHP program standards and complete evidence/recruitment/orientation/audit workflows; later phase |
| Monitoring / releases | Source queue and review-only monitoring, reproducible packet, current audit | Verify uploaded monitoring workflow and dated controlling-source comparisons; never auto-publish clinical changes |

## Current position

**Phase 01B — local continuity and structured reporting is implemented, with browser acceptance pending. The full platform is incomplete.** Four-pillar foundation is delivered; clinical pathways, medication completeness, quality measures and education remain partial. Residency remains deferred. This release adds a current-encounter reporting view, evidence-completeness flags and privacy-minimal reviewed CSV. Longitudinal/institution-approved reporting remains future work.

## Release acceptance

Completed: historical 11-page/46-route and fictional workflow audit; current mixed-deployment detection (v0.6.1 index with v0.7 assets), four-pillar/diabetes/draft browser checks; v0.7 fixes/local continuity implementation; 144 passing automated tests.

Pending: v0.7 browser acceptance after owner uploads. Next implementation priority: medication section completeness and governed longitudinal reporting, before additional prescribing algorithms. Full pathway expansion is blocked where controlling sources, independent fixtures or institution-approved workflows are absent.
