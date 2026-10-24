# Upload ClinicalRx 0.21.0

1. Extract `ClinicalRx_0.21.0_Upload_Batches.zip`.
2. Open `01_SITE`. Upload its **contents** to the repository root in one commit. Keep `docs/` intact.
3. Upload each support batch's contents separately; each has at most 90 files.
4. Do not upload the ZIP, numbered folders, `START_HERE.txt`, or packet `SHA256SUMS.json`.
5. Keep Pages configured to `main` / `docs`. Wait for the Pages deployment, then confirm release 0.21.0.
6. Follow `documentation/SOURCE_MONITOR_SETUP.md` to install and verify the two workflows if still absent.

## Optional root cleanup after upload

Historical upload instructions are now preserved under `documentation/history/upload-guides/`. After the support batches succeed, remove their old root copies listed in `documentation/REPOSITORY_CLEANUP.md`. Uploading a packet does not remove these obsolete remote paths. Do not delete application folders or source data.

The mistakenly uploaded root `START_HERE.txt` and `SHA256SUMS.json` are packaging instructions/inventory, not application dependencies. They may be removed after the current upload succeeds. This packet does not silently delete remote files. No mass repository deletion is needed.

## Acceptance

Verify release 0.21.0. Open Taper & Switch: no target options until a current product is chosen; select carvedilol IR or glipizide IR and check only the correct target appears. Exercise missing review, unsupported dose and risk exclusions. Use fictional cases. New recommendations require independent clinical review; source availability and clinical approval are not inferred from software tests. See CORE_ACCEPTANCE_PLAN.md for the original 13 tracks.
