# ClinicalRx v0.7.0 — local continuity and workflow corrections

2026-10-13. Adds explicit local draft download/preview/restore, with bounded validation and fresh review requirements. Corrects stale medication-label display, repeat cabinet additions, missing cabinet date provenance and impossible external-result dates. Improves worksheet reference navigation and hub labels. Preserves four pillars, free access, external calculator policy, LinkedIn-only contact and local clinical data handling.

137 automated tests pass. Deployed v0.6.1 was browser-tested; new v0.7.0 browser acceptance remains pending upload. See AUDIT_0.7.0.md for precise coverage and limits. No new clinical dose algorithms or payer eligibility claims were added. Imported files are unencrypted drafts, not authenticated records or signatures.

Upload the extracted docs folder at repository root, preserving nested paths and replacing matching files. Do not upload the ZIP itself or patient drafts. Pages remains main:/docs. No repository deletion needed. Install documentation/scripts/tests/.github through a local clone/GitHub Desktop to preserve the complete reproducible source packet.
