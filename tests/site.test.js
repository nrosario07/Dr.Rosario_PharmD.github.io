const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const root = path.join(__dirname, "..");
const read = p => fs.readFileSync(path.join(root,p),"utf8");

test("published entry point and core assets exist", () => {
  for (const p of ["docs/index.html","docs/assets/app.js","docs/assets/content.js","docs/assets/styles.css"]) {
    assert.ok(fs.existsSync(path.join(root,p)), `${p} should exist`);
  }
});

test("site loads local scripts only and contains privacy notice", () => {
  const html = read("docs/index.html");
  assert.match(html, /assets\/content\.js/);
  assert.match(html, /assets\/app\.js/);
  assert.match(html, /Do not enter PHI|clinical education resource/i);
  assert.doesNotMatch(html, /google-analytics|gtag\(|hotjar/i);
});

test("clinical workflows remain distinct", () => {
  const app = read("docs/assets/app.js");
  assert.match(app, /drug-intelligence/);
  assert.match(app, /medication-review/);
  assert.match(app, /Drug Intelligence/);
  assert.match(app, /Medication Review & Reconciliation/);
});

test("no browser persistence APIs are used", () => {
  const app = read("docs/assets/app.js");
  assert.doesNotMatch(app, /localStorage|sessionStorage|indexedDB/);
});

test("out-of-scope VDP workflows are not included", () => {
  const all = ["README.md","AGENTS.md","docs/assets/app.js","docs/assets/content.js"].map(read).join("\n");
  assert.match(all, /Vendor Drug Program/);
  assert.match(all, /out of scope|exclude/i);
});
