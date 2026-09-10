#!/usr/bin/env python3
"""One-time asset optimization pass for emily-portfolio.

Photos stored as oversized PNGs get converted to JPEG (callers must update
the JSON `thumb` fields). GIFs are reduced in dimension with an adaptive
palette. Everything else is resized in place.
"""
import os
import glob
from PIL import Image, ImageOps

ROOT = "/Users/emilysarale/emily-portfolio"
IMG = os.path.join(ROOT, "assets/images")

renames = {}   # old basename -> new basename
report = []


def kb(p):
    return os.path.getsize(p) // 1024


def fit(im, cap):
    """Downscale so the longest edge is at most `cap`. Never upscales."""
    w, h = im.size
    if max(w, h) <= cap:
        return im
    s = cap / max(w, h)
    return im.resize((round(w * s), round(h * s)), Image.LANCZOS)


def save_jpeg(im, out, q):
    im = im.convert("RGB")
    im.save(out, "JPEG", quality=q, optimize=True, progressive=True)


def do_jpeg(path, cap=1600, q=82):
    before = kb(path)
    im = ImageOps.exif_transpose(Image.open(path))
    save_jpeg(fit(im, cap), path, q)
    report.append((before, kb(path), os.path.relpath(path, ROOT)))


def do_png_to_jpeg(path, cap=1400, q=86):
    """Photos wearing a PNG costume. Flatten alpha onto cream, re-encode."""
    before = kb(path)
    im = ImageOps.exif_transpose(Image.open(path))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (251, 233, 200, 255))  # --cream
        im = Image.alpha_composite(bg, im)
    out = os.path.splitext(path)[0] + ".jpg"
    save_jpeg(fit(im, cap), out, q)
    if out != path:
        os.remove(path)
        renames[os.path.basename(path)] = os.path.basename(out)
    report.append((before, kb(out), os.path.relpath(out, ROOT)))


def do_png(path, cap=1500, colors=None):
    """Flat graphics with baked-in type — stay PNG so text edges stay hard."""
    before = kb(path)
    im = Image.open(path)
    im = fit(im, cap)
    if colors:
        im = im.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=colors)
    im.save(path, "PNG", optimize=True)
    report.append((before, kb(path), os.path.relpath(path, ROOT)))


def do_gif(path, cap=900, colors=128):
    before = kb(path)
    im = Image.open(path)
    frames, durations = [], []
    for i in range(getattr(im, "n_frames", 1)):
        im.seek(i)
        durations.append(im.info.get("duration", 100))
        f = fit(im.convert("RGBA"), cap)
        frames.append(f.convert("P", palette=Image.ADAPTIVE, colors=colors))
    frames[0].save(
        path, "GIF", save_all=True, append_images=frames[1:],
        loop=0, duration=durations, optimize=True, disposal=2,
    )
    report.append((before, kb(path), os.path.relpath(path, ROOT)))


# ---- photography: plain photos, biggest win is dimension ----
for p in sorted(glob.glob(f"{IMG}/photography/*.jpg")):
    do_jpeg(p, cap=1600, q=82)
for p in sorted(glob.glob(f"{IMG}/photography/*.gif")):
    do_gif(p, cap=900, colors=128)

# ---- films: video frames saved as PNG, convert to JPEG ----
for p in sorted(glob.glob(f"{IMG}/films/*.png")):
    do_png_to_jpeg(p, cap=1400, q=86)
for p in sorted(glob.glob(f"{IMG}/films/*.jpg")):
    do_jpeg(p, cap=1400, q=86)

# ---- social: title cards with type, keep PNG ----
for p in sorted(glob.glob(f"{IMG}/social/*.png")):
    do_png(p, cap=1500)
for p in sorted(glob.glob(f"{IMG}/social/*.jpg")):
    do_jpeg(p, cap=1500, q=86)

# ---- portrait: stays PNG so generate.py needs no edit ----
do_png(f"{IMG}/about/emily.png", cap=900)

report.sort(reverse=True)
print(f"{'before':>9} {'after':>9}  file")
for b, a, name in report:
    print(f"{b:>7}KB {a:>7}KB  {name}")
tb, ta = sum(r[0] for r in report), sum(r[1] for r in report)
print(f"\nTOTAL  {tb/1024:.1f}MB -> {ta/1024:.1f}MB  ({100 - ta * 100 // tb}% smaller)")

# ---- point films.json at the new .jpg names ----
if renames:
    import json

    fp = os.path.join(ROOT, "data/films.json")
    with open(fp, encoding="utf-8") as f:
        films = json.load(f)
    changed = 0
    for film in films:
        if film.get("thumb") in renames:
            film["thumb"] = renames[film["thumb"]]
            changed += 1
    with open(fp, "w", encoding="utf-8") as f:
        json.dump(films, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\nRenamed {len(renames)} file(s); updated {changed} thumb "
          f"reference(s) in data/films.json.")
    print("Now run: python3 generate.py")
