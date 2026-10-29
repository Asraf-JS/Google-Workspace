# Google Workspace Training

## Shared Conventions

Use Asraf's shared [course conventions](https://github.com/Asraf-JS/training-book-kit/blob/main/COURSE-CONVENTIONS.md) for writing, fictional data, real screenshots and review. The user chose one repository for all six courses.

This package intentionally uses a static site build from Markdown for the six-course hub. The shared layout includes the existing kit's screenshot lightbox, chapter navigation, expected-result and side-window snippets. Previous/next navigation is scoped to one course. Do not replace this with six separate repositories or publish the current drafts as finished material.

## Structure

- Each numbered top-level course folder has a landing README and its own numbered chapter folders.
- Each chapter has README.md, prompts.md and an images directory. The reference chapter uses the same pattern.
- Shared fictional inputs live in shared/sample-files. Preserve source facts and generate calculations during the learner exercises.
- Six book configurations live in book/. The root build adapter reuses the pinned training-book-kit engine.
- _trainer and _local are private, ignored directories. Never put them in the participant site, public repository or public package.

## Where Things Stand

Version 0.4, review draft (29 October 2026). All 50 chapters are written drafts with staged author-reference screenshots: 1,201 lesson images (109 masterclass, 165 Docs, 173 Slides, 213 Foundation, 416 Advanced, 125 AI) and 1,198 retained full-window PNG sources. Practice files, six review books and the course site are present; the site is live on GitHub Pages.

Author-reference runs are not learner validation. Independent challenges, partner and reviewer checks, spoken delivery, account-specific feature checks and classroom timings remain pending; Asraf volunteered as the first pilot reviewer, and only the Lab 8 FAQ copy/paste check has been returned. AI Lab 5's audio audit was skipped after a 403 download and AI Lab 7's missing response is unscored. Planned durations are designed allocations, not measured times. See planning/FINAL-CHECKLIST.md and planning/VALIDATION-STATUS.md.

Book PDFs are committed, so every rebuild adds the whole file to git history. `tools/build-books.mjs` compresses each book with Ghostscript (`gs`, 200 ppi JPEG): install it before rebuilding, keep each PDF well under GitHub's 50 MB warning size, and only commit a rebuilt book when its content changed. See planning/VALIDATION-STATUS.md for public validation state, and ignored _local records for private demo identities. Rebuild the books and site after changing content. Inspect the final PDFs after changes. Keep status records accurate rather than claiming a draft chapter is validated.

## Docs Conventions Alignment

The Google Docs course (02-google-docs) now follows the training-book-kit chapter skeleton: a `> **Prompts:**` callout, `**Estimated time:** NN minutes` (the planned split follows on the same line), a `---` rule before What You Will Learn, Independent Practice with an Evidence to Hand Over subsection, and an italic caption under every screenshot. Prompts pages are titled `NN - Title: Prompts` and use `## Part N: Name` headings, with Session/Grounding lines above Gemini prompts. Google Slides (03-google-slides) follows the same pattern. Apply it to the remaining four courses once their screenshot branches are merged. Image file names keep the course prefix (`c02-...`) because six courses share chapter numbers. The participant site follows the kit's BRAND.md: logo.png at the root (copied from training-book-kit/brand), navy/teal/purple tokens in assets/site.css with a dark-mode set, and a teal-cloud sidebar in light mode. The six review books keep their Google product palettes (assets/book-palette*.css), as BRAND.md allows for books. program-flow.png is rendered by _design/render-program-flow.py in the brand colours.

## Reference-Run Notes

Keep numbered steps as plain learner instructions. Anything that reports what happened in the author's own run (page counts, observed UI, what was or wasn't tested in the reference) goes in a `> **Reference run:** ...` line directly under its step. The site builder gives these a quieter style. Don't delete them: they are the evidence behind each chapter's status.

## Next Production Work

Confirm the customer Workspace edition, enabled services, language and actual teaching timetable. Execute the untested lab routes in order, capture real screenshots, repair control wording and reconcile expected results with private assessment controls. Pilot the chapter timings. Publish only after the required review and the user's instruction to publish.

## Depth Revision 0.4

All 44 specialist chapters now include casework, independent changed requirements and evidence gates. See planning/specialist-depth-map.json and private _trainer/specialist-depth-controls.md. The cases and timing targets are written designs, not executed learner evidence. Keep baseline and scenario copies distinct. Never upload all specialist-case-cards.txt as authoritative project evidence in an AI lab.

## Repository Review

Use a branch and a pull request, following the shared course conventions. The initial six-course import was merged through pull request #1. GitHub Pages is live at https://asraf-js.github.io/Google-Workspace/ with Source set to GitHub Actions (October 2026). The Publish course site workflow runs on every push to main, so merging a pull request publishes it; keep unfinished work on branches. Branch deploys use Jekyll, which cannot fill this site's {{base}}, {{courseLinks}} and {{chapterNav}} placeholders, so never switch the Pages source back to Deploy from a branch. Pushing the source does not authorise granting Drive access or publishing native Google Sites.

## Screenshot Sources

Asraf wants uncropped screenshots retained for later framing adjustments. `_design/screenshots/full/` holds 1,198 retained sources at their captured dimensions with privacy masks, listed in `_design/screenshots/manifest.json`. A lossless pass (planning/IMAGE-OPTIMIZATION.md) re-encoded them without changing pixels. Never crop, resize or lossily re-encode those sources, and never expose unmasked originals. Three early workspace originals were not retained and need recapture. Two procedure-plan full frames include later surrounding context and must be recaptured before whole-frame use in participant notes. Keep existing approved lesson crops until an adjusted frame is reviewed.

Docs (165), Slides (173) and Sheets Foundation Lab 1 (26) lesson images are converted to the series style: 1600 px app window, red boxes and step numbers drawn by training-book-kit annotate-shots. See _design/shots/README.md for the pipeline and annotation rules before converting the next lab. Foundation Lab 1's old .jpg crops are still in the repo, unused, because the screenshot manifest and README link to them; delete them and update those two files when Foundation is converted. Every image must show only work that exists at its step: never replace an early screenshot with a completed artifact. For every new stage, retain the full application-window PNG before making a crop.

## Review Chain

Codex delivered the four remaining courses as a stack of pull requests (#13 to #51), each based on the previous branch. Do not flatten or rebase the stack. Main later gained the Docs and Slides annotated PNGs, the step fixes and book compression, so the cleanup branch on top of the stack merges main: the PNG conversion wins over the old JPEGs, and books keep the Ghostscript step. Merge the stack top-down only on Asraf's instruction. Codex's Windows authoring folder and private `work/` records are outside this repository; treat the repository as the source of truth and list changes Asraf needs to copy back.
