# Upload ClinicalRx 0.24.0

1. Extract `ClinicalRx_0.24.0_Upload_Batches.zip`.
2. Open `01_SITE`. Upload its **contents** to the repository root in one commit. Keep `docs/` intact.
3. Upload each support batch's contents separately; each has at most 90 files.
4. Do not upload the ZIP, numbered folders, `START_HERE.txt`, or packet `SHA256SUMS.json`.
5. Keep Pages configured to `main` / `docs`. Wait for the Pages deployment, then confirm release 0.24.0.
6. Follow `documentation/SOURCE_MONITOR_SETUP.md` to install and verify the source-monitor, release-check and Texas retrieval workflows if still absent.

## Optional root cleanup after upload

Historical upload instructions are now preserved under `documentation/history/upload-guides/`. After the support batches succeed, remove their old root copies listed in `documentation/REPOSITORY_CLEANUP.md`. Uploading a packet does not remove these obsolete remote paths. Do not delete application folders or source data.

The mistakenly uploaded root `START_HERE.txt` and `SHA256SUMS.json` are packaging instructions/inventory, not application dependencies. They may be removed after the current upload succeeds. This packet does not silently delete remote files. No mass repository deletion is needed.

## Acceptance
Confirm 0.24.0 in the footer. Open the Texas drug data sources card from Clinical Tools or the medication data guide. Nine sources should appear; search 340B should show the formulary drug source. No live prices should appear. Install the Texas retrieval workflow as described in documentation/TEXAS_DATA_INTEGRATION.md. Its hosted execution and current data schemas still require verification.
