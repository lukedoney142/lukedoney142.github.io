import sys, html, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import CASES, ORDER

# Usage: python3 tools/build.py <output folder>   (run from the site folder with "." to rebuild in place)
OUT = sys.argv[1]
e = html.escape
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,200..600&family=IBM+Plex+Mono:wght@400&display=swap">')
NAV = [("work.html", "Work"), ("projects.html", "Projects"), ("rocketry.html", "Rocketry"), ("aviation.html", "Aviation")]
EMAIL = "lukedoney142@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/luke-doney-762349265"

ROCKET = '''<svg class="rk" viewBox="0 0 640 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Side profile of the two-stage rocket with fins and a motor in each stage">
            <path class="fill" d="M24 52 L24 80 L270 80 L270 52 Z"/>
            <path class="fill" d="M28 52 L84 52 L46 26 L16 26 Z"/>
            <path class="fill" d="M28 80 L84 80 L46 106 L16 106 Z"/>
            <rect class="motor" x="30" y="56" width="150" height="20"/>
            <path class="fill" d="M270 54 L300 56 L300 76 L270 78 Z"/>
            <path class="fill" d="M300 56 L520 56 L520 76 L300 76 Z"/>
            <path class="fill" d="M304 56 L346 56 L318 37 L296 37 Z"/>
            <path class="fill" d="M304 76 L346 76 L318 95 L296 95 Z"/>
            <rect class="motor" x="306" y="59" width="120" height="14"/>
            <path class="fill" d="M520 56 Q600 58 630 66 Q600 74 520 76 Z"/>
            <text class="k" x="100" y="44">PRO75</text>
            <text class="k" x="360" y="48">PRO54</text>
            <text x="30" y="126">STAGE 1 · BOOSTER</text>
            <text x="306" y="126">STAGE 2 · SUSTAINER</text>
            <path class="dim" d="M6 140 L630 140"/>
            <text x="444" y="134">APOGEE 35,000 FT · MACH 1.7</text>
          </svg>'''

def visual(key, cls="visual"):
    v = CASES[key]["visual"]
    if v == "rocket":
        return f'<div class="{cls} draw">{ROCKET}</div>'
    if v == "chrima":
        return f'<div class="{cls}"><img src="assets/img/trackit-scan.jpg" alt="Meshed TrackIt scan of a welded fixture, separated cleanly from the table" width="1600" height="686" loading="lazy"></div>'
    if v == "f150":
        return f'<div class="{cls}"><img src="assets/img/f150-finished.jpg" alt="The finished 1992 Ford F-150 at sunset" width="1242" height="932" loading="lazy"></div>'
    if v == "robotweld":
        return f'<div class="{cls}"><img src="assets/img/robot-weld.jpg" alt="Close-up of a robotic weld bead on steel tube" width="1050" height="1400" loading="lazy" style="object-position: 50% 55%"></div>'
    if v == "outboard":
        return f'<div class="{cls}"><img src="assets/img/outboard.jpg" alt="The Johnson 40 hp powerhead with its cylinders exposed" width="966" height="1180" loading="lazy" style="object-position: 50% 40%"></div>'
    if v == "conrad":
        return f'<div class="{cls} type" aria-hidden="true"><div><strong class="wide">Conrad</strong><span class="label">AI assistant · self check-in</span></div></div>'
    if v == "milton":
        return (f'<div class="{cls} mil" aria-hidden="true">'
                '<svg class="rink" viewBox="0 0 800 340" preserveAspectRatio="xMidYMid slice"><rect x="40" y="30" width="720" height="280" rx="120"/>'
                '<path d="M400 30 V310 M260 30 V310 M540 30 V310"/><circle cx="400" cy="170" r="54"/><circle cx="400" cy="170" r="4"/></svg>'
                '<div class="mil-in"><span class="label">Founded 2023 · Milton, Ontario</span><strong>Milton Ivy League</strong></div>'
                '<span class="mil-conrad"><i></i>Conrad</span></div>')

