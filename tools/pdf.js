// Usage: node tools/pdf.js <input.html> <output.pdf> [preview-prefix]
const { chromium } = require('playwright');
(async () => {
  const [inp, out, shots] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1056, height: 816 } });
  await p.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log('fonts', await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight).join(', ')));
  // Flag any page whose content overflows its sheet
  console.log('overflow', await p.evaluate(() => [...document.querySelectorAll('.page')].map((s, i) => [i + 1, [...s.querySelectorAll('.text, dl')].some(t => t.scrollHeight > t.clientHeight + 1 || t.getBoundingClientRect().bottom > s.getBoundingClientRect().bottom - 40)]).filter(x => x[1]).map(x => x[0])));
  if (shots) await p.screenshot({ path: shots + '.png', fullPage: true });
  await p.pdf({ path: out, width: '11in', height: '8.5in', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
