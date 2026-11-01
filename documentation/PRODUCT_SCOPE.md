# ClinicalRx Product Scope

## Four pillars
1. Clinical Care
2. Drug & Evidence Intelligence
3. Professional Practice
4. Education

## Core experiences
- Professional profile and public portfolio.
- Drug Intelligence: general drug reference and evidence discovery.
- Medication Review & Reconciliation: distinct patient-case workflow, fictional/de-identified only.
- Guideline Repository: cross-specialty, historical versions and six-month update banner based on verified metadata.
- Pharmacist Billing Intelligence: Texas-first, national CMS-ready.
- Texas CPA authority, pharmacist practice pathways, white papers and primary literature.
- Clinical education tools and curated references.

## Explicitly out of scope
- MedCoverageIQ.
- Texas Vendor Drug Program ingestion.
- Texas Medicaid formulary/drug coverage.
- Texas drug pricing/reimbursement datasets and NDC-HCPCS workflows.
- Paid backend, accounts, PHI, cloud storage of drafts, and patient-record integrations.

## MVP order
1. Static site shell, profile and privacy/security tests.
2. Navigation, content migration and accessibility.
3. Drug Intelligence reference architecture and one permitted public source integration.
4. Medication Review/Reconciliation with isolated state, explicit review gates and no persistence.
5. Guideline repository schema and curated initial records.
6. Texas CPA and practice reference library.
7. Pharmacist billing reference architecture and CMS PFS data provenance.
8. Scheduled source monitoring, then source-specific retrieval only after legal/schema/test review.
9. Independent clinical, legal and coding review.
10. Deployed acceptance and release.
