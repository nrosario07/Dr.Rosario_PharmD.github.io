# clinicalrx-rxnav

Small Python client for NLM RxNav endpoints. It is an integration adapter, not a clinical recommendation engine.

Install: `python -m pip install .`

CLI examples:
```
rxnav name ibuprofen
rxnav drug 5640
rxnav related 5640 --tty SCD
rxnav class 5640
rxnav rxterms 5640
```

Python:
```python
from clinicalrx_rxnav import RxNavClient
client = RxNavClient()
print(client.find_rxcui("ibuprofen"))
```

Features: explicit connect/read timeouts, bounded retries for transient failures/429, exponential backoff, Python logging, optional in-memory TTL cache, optional UMLS bearer token from `RXNAV_UTS_API_KEY`. API response dictionaries still require caller-side schema validation.

NLM attribution requested by RxNav: “This product uses publicly available data from the U.S. National Library of Medicine (NLM), National Institutes of Health, Department of Health and Human Services; NLM is not responsible for the product and does not endorse or recommend this or any other product.” Review current API terms/rate limits before production use.
