# Privacy, Safety and Clinical Limits

- ClinicalRx is a public educational resource, not an EHR or clinical record system.
- Never enter PHI, patient identifiers, dates of birth, member IDs, or confidential records.
- No account, analytics, remote draft storage, or automatic browser persistence.
- Clinical drafts must remain in tab memory only. Do not introduce localStorage, sessionStorage, IndexedDB, cookies, or service-worker caching of user input.
- Do not transmit medication lists, clinical notes, SOAP drafts or encounter details to external APIs.
- If public drug lookup is enabled, transmit only the explicit drug term or identifier required for that lookup and disclose this before use.
- All clinical outputs require professional verification against current sources, patient-specific facts and local policy.
- CPA authority, institutional privileges, credentialing, payer participation, code eligibility and payment are distinct determinations.
- Nutrition or wellness content must remain educational unless independently reviewed and authorized for a different scope.
