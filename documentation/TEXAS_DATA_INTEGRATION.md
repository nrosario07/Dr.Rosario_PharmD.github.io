# Texas VDP integration — 0.24.0

Checked October 25, 2026. This release prepares retrieval; it does not publish Texas prices or coverage data.

## Source and access status

Official index: https://www.txvendordrug.com/resources/data-files

Nine user-supplied URLs and purposes are recorded in texas-vdp-sources.json. The index, sampled official layouts and formulary drug download returned HTTP 403 from the audit environment. This does not establish that the site is unavailable to everyone. Monday publication timing is user-reported, not independently verified.

Texas-reported 340B fields must be distinguished from HRSA ceiling prices. Current field definitions, effective dates, missing-value conventions and price units have not been verified. Do not substitute a percentage discount, zero, NADAC or ASP for missing values.

## Install the weekly retrieval workflow

1. In GitHub, select Add file → Create new file.
2. Name the file `.github/workflows/texas-data.yml` and paste the contents of `documentation/INSTALL_TEXAS_DATA.yml`. If the exact workflow already exists, update it instead.
3. Commit to the default branch. Open Actions → ClinicalRx Texas public data retrieval → Run workflow.
4. Inspect the run and download its `texas-vdp-review` artifact. A failed run is not a valid dataset. The JSON report records access failures and download hashes; schemaVerified remains false.
5. Scheduling is Monday 18:17 UTC (13:17 CDT / 12:17 CST). GitHub scheduling may be delayed. Artifact retention is 14 days; this is not permanent archival storage.

This workflow needs only read permission and uses no patient data or credentials. It does not write to the website. After a 401, 403 or 429 it stops remaining requests to the same origin. Empty/HTML/unsafe ZIP payloads are rejected. Downloaded text and Excel containers still require field-level verification. Existing published files are untouched on failure.

## Gates before unattended site refresh

- Obtain current official drug and CAD downloads plus their official layouts; user-provided copies can unblock initial schema review.
- Verify delimiter/encoding, identifiers, leading zeros, price units, dates, sentinels, duplicate rules and source-defined field meanings.
- Build normalized records and realistic fixtures; distinguish formulary listing from coverage and HCPCS mapping from eligibility.
- Validate joins and material row-count/schema changes; retain reviewed last-good data and explicit stale labels.
- Review the first resulting product displays before enabling automatic publication. Routine validated data refreshes can then be automated; clinical recommendations remain separately reviewed.

No bypass of source access controls is attempted. Current blockers are source access, schema verification and initial normalized-data acceptance.
