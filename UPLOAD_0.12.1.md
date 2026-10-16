# Upload 0.12.1 — focused medication recovery

Extract ClinicalRx_0.12.1_GitHub_Update.zip. Replace the repository's entire docs folder with the extracted docs folder, preserving paths. Copy the updated documentation, scripts, tests, README and root instructions as well; preserve .git and unrelated owner files. Do not upload the ZIP itself or place its contents in a new enclosing folder.

Commit: Fix medication lookup with independent FDA recovery. Push main. Keep Pages main /docs. Wait for Pages success, hard refresh and confirm 0.12.1 in the footer.

Open Medication Intelligence Engine. Enter only a public medication name such as metoprolol. Click Search FDA directly to verify the path that bypasses the failing NLM hosts. Expect label-associated RxCUI candidates and an exact-strength/form warning; choose and review the actual product label before adding to cabinet. Follow documentation/AUDIT_0.12.1.md for acceptance.

This patch intentionally leaves the reported procedure dropdown and switch display for the next focused fixes. The new patch has automated/runtime verification; post-upload browser acceptance remains open. No remote push was performed.
