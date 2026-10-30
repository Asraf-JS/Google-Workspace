# Programme Design

## Delivery Baseline

Six independently teachable courses share one fictional organisation, terminology and visual system. The supplied outline remains the scope baseline. The chapter maps are proposed teaching sequences, with changes recorded below rather than silently treated as client approval.

Assume 390 teaching minutes per day until the provider supplies the timetable. That gives 2,730 minutes across seven days. Lunch and breaks are additional. The masterclass targets approximately 30% explanation/demonstration and 70% practice across its day; this split is not a measured outcome yet. All timings need a pilot with learners.

## One Repository

```text
README.md                       Programme landing page
index.md                        Jekyll landing page, added during website production
_config.yml                     One site configuration, added during website production
_layouts/default.html           Shared layout, with course-specific navigation
assets/                         Shared styles and browser scripts
01-collaborative-tools/
  README.md                     Course landing page
  02-checked-brief/
    README.md                   Reference chapter
    prompts.md                  Compatibility link to the integrated lesson
    images/                     Real screenshots only
02-google-docs/                  Course landing page and future chapters
03-google-slides/
04-sheets-foundation-intermediate/
05-sheets-advanced/
06-notebooklm-gemini/
shared/sample-files/             Common fictional inputs
planning/                       Public production specifications without account data
_design/                        Generators, screenshot map and production scripts
book/<course>/                  Separate course configs using training-book-kit
_trainer/                       Ignored answer keys and assessment notes
_local/                         Ignored account IDs, demo URLs and run evidence
```

Use one published site, with a programme landing page and six course landing pages. Number chapters within each course. Prefix screenshot filenames with the course code to avoid collisions in the kit's annotation process, for example `c01-03-01-project-brief.png`.

Build six course books from the same Markdown using separate configurations inside `book/`. Evaluate a combined programme PDF only after the six individual books work. The existing kit assumes one course at the repository root, so verify nested paths, sample-file links and heading numbering against the reference chapter before generating all books.

Copy the established kit snippets for image lightboxes, chapter navigation, expected-result boxes and the side window into the shared layout. Scope previous/next navigation to the active course. Add a Copy button to each typed value and prompt. Do not mix programme navigation into a course's chapter sequence. Reuse the shared kit instead of forking its PDF engine.

## Scope Adjustments Proposed

| Outline item | Proposed lab treatment | Reason |
|---|---|---|
| Broad masterclass | Six substantial connected labs with independent changes and fault diagnosis | Fit a day without repeating specialist courses |
| Calendar meeting notes | Teach a meeting-notes building block; gated Meet AI demonstration | Template creation and automatic transcription are different operations |
| AI action items | Review a proposed action list, then deliberately create tasks | Avoid promising unattended synchronisation |
| Shared Drives creation | Core governance explanation and gated trainer demonstration | Access and creation permissions vary |
| Explore research | Source comparison and Gemini where available | Do not base new exercises on an unverified legacy tool |
| Sheets split view | Freeze headers and use filter views | Teach a documented route for keeping labels visible |
| Foundation formulas | Add arithmetic, aggregation and reference copying | Required before advanced analysis |
| Copyright-free AI images | Generate, inspect and document provenance/terms | Avoid an unsupported rights guarantee |
| AI print optimisation | Manual print preview, scaling and inspection | The learner must verify the actual pages |
| Automatic proposal workflow | Repeatable checked prompt sequence | Deployment and unattended automation need a separate scope |

## Production Sequence

1. Review the six maps and the reference chapter. Confirm target learners, daily timetable and target Workspace edition with the provider.
2. Test the reference chapter in the selected account. Record UI differences, generated output checks, timing and screenshots. Do not infer customer availability from the trainer's account.
3. Build and inspect the common website layout and one course-book PDF against this chapter.
4. Finish the masterclass, including its starter files, capstone and trainer-only assessment rubric.
5. Write Docs and Slides, followed by Sheets foundation and Advanced, then NotebookLM/Gemini. Generate each course's independent starting pack.
6. Execute each lab in its prescribed learner UI, capture real screenshots, repair wording and reconcile expected-result boxes against private answer keys.
7. Build six books, check site navigation/downloads/copy controls and package the single repository for publication.

## Release Criteria

A chapter is ready only when its learner route has been executed, outputs checked, screenshots captured with private information hidden, prompt/value blocks checked, dependencies documented and book pages visually inspected. Passing API reads alone does not validate a click-by-click guide. Independent tasks and capstones must have private assessment criteria.

## Current Position

Completed as drafts: all 50 chapter notes with inline prompts and values; six course maps; two starter workbooks, CSV inputs and source texts; a shared static participant site; six course book configurations and review PDFs; private pre-check questions and practical assessment rubrics.

The static builder and manual Pages workflow implement one hub using the shared layout helpers. This replaces the proposed Jekyll landing-page conversion while keeping the Markdown source structure and one-course chapter navigation. The shared kit is pinned and reused for PDF layout, with a Google-specific adapter and relative file links while the repository is unpublished.

Live validation: the reference brief chapter core path was executed with a recorded recovery prompt, checked facts, heading styles and named version. Other lab execution, independent tasks, planned screenshot rounds, customer access checks and classroom timing pilots remain. See VALIDATION-STATUS.md. No GitHub repository or public site has been created.

## Masterclass Depth Revision

The masterclass now has six expanded labs rather than eight short chapters. See [Lab Depth and Timing Pilot](./LAB-DEPTH-AND-PILOT.md). Revision 0.4 adds substantial casework, changed requirements and evidence gates to all 44 specialist chapters. All expanded application routes and actual timings still need learner execution and a pilot.
