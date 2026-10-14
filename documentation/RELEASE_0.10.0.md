# ClinicalRx 0.10.0 — 2026-10-14

Phase 02 medication-section normalization and package integrity. Existing four pillars, free access, LinkedIn-only contact and tab-local fictional/de-identified encounter handling are preserved. No automatic patient-data persistence or save/restore.

## Changes
- Sixteen medication topics now expose FIELD_RETURNED, BROADER_SECTION_REVIEW or NOT_RETURNED with actual source field names. Broader population/pharmacology sections do not become inferred topic-specific findings. Combined dosage and adverse-reaction sections retain explicit limits.
- New searches and blank label selection clear the previous product selection. Stale search/label request errors cannot overwrite a newer view.
- SHA-256 public-file manifest and deterministic package validator identify missing assets, mixed versions and changed loaded files. Packaging refuses a mismatched manifest.
- Read-only GitHub validation workflow runs unit/workflow tests and package validation. Upload `.github` explicitly; it was absent in the audited remote tree.

## Verification
Deployed **0.9.0**: latest Pages run succeeded at 6b96dbe7d1e141596dbda6b5f0905ef5891ac727. Live index and 24 loaded assets matched the 0.9 package. Browser: 47 distinct route headings; public apixaban identity/exact label/enrichment → cabinet → SOAP → agreed patient plan; export gate/download; clear-all/reload; quality/E/M fixtures; FDA relationship search; ARV threshold/insulin methodology boundary; supported and unsupported switches; dated anticoagulation calendar.

New **0.10.0**: 161/161 automated tests pass. Manifest verifies 25 loaded assets and 32 public-file hashes. Browser interaction/layout testing of the new release is pending deployment. Automated DOM harness checks data flow, not visual appearance or clinical validation. Mobile, print/PDF layout, all workflow branches and external API outage behavior remain unverified.

No new clinical dosing, billing-eligibility or economic recommendation is introduced. Missing label fields are not absent-risk findings. Full normalized monographs, comprehensive DDI, prices, condition-specific guideline roles and the complete ADA app remain unfinished.

Integrity negative fixture: an isolated modified medication asset was rejected with manifest mismatch. Browser-downloaded fictional patient-plan text was independently verified.
