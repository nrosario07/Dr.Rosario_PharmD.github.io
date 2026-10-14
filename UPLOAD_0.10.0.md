# Upload ClinicalRx0.10.0

The current Pages deployment is healthy. Do not delete/recreate the repository or change its working Pages settings.

1. Download and extract ClinicalRx_0.10.0_GitHub_Update.zip. The extracted root contains docs/, scripts/, tests/, documentation/, .github/ and README.md. Upload the contents, not the ZIP and not an enclosing packet directory.
2. Preferred: GitHub Desktop → clone nrosario07/nrosario07.github.io → copy extracted contents into the clone, replacing matching files and preserving directory structure. Ensure hidden .github/workflows/validate-site.yml and source-monitor.yml are present.
3. Delete the obsolete docs/assets/local-draft.js and tests/local-draft.test.js in that clone if present. No current code uses them. Do not delete other user-owned files or the repository history.
4. In GitHub Desktop review changes, commit “Release ClinicalRx0.10.0 medication coverage and package validation”, then Push origin. Alternatively GitHub web root → Add file → Upload files: drag whole docs, scripts, tests, documentation folders and root files. Add .github/workflows files separately at the exact path if hidden folder is omitted. Do not flatten assets or create docs/docs.
5. Confirm repository docs/index.html, docs/assets/medication-sections.js, docs/data/release-manifest.json and .github/workflows/validate-site.yml. Keep Pages main /docs. Confirm latest Pages deployment and Validate ClinicalRx package jobs both succeed. Source-monitor workflow is review-only, not automatic clinical-rule publication.
6. Hard refresh the site. Footer/assets should show0.10.0. Run medication lookup→exact label→cabinet→SOAP→agreed patient plan; verify new coverage statuses and no-PHI export gate. Repeat a new medicine query and blank-label selection to ensure prior selection clears. New-release visual/interactive verification remains pending until this step.

Optional local checks: node --test tests/*.test.js; python scripts/validate-site.py. After intentional source edits regenerate manifest with python scripts/validate-site.py --write, rerun checks, then python scripts/package.py. Do not regenerate merely to silence an unexplained mismatch.
