# Install source monitoring and release checks

Rechecked October 25, 2026. The source-monitor workflow path returned 404 remotely. Neither workflow was installed by this release-building session. No clinical updates are published automatically.

1. In GitHub, at repository root choose Add file → Create new file.
2. Name it `.github/workflows/source-monitor.yml`. Paste the exact contents of `documentation/INSTALL_SOURCE_MONITOR.yml`. Commit.
3. Repeat for `.github/workflows/release-check.yml` using `documentation/INSTALL_RELEASE_CHECK.yml`.
4. Under Actions choose **ClinicalRx release checks** → Run workflow. Inspect the integrity, application and governance test results. This workflow does not automatically block the separately configured Pages deployment.
5. Choose **ClinicalRx public source review** → Run workflow. Inspect its summary and download the `public-source-review` artifact. Scheduled checks run Mondays at 14:00 UTC (9 a.m. Central daylight time / 8 a.m. Central standard time); runs may be delayed.

Browser folder uploads may omit `.github`. A YAML copy under documentation is instructional only. GitHub executes workflows under `.github/workflows`.

## Interpret source status

- BASELINE_NEEDED: first successful observation, without a reviewed earlier fingerprint.
- CONTENT_CHANGED_REVIEW: changed bytes may be cosmetic. Review controlling text, publication/effective dates, proposal/final/withdrawal status, affected modules and tests needed.
- UNAVAILABLE_REVIEW: source could not be read. Inspect it manually; never approve an error response.
- TOO_LARGE_USE_SOURCE: response exceeds the download cap; inspect manually.
- UNCHANGED: same checked bytes, not proof of clinical currency.

The maintained URL set is not comprehensive discovery of every new guideline, safety notice or label change.

## Approve selected baseline entries manually

After inspecting a successful source response, from the repository root run:

```bash
python scripts/review-source-baseline.py --report source-monitor-report.json --url 'https://example.org/replace-with-actual-source' --reviewer 'Reviewer name or role' --rationale 'Publication/effective dates, materiality, affected modules and review/tests needed.'
```

Replace the example URL with the exact report URL. Repeat --url only when the same rationale applies. The script rejects unavailable responses and bad hashes, preserves other baseline entries and records reviewer/rationale. Inspect the resulting `documentation/source-monitor-baseline.json` diff before committing. It updates fingerprints only, not clinical rules. No baseline was approved automatically in this release. Future clinical revisions require separate source review and a tested release.

## Primary implementation references

GitHub. Workflow syntax for GitHub Actions. Accessed October 21, 2026. https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax

GitHub. Workflow commands for GitHub Actions: adding a job summary. Accessed October 21, 2026. https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
