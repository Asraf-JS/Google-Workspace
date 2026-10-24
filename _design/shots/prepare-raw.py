"""Scale the retained full-window sources to the series' 1600 px width for annotate-shots.

  python _design/shots/prepare-raw.py 02-google-docs/01-document-sources

Reads _design/screenshots/full/<course>/<chapter>/*.png and writes
_design/shots/raw/<course>/<chapter>/*.png (git-ignored, regenerated on demand).
Box and crop coordinates in _design/shots/<course>/<chapter>.json use these
1600 px images, so the 3 px red outline matches the other course sites.
"""
import sys
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[2]
WIDTH = 1600
for chapter in sys.argv[1:]:
    src = root / "_design/screenshots/full" / chapter
    out = root / "_design/shots/raw" / chapter
    out.mkdir(parents=True, exist_ok=True)
    for f in sorted(src.glob("*.png")):
        im = Image.open(f).convert("RGB")
        if im.width != WIDTH:
            im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
        im.save(out / f.name)
        print(f"  {chapter}/{f.name} {im.width}x{im.height}")
