# Upload ClinicalRx 0.25.0

1. Extract `ClinicalRx_0.25.0_Upload_Batches.zip`.
2. Open `01_SITE`. Upload its **contents** to the repository root in one commit. Keep `docs/` intact.
3. Upload each support batch's contents separately; each has at most 90 files.
4. Do not upload the ZIP, numbered folders, `START_HERE.txt`, or packet `SHA256SUMS.json`.
5. Keep Pages configured to `main` / `docs`. Wait for the Pages deployment, then confirm release 0.25.0.
6. Follow `documentation/SOURCE_MONITOR_SETUP.md` to install and verify the source-monitor, release-check and Texas retrieval workflows if still absent.

## Optional root cleanup after upload

Historical upload instructions are now preserved under `documentation/history/upload-guides/`. After the support batches succeed, remove their old root copies listed in `documentation/REPOSITORY_CLEANUP.md`. Uploading a packet does not remove these obsolete remote paths. Do not delete application folders or source data.

The mistakenly uploaded root `START_HERE.txt` and `SHA256SUMS.json` are packaging instructions/inventory, not application dependencies. They may be removed after the current upload succeeds. This packet does not silently delete remote files. No mass repository deletion is needed.

## Acceptance
Confirm 0.25.0 in the footer. Open the calculator directory: filter Mental health, search PHQ, clear filters and test an unmatched query. Open the two data-guide links from pillar 02. Review the current checklist and AUDIT_0.25.0.md.

## Required workflow installation
The three workflow paths remain absent. Direct creation was rejected with GitHub 403: Resource not accessible by integration. Uploading documentation YAML copies does not install workflows. Use Add file → Create new file to create each exact path below with its supplied copy, then commit:

| Destination | Copy content from |
|---|---|
| .github/workflows/release-check.yml | documentation/INSTALL_RELEASE_CHECK.yml |
| .github/workflows/source-monitor.yml | documentation/INSTALL_SOURCE_MONITOR.yml |
| .github/workflows/texas-data.yml | documentation/INSTALL_TEXAS_DATA.yml |

Run each from Actions and inspect its report. Texas access/schema failures are review outcomes, not valid price data. No automatic clinical-rule publication is enabled.
