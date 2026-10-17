# Audit 0.16.0 — October 17, 2026

## Evidence and scope
- Browser visual inspection: deployed Clinical Tools hub reports 0.15.0; four pillars present. Reference provider page inspected for spacing, typography and navigation only. No reference branding/content incorporated.
- Repository check: GitHub docs/data/release-manifest.json equals the prior local 0.15.0 manifest (all recorded hashes). This is manifest parity, not a byte-by-byte download of every deployed asset.
- Verified usability issues: tool search below all pillars searched modules only; no no-match feedback; placeholder advertised the removed diabetes module; large link-pill groups and expanded module list added scanning burden.
- Repairs: local unified finder above content, pillar selector, live counts, reset, no-match state, compact row links, condition-module disclosure, responsive result grid and explicit focus styles.

## Validation distinction
340 Node tests pass, including finder alias, module, pillar, reset, empty-state and injection tests. These use an event-capable DOM harness; they do not verify rendered geometry. Static manifest validation and ZIP CRC/extraction verification are recorded in the delivery process.

No new clinical rules, evidence claims, API calls, storage or contact details were introduced. Live browser inspection covers the prior hub, not new 0.16.0 controls. No claim of a complete all-page audit or full medication-to-SOAP workflow test is made this release.

## Outstanding acceptance
New desktop/mobile/keyboard layout and finder require deployed browser acceptance. Full 0.15 switching acceptance, public API resilience, cabinet-to-SOAP-to-plan regression and independent clinical/coding review remain pending. The Sites environment does not provide a local browser preview here; no substitute preview server was started. Existing GitHub integration write permission remains a known limitation from the prior 403; no new write attempt or deployment was made.
