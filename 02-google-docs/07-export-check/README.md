# 07 - Export and Check Interoperability

In this chapter you will export a copy and inspect headings, page breaks and tables after conversion.

> **Prompts:** the [prompts page](./prompts.md) has every value and prompt for this chapter, each with a Copy button.

**Estimated time:** 40 minutes, planned as 10 explanation and demonstration, 10 guided build and casework, 15 independent practice and 5 verification and repair. Not yet timed with learners.

**Your result:** Checked Word and PDF export copies of the maintained procedure.

> **Status:** sections 7.1-7.4 have an author reference run with 17 staged images and retained sources. Word/PDF scope, a connected-Drive round trip, native comparison, an instruction revision and a checked r2 export are recorded. Browser upload, interactive PDF-viewer checks, Microsoft Word desktop rendering, independent challenge and learner timing remain unverified. PDF pages were rendered offline; that is not an interactive viewer test.

---

## What You Will Learn

- Export a document to Word and PDF.
- Check conversion effects.
- Choose a distribution format deliberately.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use your checked procedure. This chapter creates local export copies; it does not publish or email them.

## 7.1 Export Two Formats

1. In the checked native **Working** document, click **File**, **Download**, **Microsoft Word (.docx)**.

![File > Download offers separate Word and PDF formats](./images/c02-07-01-download-formats.png)

*File > Download offers separate Word and PDF formats.*

2. Download **PDF document (.pdf)** separately. Keep identifiable local names such as `Procedure-practice-r1.docx` and `Procedure-practice-r1.pdf`; retain these as prior working snapshots.
3. Keep the native Google Doc as the working source. Downloads are snapshots and do not follow later source edits.

<details markdown="1">
<summary>What should you see?</summary>

Two local practice exports and the unchanged maintained native source.

</details>

## 7.2 Inspect the Copies

1. Open both exports in approved available viewers. Inspect all pages, including the last. DOCX heading/table structure was inspected before the native Docs round trip in 7.4.

> **Reference run:** Browser controls blocked local PDF URLs, so the PDF was rendered and inspected offline. **Microsoft Word desktop rendering was not tested.**

![The initial PDF reader copy is inspected offline from the first page to the last](./images/c02-07-23-initial-pdf-reader-copy.png)

*The initial PDF reader copy is inspected offline from the first page to the last.*

2. Check title, contents links, heading hierarchy, page numbers, tables, images where present and final paragraph. Record the viewer and exactly what was checked. The initial PDF had 11 pages with no blank pages or text outside page bounds. Its six tables and final training paragraph were present; no instructional image existed.
3. Record actual differences. Correct the native scenario source when appropriate and export again; keep prior snapshots. Do not infer interactive link behaviour from a picture or document text alone.

<details markdown="1">
<summary>What should you see?</summary>

A check through the final page, with viewer limitations and real defects recorded separately from no-difference findings.

</details>

## 7.3 Choose the Handover

1. Choose an editable Word file when the recipient needs to revise it, or PDF for a fixed reader handout. Keep the native source for future controlled changes.
2. Inspect comments and tracked content before distribution. The first working DOCX retained an open review comment, even though the rendered PDF did not show it. Retain the prior snapshot; make a separate release practice copy with comment copying unchecked. Do not resolve the maintained source's evidence question merely to clean an export.
3. Confirm filenames, revision and fictional labels. No sharing, publishing or email is performed in this exercise.

## 7.4 Test Conversion and Issue a Reproducible Release

1. Click **File**, **Make a copy** to create `GW - Reporting Procedure - Release Practice`. Leave sharing and comment-copy boxes unchecked. This is the native **scenario release source**; the maintained Working document stays separate. Add a Release Checklist with Native source, Revision, Export scope, Filename, Viewer and Result. Use `Practice release r1`, distinct r1 filenames and a pending result until checked.

![The separate release practice copy excludes sharing and review comments](./images/c02-07-02-release-copy-excludes-comments.png)

*The separate release practice copy excludes sharing and review comments.*

2. Rename the main tab **Procedure** (click the three dots on the tab, then **Rename**). Add a separate **Examples** tab with the supplied fictional appendix and scope marker. Name the baseline version `Practice release r1`. Select **Procedure** before exporting the main-only file. With multiple tabs, the Download dialog offers **Current Tab** and **All Tabs**. Inspect the setting for **every** export.

> **Reference run:** The reference dialog reset to Current Tab.

![A separate Examples tab has a recognisable complete-handout marker](./images/c02-07-04-examples-tab-scope-marker.png)

*A separate Examples tab has a recognisable complete-handout marker.*

Export `Procedure-r1-main.pdf` with **Current Tab**, then `Procedure-r1-complete.pdf` and `Procedure-r1-complete.docx` with **All Tabs**. If tabs are unavailable, state which appendix content is included instead of claiming an all-tabs test.

![Current Tab exports only the selected Procedure tab](./images/c02-07-06-current-tab-export-scope.png)

*Current Tab exports only the selected Procedure tab.*

![All Tabs includes Procedure and Examples in the complete handout](./images/c02-07-07-all-tabs-complete-scope.png)

*All Tabs includes Procedure and Examples in the complete handout.*

![The editable Word handover also deliberately includes all tabs](./images/c02-07-08-word-all-tabs-scope.png)

*The editable Word handover also deliberately includes all tabs.*

3. Inspect the files through their final page. The clean Word export contained no comment metadata or tracked insertions/deletions. Check three internal links, the contents list, a table and the final procedure/appendix paragraphs. PDF structural checks resolved the three quick-link destinations to the expected pages; interactive PDF viewing remained pending.

