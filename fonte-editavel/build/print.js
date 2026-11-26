const { chromium } = require('playwright');
(async () => {
  const [,, html, pdf, shotsDir] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  await p.goto('file://' + html, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: pdf, width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true, tagged: true });
  if (shotsDir) {
    const els = await p.$$('.page');
    for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${shotsDir}/p${String(i + 1).padStart(2, '0')}.png` });
  }
  await b.close();
})();
