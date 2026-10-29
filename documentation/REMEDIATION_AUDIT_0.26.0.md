# v0.26.0 ZIP remediation audit

**Scope:** Repository ZIP supplied by the maintainer, remediated as a working copy. The live GitHub Pages deployment was not changed or inspected during this package run.

## Changes made

1. Installed the three supplied GitHub Actions templates at their active paths:
   - `.github/workflows/release-check.yml`
   - `.github/workflows/source-monitor.yml`
   - `.github/workflows/texas-data.yml`
2. Removed the retired `docs/assets/local-draft.js` module and its obsolete five-test suite. The public site and privacy tests already require that local draft save/restore not be shipped or loaded; the leftover asset was the reason the suite failed.
3. Regenerated `docs/data/release-manifest.json` from the current public files after the retired module was removed.
4. Replaced stale root `START_HERE.txt` with current v0.26.0 entry instructions.
5. Updated `UPLOAD.md`, `README.md`, `documentation/PHASE_CHECKLIST.md`, and `scripts/package.py` so workflow instructions describe the three active workflow paths and hosted-run verification requirement.

## Verification performed in this environment

| Check | Result |
|---|---:|
| JavaScript regression tests (`node --test tests/*.test.js`) | **408 passed, 0 failed** |
| Python governance tests (`python -m unittest discover -s tests -p 'test_*.py'`) | **24 passed, 0 failed** |
| Public site manifest (`python scripts/validate-site.py`) | **PASS**, 34 loaded assets and 48 public-file hashes |
| Packaging script (`python scripts/package.py`) | **PASS**, verified ZIP integrity and upload batch sizes |
| ZIP archive integrity | **PASS** |

The 408 JavaScript and 24 Python results were rerun against the remediated working copy. The historical test-results document was not rewritten as if it were a newly generated release artifact.

## Still open / not certified

- GitHub Actions hosted execution cannot be verified from the ZIP. Commit the workflow paths, then inspect the release-check run and manually run the two scheduled workflows.
- No deployed-browser acceptance was run here. Verify v0.26.0 after deployment, especially payer/cabinet reset, renewed patient-plan agreement, mobile/responsive behavior, keyboard paths, and handout print/PDF output.
- `docs/assets/icd-index.js` is approximately 6.8 MB and is still loaded on every route. It was deliberately not changed in this patch because safely lazy-loading it requires workflow/browser acceptance of the ICD search paths.
- Clinical, coding, economic, Texas professional/legal, source-currency, licensing, privacy-institutional, bilingual/comprehension, and payer reviews remain separate gates. Automated tests do not certify those areas.
- Diabetes Phase04D and residency Phase08 remain unimplemented per the phase checklist.
- The app release label remains 0.26.0. This is a maintenance/remediation package, not a claim that the deployed site has been released or accepted.

## Recommended owner sequence

1. Upload/commit the modified repository including `.github/workflows/`.
2. Confirm release-check passes in GitHub Actions.
3. Manually run source-monitor and Texas-data retrieval; inspect artifacts without auto-publishing source or clinical-rule changes.
4. Deploy via `main` / `docs` and complete the pending browser acceptance checklist.
5. Only after those gates pass, prepare a new release/version and corresponding deployment integrity evidence.
