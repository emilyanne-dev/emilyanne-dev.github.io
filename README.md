# saralealberti.com

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

| | |
| --- | --- |
| Host | GitHub Pages, `main` branch, `/` root |
| Repo | `emilyanne-dev/emilyanne-dev.github.io` |
| Domain | `saralealberti.com` |

- `CNAME` holds the custom domain. **While it exists, `emilyanne-dev.github.io`
  redirects to `saralealberti.com`** — so if you need to preview on the
  github.io URL before DNS resolves, temporarily rename `CNAME`.
- `.nojekyll` stops GitHub from running Jekyll over the files.
- `SITE_URL` in `generate.py` must match the live origin or link previews
  (Open Graph) break. Re-run `generate.py` after changing it.

DNS at the registrar — four A records on the apex, one CNAME on `www`:

```
@     A      185.199.108.153
@     A      185.199.109.153
@     A      185.199.110.153
@     A      185.199.111.153
www   CNAME  emilyanne-dev.github.io
```

Because the site is served from the domain root, paths in `404.html` are
absolute. If this is ever moved to a project-page URL such as
`user.github.io/repo/`, those need revisiting.

## Asset weight

`optimize_assets.py` did a one-time pass taking `assets/images` from 63MB to
22MB. Re-run it after adding photography, then check its before/after table —
**re-encoding an already-compressed file can make it bigger.** Five files did
grow and were reverted; if that happens again, restore them with
`git checkout <commit> -- <path>`.
