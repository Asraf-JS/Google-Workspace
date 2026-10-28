# 04 - Build a Source-Based Notebook

In this chapter you will add the pack to Gemini Notebook, ask questions and inspect citations in context.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 60 minutes: 15 explanation/demonstration, 17 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 45 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A three-source evidence notebook with citation and missing-fact checks.

> **Status:** author reference with 29 staged captures. Three original sources, decision/date checks, meeting-only scope, six-question citation audit and separate conflict/revision test verified. Independent challenge, human review and classroom timing remain pending.

## What You Will Learn

- Create a notebook with selected sources.
- Inspect citations in context.
- Handle missing information explicitly.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use the three-file fictional source pack from Chapter 1. Gemini Notebook creation and source access must be available.

## 4.1 Create the Notebook

1. Open Gemini Notebook in the training account and create **GW - Project Reporting Pilot - Evidence**. Verify the account before adding any sources.

![blank evidence notebook](./images/c06-04-01-blank-evidence-notebook.jpg)

2. Choose **Add sources → Copied text** and paste the complete supplied `project-facts.txt`. Choose **Insert**. In the observed interface, copied text appears under **Notes** and can be selected as a source. Open it, inspect its entire body and name it **S1 - project-facts.txt - supplied original**. The fact sheet has no supplied version number.

![fact sheet before insert](./images/c06-04-02-fact-sheet-before-insert.jpg)

![fact sheet imported](./images/c06-04-03-fact-sheet-imported.jpg)

3. Repeat with the complete `meeting-record.txt`. Name it **S2 - meeting-record.txt - scripted original**. Confirm that the record says it is scripted and retains all three actions, owners and relative due weeks.

![meeting before insert](./images/c06-04-04-meeting-before-insert.jpg)

![scripted meeting imported](./images/c06-04-05-scripted-meeting-imported.jpg)

4. Add the complete `reporting-guidance.txt` as **S3 - reporting-guidance.txt - proposed v1**. Inspect the statement that it is proposed training guidance, not approved company policy. Wait until processing finishes and all three checkboxes are selected. The generated overview is an AI output; it is not an additional original source.

![guidance before insert](./images/c06-04-06-guidance-before-insert.jpg)

![proposed guidance imported](./images/c06-04-07-proposed-guidance-imported.jpg)

## 4.2 Ask and Follow a Citation

1. With all three sources selected, ask **What decisions are still needed before the pilot starts? Use only these sources.**

![decisions prompt](./images/c06-04-08-decisions-prompt.jpg)

2. The author answer identified budget approval and start-date agreement as unresolved. Do not treat its “before the pilot can start” phrasing as evidence of a separate formal launch gate.

![decisions answer](./images/c06-04-09-decisions-answer.jpg)

3. Click the citation beside budget approval. The observed UI opens the imported note in the right panel with its text selected. Read the complete surrounding passage: the scripted meeting record says the proposed RM12,000 ceiling still needs Farid Hassan’s approval and the start date has not been agreed. A citation marker alone does not establish support.

![budget citation context](./images/c06-04-10-budget-citation-context.jpg)

## 4.3 Test a Missing Fact

1. Ask **What is the approved pilot start date?** The recorded answer said no approved start date exists and distinguished relative practice weeks from calendar dates.

![missing date answer](./images/c06-04-11-missing-date-answer.jpg)

2. Open the fact-sheet citation and confirm **Start date: not yet agreed**. If your answer invents a date, mark it unsupported and repair it against this text.

![date citation context](./images/c06-04-12-date-citation-context.jpg)

3. Deselect S1 and S3, leaving only S2 selected. Ask for preparation actions, owners, due practice weeks and budget approval status using only the scripted record.

![meeting only scope](./images/c06-04-13-meeting-only-scope.jpg)

4. The author answer retained Aina’s template in week1, Bala’s status-definition review in week1, Siti’s fictional sample in week2 and the unapproved budget. Open the citation to check those exact statements. This conversation retained earlier answers; the scope demonstration does not isolate selection as a causal effect. For a fresh-context comparison, repeat in a separate notebook with the intended originals only.

![meeting only answer](./images/c06-04-14-meeting-only-answer.jpg)

![meeting action citation](./images/c06-04-15-meeting-action-citation.jpg)

