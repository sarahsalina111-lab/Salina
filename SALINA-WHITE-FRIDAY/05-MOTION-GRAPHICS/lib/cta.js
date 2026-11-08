/* Shared end card (CTA) for SALINA WHITE FRIDAY videos.
   «قبل ما تدوسي...» → a checkout button «إتمام الشراء» and a cursor about to tap it →
   «استني عروض Salina» lands, the button dims, the cursor backs off → gold tag «تابعينا عشان تلحقيها» gets tapped.
   Usage: CTA.init(stageEl); then inside renderAt(t): CTA.render(t, startTime). Lasts ~2.4s on a purple background.
   The account handle line stays empty until it is filled in HANDLE below. */
(function () {
  const HANDLE = '';   // e.g. '@salina.academy' — leave empty to hide the line
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const P = (t, t0, t1) => clamp((t - t0) / (t1 - t0));
  const lerp = (a, b, p) => a + (b - a) * p;
  const outCubic = p => 1 - (1 - p) ** 3, inCubic = p => p ** 3;
  const outBack = (p, s = 1.7) => 1 + (s + 1) * (p - 1) ** 3 + s * (p - 1) ** 2;
  const spring = (dt, amp, f = 18, k = 9) => dt < 0 ? 0 : amp * Math.exp(-k * dt) * Math.cos(f * dt);

  const CTA = {};
  // opts (all optional): { b: HTML of the big line, bSize: px, tag: text on the gold tag, handle: text under the tag }
  CTA.init = function (stage, opts = {}) {
    const B = opts.b || 'استني عروض <span style="color:#F5C04A">Salina</span>', BS = opts.bSize || 104;
    const TAG = opts.tag || 'تابعينا عشان تلحقيها', H = opts.handle !== undefined ? opts.handle : HANDLE;
    const w = document.createElement('div');
    w.id = 'cta'; w.style.cssText = 'position:absolute;inset:0;pointer-events:none;visibility:hidden';
    w.innerHTML = `
      <style>
        #cta .row{position:absolute;left:0;right:0;display:flex;justify-content:center;gap:.26em;direction:rtl;white-space:nowrap;line-height:1.25}
        #cta .m{display:inline-block;overflow:hidden;padding:.12em .04em .2em;margin:-.12em -.04em -.2em}
        #cta .m>span{display:inline-block}
      </style>
      <div class="row" id="ctaA" style="top:400px;font:800 84px/1.25 'Tajawal',sans-serif;color:#E9DCF0">
        <span class="m"><span>قبل</span></span><span class="m"><span>ما</span></span><span class="m"><span>تدوسي...</span></span></div>
      <div id="ctaBtn" style="position:absolute;left:230px;top:570px;width:620px;height:146px;border-radius:999px;background:#FFF8EE;color:#58346F;
           display:flex;align-items:center;justify-content:center;gap:24px;direction:rtl;font:900 64px/1 'Tajawal',sans-serif;box-shadow:0 12px 0 #3E2350">
        <svg width="70" height="60" viewBox="0 0 70 60"><path d="M4 6h10l8 34h34l8-24H18" fill="none" stroke="#58346F" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="26" cy="52" r="6" fill="#58346F"/><circle cx="52" cy="52" r="6" fill="#58346F"/></svg>
        <span>إتمام الشراء</span></div>
      <svg id="ctaHand" width="96" height="128" viewBox="0 0 96 128" style="position:absolute;left:0;top:0">
        <path d="M8 6L8 104 34 80 52 120 70 112 52 74 88 74Z" fill="#FFF8EE" stroke="#30263A" stroke-width="7" stroke-linejoin="round"/></svg>
      <div class="row" id="ctaB" style="top:810px;font:900 ${BS}px/1.25 'Tajawal',sans-serif;color:#FFF8EE">
        <span id="ctaBin" style="display:inline-block">${B}</span></div>
      <div id="ctaTag" style="position:absolute;left:150px;top:1060px;width:780px;height:150px;background:#F5C04A;color:#58346F;
           clip-path:polygon(70px 0,100% 0,100% 100%,70px 100%,0 50%);display:flex;align-items:center;justify-content:center;
           padding-left:60px;box-sizing:border-box;font:900 64px/1 'Tajawal',sans-serif;direction:rtl;white-space:nowrap">
        <i style="position:absolute;left:46px;top:63px;width:24px;height:24px;border-radius:50%;background:#58346F;display:block"></i>${TAG}</div>
      <div class="row" id="ctaH" style="top:1236px;font:700 46px/1.2 'Cairo',sans-serif;color:#E9DCF0;direction:ltr">${H}</div>`;
    stage.appendChild(w);
  };

  CTA.render = function (t, c) {
    const $ = id => document.getElementById(id);
    const w = $('cta'); if (!w) return;
    w.style.visibility = t >= c ? 'visible' : 'hidden';
    if (t < c) return;
    // «قبل ما تدوسي...»
    [...$('ctaA').querySelectorAll('.m>span')].forEach((s, i) => {
      const a = outCubic(P(t, c + .2 + i * .12, c + .65 + i * .12)); s.style.transform = `translateY(${(1 - a) * 115}%)`; });
    // checkout button pops, then dims when «استني» lands
    const bp = P(t, c + .5, c + .85), dim = outCubic(P(t, c + 1.15, c + 1.45));
    $('ctaBtn').style.transform = `scale(${lerp(.4, 1, outBack(bp, 2.2)) * lerp(1, .9, dim)})`;
    $('ctaBtn').style.opacity = clamp(bp * 3) * lerp(1, .4, dim);
    // cursor glides in, hesitates, backs off
    const hp = outCubic(P(t, c + .7, c + 1.1)), back = outCubic(P(t, c + 1.15, c + 1.5));
    const hx = lerp(lerp(980, 700, hp), 900, back), hy = lerp(lerp(1000, 668, hp), 600, back);
    const hand = $('ctaHand'); hand.style.transform = `translate(${hx}px, ${hy}px) rotate(${lerp(-8, 6, back)}deg)`;
    hand.style.opacity = P(t, c + .65, c + .8) * (1 - P(t, c + 1.6, c + 1.9));
    // «استني عروض Salina» lands
    const sp = P(t, c + 1.15, c + 1.5);
    $('ctaBin').style.transform = `scale(${lerp(1.7, 1, outBack(sp, 2.4))}) rotate(${lerp(-6, 0, outBack(sp, 2))}deg)`;
    $('ctaB').style.opacity = clamp(sp * 4);
    // gold tag: pops, then gets tapped
    const tp = P(t, c + 1.55, c + 1.9);
    const press = (t > c + 2.05 && t < c + 2.17) ? .93 : 1 + spring(t - (c + 2.17), .05, 20, 10);
    $('ctaTag').style.transform = `translateX(${(1 - outBack(tp, 1.8)) * -160}px) scale(${press})`;
    $('ctaTag').style.opacity = clamp(tp * 3);
    $('ctaH').style.opacity = P(t, c + 1.85, c + 2.1);
  };
  window.CTA = CTA;
})();
