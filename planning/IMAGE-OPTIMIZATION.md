# Lossless image optimization

Completed 29 October 2026 after staged capture coverage reached all 50 draft chapters.

The lesson JPEG figures below were measured before the review chain merged main. Main had already replaced the 338 Docs and Slides lesson JPEGs with annotated 1600 px PNGs (see _design/shots/README.md), so those 338 optimized JPEGs were dropped in the merge. The retained PNG sources were not affected.

| Collection | Files | Before | After | Saved |
| --- | ---: | ---: | ---: | ---: |
| Retained PNG sources | 1,198 | 547,970,228 bytes | 451,903,618 bytes | 17.53% |
| Lesson JPEGs | 1,201 | 213,913,714 bytes | 175,534,916 bytes | 17.94% |

Total image bytes: 761,883,942 → 627,438,534; 134,445,408 bytes saved (17.65%).

Every candidate was decoded and compared with its original: dimensions and SHA-256 of RGBA pixels must match. ICC, EXIF, DPI, gamma, sRGB and chromaticity metadata were checked. Candidates with a metadata difference or no size reduction retained the original file. Full dimensions, filenames, crop coordinates and screenshot stage order are preserved. Private unoptimized backups remain outside the published package.

PNG: [pyoxipng](https://github.com/nfrasser/pyoxipng) 9.1.1, level 2; alpha optimization, bit-depth/color/palette/grayscale reductions disabled; no chunks stripped and interlacing preserved. JPEG: [jpegtran-bin](https://github.com/imagemin/jpegtran-bin) 7.0.0 Windows x64 vendor binary, `-copy all -optimize`; no re-encoding quality setting.

The screenshot manifest records the new source PNG hashes. A private per-file audit records before/after hashes, byte sizes, dimensions and decoded-pixel hashes. Existing capture privacy masks remain in place. This changes current file encodings; Git history is preserved.

## Rebuilt artifacts

All six books were rebuilt: 73, 118, 144, 144, 304 and 105 pages (888 total). Every rebuilt page matched its baseline at 0.4-scale PDF rendering and in extracted-text SHA-256. Representative rendered pages were also visually inspected. The site and ZIP packages were refreshed from the optimized sources.
