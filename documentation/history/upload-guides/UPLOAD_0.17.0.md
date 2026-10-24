# Upload 0.17.0

Extract the ZIP. Upload the contents at the existing repository root, preserving docs/. Replace matching files; do not upload the ZIP itself or add an enclosing directory. Keep Pages main /docs. Commit: Add ClinicalRx source library and FDA shortage lookup (0.17.0).

## Install the missing source monitor
GitHub returned 404 for .github/workflows/source-monitor.yml on October 17, 2026. Browser uploads can omit hidden folders.

1. Choose Add file → Create new file in GitHub.
2. Enter .github/workflows/source-monitor.yml as the file name.
3. Paste the exact contents of documentation/INSTALL_SOURCE_MONITOR.yml and commit.
4. Open Actions → ClinicalRx public source review → Run workflow. Inspect the public-source-review artifact.
5. Review source changes/effective dates and approve baselines manually. The Monday 14:00 UTC schedule can be delayed by GitHub; it is monitoring, not automatic clinical publication.

After Pages deployment succeeds, hard-refresh and verify release 0.17.0. Open Clinical Tools → Evidence & education resources; test category/search/reset and FDA shortage queries. Verify product/status/date and no-match/error behavior. Mobile/browser acceptance of the new layout is still pending. No new dose or billing rules are included.
