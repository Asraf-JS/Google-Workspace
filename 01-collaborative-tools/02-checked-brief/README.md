# 02 - Create, Review and Revise a Checked Brief

**Your assignment:** Produce a structured brief with traceable facts, a decision table, a review history and a checked PDF.

**Target allocation:** 65 minutes: 20 demonstration and discussion, 25 guided build, 15 independent challenge, 5 verification and repair. These are design allocations, not measured completion times. Finish the challenge and checks before moving on; finishing the guided clicks is not completion of the lab.

**Status:** core sections 2.1–2.3 executed and captured in a fresh private document: ten fact checks, eight section headings, decision table, verified links, two named versions, an accepted editorial suggestion, a rejected factual distortion, an open review thread and a three-page PDF inspected page by page. The independent challenge and classroom timings remain unvalidated.

## What You Will Learn

- Ground an AI draft in supplied facts and independently audit it.
- Use paragraph styles, document navigation, tables and source links.
- Distinguish a comment, an editorial suggestion and an actual project approval.
- Preserve a baseline and inspect an exported copy.

## Before You Begin

Use the workspace from Lab 1. Have project-facts.txt, checked-brief.txt and review-examples.txt available. If Gemini is unavailable, use checked-brief.txt for the draft and perform the same factual audit and revision tasks manually.

Use the values beside the steps below and [shared practice files](../../shared/sample-files/README.md). Keep fictional role names as text. Use only trainer-assigned test identities for any access test.

## 2.1 Draft and Audit the Facts

1. Create a Doc in **02 Working** named `GW - Project Reporting Pilot - Brief`. Add the fictional-material label.

**Copy: Name the Document**

```text
GW - Project Reporting Pilot - Brief
```


![A fresh labelled brief before any AI draft, audit table or headings have been added](./images/c01-02-01-start.jpg)

2. If available, open **Ask Gemini** and use the panel-only prompt provided below with the full fact sheet. If it proposes an in-place edit, inspect it before accepting. Reject any replacement of known facts with placeholders; use the recovery prompt.

**Copy: Draft from Supplied Facts**

**Session:** new chat | **Grounding:** pasted project fact sheet, no web research

```text
Reply in the side panel only. Do not edit the document.
Goal: Draft a concise project brief for the Project Reporting Pilot.
Context: I am the project coordinator at the fictional Seri Maju Projects in Petaling Jaya. This is fictional training material.
Source: Use only the FACTS pasted below. Do not search my other files or email, and do not use the web.
Expectations: Use British English and these headings: Purpose, Scope and Outputs, Roles, Schedule, Budget, Risk, Success Measure, Decisions Needed. Keep the brief below 350 words. Preserve all numbers and approval conditions. If a fact is missing, write "To be confirmed". Do not invent a start date, approval, benefit percentage or supplier. Label the document "Fictional training material".

FACTS:
[paste the full project fact sheet here]
```

Replace `[paste the full project fact sheet here]` with the full contents of the supplied file before submitting.


**Copy: Recovery Prompt**

**Session:** same chat | **Grounding:** facts embedded below

This exact request produced the successful panel response during the live test. Check the result again; AI wording can vary.

```text
Reply in the side panel only. Do not edit the document. Draft the brief using the following facts in this message, not other files. Organisation: fictional Seri Maju Projects, Petaling Jaya. Project: Project Reporting Pilot. Purpose: test a consistent weekly project reporting process. Coordinator: Aina Rahman. Sponsor: Farid Hassan. Teams: Planning, Procurement and Site Coordination. Duration: four weeks. Start date: not agreed. Proposed budget ceiling: RM 12,000; NOT approved. Outputs: project brief, task register, weekly status update, project hub. Cadence: every Friday during the pilot. Risk: inconsistent definitions of task status. Success: all three teams submit on time for the final two weeks. Decisions needed: sponsor approval of the budget and start date. Only fictional training data; no live construction records, purchasing commitments or external publication. Use British English, fewer than 350 words, label Fictional training material, and headings Purpose, Scope and Outputs, Roles, Schedule, Budget, Risk, Success Measure, Decisions Needed. Include the known facts; only mark the missing start date To be confirmed. Do not replace supplied facts with placeholders.
```


![The draft stays in Gemini while the document contains only its fictional-material label](./images/c01-02-01-panel.jpg)

3. Create a check table at the end of the document: Claim, Source wording and Verdict. Check duration, teams, coordinator, sponsor, budget condition, reporting cadence, risk and success measure.

**Copy: Review Table**

```text
Claim | Source wording | Verdict
Decision | Decision-maker | Current state | Evidence required
```


4. Check the unresolved start date and budget approval separately. Use the AI audit prompt only as a second opinion; compare its answer with your own table.

**Copy: Check the Draft**

**Session:** same chat | **Grounding:** original fact sheet and draft

```text
Compare your draft with the original FACTS. List any claim that is unsupported, changes a number, or turns a proposed item into an approved item. For each claim give the source fact and a correction. If none are found, say that none were found. Do not rewrite or edit the document yet.
```

Check the result yourself against the fact sheet. An AI self-check can miss an error.


![Ten source-backed checks before inserting the draft; unresolved facts remain unresolved](./images/c01-02-01-audit.jpg)

5. Insert the checked brief. Remove unsupported benefits, suppliers or approvals. If no AI is available, copy the recovery brief and still complete all ten factual checks.

