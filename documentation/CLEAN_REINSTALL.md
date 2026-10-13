# Clean reinstall — ClinicalRx 0.5.1

Repository: https://github.com/nrosario07/nrosario07.github.io
Site: https://nrosario07.github.io/#clinical-tools

## What was found

On inspection, the repository contained older flattened files in its root as well as the correctly structured v0.5 site in docs/. The live index and six checked assets matched the v0.5 packet. The recording shows flattened root uploads, not the rendered website or its browser console; it does not prove the reason the pillars were missing. A cached older script is a possible cause. v0.5.1 adds cache-version URLs and a visible startup-error notice. The four-pillar hub remains implemented and tested.

Do not delete/recreate the GitHub repository. Keep the repository name and history. No clinical functionality has been newly validated by this deployment patch; existing documented limitations remain.

## Browser procedure — site replacement only

1. Download a backup first: repository → Code → Download ZIP.
2. Download ClinicalRx_0.5.1_SITE_ONLY.zip and use Windows Extract All. Open the extracted folder. It contains START_HERE.txt and one docs folder.
3. You can replace the existing docs folder for a clean site reinstall: open repository docs/ → top-right … → Delete directory → review → commit the deletion. Do not delete the repository. The site may briefly be unavailable until the replacement deploys.
4. Return to the repository ROOT (the main file list; not inside docs/). Select Add file → Upload files.
5. Drag the entire extracted docs FOLDER from File Explorer into the upload area. Do NOT select all individual files from assets, data, downloads, or documentation and upload them together. Do NOT upload the ZIP itself. Do NOT drag docs into an existing docs directory, which would create docs/docs/.
6. Review the upload paths before committing: docs/index.html; docs/assets/app.js; docs/assets/platform.js; docs/assets/advanced-platform.js; docs/assets/startup.js; docs/data/clinical-rules.json; docs/downloads/Norbert_Rosario_Public_CV.pdf. If paths are flattened, cancel the upload and retry by dragging the folder.
7. Commit message: Restore ClinicalRx 0.5.1 site with correct folders.
8. Settings → Pages → Deploy from a branch → main → /docs → Save if needed.
9. Wait for the Pages deployment workflow to finish successfully. Open https://nrosario07.github.io/?v=0.5.1#clinical-tools and press Ctrl+Shift+R. Expect four pillars: Clinical Care; Drug & Evidence Intelligence; Professional Practice; Education.
10. Check Medication Intelligence Engine, Anticoagulation Command Center, Taper & Switch, FIB-4, PREVENT handoff and Education Studio. Footer should say 0.5.1. A loading error now tells you if a required asset failed. This is a deployment smoke check, not clinical validation.

Old root-level duplicates may remain after the site-only replacement. They do not power the site when Pages serves /docs. The list below identifies them for optional cleanup; keep README.md and the structured folders. Use GitHub Desktop if you want one commit that replaces the site and removes these duplicate files.

## GitHub Desktop — one complete replacement commit

1. Install GitHub Desktop from https://desktop.github.com/download/ and sign into your own GitHub account.
2. File → Clone repository → URL → https://github.com/nrosario07/nrosario07.github.io.git → choose a local folder → Clone. Fetch/Pull the latest main branch.
3. Repository → Show in Explorer. Download and extract ClinicalRx_0.5.1_GitHub_Update.zip elsewhere.
4. In the local clone, replace the complete docs, documentation, scripts, tests and .github folders with those from the packet. Copy the packet README.md. Preserve .git and unrelated owner files. Do not copy the ZIP or preview HTML into docs.
5. Optionally remove the root-level duplicate filenames from the exact observed list below. They have correctly located counterparts in the replacement. Do not remove unrelated files by extension or use a blanket delete command. Leave the empty docs/download placeholder unless you separately choose to remove it.
6. GitHub Desktop → Changes: review additions/replacements/deletions. Paths must keep the nested structure. Summary: Restore ClinicalRx 0.5.1 and remove flattened duplicates → Commit to main → Push origin. This keeps all previous commits recoverable.
7. Pages settings remain main:/docs. Check the deployment and refresh as in browser steps8–10.

## Observed older root-level duplicates

BUILD_SPECIFICATION.md
EHR_Template_Adaptation_Guide.txt
MTP_EHR_Note_Template.txt
Norbert_Rosario_Public_CV.pdf
Norbert_Rosario_Public_CV.txt
RELEASE_0.3.1.md
RELEASE_0.3.md
RELEASE_0.4.md
app.js
check-sources.py
clinical-rules.json
clinical.js
clinical.test.js
content.js
contract.test.js
core.js
core.test.js
drug-api.js
index.html
mark.svg
module-data.js
modules.js
modules.json
modules.test.js
package.py
platform.js
public-cv.py
rebuild-clinical-references.py
registry.json
routes.test.js
rules.js
source-monitor-baseline.json
source-monitor.yml
styles.css
sync-modules.js
sync-registry.js
workflow.test.js
workspaces.js

The root files download and download (1) were also present but have no known role. Review them independently rather than treating them as site dependencies.

## What this packet does not complete

PREVENT remains an official-calculator handoff pending the AHA licensed source package. Drug interaction review is limited to duplicates and label mentions. Live prices, comprehensive therapeutic algorithms, finalized exact perioperative dose times and final clinician-approved patient orders remain outside this release. Clinical reference limits are in BUILD_SPECIFICATION.md.
