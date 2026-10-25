# Upload ClinicalRx 0.23.0

1. Extract `ClinicalRx_0.23.0_Upload_Batches.zip`.
2. Open `01_SITE`. Upload its **contents** to the repository root in one commit. Keep `docs/` intact.
3. Upload each support batch's contents separately; each has at most 90 files.
4. Do not upload the ZIP, numbered folders, `START_HERE.txt`, or packet `SHA256SUMS.json`.
5. Keep Pages configured to `main` / `docs`. Wait for the Pages deployment, then confirm release 0.23.0.
6. Follow `documentation/SOURCE_MONITOR_SETUP.md` to install and verify the two workflows if still absent.

## Optional root cleanup after upload

Historical upload instructions are now preserved under `documentation/history/upload-guides/`. After the support batches succeed, remove their old root copies listed in `documentation/REPOSITORY_CLEANUP.md`. Uploading a packet does not remove these obsolete remote paths. Do not delete application folders or source data.

The mistakenly uploaded root `START_HERE.txt` and `SHA256SUMS.json` are packaging instructions/inventory, not application dependencies. They may be removed after the current upload succeeds. This packet does not silently delete remote files. No mass repository deletion is needed.

## Acceptance
Confirm0.23.0 in the footer. Biosimilars should show12 rows with next/previous controls. Search Ahzantive, then select interchangeable: no results. Reset and filter reference/marketing status. Check keyboard controls and narrow-screen presentation labels. Repeat medication→cabinet→SOAP→patient-plan with fictional data. See AUDIT_0.23.0.md for the completed checks and limits.

## Continuous monitoring still needs installation
Both .github/workflows files returned404 on October25. Follow documentation/SOURCE_MONITOR_SETUP.md to create the two workflow files explicitly, run them in Actions and inspect the results. Uploading the instructional YAML under documentation does not activate monitoring.
