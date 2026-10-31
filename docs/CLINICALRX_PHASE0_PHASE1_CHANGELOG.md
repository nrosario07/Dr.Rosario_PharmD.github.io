# ClinicalRx Phase 0 / Phase 1 Change Record

Prepared 2026-10-31. Target repository: `nrosario07/nrosario07.github.io`. Intended for a review branch, not direct `main` changes.

## Approved requirements
- Medication Intelligence includes separate Drug Intelligence and Medication Review/Reconciliation workflows.
- Guideline Repository targets broad major-specialty coverage.
- Pharmacist Billing Intelligence prioritizes Texas payer pathways while retaining national CMS references and a national-ready schema.
- Texas VDP ingestion, Texas Medicaid formulary/coverage/pricing datasets and dependent pipelines belong to MedCoverageIQ, not ClinicalRx.
- Retain Texas CPA authority, pharmacist code-pathway documents, white papers, primary literature and CMS physician fee schedule references.

## Profile corrections
- University Health: full-time through June 2024, per-diem from July 2024; verify precise HR/CV date wording.
- MBA: University of Southern Indiana, dual focus in Artificial Intelligence and Healthcare Administration, 4.0 GPA; do not invent completion date.
- UT Health San Antonio: Joe R. & Teresa Lozano Long School of Medicine, Department of Family & Community Medicine; MS3 teaching; resident pharmacotherapy rotation precepting when in clinic.
- Retain adjunct faculty/preceptor roles at University of Texas College of Pharmacy and UIW.
- H-E-B PGY1 Community-Based Residency assistance is historical, not current.
- Spanish: conversational, intermediate-to-advanced.
- Promote teaching, featured medication-adherence validation publication, DOI and PubMed links.
- Attribute organizational outcomes accurately; correct “across25 grouped scopes”; separate licenses, board certifications, residency training, certificates and professional development.

## Texas VDP retirement candidates
After dependency checks remove `.github/workflows/texas-data.yml`, `scripts/fetch-texas-vdp.py`, `tests/test_texas_data.py`, `documentation/INSTALL_TEXAS_DATA.yml`, `documentation/TEXAS_DATA_INTEGRATION.md`, `documentation/texas-vdp-sources.json`, and dependent Texas Medicaid drug datasets/code.

Preserve `docs/downloads/Texas_CPA_Authority.md`, `docs/downloads/Texas_Pharmacist_Code_Pathways.csv`, `docs/downloads/Texas_Pharmacist_Code_Pathways.md`, `documentation/TEXAS_CODE_PATHWAYS_0.9.0.md`, `documentation/TEXAS_CPA_LAWS_0.9.0.md`, `docs/assets/fee-reference.js` and CMS fee-reference tooling pending validated replacement.

## Not yet accepted
CMS PFS resource/API mapping; automated Purple Book latest-month discovery and validation; CMS ICD workbook discovery/validation; RxNorm monthly bulk comparison; broad guideline publisher register; hosted workflow run evidence; deployed UI freshness display; clinical/legal billing review; public profile rewrite and visual acceptance.