## 4.4 Audit Citations, Source Selection and Conflicts

1. Restore all three original source selections and run the six-question bank from the prompts page. Record the answer; keep approval status, unresolved decisions and proposed guidance distinct.

![six question answer](./images/c06-04-16-six-question-answer.jpg)

2. Open the cited originals and compare each claim with its passage. In the recorded answer, the six core facts matched: S1 supports purpose/duration, teams, Friday cadence, success measure, proposed/unapproved ceiling and unagreed start; S2 supports the three action-owner-week tuples; S3 supports relative weeks and proposed Friday practice.

![bank fact citation](./images/c06-04-17-bank-fact-citation.jpg)

![bank action citation](./images/c06-04-18-bank-action-citation.jpg)

![bank guidance citation](./images/c06-04-19-bank-guidance-citation.jpg)

3. Record repairs as well as matches. The answer grouped known unapproved budget status under an “Unknown” label; the future sponsor decision is unresolved, while the current status is known. Its extra “no purchases authorised” claim included a fact-sheet citation that only gives related scope wording. S2 states the authorisation status explicitly; cite that exact passage rather than accepting a nearby topic mention.
4. Create a separate notebook, **GW - Project Reporting Pilot - Conflict Practice**. Import extract A and extract B from the prompts page through Copied text. Inspect both complete bodies. Keep the core three-source notebook unchanged.

![conflict source a](./images/c06-04-20-conflict-source-a.jpg)

![conflict source b](./images/c06-04-21-conflict-source-b.jpg)

5. Ask **Which reporting day is approved? Use only the selected sources and cite the supporting text.** The recorded answer said neither day is recorded as approved. Open both citations: A proposes Friday and B proposes Wednesday, and both say approval is not recorded. Titles and upload order do not establish authority.

![conflict no approved day](./images/c06-04-22-conflict-no-approved-day.jpg)

![conflict citation context](./images/c06-04-23-conflict-citation-context.jpg)

6. Add the labelled **B revision2** test source from the prompts page using **Add sources → Copied text**. This additional fictional test input withdraws the Wednesday proposal and proposes no alternative; it does not modify the core project facts. Open the imported body to prove which revision is present. The earlier answer still shows the original proposals.

![revised source old answer](./images/c06-04-24-revised-source-old-answer.jpg)

7. Retain original B as evidence but deselect it. Leave A and revision2 selected, then rerun the identical approved-day question. The new answer cited revision2, recognised the withdrawal and retained the lack of approval. Open the revision citation to verify the text. The unchanged old answer remains a record of its earlier source scope.

![revised selection rerun](./images/c06-04-25-revised-selection-rerun.jpg)

![revised answer](./images/c06-04-26-revised-answer.jpg)

![revision citation proof](./images/c06-04-27-revision-citation-proof.jpg)

8. Record a six-row citation audit in your review log, including source, exact claim support and repairs. The author created an editable Google Docs table and a conflict/version note. The budget and date results are checks of fictional supplied evidence, not real approvals.

![six question audit table](./images/c06-04-29-six-question-audit-table.jpg)

![audit limitations and conflict note](./images/c06-04-28-audit-limitations-and-conflict-note.jpg)

**Author-run scope:** three Copied text imports inspected in full; decision/date citations, single-source action extraction, six-question bank, separate conflicting proposals and revised-source rerun checked. Native audit table has six result rows plus its header. The 60-minute classroom allocation, independent challenge and separate human review remain unvalidated.

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Write two independent multi-source questions and one missing-fact question. Inspect every cited passage supporting their answers.

2. Challenge one answer with “Which exact source sentence establishes this?” and record any unsupported certainty, including a citation that merely mentions the topic.

3. Produce a source-version and conflict-handling note that another learner can use without guessing which source is authoritative.

## Evidence to Hand Over

- Six-question citation audit with exact claim-to-passage checks.
- Separate conflict context with unresolved authority handled explicitly.
- Verified source-version change and an old-versus-new answer comparison.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A citation exists but does not support the answer | Read the surrounding passage and compare the exact approval/date wording rather than trusting the marker. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Notebook answers become useful when citations are checked against their source context.

**Check yourself:** What must you inspect after following a citation?