def case_visual(key):
    if CASES[key]["visual"] == "robotweld":
        return ('<div class="case-visual visual clip" style="aspect-ratio: 4 / 5; max-width: 560px"><video style="object-position: 50% 30%" src="assets/video/robot-cell.mp4" poster="assets/img/robot-poster.jpg" '
                'controls muted playsinline preload="metadata" aria-label="Video of the upgraded FANUC robot welding on the fixture table"></video></div>')
    return visual(key, "case-visual visual")

EXTRA = {
"rocketry": '''<figure class="drawing">
        <a href="assets/img/bulkhead-drawing.png" target="_blank" rel="noopener"><img src="assets/img/bulkhead-drawing.png" alt="Engineering drawing of the booster stage bulkhead in G10 fibreglass" width="1400" height="1980" loading="lazy"></a>
        <figcaption class="label">Booster stage bulkhead · G10 fibreglass · Drawing 1.0</figcaption>
      </figure>''',
"chrima": '''<div class="thumbs">
        <img src="assets/img/trackit-laser.jpg" alt="TrackIt scanner projecting laser lines onto a steel part" width="1050" height="1400" loading="lazy">
        <img src="assets/img/trackit-pins.jpg" alt="Steel part resting on reflective support pins" width="1400" height="1050" loading="lazy">
        <img src="assets/img/trackit-tripod.jpg" alt="Revopoint TrackIt optical tracker on a tripod" width="1050" height="1400" loading="lazy">
        <img src="assets/img/trackit-scanner.jpg" alt="Handheld TrackIt scanner head with reflective targets" width="1400" height="1050" loading="lazy" style="object-position: 20% 50%">
        <img src="assets/img/welding.jpg" alt="Luke welding steel T-joint test pieces" width="1240" height="1204" loading="lazy">
      </div>
      <div class="case-visual visual clip" style="aspect-ratio: 16 / 9; margin-top: 32px"><video src="assets/video/trackit-metrology.mp4" poster="assets/img/trackit-poster.jpg" controls muted playsinline preload="metadata" aria-label="Video of the TrackIt metrology station"></video></div>''',
"robotweld": '''<div class="thumbs">
        <img src="assets/img/robot-parts.jpg" alt="Welded frames and fixtures staged on the Chrima shop floor" width="1050" height="1400" loading="lazy">
      </div>''',
"f150": '''<div class="thumbs">
        <img src="assets/img/f150-brakes.jpg" alt="Front brake rebuild with new rotor and caliper" width="1050" height="1400" loading="lazy">
        <img src="assets/img/f150-engine.jpg" alt="Engine bay of the 300 inline-six" width="1400" height="1050" loading="lazy">
        <img src="assets/img/f150-primer.jpg" alt="The F-150 in primer during bodywork" width="1050" height="1400" loading="lazy">
      </div>''',
}

