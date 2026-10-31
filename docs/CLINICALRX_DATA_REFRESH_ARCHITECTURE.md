# ClinicalRx Data Refresh Architecture

**Status:** Phase 0/1 proposed implementation baseline. **Hosting:** static GitHub Pages, no private backend or user accounts.

## Requirement
Every supported source must be queried live when a user invokes a tool, or checked/refreshed automatically on a documented schedule. A source mentioned in code, CSP or documentation is not proof of end-to-end integration.

## Lifecycle
`official publisher -> discovery -> retrieval -> integrity checks -> schema validation -> domain validation -> diff/version archive -> candidate artifact -> release checks -> deployment -> visible source/freshness metadata`

Every source record carries source ID/owner/URL, retrieval timestamp, publisher release/effective date, HTTP status, checksum/ETag/Last-Modified, schema version, validation result, record count, last success/attempt, next check, license/attribution, rate limits, API-key requirements, consuming tool, and failure behavior.

A failed or unvalidated candidate must never replace last-known-good data.

## Live APIs
- RxNav: RxNorm, RxClass, RxTerms, Prescribable RxNorm, RxMix.
- DailyMed: current SPL labels and label history.
- openFDA: additional FDA indexed public data, not sole authority for clinical decisions.
- NLM Clinical Tables: terminology/code lookups.
- MedlinePlus Connect: coded-topic linkage, not a drug-monograph replacement.
- NCBI E-utilities/PubMed: literature discovery and metadata, not evidence grading by itself.

Use bounded timeouts, retries only for transient errors, exponential backoff, bounded concurrency, source-specific rate limits, response validation and TTL caching. Do not log potentially sensitive search terms.

## CMS Physician Fee Schedule
The supplied dataset IDs are distinct 2026 datasets:
- `7c7df311-5315-4f38-b9ed-fd62f8bebe11`: Indicators for 2026.
- `81f942b8-3f6c-4b36-a151-0888376d9ca0`: Localities for 2026.

Treat them as separate inputs and join only on verified fields. Discover current resources through CMS catalog metadata/API rather than hard-coding year-specific file names. The existing `scripts/rebuild-fee-reference.py` is a manual hash-pinned subset rebuild, not an automatic CMS API integration. Replace it only after exact endpoints, schemas, locality/code/modifier/facility semantics, effective dates and reconciliation are tested.

Display amounts as CMS physician fee-schedule reference amounts, never as pharmacist reimbursement or guaranteed payment. Pharmacist eligibility is independent and must be assessed by payer, billing entity, enrollment, scope, CPA, supervision, documentation, place of service, medical necessity and contract.

## FDA Purple Book
Discover the newest release month/year from the official FDA download page every run. Prefer CSV. Retain monthly change records and full snapshot, release month/year, URL, retrieval timestamp, checksum, product identifiers and supplied change category. Never hard-code the current month. If no newer release is posted, preserve the last good snapshot.

## ICD-10 lists
Discover the newest fiscal-year workbook from the official CMS index weekly. Do not hard-code an FY27 filename. Validate workbook type, sheet names, columns, code uniqueness, effective year and row counts before publishing.

## Guideline repository
Broad major-specialty coverage is the target. For each official publisher use RSS/Atom/API where available, official publication endpoints, or page change detection as a fallback. A page hash change is a detection signal, not proof of a clinically meaningful revision.

Required metadata: title, organization, specialty, publication/revision dates, first-detected date, version, official URL, previous-version link, change summary, retrieval timestamp, last successful check and validation state. Keep older guidelines searchable. The six-month banner is a derived view of verified records, newest first.

## Initial cadence
- Daily: guideline publisher feeds/pages and machine-readable safety/label announcements.
- Weekly: CMS PFS metadata/resources, CMS ICD index, Purple Book release page and source availability.
- Monthly: RxNorm full-release/bulk comparison and source catalogue review.
- On demand: live RxNav, DailyMed, openFDA, Clinical Tables, MedlinePlus and PubMed lookups.

Schedules are maximum check intervals, not promises that publishers release data that often.

## Publication gates
Require official allowlisted host, successful retrieval, expected content type, non-empty file, checksum, expected schema, plausible dates, uniqueness/referential checks, reasonable row-count change, diff report, attribution/license metadata and passing tests. Clinical/legal changes also require professional review. Never automatically publish clinical interpretations just because a source changed.

## Status vocabulary
`LIVE_QUERY`, `SCHEDULED_CHECK`, `CANDIDATE_DOWNLOADED`, `VALIDATED_CANDIDATE`, `REVIEW_REQUIRED`, `PUBLISHED`, `STALE`, `FAILED`.

## Privacy/security
No PHI in queries/logs/artifacts. No private keys in static JavaScript. Use GitHub Actions secrets only where required. GitHub Pages is static hosting; scheduled workflows can publish validated public artifacts, but cannot provide a secure private API proxy.
