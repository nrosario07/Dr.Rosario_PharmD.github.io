# Upload ClinicalRx0.14.2

1. Fully extract ClinicalRx_0.14.2_GitHub_Update.zip. Do not upload the ZIP itself.
2. In the repository root, replace the complete docs folder with the extracted docs folder, preserving its assets/data/downloads subfolders. Copy documentation, scripts, tests and root instructions alongside it. Do not add an enclosing ClinicalRx folder. Preserve .git and unrelated owner files.
3. Commit: Update ClinicalRx to 0.14.2 — workflow reliability and usability.
4. Keep GitHub Pages configured for main /docs. Wait for deployment success, then hard-refresh and confirm footer0.14.2.
5. Follow documentation/AUDIT_0.14.2.md. Specifically test the blocked CSV path, then reviewed export; use the app links for medication → cabinet → SOAP → patient plan. New UI requires deployed browser acceptance; automated tests do not establish this.

Direct publishing was blocked by GitHub integration permissions. This package has not been deployed by the assistant. Never delete the repository to upload a release.
