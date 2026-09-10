#!/usr/bin/env python3
"""Rebuilds index.html, photography.html, about.html and films/*.html
from data/films.json and data/photography.json.

To add a new film: add an object to data/films.json, then run:
    python3 generate.py
"""
import json
import os
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


BASE = read("templates/base.html")
YEAR = str(datetime.date.today().year)

# Absolute origin of the live site, no trailing slash. Needed because
# Open Graph requires absolute URLs — link previews stay blank until this
# is set. Fill in once the domain is pointed at GitHub Pages, e.g.
# "https://saralealberti.com", then re-run this script.
SITE_URL = "https://saralealberti.com"


def render_page(title, content, prefix="", active=""):
    html = BASE
    html = html.replace("{{SITE_URL}}", SITE_URL)
    html = html.replace("{{TITLE}}", title)
    html = html.replace("{{CONTENT}}", content)
    html = html.replace("{{PREFIX}}", prefix)
    html = html.replace("{{YEAR}}", YEAR)
    html = html.replace("{{ACTIVE_FILMS}}", "active" if active == "films" else "")
    html = html.replace("{{ACTIVE_SOCIAL}}", "active" if active == "social" else "")
    html = html.replace("{{ACTIVE_PHOTO}}", "active" if active == "photo" else "")
    html = html.replace("{{ACTIVE_ABOUT}}", "active" if active == "about" else "")
    return html


def build_films_index(films):
    cards = []
    for f in films:
        extra = f' &middot; {f["extra"]}' if f.get("extra") else ""
        cards.append(f"""
      <a class="film-card" href="films/{f['slug']}.html">
        <div class="frame">
          <div class="thumb-wrap">
            <img src="assets/images/films/{f['thumb']}" alt="{f['title']}" loading="lazy">
            <div class="play-badge">&#9654;</div>
          </div>
        </div>
        <div class="film-meta">
          <h3>{f['title']}</h3>
          <span class="tag">{f['client']}</span>
        </div>
      </a>""")

    content = f"""
  <section class="films-grid">{''.join(cards)}
  </section>"""
    write("index.html", render_page("Emily Sarale Alberti — Films", content, "", "films"))


def build_film_pages(films):
    for i, f in enumerate(films):
        prev_f = films[i - 1] if i > 0 else None
        next_f = films[i + 1] if i < len(films) - 1 else None

        video = f.get("video")
        if not video:
            embed = f'<img src="../assets/images/films/{f["thumb"]}" alt="{f["title"]}" style="width:100%; height:100%; object-fit: cover;">'
        elif video["type"] == "youtube":
            embed = f'<iframe src="https://www.youtube.com/embed/{video["id"]}" title="{f["title"]}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        elif video["type"] == "vimeo":
            embed = f'<iframe src="https://player.vimeo.com/video/{video["id"]}" title="{f["title"]}" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>'
        else:
            embed = f'<video src="../assets/videos/films/{video["id"]}" poster="../assets/images/films/{f["thumb"]}" controls playsinline></video>'

        pending_note = '<p class="eyebrow" style="margin-top: 0.75rem;">&#10035; Web-ready video coming soon</p>' if not video else ""

        extra_pill = f'<span class="credit-pill"><b>{f["extra"]}</b></span>' if f.get("extra") else ""

        nav_bits = []
        if prev_f:
            nav_bits.append(f'<a class="pill-btn" href="{prev_f["slug"]}.html">&larr; {prev_f["title"]}</a>')
        else:
            nav_bits.append("<span></span>")
        if next_f:
            nav_bits.append(f'<a class="pill-btn" href="{next_f["slug"]}.html">{next_f["title"]} &rarr;</a>')
        else:
            nav_bits.append('<a class="pill-btn" href="../index.html">All Films &rarr;</a>')

        content = f"""
  <section class="case-study">
    <p class="eyebrow"><a href="../index.html">&larr; All Films</a></p>
    <h1 style="font-style: italic; margin-top: 0.6rem;">{f['title']}</h1>
    <div class="ticket" style="margin-top: 1.5rem;">
      <div class="video-frame">
        {embed}
      </div>
      {pending_note}
      <div class="credits">
        <span class="credit-pill"><b>Client</b> &mdash; {f['client']}</span>
        <span class="credit-pill"><b>Director</b> &mdash; {f['director']}</span>
        <span class="credit-pill"><b>Production Co.</b> &mdash; {f['production']}</span>
        {extra_pill}
      </div>
    </div>
    <div class="case-nav">
      {nav_bits[0]}
      {nav_bits[1]}
    </div>
  </section>"""
        write(f"films/{f['slug']}.html", render_page(f"{f['title']} — Emily Sarale Alberti", content, "../", "films"))


