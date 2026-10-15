#!/usr/bin/env python3
"""Génère les images Open Graph 1200x630 (images/og/*.jpg) à partir de images/*.webp.

Usage (depuis la racine du dépôt) :
    python3 -m venv .venv && .venv/bin/pip install Pillow
    .venv/bin/python scripts/generate_og_images.py
"""
import glob
import os

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "images")
OUT = os.path.join(SRC, "og")
W, H = 1200, 630


def main():
    os.makedirs(OUT, exist_ok=True)
    for path in sorted(glob.glob(os.path.join(SRC, "*.webp"))):
        im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        canvas = ImageOps.fit(im, (W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(30))
        canvas = ImageEnhance.Brightness(canvas).enhance(0.7)
        photo = ImageOps.contain(im, (W, H), Image.LANCZOS)
        canvas.paste(photo, ((W - photo.width) // 2, (H - photo.height) // 2))
        name = os.path.splitext(os.path.basename(path))[0] + ".jpg"
        canvas.save(os.path.join(OUT, name), "JPEG", quality=85, optimize=True, progressive=True)
        print(name)


if __name__ == "__main__":
    main()
