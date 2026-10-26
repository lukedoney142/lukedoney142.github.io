import sys, os, re, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import CASES

# Usage: python3 tools/pdf.py <output.html>   (run from the site folder; print the HTML to PDF with tools/pdf.js)
# Letter landscape, one case per page, ordered for mechanical design roles: CAD first, then hands-on work.
OUT = sys.argv[1]
SITE = os.path.abspath(".")
e = html.escape
ROCKET = re.search(r"ROCKET = '''(.*?)'''", open(os.path.join(SITE, "tools/build.py")).read(), re.S).group(1)
EMAIL, PHONE, LINKEDIN, WEB = "lukedoney142@gmail.com", "+1 (365) 778-6181", "linkedin.com/in/luke-doney-762349265", "lukedoney142.github.io"
ORDER = ["rocketry", "chrima", "robotweld", "f150", "milton"]

def img(name, alt, pos="50% 50%"):
    return f'<img src="file://{SITE}/assets/img/{name}" alt="{e(alt)}" style="object-position:{pos}">'

FIGS = {
"rocketry": f'''<div class="figs rk-figs">
    <div class="drawing">{img("bulkhead-drawing.png", "Booster stage bulkhead drawing")}<span class="cap">Booster stage bulkhead · G10 fibreglass · Drawing 1.0</span></div>
    <div class="rk-col"><div class="rk-wrap">{ROCKET}</div><span class="cap">Vehicle layout</span></div>
  </div>''',
"chrima": f'''<div class="figs grid g-chrima">
    <div class="a">{img("trackit-scan.jpg", "Meshed TrackIt scan of a welded fixture")}</div>
    <div>{img("trackit-pins.jpg", "Part on reflective support pins")}</div>
    <div>{img("trackit-laser.jpg", "Scanner projecting laser lines", "50% 45%")}</div>
    <div>{img("trackit-tripod.jpg", "TrackIt tracker on a tripod")}</div>
  </div>''',
"robotweld": f'''<div class="figs grid g-three">
    <div>{img("robot-poster.jpg", "Upgraded FANUC robot at the fixture table", "50% 30%")}</div>
    <div>{img("robot-weld.jpg", "Robotic weld bead on steel tube", "50% 55%")}</div>
    <div>{img("robot-parts.jpg", "Welded frames staged on the shop floor")}</div>
  </div>''',
"f150": f'''<div class="figs grid g-f150">
    <div class="a">{img("f150-finished.jpg", "The finished 1992 Ford F-150")}</div>
    <div>{img("f150-engine.jpg", "300 inline-six engine bay")}</div>
    <div>{img("f150-brakes.jpg", "Front brake rebuild")}</div>
    <div>{img("f150-primer.jpg", "The truck in primer")}</div>
  </div>''',
"milton": '''<div class="figs mil">
    <svg class="rink" viewBox="0 0 800 340" preserveAspectRatio="xMidYMid slice"><rect x="40" y="30" width="720" height="280" rx="120"/><path d="M400 30 V310 M260 30 V310 M540 30 V310"/><circle cx="400" cy="170" r="54"/><circle cx="400" cy="170" r="4"/></svg>
    <div class="mil-in"><span class="lbl">Founded 2023 · Milton, Ontario</span><strong>Milton Ivy League</strong></div>
    <span class="mil-conrad"><i></i>Conrad</span>
  </div>''',
}

def ul(xs):
    return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in xs) + "</ul>"

def frame(n, section, body):
    return f'''<section class="page">
  <header class="run"><span>Luke Doney</span><span>{e(section)}</span><span>{n:02d}</span></header>
  {body}
</section>'''

def case(n, key):
    c = CASES[key]
    body = f'''<div class="case case-{key}">
    <div class="text">
      <span class="lbl">{e(c["org"])} · {e(c["role"])} · {e(c["dates"])}</span>
      <h2>{e(c["title"])}</h2>
      <dl>
        <div><dt>{c.get("first", "Problem")}</dt><dd>{e(c["problem"])}</dd></div>
        <div><dt>Constraints</dt><dd>{ul(c["constraints"])}</dd></div>
        <div><dt>Solution</dt><dd>{ul(c["solution"])}</dd></div>
        <div class="res"><dt>Result</dt><dd>{e(c["result"])}</dd></div>
      </dl>
    </div>
    {FIGS[key]}
  </div>'''
    return frame(n, c["org"], body)

