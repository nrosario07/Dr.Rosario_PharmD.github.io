"""Check public package integrity. No clinical inputs or network requests."""
from pathlib import Path
import hashlib,json,re,sys
root=Path(__file__).resolve().parent.parent
site=root/'docs'; manifest=site/'data/release-manifest.json'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
html=(site/'index.html').read_text()
assets=re.findall(r'(?:src|href)="(assets/[^"?]+)\?v=([^"?]+)"',html)
versions={v for _,v in assets}
assert len(versions)==1, 'Mixed entry-page asset versions'
assert assets and all((site/f).is_file() for f,_ in assets), 'Missing loaded asset'
assert 'local-draft.js' not in html, 'Retired persistence module loaded'
assert not re.search(r'<script[^>]+src="https?://',html), 'Unexpected external script'
version=next(iter(versions))
assert f'name="clinicalrx-release" content="{version}"' in html, 'HTML release metadata mismatch'
assert f"const releaseVersion='{version}'" in (site/'assets/app.js').read_text(), 'Application release version mismatch'
paths=sorted(str(p.relative_to(site)) for p in site.rglob('*') if p.is_file() and p!=manifest and not any(part.startswith('.') for part in p.relative_to(site).parts))
current={p:digest(site/p) for p in paths}
if '--write' in sys.argv:
 manifest.write_text(json.dumps({'version':version,'sha256':current},indent=2)+'\n')
else:
 saved=json.loads(manifest.read_text());assert saved['version']==version,'Manifest version mismatch';assert saved['sha256']==current,'Manifest mismatch: missing or changed public asset'
print(f'PASS: release {version}, {len(assets)} loaded assets, {len(current)} public-file hashes; no external scripts or retired persistence loader.')
