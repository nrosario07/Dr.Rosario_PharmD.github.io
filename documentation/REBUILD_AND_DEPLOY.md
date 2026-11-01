# Rebuild and Deploy Instructions

## Before deleting the old repository
1. Download an archive of the existing repository (`Code` → `Download ZIP`) and keep it outside GitHub.
2. Save a copy of any public CV PDF, approved downloads and source datasets that are not safely reproducible.
3. Keep the archive until the rebuilt site passes acceptance.
4. Deleting a GitHub repository is destructive. Confirm the exact repository name and owner before deletion.

## Create the clean repository
1. Extract this ZIP locally.
2. Open the extracted `ClinicalRx_Clean_Rebuild_Kit` folder.
3. Create a new empty repository named `nrosario07.github.io` under `nrosario07`, or recreate it after deletion.
4. Do not initialize the remote repository with another README or license.
5. From the extracted folder, run:

   ```bash
   git init
   git add .
   git commit -m "Initialize ClinicalRx clean rebuild"
   git branch -M main
   git remote add origin https://github.com/nrosario07/nrosario07.github.io.git
   git push -u origin main
   ```

## Configure GitHub Pages
Preferred: GitHub Actions deployment.
1. Open repository Settings → Pages.
2. Under Build and deployment, choose **GitHub Actions**.
3. Ensure Actions are enabled.
4. Push to `main`; the validation and deployment workflows should run.
5. Open Actions and verify both workflows pass.
6. Confirm the deployed site at `https://nrosario07.github.io/`.

Do not select a `/docs` branch-source configuration while using the included Actions deployment workflow. Choose one deployment method, not both.

## First acceptance checks
- [ ] `node --test tests/*.test.js` passes locally.
- [ ] `python scripts/validate-site.py` passes.
- [ ] GitHub Actions validation passes.
- [ ] Pages deployment passes.
- [ ] Desktop and mobile navigation work.
- [ ] Keyboard-only navigation and visible focus work.
- [ ] No PHI collection, analytics, accounts or automatic persistence.
- [ ] Drug Intelligence and Medication Review remain separate.
- [ ] Public CV and profile facts have been reviewed and approved.
- [ ] All links/downloads resolve.
- [ ] No VDP/formulary/pricing pipeline remains.
- [ ] Source and clinical/legal/coding review limitations are visible.

## Rollback
The old ZIP archive is the recovery point. Do not delete it until the new deployment and content migration are accepted.
