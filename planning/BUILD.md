# Build and Publication

## Local Preview

Install Node.js 20 or later, run `npm install`, then `npm run build:site`. This writes the static preview to `_site/`. Run `npm run serve` and open the printed local address. No cloud publication occurs.

The included manual GitHub Pages workflow builds the static site from the Markdown and shared layout. It uses the repository base path reported by Pages, so the six course sections can share one site. The layout reuses the established kit snippets. No Jekyll service or cloud site has been created. Set an online book resource URL after the eventual repository exists; until then book download links are relative to this package. Do not publish a review draft as a finished course.

## Course Books

Run `npx playwright install chromium` once, then `npm run build:books`. This uses Asraf's shared training-book-kit, with a small local adapter for Google branding, unpublished relative file links and the selected Chromium executable. The shared engine and series layout are reused. Six course configurations live in `book/`, and generated PDFs go in `books/`.

Set `TRAINING_BOOK_KIT_DIR` to an existing installed kit only when building in a managed environment. Set `TRAINING_CHROMIUM_PATH` only to an existing Chromium executable when its default download is unavailable. Normal installations need neither variable.

The adapter validates the source patterns before replacing them; an incompatible kit update stops with a clear error instead of silently producing an incorrect book. The tested kit revision is recorded in package.json.

## Source and Private Files

Keep `_trainer/`, `_local/`, browser profiles, node_modules and generated preview/build intermediates out of Git. Build data with `_design/generate-samples.mjs` only in a development environment containing the documented Codex artifact runtime. The checked-in starter files can be used without that generator.

`npm run check` checks local links, chapter inventory and source structure. It does not execute Google Workspace labs. Keep the published validation status accurate.
