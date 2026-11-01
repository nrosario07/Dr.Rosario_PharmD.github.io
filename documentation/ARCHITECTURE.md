# Architecture

## Hosting
GitHub Pages serves the `docs/` directory. The site is a static browser application. No application server is required for the baseline.

## Layers
- `docs/index.html`: semantic shell and security policy.
- `docs/assets/`: browser code, styles and public content.
- `docs/data/`: public, versioned source registry and later validated snapshots.
- `documentation/`: scope, governance and implementation decisions.
- `scripts/`: validation and future deterministic ingestion tools.
- `tests/`: regression and privacy-boundary tests.
- `.github/workflows/`: validation and Pages deployment.

## Separation of concerns
Drug Intelligence is a public drug-reference workflow. Medication Review/Reconciliation is a separate clinical-case workflow. A future integration may pass a selected, verified drug concept into a case only through an explicit user action; case details must never be sent to the drug source.

## Data states
1. Source reference: a link only.
2. Live API call: an explicit runtime request with documented payload.
3. Published snapshot: locally hosted data with provenance, license, retrieval date, schema validation, checksum and human approval.

Monitoring a source is not the same as refreshing or publishing its data.

## Security
- No secrets in frontend code.
- No accounts or PHI.
- No automatic draft persistence.
- CSP allowlist must be updated only when a new integration is reviewed.
- External links use `rel="noopener noreferrer"`.
- Clinical output requires clear review and limitations.
