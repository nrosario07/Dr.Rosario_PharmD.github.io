"""Create a portable preview and source ZIP. No private uploads are included."""
from pathlib import Path
import base64
import re
import zipfile
root=Path(__file__).resolve().parent.parent
out=root.parent/'output'
out.mkdir(exist_ok=True)
site=root/'docs'
html=(site/'index.html').read_text()
html=html.replace("script-src 'self'", "script-src 'self' 'unsafe-inline'").replace("style-src 'self'", "style-src 'self' 'unsafe-inline'")
html=html.replace('<link rel="stylesheet" href="assets/styles.css?v=0.8.0">','<style>'+ (site/'assets/styles.css').read_text()+'</style>')
icon='data:image/svg+xml;base64,'+base64.b64encode((site/'assets/mark.svg').read_bytes()).decode()
html=html.replace('assets/mark.svg?v=0.8.0',icon)
rules_uri='data:application/json;base64,'+base64.b64encode((site/'data/clinical-rules.json').read_bytes()).decode()
html=html.replace('data/clinical-rules.json',rules_uri)
for name in ['startup.js','content.js','core.js','rules.js','clinical.js','module-data.js','modules.js','drug-api.js','icd-index.js','advanced.js','advanced-platform.js','next-phase.js','next-platform.js','calculator-links.js','local-draft.js','reporting.js','platform.js','workspaces.js','app.js']:
    js=(site/'assets'/name).read_text()
    for item in (site/'downloads').iterdir():
        mime='application/pdf' if item.suffix=='.pdf' else 'text/plain;charset=utf-8'
        uri='data:'+mime+';base64,'+base64.b64encode(item.read_bytes()).decode()
        js=js.replace('data/clinical-rules.json',rules_uri)
        js=js.replace('downloads/'+item.name,uri)
        html=html.replace('downloads/'+item.name,uri)
    html=html.replace(f'<script defer src="assets/{name}?v=0.8.0"></script>','<script defer>'+js.replace('</script','<\\/script')+'</script>')
# Inline classic scripts must execute after the DOM: defer applies only to external scripts.
scripts=re.findall(r'<script defer>.*?</script>',html,re.S)
html=re.sub(r'<script defer>.*?</script>','',html,flags=re.S)
html=html.replace('</body>','\n'+ '\n'.join(s.replace('<script defer>','<script>') for s in scripts)+'\n</body>')
(out/'ClinicalRx_0.8.0_Preview.html').write_text(html)
(out/'ClinicalRx_0.8.0_Build_Specification.md').write_text((root/'documentation/BUILD_SPECIFICATION.md').read_text())
with zipfile.ZipFile(out/'ClinicalRx_0.8.0_GitHub_Update.zip','w',zipfile.ZIP_DEFLATED) as z:
    for item in sorted(root.rglob('*')):
        if item.is_file() and '.git' not in item.parts and '__pycache__' not in item.parts and item.name != 'source-monitor-report.json' and item.suffix != '.pyc':
            z.write(item,str(item.relative_to(root)))
print('Preview, specification and source ZIP created.')
