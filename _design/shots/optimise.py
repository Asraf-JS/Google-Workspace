"""Shrink annotated lesson PNGs with a 256-colour palette (no dithering).

  python _design/shots/optimise.py 02-google-docs/01-document-sources

Run after annotate-shots. Screenshots of app windows use few colours, so the palette
keeps text and the red highlight sharp while cutting file size by about two thirds.
"""
import sys
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[2]
for chapter in sys.argv[1:]:
    for f in sorted((root / chapter / "images").glob("*.png")):
        before = f.stat().st_size
        im = Image.open(f)
        if im.mode != "P":
            im.convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)
        print(f"  {f.relative_to(root)} {before // 1024} KB -> {f.stat().st_size // 1024} KB")
