# Upload ClinicalRx 0.18.2

1. Extract the ZIP and upload its contents to the repository root. Preserve docs/, documentation/, scripts/, tests/. Do not nest another folder or upload the ZIP itself.
2. Keep GitHub Pages main → /docs. Confirm footer 0.18.2 after deployment.
3. Follow documentation/SOURCE_MONITOR_SETUP.md to create both .github/workflows files if folder upload omitted them. Visible copies are supplied in documentation. This installation is needed for automated checks.
4. Test with fictional data: add medication, sync cabinet, edit regimen, verify stale warning, visit SOAP and confirm export refusal, re-sync, review the plan and verify export succeeds after no-PHI review.
5. Existing clinical content and four pillars remain. No dosing rules changed. New browser/hosted workflow acceptance is pending.