> **Reference run:** The reference main-only PDF had **12 pages without the Examples marker**; the complete PDF had **13 pages with it**.
4. Add a native defect table with **Source location**, **Format**, **Observed difference**, **Severity/action**. Record no-difference findings for elements actually checked. A PDF parser also reported a duplicate title destination key: retain that warning rather than claiming every PDF link is validated.

> **Reference run:** The reference record includes the initial Word comment, unnumbered Examples page, preserved heading hierarchy/table dimensions and tab flattening after import.
5. Upload `Procedure-r1-complete.docx` as a distinct practice file and open/convert it in Docs, named `GW - Procedure r1 - Round Trip Practice`. Do not replace the scenario or maintained source.

> **Reference run:** The browser upload required an unavailable extension permission in this run, so connected Drive imported only this authorised fictional DOCX. **Browser upload was not verified.**

![The imported round-trip copy retains headings and quick links in one tab](./images/c02-07-09-round-trip-heading-and-links.png)

*The imported round-trip copy retains headings and quick links in one tab.*

6. Compare heading hierarchy, table dimensions, links and final content. Follow the three quick links and a contents entry. Find/select the link label and use **Alt+Enter**, or use its link popup.

> **Reference run:** The reference import retained **six table structures and 16 heading targets**, including Examples, but flattened two native tabs into one. The reference reached Status Definitions, Missing Information, Questions for the Sponsor and Submission Example.

![The imported bookmark lands at Status Definitions](./images/c02-07-10-round-trip-status-link-destination.png)

*The imported bookmark lands at Status Definitions.*

![The second imported quick link reaches Missing Information](./images/c02-07-11-round-trip-missing-owner-destination.png)

*The second imported quick link reaches Missing Information.*

![A converted contents entry reaches Submission Example](./images/c02-07-13-round-trip-contents-destination.png)

*A converted contents entry reaches Submission Example.*

Use **Tools**, **Compare documents** if available. Choose the observed source, exclude comments and inspect the generated report. Prefer the matching frozen r1 reference for an exact wording comparison. The generated report flagged margins, styles, sections and headers/footers. Do not accept all suggestions or interpret the report's comment count as a defect count.

> **Reference run:** In this run the current source already contained later review-record additions, so those expected additions were distinguished from conversion effects.

![Native comparison generates suggestions for structure and formatting; these are inspected rather than accepted together](./images/c02-07-16-native-comparison-format-flags.png)

*Native comparison generates suggestions for structure and formatting; these are inspected rather than accepted together.*

7. Repair the actual source issue and change a real instruction in the **scenario** source. In **Examples**, use **Insert**, **Page elements**, **Page numbers** to add a first-page footer field; prefix it `Examples - page `. This makes the appendix's own sequence explicit. In **Procedure**, append the supplied post-clarification source-recheck action to the exact missing-owner paragraph. Confirm the selected tab and a unique search match before replacing text.

![A native page field adds an explicit Examples page sequence](./images/c02-07-17-examples-numbering-repaired.png)

*A native page field adds an explicit Examples page sequence.*

![The r2 source explicitly requires a source recheck after clarification](./images/c02-07-19-r2-procedure-instruction-checked.png)

*The r2 source explicitly requires a source recheck after clarification.*

Update the source checklist to r2 filenames and record the inspected comparison, repair and viewer limitations. Name the revision `Practice release r2`. Export `Procedure-r2-main.pdf` with Current Tab, then the complete PDF and Word with All Tabs. Keep all r1 files and check that they are unchanged (same file size and modified time in your downloads folder).

![The r2 source record distinguishes conversion evidence and pending viewer checks](./images/c02-07-21-r2-source-record-clean.png)

*The r2 source record distinguishes conversion evidence and pending viewer checks.*

![The revised native source receives a distinct release milestone](./images/c02-07-22-release-r2-name.png)

*The revised native source receives a distinct release milestone.*

Check the new files and record results in an external release manifest. The revised instruction was present in both scopes, and the earlier working snapshots retained their original hashes. These are fictional training copies, not project approval or a distributed release.

> **Reference run:** The reference r2 main-only PDF had **13 pages** and excluded Examples; the complete PDF had **14 pages**, included Examples and displayed **Examples - page 1**.

![The final complete PDF includes the fictional Examples appendix and its repaired page number](./images/c02-07-24-r2-pdf-numbered-examples.png)

*The final complete PDF includes the fictional Examples appendix and its repaired page number.*

<details markdown="1">
<summary>What should you see?</summary>

Distinct prior/current filenames, checked export scopes, a separate round trip, recorded conversion differences and a revised source/export pair. Browser upload, interactive PDF viewing and Word desktop compatibility are not claimed from the fallback checks.

</details>

## Independent Practice

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Prepare a distribution manifest for an editable handover and a fixed reader copy. State exactly which source revision and tabs/appendices each contains.

2. Have a reviewer identify the current release using only your filenames and manifest. If they choose the wrong one, repair the naming or status label.

3. Demonstrate that the earlier downloaded copy does not change after a native edit, and explain which format would suit each reader.

### Evidence to Hand Over

- Scope-checked PDF/Word copies and a round-trip comparison.
- Element-by-element conversion record, including no-defect findings where observed.
- Release manifest and a checked revised export with an unambiguous current version.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Examples disappear from the complete handout | Check current-tab versus all-tabs export scope, then inspect the end of the new file. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Conversion is complete only after checking the exported files. Next, demonstrate the complete procedure workflow.

**Check yourself:** Which file remains the maintained source after export?
