# ClinicalRx Phase 0 / Phase 1 Refresh Package

These are reviewable starter files for `nrosario07/nrosario07.github.io`.

**Not pushed:** GitHub branch creation was rejected by the connected integration with HTTP 403. No repository files were changed.

## Upload order
1. Add `docs/CLINICALRX_DATA_REFRESH_ARCHITECTURE.md`.
2. Add `docs/data/source-registry.json`.
3. Add `clinicalrx-rxnav/` as a standalone pip-installable client.
4. Add `.github/workflows/clinicalrx-source-refresh.yml` and `scripts/clinicalrx_source_monitor.py`.
5. Add guideline and Texas retirement documentation.
6. Review dependencies before deleting any existing Texas VDP files.

The source monitor in this package is deliberately a check/report stage, not a data publisher. Add source-specific download, schema, semantic, diff and publish jobs only after testing official formats. Never publish an unvalidated candidate or overwrite last-known-good data.

No PHI belongs in GitHub workflows, logs, artifacts or issues. Do not put secrets in browser JavaScript or static files.
