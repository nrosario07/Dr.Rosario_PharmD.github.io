# ClinicalRx 0.18.2 — workflow integrity and release governance

Date: October 21, 2026 (America/Chicago).

## Verified deployment
GitHub and the deployed footer report 0.18.1. The remote manifest matches all 40 hashes in the previously packaged local manifest. Individual remote files were not independently rehashed.

## Reproduced issue and fix
After syncing a fictional metformin regimen, editing it left the cabinet's synced message unchanged. SOAP retained the old regimen. New code compares the current cabinet with the linked snapshot and the reconciliation block, shows stale status on cabinet and SOAP, and blocks download/copy/print through the shared export controls for connected clinical workspaces until the cabinet is re-synced. Existing clinical prose outside the cabinet block is preserved. This does not synchronize treatment decisions or turn a medication list into patient instructions.

## Next phase increment: 09 governance
Added a read-only release-check workflow (bundle integrity, JS regressions, Python governance tests), a human-readable source review summary, and explicit per-source baseline approval with reviewer/rationale. No automatic clinical recommendations, doses or baseline approvals. The source-monitor workflow remains absent remotely; workflow installation and first successful hosted run remain blocked on repository setup. The test workflow does not automatically gate the separate Pages deployment.

## Browser-tested on deployed 0.18.1
- RxNorm metformin lookup: 134 identities; filter “500 oral”: 51 results.
- RxCUI 861007 remains selected when filtering for 1000.
- Selected Ascend FDA label, added/reconciled fictional cabinet, synced and used direct SOAP link.
- Reproduced stale synced status after regimen edit; re-sync placed corrected regimen in SOAP.
- Generated fictional patient plan, confirmed review/no-PHI gate, downloaded actual text and inspected it. File matches displayed plan and excludes RxCUI/internal coding text.

## Automated verification
349 JavaScript regression tests passed, including stale-cabinet export refusal and recovery after re-sync. Five Python governance tests passed, including refusal of unavailable/bad-hash sources and preservation of unrelated baseline entries. Final manifest and ZIP integrity results accompany packaging.

## Still unverified
New 0.18.2 browser behavior after upload; mobile/keyboard regression; broad drug and clinical coverage; hosted workflow execution; first reviewed monitoring baseline. No new clinical algorithm or dosing equivalence was released.

## Progress
Initial capability: 11/13 phase tracks. Full acceptance: 0/13. Phase02 connected workflows now has a completed desktop export checkpoint; Phase09 adds tested maintainer tooling. Entire phase completion still requires its broader acceptance criteria. Next: deploy/test this fix, install/run workflows, complete responsive regression, then normalized evidence and exact-product switch expansion.
