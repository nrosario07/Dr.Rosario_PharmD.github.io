# Upload 0.18.0

Extract the ZIP and upload contents at the existing repository root, preserving docs/. Replace matching files; do not upload the ZIP itself. Keep Pages main /docs. Verify footer0.18.0 after successful deployment.

Open Clinical Tools → Build progress & sources. Verify 11/13 initial implementation, 0/13 full acceptance, all13 track descriptions and the monitoring blocker. Check keyboard and narrow-screen layout.

Source monitoring is still missing. Create .github/workflows/source-monitor.yml using the exact contents of documentation/INSTALL_SOURCE_MONITOR.yml. Then Actions → ClinicalRx public source review → Run workflow; inspect its report. See UPLOAD_0.17.0.md for details. A workflow file in documentation/ alone does not install scheduled monitoring.
