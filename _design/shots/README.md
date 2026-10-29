# Annotated Screenshots

Lesson screenshots follow the series style from training-book-kit: the real app window at 1600 px wide, a 3 px red (232, 17, 35) box around each thing to click and a numbered circle for the step it belongs to. The boxes are drawn by the kit's `annotate-shots`, so they can be moved and redrawn without recapturing.

Converted so far: all eight Google Docs labs (165 images), all eight Google Slides labs (173 images), all eight Sheets Foundation labs (213 images) and all six masterclass labs (109 images). Three masterclass Lab 1 images have no retained original, so they are annotated from their existing crops at their own size. The other courses still use the earlier hand-cropped `.jpg` images.

## Files

| Path | What it is |
|---|---|
| `_design/screenshots/full/<course>/<chapter>/` | Retained full-window captures with privacy masks (the clean sources) |
| `_design/shots/raw/<course>/<chapter>/` | The same captures scaled to 1600 px. Git ignores this folder; `prepare-raw.py` regenerates it |
| `_design/shots/<course>/<chapter>.json` | Crop, boxes and arrows for each screenshot, in 1600 px coordinates |
| `<course>/<chapter>/images/*.png` | The annotated lesson images the notes and books use |

## Rebuild a Chapter

From the repository root, after `npm install`:

```text
python _design/shots/prepare-raw.py 02-google-docs/01-document-sources
node node_modules/training-book-kit/bin/annotate-shots.mjs _design/shots/02-google-docs/01-document-sources.json
python _design/shots/optimise.py 02-google-docs/01-document-sources
```

`annotate-shots` only overwrites a lesson image that already exists. For a new screenshot, copy its 1600 px file from `_design/shots/raw/` into the chapter's `images/` folder first. Add `c02-01-name.png` (or another single file name) after the JSON path to redraw just that image.

`optimise.py` converts each PNG to a 256-colour palette, which keeps text and the red highlight sharp and makes the files about a third of the size.

## Annotation Rules

- Each box is `[x0, y0, x1, y1, step]`, with the step number matching the numbered instruction in that section. Leave the step out for a plain box. A sixth value (`"below"`, `"left"` and so on) moves the number when it would cover a label.
- Box whole paragraphs, tables or controls. In dense text (lines about 13 px apart) a box around one line cuts through its neighbours, so point at the line with an arrow instead: `"arrows": [[x0, y0, x1, y1]]`, head at the second point.
- Keep at least 12 px between neighbouring boxes.
- Crop away empty margins only. Google Docs frames use `[0, 0, 1440, 680]`, which drops the blank strip to the right of the app.
