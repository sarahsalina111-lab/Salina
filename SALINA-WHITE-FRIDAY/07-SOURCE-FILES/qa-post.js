// QA + export for a 1080x1350 post source.
// Usage: node qa-post.js <post.html> <out.png>
// Checks: stage size, every text box inside the stage, fonts actually used, WCAG contrast of each text run, raster images used.
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const [, , input, out] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  const failed = []; p.on('requestfailed', r => failed.push(r.url()));
  await p.goto('file://' + path.resolve(input)); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const r = await p.evaluate(() => {
    const st = document.getElementById('stage'), S = st.getBoundingClientRect();
    const rgb = s => { const m = s.match(/[\d.]+/g).map(Number); return { r: m[0], g: m[1], b: m[2], a: m[3] ?? 1 }; };
    const lin = c => { c /= 255; return c <= .03928 ? c / 12.92 : ((c + .055) / 1.055) ** 2.4; };
    const L = c => .2126 * lin(c.r) + .7152 * lin(c.g) + .0722 * lin(c.b);
    const bgOf = el => { for (let e = el; e; e = e.parentElement) { const c = rgb(getComputedStyle(e).backgroundColor); if (c.a > .9) return c; } return { r: 255, g: 255, b: 255 }; };
    const texts = [];
    const walker = document.createTreeWalker(st, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const n = walker.currentNode, t = n.textContent.trim(); if (!t) continue;
      const el = n.parentElement, cs = getComputedStyle(el), rg = document.createRange(); rg.selectNodeContents(n); const R = rg.getBoundingClientRect();
      const fg = rgb(cs.color), bg = bgOf(el); const cr = (Math.max(L(fg), L(bg)) + .05) / (Math.min(L(fg), L(bg)) + .05);
      const px = parseFloat(cs.fontSize), large = px >= 24 * 1.333 || (px >= 18.66 && +cs.fontWeight >= 700);
      texts.push({ t: t.slice(0, 28), px: Math.round(px), font: cs.fontFamily.split(',')[0].replace(/"/g, ''), w: cs.fontWeight, contrast: +cr.toFixed(2), need: large ? 3 : 4.5,
        inside: R.left >= S.left - 1 && R.right <= S.right + 1 && R.top >= S.top - 1 && R.bottom <= S.bottom + 1 });
    }
    const clipped = [...st.querySelectorAll('.card,.price,[data-fit]')].flatMap(box => { const B = box.getBoundingClientRect();
      return [...box.querySelectorAll('*'), box].filter(e => e !== box || box.hasAttribute('data-fit')).filter(e => { const R = e.getBoundingClientRect(); return R.width && (e.scrollWidth > e.clientWidth + 1 || (e !== box && (R.bottom > B.bottom + 1 || R.left < B.left - 1))); }).map(e => (e.textContent || e.className).trim().slice(0, 24)); });
    return { size: [S.width, S.height], texts, clipped: [...new Set(clipped)], imgs: [...st.querySelectorAll('img')].map(i => [i.getAttribute('src').split('/').pop(), i.naturalWidth > 0]),
      fonts: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/"/g, '') + ' ' + f.weight) };
  });
  console.log(`\n== ${path.basename(input)}  stage ${r.size.join('x')}`);
  console.log('fonts loaded:', [...new Set(r.fonts)].join(', '));
  console.log('images:', JSON.stringify(r.imgs), failed.length ? 'FAILED: ' + failed.join(' ') : 'all assets loaded');
  console.log(r.clipped.length ? 'CLIPPED: ' + JSON.stringify(r.clipped) : 'no clipped content');
  for (const t of r.texts) console.log(`${t.contrast >= t.need ? 'ok ' : 'LOW'} ${String(t.contrast).padStart(5)} (need ${t.need}) ${t.inside ? 'in ' : 'OUT'} ${t.px}px ${t.font} ${t.w}  ${t.t}`);
  await p.locator('#stage').screenshot({ path: out }); console.log('exported', out);
  await b.close();
})();