def build_social_index(items):
    cards = []
    for s in items:
        cards.append(f"""
      <a class="film-card film-card--fit" href="social/{s['slug']}.html">
        <div class="frame">
          <div class="thumb-wrap">
            <img src="assets/images/social/{s['thumb']}" alt="{s['title']}" loading="lazy">
            <div class="play-badge">&#9654;</div>
          </div>
        </div>
        <div class="film-meta">
          <h3>{s['title']}</h3>
          <span class="tag">{s['client']}</span>
        </div>
      </a>""")

    content = f"""
  <section class="films-grid">{''.join(cards)}
  </section>"""
    write("social.html", render_page("Emily Sarale Alberti — Social & Activations", content, "", "social"))


def build_social_pages(items):
    for i, s in enumerate(items):
        prev_s = items[i - 1] if i > 0 else None
        next_s = items[i + 1] if i < len(items) - 1 else None

        paragraphs = "".join(f"<p>{p}</p>" for p in s["body"].split("\n\n"))

        video = s["video"]
        if video["type"] == "youtube":
            embed = f'<iframe src="https://www.youtube.com/embed/{video["id"]}" title="{s["title"]}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        elif video["type"] == "vimeo":
            embed = f'<iframe src="https://player.vimeo.com/video/{video["id"]}" title="{s["title"]}" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>'
        else:
            embed = f'<video src="../assets/videos/social/{video["id"]}" poster="../assets/images/social/{s["thumb"]}" controls playsinline></video>'

        awards = s.get("awards") or []
        awards_pill = (
            f'\n        <span class="credit-pill"><b>Awards</b> &mdash; {", ".join(awards)}</span>'
            if awards else ""
        )

        nav_bits = []
        if prev_s:
            nav_bits.append(f'<a class="pill-btn" href="{prev_s["slug"]}.html">&larr; {prev_s["title"]}</a>')
        else:
            nav_bits.append("<span></span>")
        if next_s:
            nav_bits.append(f'<a class="pill-btn" href="{next_s["slug"]}.html">{next_s["title"]} &rarr;</a>')
        else:
            nav_bits.append('<a class="pill-btn" href="../social.html">All Social &amp; Activations &rarr;</a>')

        content = f"""
  <section class="case-study">
    <p class="eyebrow"><a href="../social.html">&larr; All Social &amp; Activations</a></p>
    <h1 style="font-style: italic; margin-top: 0.6rem;">{s['title']}</h1>
    <div class="ticket" style="margin-top: 1.5rem;">
      <div class="video-frame">
        {embed}
      </div>
      <div class="credits">
        <span class="credit-pill"><b>Client</b> &mdash; {s['client']}</span>
        <span class="credit-pill"><b>Results</b> &mdash; {s['result']}</span>{awards_pill}
      </div>
    </div>
    <div class="about-bio" style="margin-top: 2rem; max-width: 44em;">
      {paragraphs}
    </div>
    <div class="case-nav">
      {nav_bits[0]}
      {nav_bits[1]}
    </div>
  </section>"""
        write(f"social/{s['slug']}.html", render_page(f"{s['title']} — Emily Sarale Alberti", content, "../", "social"))


def build_photography(photos):
    items = []
    for i, p in enumerate(photos):
        rot = [-2, 1.5, -1, 2, -1.5, 1][i % 6]
        items.append(f"""
    <div class="photo-item" style="--r: {rot}deg">
      <img src="assets/images/photography/{p['file']}" alt="{p['caption']}" loading="lazy">
    </div>""")

    content = f"""
  <section class="photo-grid">{''.join(items)}
  </section>
  <div class="lightbox">
    <button class="lightbox-close">&times;</button>
    <img src="" alt="">
  </div>"""
    write("photography.html", render_page("Emily Sarale Alberti — Photography", content, "", "photo"))


def build_about():
    content = f"""
  <section class="about-section">
    <h1>About Emily</h1>
    <div class="about-grid">
      <div class="about-col">
        <div class="about-bio">
          <p>Emily is a Creative Producer based in San Francisco in the marketing and advertising space with almost a decade of experience. Raised in a farming family, she currently enjoys working with food, beverage and beyond at Instacart as part of Local Produce, Instacart's in-house creative agency. In her free time, she enjoys experimenting in the kitchen. Have a recipe to share? Please drop below.</p>
        </div>
        <div class="about-honor">
          <span class="credit-pill"><b>Local Produce</b> &mdash; Ad Age 2026 In-House Agency of the Year</span>
        </div>
        <div class="contact-card">
          <p class="eyebrow" style="color: var(--cocoa)">Say Hello</p>
          <p>Got a project, a recipe, or just want to say hi?</p>
          <a class="btn-accent" href="mailto:emilyannesarale@gmail.com">Email Emily &rarr;</a>
        </div>
        <div class="contact-card">
          <p class="eyebrow" style="color: var(--cocoa)">R&eacute;sum&eacute;</p>
          <div class="card-actions">
            <a class="btn-accent" href="resume.html" target="_blank" rel="noopener">View R&eacute;sum&eacute; &rarr;</a>
            <a class="pill-btn" href="assets/files/emily-sarale-alberti-resume.pdf" download>&#8681; Download PDF</a>
          </div>
        </div>
      </div>
      <figure class="about-portrait">
        <img src="assets/images/about/emily.png" alt="Emily Sarale Alberti">
      </figure>
    </div>
  </section>"""
    write("about.html", render_page("Emily Sarale Alberti — About", content, "", "about"))


