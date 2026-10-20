# Production Assets

Use this directory for reproducible fictional data generators, programme-flow source and screenshot specifications. Keep account identifiers, browser sessions and raw private captures outside tracked content.

The first screenshot plan is in the reference chapter's SCREENSHOT comments. Empty image folders are intentional until real screenshots have been captured. No fake screenshots are included.

The [screenshot editing library](./screenshots/README.md) keeps 159 retained source images at their original dimensions, with privacy masks. Its manifest maps sources to the participant crops and records missing originals and focused captures. Use it to adjust framing without losing the available capture area. Future captures must retain the whole application window before cropping.

`generate-samples.mjs` reproduces the fictional workbook inputs and independent control figures using the Codex artifact-tool runtime. It requires that runtime's package directory to be available through Node module resolution. The checked-in XLSX/CSV inputs do not require the generator to be run. Private answer controls are written into the ignored `_trainer/` directory.
