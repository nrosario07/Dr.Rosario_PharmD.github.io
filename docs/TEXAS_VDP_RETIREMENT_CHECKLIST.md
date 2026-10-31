# Texas Vendor Drug Program Retirement Checklist

Texas VDP drug-data ingestion and Texas Medicaid drug coverage/formulary/pricing datasets are assigned to MedCoverageIQ and must not remain in ClinicalRx runtime or scheduled workflows.

## Remove after dependency checks
- `.github/workflows/texas-data.yml`
- `scripts/fetch-texas-vdp.py`
- `tests/test_texas_data.py`
- `documentation/INSTALL_TEXAS_DATA.yml`
- `documentation/TEXAS_DATA_INTEGRATION.md`
- `documentation/texas-vdp-sources.json`
- dependent Texas VDP/Medicaid drug datasets and consumers

## Preserve
- `docs/downloads/Texas_CPA_Authority.md`
- `docs/downloads/Texas_Pharmacist_Code_Pathways.csv`
- `docs/downloads/Texas_Pharmacist_Code_Pathways.md`
- `documentation/TEXAS_CODE_PATHWAYS_0.9.0.md`
- `documentation/TEXAS_CPA_LAWS_0.9.0.md`
- `docs/assets/fee-reference.js` and CMS fee-reference tooling

Search imports, fetch URLs, CSP, navigation, tests, docs, release manifests and workflows before deleting. Preserve historical audit records and mark retired items superseded.
