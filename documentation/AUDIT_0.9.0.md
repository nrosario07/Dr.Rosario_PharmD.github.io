# ClinicalRx reassessment — v0.9.0

Checked October14,2026 UTC (October13 local). Live deployed0.8.0; commit871e739fd6fd9846703ca791c6638407072c3a5f. All21 loaded entrypoint assets matched0.8 archive. The prior mixed-deployment issue is resolved. DEPLOYMENT_CHECK_0.9.0.json contains comparisons.

## Browser evidence this turn

Four-pillar hub inspected: old diabetes, save/restore, Gap Closer and duplicated Patient Plan entries are still present on deployed0.8, as expected before new upload. Loaded fictional SOAP case, verified note contents, then navigated to MTP reporting: one educational action, zero accepted/implemented/resolved. This is a current deployed workflow test. Earlier medication/cabinet/patient-plan full browser runs are historical evidence, not re-run or relabeled here. Current turn did not test every page or all external endpoints.

## Implemented and automated results

155 tests passed with zero failures. Coverage includes taxonomy36 stable IDs; current MDM/time thresholds independent of payer eligibility; quality prefix leads and limitations; economic benchmark provenance/no sum; PQA80/90 and non-PDC boundaries; supported/unsupported switching gates; exact FDA snapshot filtering; safe new route rendering; removed public entries; note appendix integration; inherited clinical/privacy/cabinet/report workflows. No-PHI confirmation now required for application exports. Removal of old interfaces changed test scope; counts are not directly comparable to last release.

## Clinical/source review

Read supplied PDFs/workbook and visually reviewed Novitas page4 plus Texas slide. Current CMS office E/M framework agrees with Novitas footnote; historical grid/99201 is not activated. Current TSBP statutory/signing-notification branch is distinguished from all DTM. TMB official reorganization matrix was visually read and confirms Chapter193 →169. Primary portal/archived section-text retrieval remains incomplete (archive returned403); §169.20 is a locator to verify before governed template use. Published adherence evidence and work-in-progress pilot are separated. Public PQA thresholds and FDA latest listed monthly inventory verified. Snapshot count246 total biosimilar presentations,146 interchangeable presentations. Not unique product counts. Switching is a narrow externally sourced pilot and requires US-label/prescriber verification. Source hashes and dates are retained.

## Still incomplete/unverified

New0.9 browser/mobile/print QA pending deployment because local file previews are blocked. Generic calculator URLs were not all freshly opened this turn. Published dosing schedules need independent clinical review before real care; dataset FDA-currentness is only September snapshot, not guaranteed current at use. No full ADA app; it is removed. No category-specific patient savings/avoidance estimates; numeric study benchmarks are broader analogies and cannot be summed. Quality leads are not eligibility or certified HEDIS/Stars calculations. General code inventory is not every possible product/service code or pharmacist-specific payer eligibility. Private source documents are excluded from packet; source references/taxonomy/selected public FDA data only are included. The monitoring workflow’s live activation is unverified.

## Post-upload acceptance

1. Footer0.9.0 and all four pillars; no unwanted links, save/restore, standalone Gap Closer, basic diabetes app or duplicate patient-plan link.
2. Calculator/screening/conversion aliases all show one external directory; no local result/scoring forms.
3. Fictional medication → cabinet → SOAP → agreed patient plan. Confirm note edits clear review and no-PHI export gate. Clear-all refresh discards tab inputs.
4. Add an MTP; confirm taxonomy, numeric historical benchmark/AMA citations in internal appendix only, no patient instruction or total saving. Confirm diagnosis quality leads, separate E/M documentation candidate, missing evidence and payer limits.
5. Adherence PDC below/at80%, ARV90%; insulin/HCV do not get a PDC adherence classification. Scale0–8 prompts investigation; no unreported MMAS-8 result.
6. Supported switch with prescriber/label review generates conditional source-linked relative-day draft; unsupported/complex/missing review returns no schedule.
7. FDA search Humira shows exact licensed interchangeable reference relationships and September2026 snapshot. Non-interchangeable biosimilars do not appear as interchangeable.
8. Review legal/CPT charts, mobile layout, print, API failure states and clinical-text network privacy. Publish source workflow through clone; confirm Actions enabled without changing clinical rules automatically.
