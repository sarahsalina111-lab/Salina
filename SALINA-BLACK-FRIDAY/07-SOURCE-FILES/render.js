// Render an HTML design to PNG at its exact stage size.
// Usage: node render.js <input.html> <output.png> [width] [height]
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [, , input, output, w = '1080', h = '1350'] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(input));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  await page.locator('#stage').screenshot({ path: output });
  await browser.close();
  console.log('rendered', output);
})();
