(function(){
'use strict';
function warn(message){const panel=document.getElementById('startup-status');if(panel){panel.hidden=false;panel.textContent=message;}else{const main=document.getElementById('main');if(main&&main.childElementCount===0)main.textContent=message;}}
window.addEventListener('error',function(event){if(event.target&&event.target.tagName==='SCRIPT')warn('A required site file could not load. Check that index.html is inside docs/ and scripts are inside docs/assets/. Reload with Ctrl+Shift+R.');else if(event.filename&&event.filename.includes('/assets/'))warn('The clinical workspace could not initialize. Reload with Ctrl+Shift+R. If this continues, check that all assets come from the same release.');},true);
window.addEventListener('load',function(){const main=document.getElementById('main'),panel=document.getElementById('startup-status');if(main&&main.childElementCount>0&&panel)panel.hidden=true;else warn('The site has not initialized. Check the upload folders and enabled JavaScript, then reload with Ctrl+Shift+R.');});
})();
