"""Create a portable preview and source ZIP. No private uploads are included."""
from pathlib import Path
import base64
import re
import zipfile
import subprocess
import sys
import json
root=Path(__file__).resolve().parent.parent
out=root.parent/'output'
out.mkdir(exist_ok=True)
site=root/'docs'
version=json.loads((site/'data/release-manifest.json').read_text())['version']
subprocess.run([sys.executable,str(root/'scripts/validate-site.py')],check=True)
html=(site/'index.html').read_text()
html=html.replace("script-src 'self'", "script-src 'self' 'unsafe-inline'").replace("style-src 'self'", "style-src 'self' 'unsafe-inline'")
html=html.replace(f'<link rel="stylesheet" href="assets/styles.css?v={version}">','<style>'+ (site/'assets/styles.css').read_text()+'</style>')
icon='data:image/svg+xml;base64,'+base64.b64encode((site/'assets/mark.svg').read_bytes()).decode()
html=html.replace(f'assets/mark.svg?v={version}',icon)
rules_uri='data:application/json;base64,'+base64.b64encode((site/'data/clinical-rules.json').read_bytes()).decode()
html=html.replace('data/clinical-rules.json',rules_uri)
for name in ['startup.js','content.js','mtp-taxonomy.js','core.js','rules.js','clinical.js','module-data.js','modules.js','drug-api.js','icd-index.js','advanced.js','medication-sections.js','advanced-platform.js','next-phase.js','next-platform.js','calculator-links.js','reporting.js','clinical-support.js','purple-data.js','support-platform.js','platform.js','encounter-review.js','fee-reference.js','cpa-workspace.js','lai-switch.js','decision-support.js','decision-workspaces.js','cpa-template.js','cpa-builder.js','workspaces.js','app.js']:
    js=(site/'assets'/name).read_text()
    for item in (site/'downloads').iterdir():
        mime='application/pdf' if item.suffix=='.pdf' else 'text/plain;charset=utf-8'
        uri='data:'+mime+';base64,'+base64.b64encode(item.read_bytes()).decode()
        js=js.replace('data/clinical-rules.json',rules_uri)
        js=js.replace('downloads/'+item.name,uri)
        html=html.replace('downloads/'+item.name,uri)
    html=html.replace(f'<script defer src="assets/{name}?v={version}"></script>','<script defer>'+js.replace('</script','<\\/script')+'</script>')
# Inline classic scripts must execute after the DOM: defer applies only to external scripts.
scripts=re.findall(r'<script defer>.*?</script>',html,re.S)
html=re.sub(r'<script defer>.*?</script>','',html,flags=re.S)
html=html.replace('</body>','\n'+ '\n'.join(s.replace('<script defer>','<script>') for s in scripts)+'\n</body>')
(out/f'ClinicalRx_{version}_Preview.html').write_text(html)
(out/f'ClinicalRx_{version}_Build_Specification.md').write_text((root/'documentation/BUILD_SPECIFICATION.md').read_text())
archive=out/f'ClinicalRx_{version}_GitHub_Update.zip'
staging=archive.with_suffix('.zip.part')
with zipfile.ZipFile(staging,'w',zipfile.ZIP_DEFLATED) as z:
    for item in sorted(root.rglob('*')):
        if item.is_file() and '.git' not in item.parts and '__pycache__' not in item.parts and item.name != 'source-monitor-report.json' and item.suffix != '.pyc' and not any(part.startswith('.') and part not in ('.github','.nojekyll','.gitignore') for part in item.relative_to(root).parts):
            z.write(item,str(item.relative_to(root)))
with zipfile.ZipFile(staging) as verified:
    bad=verified.testzip()
    if bad: raise RuntimeError('Archive integrity failure: '+bad)
    if 'docs/index.html' not in verified.namelist(): raise RuntimeError('Missing site entrypoint')
staging.replace(archive)
print('Preview, specification and verified source ZIP created.')


# Browser upload packet: one complete site batch, supporting files in <=90-file batches.
from upload_batches import make_batches
files=[p for p in sorted(root.rglob('*')) if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts and p.name!='source-monitor-report.json' and p.suffix!='.pyc' and not any(part.startswith('.') and part not in ('.github','.nojekyll','.gitignore') for part in p.relative_to(root).parts)]
batches=make_batches([p.relative_to(root).as_posix() for p in files])
packet=out/f'ClinicalRx_{version}_Upload_Batches.zip'
counts={name:len(paths) for name,paths in batches.items()}
instructions=f"""ClinicalRx {version} — browser upload packet
Extract this ZIP first. Do NOT upload this ZIP or the numbered wrapper folders.
For each numbered batch, open it and upload its CONTENTS at the GitHub repository ROOT.
Keep folder paths intact: docs stays docs, documentation stays documentation, tests stays tests.
Commit each batch separately. Each batch is below GitHub's 100-file limit.
Upload the complete site batch first; it includes all site assets in one commit.
Do not delete the existing repository. Existing files with matching paths are replaced.
Pages remains main /docs. Wait for deployment before checking the new version.
Hidden .github files may not appear in your file picker: create the two workflow files manually using documentation/SOURCE_MONITOR_SETUP.md if needed.
The numbered batches are: {json.dumps(counts)}
SHA256SUMS.json maps repository paths to checksums for verification. Do not upload it or this instruction file.
"""
import hashlib
with zipfile.ZipFile(packet,'w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('START_HERE.txt',instructions)
    z.writestr('SHA256SUMS.json',json.dumps({str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2))
    for name,paths in batches.items():
        for path in paths:z.write(root/path,name+'/'+path)
with zipfile.ZipFile(packet) as z:
    assert z.testzip() is None
    for name,paths in batches.items():
        assert len(paths)<100
        for path in paths:assert z.read(name+'/'+path)==(root/path).read_bytes()
print('Verified browser upload batches:',counts)