cover = f'''<div class="cover">
    <div class="c-text">
      <span class="lbl">Engineering portfolio · Summer 2027</span>
      <h1>Luke<br>Doney</h1>
      <p class="intro">Electrical engineering student and <b>commercial pilot</b>. <b>Lead propulsion engineer</b> on Dalhousie's two-stage rocketry team, with industry experience in robotic welding and optical metrology.</p>
      <div class="contact"><span>{EMAIL}</span><span>{PHONE}</span><span>{LINKEDIN}</span><span>{WEB}</span></div>
    </div>
    <div class="c-photo">{img("headshot.jpg", "Luke Doney")}</div>
  </div>
  <div class="cover-foot">
    <div class="edu"><span class="lbl">Education</span><p>Bachelor of Engineering, Electrical · Dalhousie University, 2nd year</p><p>Advanced Diploma, Commercial Flight &amp; Aviation · Fanshawe College, 2021–2024</p></div>
    <div class="caps">
      <div><span class="lbl">Design</span><p>Onshape · SolidWorks · Fusion 360 · Fixture design</p></div>
      <div><span class="lbl">Manufacturing</span><p>Optical metrology · Weld inspection · SOPs and training · 3D printing</p></div>
      <div><span class="lbl">Software</span><p>C · C++ · AI assistants · Raspberry Pi</p></div>
    </div>
    <ol class="toc">{"".join(f"<li><span>{i:02d}</span>{e(CASES[k]['title'])}</li>" for i, k in enumerate(ORDER, 2))}<li><span>{len(ORDER)+2:02d}</span>Aviation: commercial pilot</li></ol>
  </div>'''

aviation = f'''<div class="case">
    <div class="text">
      <span class="lbl">Fanshawe College · Commercial Pilot · Aug 2026</span>
      <h2>Aviation: commercial pilot</h2>
      <p class="lede">Commercial pilot since August 2026, trained through a three-year aviation diploma at Fanshawe College. Every flight starts with a structured assessment of the weather, the aircraft and the pilot.</p>
      <dl>
        <div><dt>Planning</dt><dd>Route, weather, NOTAMs, fuel, weight and balance, and aircraft performance planned before engine start.</dd></div>
        <div><dt>Risk</dt><dd>Hazards weighed against set personal minimums for a clear go or no-go decision.</dd></div>
        <div><dt>Efficiency</dt><dd>Short, direct routes planned around winds aloft, with cruise power and mixture set for conservative fuel use.</dd></div>
        <div><dt>Systems</dt><dd>The aircraft understood as one integrated unit, so an abnormal indication can be traced to its cause.</dd></div>
      </dl>
    </div>
    <div class="figs av">
      <div class="land">{img("landing.jpg", "On final approach in a Cessna")}</div>
      <div class="quals">
        <div><span class="lbl">Licences &amp; ratings</span><p>Commercial Pilot Licence, Aug 2026</p><p>Night Rating, Nov 2024</p><p>Private Pilot Licence, Mar 2022</p><p>Radio Operator's Certificate</p><p>Category 1 Medical</p></div>
        <div><span class="lbl">Training</span><p>Advanced Diploma, Commercial Flight &amp; Aviation</p><p>Fanshawe College, 2021–2024</p><p>220 hours total time</p></div>
        <div><span class="lbl">Aircraft flown</span><p>Cessna 172</p><p>Diamond DA20</p><p>Piper PA-34 Seneca</p></div>
      </div>
    </div>
  </div>'''