def build_404():
    content = """
  <section class="about-section" style="text-align: center;">
    <h1 style="color: var(--cocoa); margin-inline: auto;">This page took a wrong turn</h1>
    <p class="eyebrow" style="margin-top: 1.5rem;">&#10035; Error 404</p>
    <div class="case-nav" style="justify-content: center; gap: 0.6rem; flex-wrap: wrap;">
      <a class="pill-btn" href="/index.html">Films</a>
      <a class="pill-btn" href="/social.html">Social &amp; Activations</a>
      <a class="pill-btn" href="/photography.html">Photography</a>
      <a class="pill-btn" href="/about.html">About</a>
    </div>
  </section>"""
    write("404.html", render_page("Page not found — Emily Sarale Alberti", content, "/", ""))


def build_resume(r):
    contact = "".join(
        f'<li><b>{c["label"]}</b>'
        + (f'<a href="{c["href"]}">{c["value"]}</a>' if c.get("href") else c["value"])
        + "</li>"
        for c in r["contact"]
    )
    skills = "".join(f"<li>{s}</li>" for s in r["skills"])
    tools = "".join(f'<span class="credit-pill">{t}</span>' for t in r["tools"])

    jobs = []
    for j in r["experience"]:
        bullets = "".join(f"<li>{b}</li>" for b in j["bullets"])
        jobs.append(f"""
        <article class="r-job">
          <div class="r-job-head">
            <div>
              <span class="r-co">{j['company']}</span>
              <h3>{j['title']}</h3>
            </div>
            <span class="r-dates">{j['dates']}</span>
          </div>
          <ul>{bullets}</ul>
        </article>""")

    ticker = "".join(
        f"<span>✳ {bit}</span>"
        for bit in [
            "Commercials &amp; Branded Films",
            "Social Media",
            "Events &amp; Activations",
            "Photography",
        ]
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{r['name']} — Resume</title>
<meta name="description" content="{r['name']} — {r['role']}. Resume." />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;1,500;1,600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css" />
<link rel="stylesheet" href="assets/css/resume.css" />
</head>
<body class="resume-body">
  <div class="print-hint">
    <span>Print or save as PDF at US Letter, margins <b>None</b>, background graphics <b>on</b>. &nbsp;<a href="index.html">&larr; Back to the site</a></span>
    <button onclick="window.print()">Save as PDF</button>
  </div>

  <div class="sheet">
    <header class="r-head">
      <h1>{r['name']}</h1>
      <p class="r-role">{r['role']}</p>
    </header>

    <div class="r-ticker">{ticker}</div>

    <div class="r-body">
      <aside class="r-side">
        <section class="r-block">
          <h2>Contact</h2>
          <ul class="r-contact">{contact}</ul>
        </section>
        <section class="r-block">
          <h2>Education</h2>
          <p class="r-edu"><strong>{r['education']['degree']}</strong><span>{r['education']['school']}</span></p>
        </section>
        <section class="r-block">
          <h2>Skills</h2>
          <ul class="r-list">{skills}</ul>
        </section>
        <section class="r-block">
          <h2>Tools</h2>
          <div class="r-pills">{tools}</div>
        </section>
      </aside>

      <main class="r-main">
        <section class="r-block">
          <h2>About</h2>
          <p class="r-about">{r['about']}</p>
        </section>
        <section class="r-block">
          <h2>Work Experience</h2>{''.join(jobs)}
        </section>
      </main>
    </div>
  </div>
</body>
</html>
"""
    write("resume.html", html)


def build_sitemap(films, social):
    """Sitemap and robots.txt so search engines can find every page.

    Skips 404.html — an error page shouldn't be indexed.
    """
    paths = ["", "social.html", "photography.html", "about.html", "resume.html"]
    paths += [f"films/{f['slug']}.html" for f in films]
    paths += [f"social/{s['slug']}.html" for s in social]

    today = datetime.date.today().isoformat()
    urls = "".join(
        f"\n  <url><loc>{SITE_URL}/{p}</loc><lastmod>{today}</lastmod></url>"
        for p in paths
    )
    write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}
</urlset>
""")

    write("robots.txt", f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
""")


if __name__ == "__main__":
    films = json.loads(read("data/films.json"))
    photos = json.loads(read("data/photography.json"))
    social = json.loads(read("data/social.json"))
    resume = json.loads(read("data/resume.json"))
    build_films_index(films)
    build_film_pages(films)
    build_social_index(social)
    build_social_pages(social)
    build_photography(photos)
    build_about()
    build_resume(resume)
    build_404()
    build_sitemap(films, social)
    print(f"Built index.html, social.html, photography.html, about.html, resume.html, 404.html, sitemap.xml, robots.txt, {len(films)} film pages, and {len(social)} social pages.")