![Checked plain text before paragraph styles, decision tables, source links or comments exist](./images/c01-02-01.jpg)

<details markdown="1">
<summary>What should you see?</summary>

The brief preserves the four-week duration and proposed RM 12,000 ceiling. It does not invent a start date, approval or benefit percentage. The audit records source evidence, not just “AI says correct”.

</details>

<!-- CAPTURED: core section 2.1 on 17 October 2026; independent challenge and learner timing pending. -->

## 2.2 Build Navigation and Decision Structure

1. Apply **Title** to the project title and **Heading 1** to Purpose, Scope and Outputs, Roles, Schedule, Budget, Risk, Success Measure and Decisions Needed.

2. Open the document outline and navigate to Budget and Decisions Needed. Confirm these are real headings, not bold body text.

![The Title and eight section headings appear in the outline before review comments or suggestions](./images/c01-02-02-headings.jpg)

3. Under **Decisions Needed**, insert a four-column table: Decision, Decision-maker, Current state and Evidence required. Add the budget ceiling and start date as two unresolved decisions. The sponsor decides budget approval; mark the start-date decision-maker **To be confirmed** unless the source names one.

If the decision heading and table split across pages, insert a page break before **Decisions Needed**. Keep the completed audit on its own page.

If the decision heading and table split across pages, insert a page break before **Decisions Needed**. Keep the completed audit on its own page.

4. Add a source link to the fact sheet. Add a link or file chip for the native task register. Open each and verify its identity.

![The decision table and verified source links before editorial review begins](./images/c01-02-02.jpg)

5. Use **File**, **Version history**, **Name current version** and name it `Brief checked against source facts`. This baseline precedes the independent editorial revision.

**Copy: Name the Checked Version**

```text
Brief checked against source facts
```


![Name the checked baseline before accepting or rejecting suggestions](./images/c01-02-02-version.jpg)

<details markdown="1">
<summary>What should you see?</summary>

Eight main headings navigate correctly. The decision table keeps open items open. A file chip provides navigation, not an access grant.

</details>

<!-- CAPTURED: core section 2.2 on 17 October 2026; independent challenge and learner timing pending. -->

## 2.3 Practise Review and Export

1. Select a sentence about the budget and add a comment asking what evidence would establish approval. Do not @mention or assign a fictional person.

![The first budget evidence question before later suggestions or replies; reviewer identity is masked](./images/c01-02-03-comment.jpg)

2. Switch from **Editing** to **Suggesting**. Propose a clearer purpose sentence without changing facts. Inspect the suggestion, then accept it only if the meaning is preserved.

![Inspect the proposed purpose replacement before accepting it; reviewer identity is masked](./images/c01-02-03-purpose.jpg)

3. Add a second suggestion that incorrectly removes the word **proposed** from the budget. Reject it and explain why this is a factual change rather than an editorial improvement.

![The incorrect deletion is still pending here, immediately before rejection; reviewer identities are masked](./images/c01-02-03-reject.jpg)

4. Reply to the budget comment that approval evidence is still missing. Leave that issue open. Name a new version `Brief reviewed - decisions still open`.

![The restored proposed-budget wording and open review thread after rejecting the factual distortion](./images/c01-02-03.jpg)

![Name the reviewed version while project decisions remain open](./images/c01-02-03-version.jpg)

5. Choose **File**, **Download**, **PDF Document**. Open the exported PDF and inspect every page, table break and heading. Compare its budget wording with the native document.

![The real File > Download menu before creating the PDF snapshot](./images/c01-02-03-download.jpg)

![Page two of the actual exported PDF: the unresolved decisions and table remain readable and together](./images/c01-02-03-export.jpg)

6. Record which file is maintained and which is a snapshot. After a later revision, the PDF must be regenerated; it does not track the native document.

**Copy: Rewrite for the Sponsor**

**Session:** same chat | **Grounding:** checked brief and original facts

```text
Write an 80 to 100 word update for the project sponsor using only the checked brief and original FACTS. Explain the purpose, proposed budget ceiling, success measure and decisions still needed. Keep approval and the start date unresolved. Do not send the update or create a calendar event.
```


<details markdown="1">
<summary>What should you see?</summary>

There is a demonstrable accepted suggestion, a rejected factual distortion and an unresolved comment. The PDF is readable and retains the source caveats.

</details>

<!-- CAPTURED: core section 2.3 on 17 October 2026; independent challenge and learner timing pending. -->

## Independent Challenge

Read review-examples.txt. Create a **Review Response** section identifying each unsupported claim, its correction and the missing evidence. Independently write an 80 to 100 word sponsor update that preserves the proposed budget and unresolved start date. Give a partner the source and your update to audit, or perform a second-pass audit if working alone. Correct one issue or document why no correction was needed, then name the revised version. Do not treat completion of this exercise as sponsor approval.

## Evidence to Hand Over

- Native brief with eight main headings, source links and a decision table.
- Ten factual checks, review response and independently written sponsor update.
- Version names, visible review evidence and inspected PDF.

## Troubleshooting

| Symptom | Repair to investigate |
|---|---|
| Gemini removes known facts | Reject the proposal and use the explicit panel-only recovery request. |
| Headings do not appear in the outline | Apply named paragraph styles to entire heading paragraphs. |
| The PDF differs from the working file | Re-export after changes and inspect the new copy. |

## Check Yourself

Explain one error you found, how you proved the correction, and which downstream result it could affect. A finished-looking file alone is not evidence that it is correct.
