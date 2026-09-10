# emilysaralealberti.com

Portfolio site for Emily Sarale Alberti, Creative Producer.

Plain static HTML/CSS/JS — no build tools, no npm, no dependencies beyond
Python 3 (already on macOS). Every page is generated from JSON so content
edits never mean touching markup.

## Editing content

| To change | Edit |
| --- | --- |
| Films (order, credits, video IDs) | `data/films.json` |
| Social & Activations case studies | `data/social.json` |
| Photography grid | `data/photography.json` |
| Résumé | `data/resume.json` |
| Bio, contact card | `build_about()` in `generate.py` |
| Nav, ticker, footer | `templates/base.html` |
| Colors, type, layout | `:root` in `assets/css/style.css` |

Then rebuild:

```sh
python3 generate.py
```

That rewrites `index.html`, `social.html`, `photography.html`, `about.html`,
`resume.html`, `404.html`, and everything in `films/` and `social/`.
**Never edit those files by hand** — the next build overwrites them.

## Résumé PDF

The Download PDF button on the About page serves a real file at
`assets/files/emily-sarale-alberti-resume.pdf`. It is *not* produced by
`generate.py`, so after any résumé change run both:

```sh
python3 generate.py && ./make_resume_pdf.sh
```

Otherwise the web résumé updates but the download still serves the old one.

## Local preview

```sh
python3 -m http.server 4321
```

Then open http://localhost:4321. Hard-refresh (Cmd+Shift+R) after CSS edits —
browsers cache `style.css` aggressively.

## Deployment

Hosted on GitHub Pages from the `main` branch, repo root.

- `CNAME` holds the custom domain. Deleting it reverts to the github.io URL.
- `.nojekyll` stops GitHub from running Jekyll over the files.
- `SITE_URL` in `generate.py` must match the live origin or link previews
  (Open Graph) break. Re-run `generate.py` after changing it.

Because the site is served from the domain root, paths in `404.html` are
absolute. If this is ever moved to a project-page URL such as
`user.github.io/repo/`, those need revisiting.
