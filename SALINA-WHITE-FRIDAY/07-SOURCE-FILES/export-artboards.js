// Exports every [data-export] artboard of a page as a 1080x1350 PNG.
// Usage: node export-artboards.js <page.html> <outDir>
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const [, , input, outDir] = process.argv;
  fs.mkdirSync(outDir, { recursive: true });
  const html = '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">' + fs.readFileSync(input, 'utf8') + '</body></html>';
  const tmp = path.join(path.dirname(path.resolve(input)), '.export-tmp.html'); fs.writeFileSync(tmp, html);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await p.goto('file://' + tmp); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
  const ids = await p.$$eval('[data-export]', els => els.map(e => [e.id, e.dataset.export]));
  await p.evaluate(() => document.documentElement.classList.add('exporting'));
  for (const [id, name] of ids) {
    await p.evaluate(i => { document.querySelectorAll('.fr.out').forEach(e => e.classList.remove('out')); document.getElementById(i).classList.add('out'); }, id);
    await p.waitForTimeout(150);
    await p.screenshot({ path: path.join(outDir, `${name}.png`), clip: { x: 0, y: 0, width: 1080, height: 1350 } });
    console.log('exported', name);
  }
  await b.close(); fs.unlinkSync(tmp);
})();