CSS = '''
@page { size: 11in 8.5in; margin: 0; }
:root { --ink:#15171b; --soft:#5c616a; --faint:#9aa0a8; --line:#dcdad4; --paper:#f7f6f2; --gold:#bc9244;
  --sans:"Archivo","Helvetica Neue",Arial,sans-serif; --mono:"IBM Plex Mono",Menlo,monospace; }
* { box-sizing:border-box; }
html, body { margin:0; background:var(--paper); color:var(--ink); font:400 9.6pt/1.55 var(--sans); -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { width:11in; height:8.5in; padding:.5in .6in .55in; display:flex; flex-direction:column; page-break-after:always; overflow:hidden; }
.page:last-child { page-break-after:auto; }
.run { display:flex; justify-content:space-between; font:400 6.8pt/1 var(--mono); letter-spacing:.16em; text-transform:uppercase; color:var(--soft); padding-bottom:10px; border-bottom:1px solid var(--line); margin-bottom:.32in; }
.lbl { display:block; font:400 6.8pt/1.5 var(--mono); letter-spacing:.14em; text-transform:uppercase; color:var(--soft); }
.cap { display:block; margin-top:8px; font:400 6.4pt/1.4 var(--mono); letter-spacing:.12em; text-transform:uppercase; color:var(--soft); }
h1, h2 { font-family:var(--sans); font-stretch:118%; font-weight:300; text-transform:uppercase; letter-spacing:.01em; margin:0; }
.case { flex:1; min-height:0; display:grid; grid-template-columns:3.55in 1fr; gap:.42in; }
.text h2 { font-size:15pt; line-height:1.18; margin:8px 0 18px; }
dl { margin:0; }
dl > div { display:grid; grid-template-columns:.95in 1fr; gap:12px; padding:9px 0; border-top:1px solid var(--line); }
dt { font:400 6.8pt/1.9 var(--mono); letter-spacing:.14em; text-transform:uppercase; color:var(--soft); }
dd { margin:0; }
dd ul { margin:0; padding:0; list-style:none; }
dd li { position:relative; padding-left:12px; }
dd li::before { content:""; position:absolute; left:0; top:.72em; width:5px; height:1px; background:var(--soft); }
.res dd { color:var(--ink); }
.res { border-bottom:1px solid var(--line); }
.lede { margin:0 0 16px; color:var(--soft); }
.figs { min-height:0; height:100%; }
.figs img { width:100%; height:100%; object-fit:cover; display:block; background:#e9e7e1; }
.grid { display:grid; gap:10px; }
.grid > div { min-height:0; overflow:hidden; }
.g-chrima { grid-template-columns:1fr 1fr 1fr; grid-template-rows:1.25fr 1fr; }
.g-chrima .a { grid-column:1 / -1; background:#2a2c30; }
.g-chrima .a img { object-fit:contain; background:#2a2c30; }
.g-three { grid-template-columns:1fr 1fr 1fr; }
.g-f150 { grid-template-columns:1fr 1fr 1fr; grid-template-rows:1.5fr 1fr; }
.g-f150 .a { grid-column:1 / -1; }
.rk-figs { display:grid; grid-template-columns:auto 1.25in; gap:.35in; align-items:start; justify-content:start; }
.drawing img { width:auto; height:6.15in; object-fit:contain; border:1px solid var(--line); background:#fff; }
.rk-col .cap { text-align:center; }
.rk-wrap { position:relative; height:6.15in; }
.rk { position:absolute; width:6.15in; height:auto; left:50%; top:50%; transform:translate(-50%,-50%) rotate(-90deg); }
.rk .fill { fill:#eceae4; stroke:var(--ink); stroke-width:1; }
.rk .motor { fill:none; stroke:var(--soft); stroke-width:1; stroke-dasharray:3 2; }
.rk text { font:400 7.5px var(--mono); letter-spacing:.12em; fill:var(--soft); }
.rk text.k { fill:var(--ink); }
.rk .dim { stroke:var(--faint); stroke-width:.8; }
.mil { position:relative; background:linear-gradient(160deg,#0c190b,#1f2d1e); display:flex; align-items:center; justify-content:center; overflow:hidden; }
.mil .rink { position:absolute; inset:0; width:100%; height:100%; fill:none; stroke:#3e4b3f; stroke-width:1.5; }
.mil-in { position:relative; text-align:center; }
.mil-in .lbl { color:var(--gold); }
.mil-in strong { display:block; margin-top:10px; color:#f3efe4; font:700 34pt/1.02 var(--sans); font-stretch:112%; }
.mil-conrad { position:absolute; right:18px; bottom:18px; display:flex; align-items:center; gap:8px; padding:6px 12px 6px 7px; border-radius:99px; background:rgba(0,0,0,.35); border:1px solid #3e4b3f; color:#f3efe4; font:500 8pt/1 var(--sans); }
.mil-conrad i { width:14px; height:14px; border-radius:50%; background:var(--gold); }
.av { display:grid; grid-template-rows:1fr auto; gap:.22in; }
.land { min-height:0; overflow:hidden; }
.quals { display:grid; grid-template-columns:1.25fr 1.1fr .8fr; gap:.25in; }
.quals p, .caps p, .edu p { margin:4px 0 0; }
.quals > div, .caps > div { border-top:1px solid var(--line); padding-top:8px; }
.cover { flex:1; display:grid; grid-template-columns:1fr 3.1in; gap:.6in; align-items:center; min-height:0; }
.cover h1 { font-size:50pt; line-height:.96; margin:14px 0 22px; }
.intro { font-size:11.5pt; line-height:1.6; color:var(--soft); max-width:31em; margin:0 0 22px; }
.intro b { color:var(--ink); font-weight:400; }
.contact { display:flex; flex-wrap:wrap; gap:6px 22px; font:400 7.4pt/1.6 var(--mono); letter-spacing:.06em; }
.c-photo { height:4.05in; overflow:hidden; }
.c-photo img { width:100%; height:100%; object-fit:cover; object-position:50% 20%; display:block; }
.case-milton { grid-template-columns:4.75in 1fr; }
.case-milton h2 { font-size:13.5pt; }
.cover-foot { display:grid; grid-template-columns:2.6in 1fr 2.9in; gap:.4in; border-top:1px solid var(--line); padding-top:14px; font-size:8.4pt; }
.edu p { color:var(--ink); }
.caps { display:grid; grid-template-columns:1fr; gap:6px; }
.caps > div { border:0; padding:0; display:grid; grid-template-columns:1in 1fr; }
.caps p { margin:0; }
.toc { margin:0; padding:0; list-style:none; }
.toc li { display:grid; grid-template-columns:.32in 1fr; line-height:1.5; }
.toc span { font:400 6.8pt/2 var(--mono); color:var(--soft); }
'''

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,200..700&family=IBM+Plex+Mono:wght@400&display=swap">'
pages = [frame(1, "Portfolio", cover)] + [case(i, k) for i, k in enumerate(ORDER, 2)] + [frame(len(ORDER) + 2, "Aviation", aviation)]
open(OUT, "w").write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Luke Doney · Portfolio</title>{FONTS}<style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
print("wrote", OUT)