def page(fn, title, desc, body):
    nav = "\n".join(f'      <li><a href="{u}"{" aria-current=\"page\"" if u == fn else ""}>{t}</a></li>' for u, t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
{FONTS}
<link rel="stylesheet" href="style.css">
</head>
<body>

<nav class="nav" aria-label="Site">
  <div class="wrap">
    <a class="mark" href="index.html">Luke Doney</a>
    <ul>
{nav}
      <li><a href="index.html#contact">Contact</a></li>
    </ul>
  </div>
</nav>
{body}
<footer>
  <div class="wrap"><span class="label">© 2026 Luke Doney</span><span class="label">Halifax, NS · Milton, ON</span></div>
</footer>
</body>
</html>
'''

def ul(xs):
    return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in xs) + "</ul>"

def case(key):
    c = CASES[key]
    return f'''
  <article class="case" id="{key}">
    <div class="wrap">
      {case_visual(key)}
      <header class="case-head">
        <h2>{e(c["title"])}</h2>
        <div class="case-meta"><span class="label">{e(c["org"])}</span><span class="label">{e(c["role"])}</span><span class="label">{e(c["dates"])}</span></div>
      </header>
      <dl class="spec">
        <div><dt><span class="label" data-n="01">{c.get("first", "Problem")}</span></dt><dd>{e(c["problem"])}</dd></div>
        <div><dt><span class="label" data-n="02">Constraints</span></dt><dd>{ul(c["constraints"])}</dd></div>
        <div><dt><span class="label" data-n="03">Solution</span></dt><dd>{ul(c["solution"])}</dd></div>
        <div class="result"><dt><span class="label" data-n="04">Result</span></dt><dd>{e(c["result"])}</dd></div>
      </dl>
      {EXTRA.get(key, "")}
    </div>
  </article>'''

def sub(fn, title, eyebrow, keys, extra=""):
    body = f'''
<main>
<header class="page-head">
  <div class="wrap">
    <span class="label">{eyebrow}</span>
    <h1 class="wide">{title}</h1>
  </div>
</header>
{"".join(case(k) for k in keys)}
{extra}
</main>
'''
    open(f"{OUT}/{fn}", "w").write(page(fn, f"{title} · Luke Doney", f"Luke Doney: {title.lower()}.", body))

sub("work.html", "Work", "Experience", ["robotweld", "chrima", "milton"])
sub("projects.html", "Projects", "Independent work", ["f150", "outboard"])
creds = '''
<section id="flight" class="flush">
  <div class="wrap">
    <div class="case-visual visual clip" style="aspect-ratio: 16 / 9; max-width: none"><img src="assets/img/landing.jpg" alt="Luke on final approach, seen from the back seat of a Cessna" width="1600" height="900" style="width: 100%; height: 100%; object-fit: cover"></div>
    <p class="intro lede">Commercial pilot since August 2026, trained through a three-year aviation diploma at Fanshawe College. Every flight starts with a structured assessment of the weather, the aircraft and the pilot.</p>
    <div class="caps three quals">
      <div><h3 class="label">Licences &amp; ratings</h3><ul><li>Commercial Pilot Licence, Aug 2026</li><li>Night Rating, Nov 2024</li><li>Radio Operator's Certificate</li><li>Category 1 Medical</li></ul></div>
      <div><h3 class="label">Training</h3><ul><li>Advanced Diploma, Commercial Flight &amp; Aviation</li><li>Fanshawe College, 2021–2024</li><li>220 hours total time</li></ul></div>
      <div><h3 class="label">Aircraft flown</h3><ul><li>Cessna 172</li><li>Diamond DA20</li><li>Piper PA-34 Seneca</li></ul></div>
    </div>
  </div>
</section>

<section id="approach">
  <div class="wrap">
    <div class="sec-head"><h2 class="wide">Airmanship</h2></div>
    <div class="pillars rows">
      <div><span class="label" data-n="01">Planning</span><p>Every flight is planned before engine start: route, weather, NOTAMs, fuel, weight and balance, and aircraft performance for the day's conditions.</p></div>
      <div><span class="label" data-n="02">Risk assessment</span><p>Hazards are weighed before and during each flight, from weather and terrain to fatigue and aircraft condition, against set personal minimums for a clear go or no-go decision.</p></div>
      <div><span class="label" data-n="03">Safe practice</span><p>Checklists, standard procedures and clear radio calls on every flight, grounded in safety management systems and human factors training.</p></div>
      <div><span class="label" data-n="04">Efficient operations</span><p>Safe flying and efficient flying go together: short, direct routes planned around winds aloft and airspace, cruise power and mixture set for conservative fuel use, and no wasted time on the ground or in the air.</p></div>
      <div><span class="label" data-n="05">Systems knowledge</span><p>The aircraft is understood as one integrated unit: how the engine, fuel, electrical, flight controls and avionics depend on each other, so an abnormal indication can be traced to its cause.</p></div>
      <div><span class="label" data-n="06">Skill</span><p>220 hours including night flying, building to a Commercial Pilot Licence: precise handling, navigation and decision-making under workload.</p></div>
  </div>
</section>

<section id="path">
  <div class="wrap">
    <div class="sec-head"><h2 class="wide">Training path</h2></div>
    <ol class="path">
      <li><span class="label">2021 – 2024</span><div><h3>Advanced Diploma, Commercial Flight &amp; Aviation</h3><p>Fanshawe College, London, ON. Flight training alongside aviation theory, human factors and safety management.</p></div></li>
      <li><span class="label">Mar 2022</span><div><h3>Private Pilot Licence</h3><p>First licence, alongside the Radio Operator's Certificate.</p></div></li>
      <li><span class="label">Nov 2024</span><div><h3>Night Rating</h3><p>Night VFR operations.</p></div></li>
      <li><span class="label">Aug 2026</span><div><h3>Commercial Pilot Licence</h3><p>220 hours total time, with a Category 1 medical.</p></div></li>
    </ol>
  </div>
</section>
'''
sub("rocketry.html", "Rocketry", "Propulsion", ["rocketry"])
sub("aviation.html", "Aviation", "Flight", [], creds)

panels = "\n".join(f'''      <a class="panel" href="{CASES[k]["page"]}.html#{k}">
        {visual(k)}
        <div class="panel-cap"><span class="label">{i:02d}</span><div><h3>{e(CASES[k]["title"])}</h3><span class="label">{e(CASES[k]["org"])}</span></div><span class="go" aria-hidden="true">&rarr;</span></div>
      </a>''' for i, k in enumerate(ORDER, 1))

home = f'''
<header class="hero" id="top">
  <svg class="trajectory" viewBox="0 0 1200 520" preserveAspectRatio="none" aria-hidden="true" focusable="false">
    <path class="arc" d="M520 560 C 620 300, 730 70, 860 70 C 990 70, 1140 220, 1240 360"/>
  </svg>
  <div class="apex" aria-hidden="true"><span class="label">35,000 ft</span></div>
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="label">Electrical Engineering · Dalhousie University</span>
        <h1 class="wide"><span>Luke</span><span>Doney</span></h1>
        <p class="intro">Electrical engineering student and <b>commercial pilot</b>. <b>Lead propulsion engineer</b> on Dalhousie's two-stage rocketry team, with industry experience in robotic welding and optical metrology.</p>
        <div class="hero-foot">
          <a class="textlink" href="#work">Selected work</a>
          <span class="label avail">Available for Summer 2027 internships</span>
        </div>
      </div>
      <figure class="portrait">
        <img src="assets/img/headshot.jpg" alt="Portrait of Luke Doney" width="800" height="1000">
      </figure>
    </div>
  </div>
</header>

<main>
<section id="work">
  <div class="wrap">
    <div class="sec-head"><h2 class="wide">Selected work</h2><span class="label">2023 – 2026</span></div>
    <div class="panels">
{panels}
    </div>
  </div>
</section>

<section id="capabilities">
  <div class="wrap">
    <div class="sec-head"><h2 class="wide">Capabilities</h2></div>
    <div class="caps">
      <div><h3 class="label">Design</h3><ul><li>Onshape</li><li>SolidWorks</li><li>Fusion 360</li><li>Fixture design</li></ul></div>
      <div><h3 class="label">Manufacturing</h3><ul><li>Optical metrology</li><li>Weld inspection</li><li>SOPs and training</li><li>3D printing</li></ul></div>
      <div><h3 class="label">Software</h3><ul><li>C</li><li>C++</li><li>AI assistants</li><li>Raspberry Pi</li></ul></div>
      <div><h3 class="label">Aviation</h3><ul><li>Commercial Pilot Licence, Aug 2026</li><li>Safety management systems</li><li>Human factors</li></ul></div>
    </div>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <div class="sec-head"><h2 class="wide">Contact</h2></div>
    <a class="contact-mail" href="mailto:{EMAIL}">{EMAIL}</a>
    <div class="contact-row">
      <a class="textlink" href="tel:+13657786181">+1 (365) 778-6181</a>
      <a class="textlink" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
    </div>
  </div>
</section>
</main>
'''
open(f"{OUT}/index.html", "w").write(page("index.html", "Luke Doney", "Luke Doney: electrical engineering student at Dalhousie, commercial pilot and lead propulsion engineer.", home))
print("built")
