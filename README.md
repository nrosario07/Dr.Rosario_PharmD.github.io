# ClinicalRx v0.12.1 by Dr. Rosario

Free four-pillar professional and clinical resource, with LinkedIn-only contact. Fictional/de-identified cases only; no PHI, automatic draft persistence, or clinical-text API requests. Intentional exports require a no-PHI review.

Current work: Phase 04 recommendation workflows, Phase 02 medication API resilience and Phase 05 CPA drafting. Full platform incomplete. See documentation/PHASE_CHECKLIST.md and documentation/BUILD_SPECIFICATION.md.

241 automated tests passed. Deployed v0.11 medication lookup succeeded in the browser; new v0.12 browser acceptance remains pending upload. See documentation/AUDIT_0.12.0.md for exact verification boundaries.

Run `node --test tests/*.test.js`, `python scripts/validate-site.py`, and `python scripts/package.py`. Read UPLOAD_0.12.1.md before replacing repository files. GitHub Pages uses main:/docs. Source monitoring queues review only; it never autonomously changes clinical rules.

Focused patch: independent FDA label-linked recovery and explicit FDA search button. See documentation/AUDIT_0.12.1.md. Reported procedure dropdown and switch rendering defects remain open.
