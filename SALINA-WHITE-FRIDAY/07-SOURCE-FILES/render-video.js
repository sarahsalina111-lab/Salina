// Renders an HTML motion source (exposes window.renderAt(t), DURATION, FPS and a #stage element) to video frames.
// Usage:
//   node render-video.js <source.html> <out.mp4>                 full render, frames piped into ffmpeg (H.264, no audio)
//   node render-video.js <source.html> <outDir> --stills 0.5,3,7  PNG stills at the given seconds (storyboard / checks)
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path'); const fs = require('fs');

(async () => {
  const [, , src, out, flag, list] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(src));
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const { DURATION, FPS } = await p.evaluate(() => ({ DURATION: window.DURATION, FPS: window.FPS }));
  const stage = p.locator('#stage');

  if (flag === '--stills') {
    fs.mkdirSync(out, { recursive: true });
    for (const s of list.split(',').map(Number)) {
      await p.evaluate(t => window.renderAt(t), s);
      await stage.screenshot({ path: path.join(out, `t${s.toFixed(2).padStart(5, '0')}.png`) });
    }
    console.log('stills ->', out); await b.close(); return;
  }

  const n = Math.round(DURATION * FPS);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'png', '-i', '-',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', String(FPS), '-movflags', '+faststart', out],
    { stdio: ['pipe', 'inherit', 'inherit'] });
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    await p.evaluate(t => window.renderAt(t), i / FPS);
    const buf = await stage.screenshot({ type: 'png' });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 60 === 0) console.log(`frame ${i}/${n}  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
  console.log(`rendered ${n} frames in ${((Date.now() - t0) / 1000).toFixed(0)}s ->`, out);
  await b.close();
})();
