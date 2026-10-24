# Upload ClinicalRx0.11.0

The current Pages deployment is healthy. Do not delete/recreate the repository or change its working Pages settings.

1. Download and extract ClinicalRx_0.11.0_GitHub_Update.zip. The extracted root contains docs/, scripts/, tests/, documentation/, .github/ and README.md. Upload the contents, not the ZIP and not an enclosing packet directory.
2. Preferred: GitHub Desktop → clone nrosario07/nrosario07.github.io → copy extracted contents into the clone, replacing matching files and preserving directory structure. Ensure hidden .github/workflows/validate-site.yml and source-monitor.yml are present.
3. Delete the obsolete docs/assets/local-draft.js and tests/local-draft.test.js in that clone if present. No current code uses them. Do not delete other user-owned files or the repository history.
4. In GitHub Desktop review changes, commit “Release ClinicalRx0.11.0 CPA encounter and clinical workflow upgrade”, then Push origin. Alternatively GitHub web root → Add file → Upload files: drag whole docs, scripts, tests, documentation folders and root files. Add .github/workflows files separately at the exact path if hidden folder is omitted. Do not flatten assets or create docs/docs.
5. Confirm repository docs/index.html, docs/assets/cpa-workspace.js, docs/data/release-manifest.json and .github/workflows/validate-site.yml. Keep Pages main /docs. Confirm latest Pages deployment and Validate ClinicalRx package jobs both succeed. Source-monitor workflow is review-only, not automatic clinical-rule publication.
6. Hard refresh the site. Footer/assets should show0.11.0. Run medication lookup→exact label→cabinet→SOAP→agreed patient plan; verify new coverage statuses and no-PHI export gate. Repeat a new medicine query and blank-label selection to ensure prior selection clears. New-release visual/interactive verification remains pending until this step.

Optional local checks: node --test tests/*.test.js; python scripts/validate-site.py. After intentional source edits regenerate manifest with python scripts/validate-site.py --write, rerun checks, then python scripts/package.py. Do not regenerate merely to silence an unexplained mismatch.


New-release browser checklist: verify referral/diagnosis-first encounter; add two established diagnoses; enter explicit fictional MTP finding; confirm it, verify sourced benchmark mapping, then edit assessment and verify re-review exclusion. Generate actual-time candidate; choose FQHC and verify no office benchmark. Review patient plan and export gate. In switching, submit supported and unsupported LAI fixtures; edits must clear prior plan. In adherence verify dropdown definitions and number above slider. Repeat public medication lookup; capture the source-specific error if it fails. Verify Pharmacist Practitioner and unified credentials on desktop/mobile. Print/PDF requires independent layout review.

This package preserves main /docs. No whole-repository deletion required. GitHub Desktop is the most reliable way to include .github/workflows; the remote tree still lacks those workflows. The optional source-monitor workflow can propose review reports; it never publishes new clinical rules.
