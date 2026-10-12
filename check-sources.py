"""Maintainer-only public source change queue. Never changes clinical rules.

Compares public-source hashes/response metadata. Changed bytes can be cosmetic;
review primary content/effective dates before updating a clinical recommendation.
No patient data, private uploads or credentials are read. Run from repository root.
"""
from pathlib import Path
import datetime
import hashlib
import json
import urllib.request
from urllib.parse import urlparse

root = Path(__file__).resolve().parent.parent
registry = json.loads((root / 'docs/data/modules.json').read_text())
urls = {x['url'] for x in registry['modules']}
urls.update(x['url'] for x in json.loads((root / 'docs/data/registry.json').read_text())['sources']
            if x['url'].startswith(('https://www.cms.gov/', 'https://www.pharmacy.texas.gov/', 'https://www.tmhp.com/')))
urls.update(['https://open.fda.gov/apis/drug/label/',
             'https://rxnav.nlm.nih.gov/REST/version.json',
             'https://www.cms.gov/medicare/health-drug-plans/part-c-d-performance-data'])
baseline_path = root / 'documentation/source-monitor-baseline.json'
baseline = json.loads(baseline_path.read_text()) if baseline_path.exists() else {}
report = {'checked': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'mode': 'Review queue only; no clinical rule updates', 'sources': []}
for url in sorted(urls):
    if urlparse(url).scheme != 'https':
        continue
    row = {'url': url}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'ClinicalRx-public-source-review/0.4'})
        with urllib.request.urlopen(request, timeout=15) as response:
            body = response.read(4_000_001)
            if len(body) > 4_000_000:
                row['status'] = 'TOO_LARGE_USE_SOURCE'
            else:
                digest = hashlib.sha256(body).hexdigest()
                row.update(status='BASELINE_NEEDED' if url not in baseline else
                           'CONTENT_CHANGED_REVIEW' if baseline[url].get('sha256') != digest else 'UNCHANGED',
                           sha256=digest, etag=response.headers.get('ETag'),
                           lastModified=response.headers.get('Last-Modified'),
                           finalURL=response.url)
    except Exception as error:
        row.update(status='UNAVAILABLE_REVIEW', error=str(error)[:200])
    report['sources'].append(row)
Path('source-monitor-report.json').write_text(json.dumps(report, indent=2) + '\n')
print('Source report written; establish/review baseline manually. No clinical bundle changed.')
