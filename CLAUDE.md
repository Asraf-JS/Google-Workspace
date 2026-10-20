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

Source inventory, relative links and daily timing allocations pass. The six books were rendered and visually reviewed; the Docs book is 95 pages and the masterclass book is 73 pages. Local browser checks passed for the captured Docs routes. Full pop-out/lightbox lifecycle checks remain pending. No remote site deployment has been performed.

See planning/VALIDATION-STATUS.md for public validation state, and ignored _local records for private demo identities. Rebuild the books and site after changing content. Inspect the final PDFs after changes. Keep status records accurate rather than claiming a draft chapter is validated.

## Next Production Work

Confirm the customer Workspace edition, enabled services, language and actual teaching timetable. Execute the untested lab routes in order, capture real screenshots, repair control wording and reconcile expected results with private assessment controls. Pilot the chapter timings. Publish only after the required review and the user's instruction to publish.

## Depth Revision 0.4

All 44 specialist chapters now include casework, independent changed requirements and evidence gates. See planning/specialist-depth-map.json and private _trainer/specialist-depth-controls.md. The cases and timing targets are written designs, not executed learner evidence. Keep baseline and scenario copies distinct. Never upload all specialist-case-cards.txt as authoritative project evidence in an AI lab.

## Repository Review

Use a branch and a pull request, following the shared course conventions. The initial six-course import was merged through pull request #1. Pushing the source does not authorise enabling Pages, running the manual publication workflow, granting Drive access or publishing native Google Sites.

## Screenshot Sources

Asraf wants uncropped screenshots retained for later framing adjustments. The editing library in `_design/screenshots/` contains 228 retained sources: 216 application-window captures, six focused captures and six PDF-page renders. All retain their captured dimensions, with privacy masks. Three early workspace originals were not retained and need recapture. Two procedure-plan full frames include later surrounding context and must be recaptured before whole-frame use in participant notes. Keep existing approved lesson crops until an adjusted frame is reviewed. For every new stage, retain the full application-window PNG before making a crop and ensure the entire visible frame contains only work completed by that step.

Docs Lab 4 now has 35 staged images and a verified nine-page native export. Continue Docs Lab 6 using the maintained Working document, which retains all earlier text and heading targets. Keep the separate Layout Practice copy in Pageless mode for comparison. The independent escalation-table challenge was skipped. The updated 81-page Docs book was rendered and visually reviewed; source checks and the 115-page site build pass.

Docs Lab 5 core is complete: 34 images, four reasoned decisions, an open missing-contact comment, baseline/checked milestones and manual comparison. The native comparison picker was blank; no generated suggestions were produced. Continue with Docs Lab 6 in the maintained Working document. Independent challenge and partner review remain pending.
