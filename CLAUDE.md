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

Version 0.4, 19 October 2026. All 50 chapter notes and companion prompt pages are written drafts. Fictional starter workbooks, CSV inputs and source texts, six review books and a static course-site builder are present.

There are 231 real stage captures: 109 across the six masterclass labs and 122 across Docs Labs 1-5. Thirty-nine specialist routes remain uncaptured. Docs Lab 5 core is complete with a recorded manual comparison fallback; native generated comparison output remains unverified. The masterclass hub's desktop and phone Preview remain blank. Independent learner/reviewer challenges and classroom timing pilots remain pending. Recorded author checks and scripted reference tests are not learner validation.

Source inventory, relative links and daily timing allocations pass. The six books were rendered and visually reviewed; the Docs book is 133 pages and the masterclass book is 73 pages. Local browser checks passed for the captured Docs routes. Full pop-out/lightbox lifecycle checks remain pending. No remote site deployment has been performed.

Book PDFs are committed, so every rebuild adds the whole file to git history. `tools/build-books.mjs` compresses each book with Ghostscript (`gs`, 200 ppi JPEG): install it before rebuilding, keep each PDF well under GitHub's 50 MB warning size, and only commit a rebuilt book when its content changed. See planning/VALIDATION-STATUS.md for public validation state, and ignored _local records for private demo identities. Rebuild the books and site after changing content. Inspect the final PDFs after changes. Keep status records accurate rather than claiming a draft chapter is validated.

## Docs Conventions Alignment

The Google Docs course (02-google-docs) now follows the training-book-kit chapter skeleton: a `> **Prompts:**` callout, `**Estimated time:** NN minutes` (the planned split follows on the same line), a `---` rule before What You Will Learn, Independent Practice with an Evidence to Hand Over subsection, and an italic caption under every screenshot. Prompts pages are titled `NN - Title: Prompts` and use `## Part N: Name` headings, with Session/Grounding lines above Gemini prompts. Google Slides (03-google-slides) follows the same pattern. Apply it to the remaining four courses once their screenshot branches are merged. Image file names keep the course prefix (`c02-...`) because six courses share chapter numbers. The participant site follows the kit's BRAND.md: logo.png at the root (copied from training-book-kit/brand), navy/teal/purple tokens in assets/site.css with a dark-mode set, and a teal-cloud sidebar in light mode. The six review books keep their Google product palettes (assets/book-palette*.css), as BRAND.md allows for books. program-flow.png is rendered by _design/render-program-flow.py in the brand colours.

## Next Production Work

Confirm the customer Workspace edition, enabled services, language and actual teaching timetable. Execute the untested lab routes in order, capture real screenshots, repair control wording and reconcile expected results with private assessment controls. Pilot the chapter timings. Publish only after the required review and the user's instruction to publish.

## Depth Revision 0.4

All 44 specialist chapters now include casework, independent changed requirements and evidence gates. See planning/specialist-depth-map.json and private _trainer/specialist-depth-controls.md. The cases and timing targets are written designs, not executed learner evidence. Keep baseline and scenario copies distinct. Never upload all specialist-case-cards.txt as authoritative project evidence in an AI lab.

## Repository Review

Use a branch and a pull request, following the shared course conventions. The initial six-course import was merged through pull request #1. GitHub Pages is live at https://asraf-js.github.io/Google-Workspace/ with Source set to GitHub Actions (October 2026). The Publish course site workflow runs on every push to main, so merging a pull request publishes it; keep unfinished work on branches. Branch deploys use Jekyll, which cannot fill this site's {{base}}, {{courseLinks}} and {{chapterNav}} placeholders, so never switch the Pages source back to Deploy from a branch. Pushing the source does not authorise granting Drive access or publishing native Google Sites.

## Screenshot Sources

Asraf wants uncropped screenshots retained for later framing adjustments. The editing library in `_design/screenshots/` contains 228 retained sources: 216 application-window captures, six focused captures and six PDF-page renders. All retain their captured dimensions, with privacy masks. Three early workspace originals were not retained and need recapture. Two procedure-plan full frames include later surrounding context and must be recaptured before whole-frame use in participant notes. Keep existing approved lesson crops until an adjusted frame is reviewed. All eight Docs labs (165 images) and all eight Slides labs (173 images) are converted to the series screenshot style, as is Sheets Foundation Lab 1 (26 images). Its old .jpg crops are kept, unused, only so the screenshot manifest and README links stay valid until Codex's Foundation PRs merge; delete them and update those two files then (1600 px app window, red boxes and step numbers drawn by training-book-kit annotate-shots); see _design/shots/README.md for the pipeline and annotation rules before converting the next lab. For every new stage, retain the full application-window PNG before making a crop and ensure the entire visible frame contains only work completed by that step.

Docs Lab 4 now has 35 staged images and a verified nine-page native export. Continue Docs Lab 6 using the maintained Working document, which retains all earlier text and heading targets. Keep the separate Layout Practice copy in Pageless mode for comparison. The independent escalation-table challenge was skipped. The updated 81-page Docs book was rendered and visually reviewed; source checks and the 115-page site build pass.

Docs Lab 5 core is complete: 34 images, four reasoned decisions, an open missing-contact comment, baseline/checked milestones and manual comparison. The native comparison picker was blank; no generated suggestions were produced. Continue with Docs Lab 6 in the maintained Working document. Independent challenge and partner review remain pending.

## Inline copyable material

At the user's request (30 October 2026), put every required prompt, typed value and case input beneath its relevant instruction in each chapter README. Keep session/source guidance with each prompt. Do not direct participants to a separate prompts page. Existing prompts.md URLs remain as compatibility references, with a link back to the integrated lesson. Books use the integrated notes and omit duplicate prompt appendices. Preserve the existing screenshot order and captions.


## Classroom clarity in Google Docs labs

Following the user's classroom feedback (30 October 2026), Docs labs explain the skill and purpose, name the file to edit, use short tasks with a visible Check, and group text pasted into the same location. Type short labels beside the instruction instead of giving each a Copy box. Supply reference tables with headings through the opt-in data-copy-with-table control; learners verify sources and actual results rather than transcribe cells. Keep comment questions and replies beside their separate actions. Never fill pending conversion or independent-review results with reference-run claims.

## Lab rewrite pattern

Docs Labs 01 and 02 and Sheets Foundation Lab 01 follow training-book-kit's `write-lab-chapter` skill; rewrite the remaining labs the same way, one lab per pull request, and fold new review lessons back into the skill. Sheets Foundation Lab 01 is the reference for Sheets: tab-separated paste blocks for Workbook Guide text, and the three records to type shown as a plain table with `<div data-no-copy></div>` before it, which stops `assets/site.js` adding a Copy table button. Focused captures of small controls (narrower than 800 px, such as `c04-01-08a-tasks-tab-menu-duplicate.png`) live beside the full-window sources and `prepare-raw.py` keeps them at their own size. Keep the names later labs depend on: `GW - Sheets - Task Register`, Tasks, Summary, Workbook Guide, Navigation Practice and Entry Practice. Sheets Foundation Labs 2 to 8 have no real captures yet.
