# Core 13-track acceptance plan

Updated October 25, 2026, release 0.23.0. Core platform first. Nutrition/affiliate commerce and the business AI studio are frozen at their current pilot/planning state until core acceptance progresses. Full acceptance means the scoped functionality, data provenance, failure handling, accessibility and relevant professional review are documented; a unit-test count alone cannot close a phase.

| Track | Next acceptance task | Evidence needed before closure |
| --- | --- | --- |
| 00 Profile/navigation | Complete desktop keyboard and narrow-screen navigation audit | Every page, focus behavior, readable layouts, current profile content |
| 01B Privacy/reporting | Repeat exports and clearing across connected workflows | No identifiers/persistence/transmission; actual downloaded file inspection |
| 01D SOAP/MTP/MDM | Expand positive/negative clinical-language fixtures | Independent clinician/coder review; safe disagreement and missing-evidence handling |
| 01E Economics | Verify each coefficient and overlap handling | Population/year/currency/context and nonadditive categories documented |
| 02 Medication intelligence | Exact identity/label normalization and recovery matrix | Live lookup → cabinet → SOAP → plan; no mismatch or silent stale data |
| 03 Calculator directory | Verify every destination and retirement status | Link/instrument/version/permission ledger |
| 04 Switching/anticoagulation | Expand exact-product rules; consolidate evidence schema | Boundary and browser fixtures, independent clinical review and provenance per direction |
| 04D Diabetes | Complete scoped application design and verified rule set | Guideline/label traceability, normalized inputs, clinical validation before reintroduction |
| 05 Professional practice | Review CPA and billing-pathway scope | Texas legal/physician/institutional and payer-specific review |
| 06 Education | Handout print/mobile/comprehension acceptance | Complete exported plan, no clinician-only content, teach-back/device/bilingual review |
| 07 Adherence/quality | Validate claims edge cases and measure usage | Denominators/exclusions/licensing plus adherence-study evidence review |
| 08 Residency | Define one initial program-type implementation | Current accreditation mapping, complete lifecycle examples, program-director review |
| 09 Release/source governance | Install and run both supplied workflows | Successful Actions run, review queue, source baseline, reproducible release |

## Execution order

1. Low-complexity acceptance gaps: workflow installation, external-link inventory, navigation/keyboard checks, export/clear tests.
2. Data quality: common switch evidence schema, ingredient/formulation/route identity, units, source sections, effective/review dates and explicit exclusions. UI and accepted-pair catalog must not diverge.
3. Broader switch coverage: product-label formulation conversions first; guideline-supported antidepressant directions next; oral/LAI antipsychotic branches after exact initiation/overlap/renal constraints. Cross-class antihypertensive and GLP comparisons need primary evidence and cannot be labeled proven equipotence merely from approximate efficacy tables.
4. Complete normalized drug, SOAP/quality/economics reviews and education acceptance.
5. Larger applications: diabetes and residency, with defined clinical/program review.

Independent reviews and GitHub workflow access are external gates, not tasks that passing code tests can waive. No complete track is yet accepted: 11/13 have initial capability and 0/13 have final acceptance.

## Later monetized application

Keep a separate backlog: domain purchase/setup, social-preview metadata, optional affiliate catalog and ranking, then React only if complexity warrants it; accounts/database only if saved user features justify them. Analytics requires a fresh privacy/cookie assessment. Neither React, authentication, a database nor Google Analytics is necessary for a basic static affiliate site. No purchases, tracking, authentication, database or affiliate links are added in this core release. Maintain a usable free path and independent clinical selection criteria.

0.23.0: Phase02 biosimilar search includes both FDA designations; pricing and specialty-data source guide added. Public integration and professional review remain acceptance gates. See AUDIT_0.23.0.md.

### 0.23.0 acceptance increment
Deployed0.22 filters and focused medication→cabinet→SOAP→patient-plan/clear workflow browser checked. New paging, filters and importer validation delivered; new visual/mobile/export acceptance remains open. Both remote workflow files still return404. No full track closed. See AUDIT_0.23.0.md.
