# Upload ClinicalRx 0.19.0

1. Extract the ZIP and upload its contents at the repository root, preserving docs/, documentation/, scripts/, tests/. Do not nest another top-level folder or upload the ZIP itself.
2. Keep Pages main → /docs. Verify footer 0.19.0 after deployment.
3. In CMM/MTP load a fictional case, review the agreed plan and check the no-PHI confirmation. Select Download printable patient handout. Open the downloaded HTML; use the browser Print menu to print or Save as PDF. Review all instructions before using any output.
4. Test that editing the plan revokes review and that a changed, previously synced cabinet blocks export until re-sync/review.
5. Follow documentation/SOURCE_MONITOR_SETUP.md to create .github/workflows/source-monitor.yml and .github/workflows/release-check.yml. BOTH were missing on this audit; visible YAML copies under documentation are not executable workflows.
6. Test a narrow-screen device and keyboard navigation, including Escape from the mobile menu. These changes have automated/source checks but not deployed browser acceptance yet.
