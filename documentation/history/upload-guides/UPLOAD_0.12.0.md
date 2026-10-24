# Upload ClinicalRx 0.12.0

1. Extract ClinicalRx_0.12.0_GitHub_Update.zip. Upload the extracted contents, not the ZIP and not a new enclosing folder.
2. In your existing nrosario07.github.io checkout, replace the entire docs folder with the packet's docs folder; copy documentation, scripts, tests, .github and root release instructions, preserving their paths. Preserve the checkout's .git directory and unrelated owner files. GitHub Desktop is preferable for nested/hidden files.
3. Commit as “Fix ClinicalRx recommendation workflows and public lookup fallback”; push main. Keep Settings → Pages → Deploy from a branch → main → /docs. Do not change to a root deployment.
4. Wait for Pages deployment success. Open https://nrosario07.github.io/ and hard refresh; confirm version 0.12.0. Follow documentation/AUDIT_0.12.0.md acceptance steps before relying on the new tools.

The repository root must contain docs/index.html; scripts remain in docs/assets and data in docs/data. Do not upload private source CPA/CV files, patient information or credentials. The new release has automated verification, not deployed-browser acceptance. No remote changes have been made for you in this run.
