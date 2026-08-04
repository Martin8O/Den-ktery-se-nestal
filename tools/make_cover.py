# -*- coding: utf-8 -*-
"""Cover for 'Nedoložení' — paper with a single red stitch seam (E4).

1600x2560 px (1:1.6, Kindle-friendly). Aged-paper field, faint file-stamp
ring, a torn seam running down the page held by red thread stitches, title
set in Palatino Linotype. Pure Pillow, no external assets.
"""
import math
import random
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1600, 2560
random.seed(1978)

PAPER = (238, 232, 218)
PAPER_DARK = (216, 208, 190)
INK = (38, 36, 40)
INK_SOFT = (90, 86, 92)
THREAD = (158, 34, 34)
THREAD_DARK = (110, 20, 20)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# --- paper: vertical tone drift + grain -----------------------------------
top, bottom = (242, 237, 224), (222, 214, 197)
for y in range(H):
    t = y / H
    c = tuple(int(a + (b - a) * t) for a, b in zip(top, bottom))
    d.line([(0, y), (W, y)], fill=c)

grain = Image.new("L", (W // 2, H // 2))
grain.putdata([random.randint(117, 138) for _ in range((W // 2) * (H // 2))])
grain = grain.resize((W, H)).filter(ImageFilter.GaussianBlur(0.6))
img = Image.composite(Image.new("RGB", (W, H), PAPER_DARK), img,
                      grain.point(lambda v: max(0, (v - 127) * 3)))
d = ImageDraw.Draw(img)

# faint blotches (age)
blot = Image.new("L", (W, H), 0)
bd = ImageDraw.Draw(blot)
for _ in range(26):
    x, y = random.randint(0, W), random.randint(0, H)
    r = random.randint(60, 260)
    bd.ellipse([x - r, y - r, x + r, y + r], fill=random.randint(6, 16))
blot = blot.filter(ImageFilter.GaussianBlur(90))
img = Image.composite(Image.new("RGB", (W, H), (206, 196, 176)), img, blot)
d = ImageDraw.Draw(img)

# --- faint archival stamp ring, top-right ---------------------------------
stamp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
cx, cy, r = W - 330, 430, 210
sd.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(120, 60, 50, 46), width=7)
sd.ellipse([cx - r + 26, cy - r + 26, cx + r - 26, cy + r - 26],
           outline=(120, 60, 50, 40), width=3)
try:
    fstamp = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 40)
    sd.text((cx, cy - 26), "F-2025-0714-K", font=fstamp,
            fill=(120, 60, 50, 52), anchor="mm")
    sd.text((cx, cy + 30), "REVIZE: 1", font=fstamp,
            fill=(120, 60, 50, 46), anchor="mm")
except OSError:
    pass
stamp = stamp.rotate(-14, center=(cx, cy), resample=Image.BICUBIC)
img = Image.alpha_composite(img.convert("RGBA"), stamp).convert("RGB")
d = ImageDraw.Draw(img)

# --- the seam: a torn line down the page, stitched shut -------------------
# seam path (slightly wandering vertical line, right of centre)
seam_x = []
x = W * 0.62
for y in range(0, H + 1, 8):
    x += random.uniform(-3.4, 3.4)
    x = max(W * 0.56, min(W * 0.68, x))
    seam_x.append((x, y))

# shadow under the seam (the tear)
tear = Image.new("RGBA", (W, H), (0, 0, 0, 0))
td = ImageDraw.Draw(tear)
td.line(seam_x, fill=(70, 60, 52, 90), width=14)
tear = tear.filter(ImageFilter.GaussianBlur(10))
img = Image.alpha_composite(img.convert("RGBA"), tear).convert("RGB")
d = ImageDraw.Draw(img)
# the tear line itself: darker, slightly ragged
for (x0, y0), (x1, y1) in zip(seam_x, seam_x[1:]):
    d.line([(x0, y0), (x1, y1)], fill=(96, 84, 72), width=4)

# stitches: red thread crossing the seam
def seam_at(y):
    i = min(len(seam_x) - 1, max(0, int(y / 8)))
    return seam_x[i][0]

y = 140
while y < H - 120:
    step = random.randint(96, 128)
    sx = seam_at(y)
    ang = random.uniform(-0.35, 0.35)
    dx, dy = 58 * math.cos(ang), 58 * math.sin(ang) + 26
    p1 = (sx - dx, y - dy)
    p2 = (sx + dx, y + dy)
    # thread shadow, then thread
    d.line([p1, p2], fill=THREAD_DARK, width=13)
    d.line([(p1[0] - 2, p1[1] - 2), (p2[0] - 2, p2[1] - 2)], fill=THREAD, width=9)
    # needle holes
    for px, py in (p1, p2):
        d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=(120, 106, 88))
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=(66, 56, 48))
    y += step

# one trailing thread at the bottom stitch, with a needle
tail_y = y - random.randint(96, 128)
sx = seam_at(tail_y)
pts = [(sx + 44, tail_y + 30)]
tx, ty = pts[0]
for i in range(1, 26):
    tx += 9 + 5 * math.sin(i * 0.7)
    ty += 26 + 7 * math.cos(i * 0.5)
    pts.append((tx, ty))
d.line(pts, fill=THREAD, width=8, joint="curve")
# needle at thread end
nx, ny = pts[-1]
needle_ang = 0.9
nl = 150
ex, ey = nx + nl * math.cos(needle_ang), ny + nl * math.sin(needle_ang)
d.line([(nx, ny), (ex, ey)], fill=(150, 148, 152), width=10)
d.line([(nx, ny), (ex, ey)], fill=(196, 195, 199), width=5)
d.ellipse([nx - 9, ny - 9, nx + 9, ny + 9], outline=(150, 148, 152), width=5)

# --- typography -----------------------------------------------------------
def font(path, size):
    return ImageFont.truetype(path, size)

try:
    f_title = font("C:/Windows/Fonts/pala.ttf", 208)
    f_author = font("C:/Windows/Fonts/pala.ttf", 66)
    f_sub = font("C:/Windows/Fonts/palai.ttf", 56)
except OSError:
    f_title = font("C:/Windows/Fonts/georgia.ttf", 208)
    f_author = font("C:/Windows/Fonts/georgia.ttf", 66)
    f_sub = font("C:/Windows/Fonts/georgiai.ttf", 56)

# title, two lines to sit left of/over the seam
tx0 = 150
ty0 = 950
d.text((tx0 + 4, ty0 + 6), "NEDO-", font=f_title, fill=(0, 0, 0, 60))
d.text((tx0, ty0), "NEDO-", font=f_title, fill=INK)
d.text((tx0 + 4, ty0 + 216), "LOŽENÍ", font=f_title, fill=(0, 0, 0, 60))
d.text((tx0, ty0 + 210), "LOŽENÍ", font=f_title, fill=INK)

# thin rule + subtitle line
d.line([(tx0 + 6, ty0 + 490), (tx0 + 560, ty0 + 490)], fill=INK_SOFT, width=4)
d.text((tx0 + 6, ty0 + 530), "román", font=f_sub, fill=INK_SOFT)

# author, bottom left
d.text((tx0 + 6, H - 260), "Martin", font=f_author, fill=INK)

out = sys.argv[1] if len(sys.argv) > 1 else "D:/Projekty/Scifi/book/cover.png"
img.save(out, "PNG")
print("cover written:", out, img.size)
