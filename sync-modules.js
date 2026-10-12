'use strict';
const fs=require('node:fs'),path=require('node:path');
const root=path.join(__dirname,'..'),data=JSON.parse(fs.readFileSync(path.join(root,'docs/data/modules.json'),'utf8'));
fs.writeFileSync(path.join(root,'docs/assets/module-data.js'),'window.ClinicalModuleData = '+JSON.stringify(data,null,2)+';\n');
console.log('Offline module registry updated.');
