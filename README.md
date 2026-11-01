# ClinicalRx | Clean Rebuild Kit

A clean, static-first foundation for the ClinicalRx professional profile and public clinical education tools.

**Deployment target:** GitHub Pages, repository `nrosario07/nrosario07.github.io`, publishing from `main` → `/docs`.

## Important scope

This package is a **clean rebuild starter**, not a byte-for-byte backup or a feature-complete copy of the previous 0.26.0 application. It intentionally starts with a small, testable foundation. Existing detailed CV/publication content and advanced clinical workflows must be reviewed and migrated from the old repository backup before they are represented as complete.

ClinicalRx remains separate from MedCoverageIQ.

### Product boundaries

- Free, static-first public site. No paid backend, user accounts, analytics, or PHI.
- LinkedIn is the only public contact method.
- Do not store clinical drafts automatically. No browser storage/localStorage/sessionStorage.
- Public drug lookup and Medication Review/Reconciliation are separate workflows.
- Do not claim live data, automatic refresh, clinical validation, coding eligibility, or source synchronization until each has been implemented and tested.
- Use fictional or appropriately de-identified examples only.
- Retain Texas CPA and pharmacist practice resources, and build billing references Texas-first with national CMS-ready architecture.
- Exclude Texas Vendor Drug Program ingestion, Texas Medicaid formulary/coverage workflows, Texas drug pricing/reimbursement/NDC-HCPCS datasets, and related pipelines/tests.

## Quick start

1. Download and extract this ZIP.
2. Open the extracted folder in VS Code.
3. Install Node.js 20 or newer.
4. Run:

   ```bash
   node --test tests/*.test.js
   python scripts/validate-site.py
   ```

5. Preview locally:

   ```bash
   python -m http.server 8000 --directory docs
   ```

   Open `http://localhost:8000`.

6. Review `docs/assets/content.js` and replace any profile placeholders only with information approved for public release.
7. Follow `documentation/REBUILD_AND_DEPLOY.md` to create a new GitHub repository or repopulate the existing repository after deleting it.

## Repository map

```text
.github/workflows/     CI validation and GitHub Pages deployment
docs/                  Published static site (GitHub Pages root)
  assets/               CSS, JavaScript, and local data
  downloads/            Publicly approved downloadable resources
documentation/          Architecture, scope, privacy, source governance
scripts/                Local validation helpers
tests/                  Node built-in regression tests
```

## Current implementation status

This starter includes:
- responsive professional profile shell and navigation;
- separate Drug Intelligence and Medication Review/Reconciliation entry points;
- guideline repository and pharmacist billing intelligence landing pages;
- Texas CPA/practice resources landing page;
- privacy and clinical-limit notices;
- static-site validation and smoke tests;
- GitHub Actions validation and Pages deployment workflows.

This starter does **not** yet include:
- production drug APIs or a drug knowledge base;
- a validated medication reconciliation engine;
- a live guideline ingestion pipeline;
- authoritative billing-code determinations or payer eligibility logic;
- automated source retrieval/publication;
- complete historical CV, publication, presentation, or project content from the prior site.

These are explicit later phases, not implied capabilities.
