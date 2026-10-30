# 02 - Plan and Draft with Gemini

In this chapter you will generate an outline, draft from supplied evidence and record unsupported claims.


**Estimated time:** 55 minutes, planned as 10 explanation and demonstration, 25 guided build and casework, 15 independent practice and 5 verification and repair. Not yet timed with learners.

**Your result:** A checked proposed procedure with outstanding sponsor questions.

> **Status:** real-app reference route captured with 13 stage images. Gemini response reviewed, eight-step table verified and normal/missing-owner paper routes checked. Independent late/incomplete challenge and reviewer pilot remain pending.

---

## What You Will Learn

- Specify a useful drafting task.
- Review an AI proposal before using it.
- Preserve unresolved facts in a procedure.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use your `GW - Reporting Procedure - Working` document from Lab 1, the supplied [project facts](../../shared/sample-files/project-facts.txt), [reporting guidance](../../shared/sample-files/reporting-guidance.txt) and [Tasks.csv](../../shared/sample-files/Tasks.csv). If Gemini isn't available in your account, follow the **No Gemini?** notes: you'll use the reference draft provided below instead and still do every check.

## 2.1 Define the Reader and Task

1. In your working document, click **Ask Gemini** (the star button at the top right). The Gemini panel opens on the right.
2. Copy the prompt below and paste it into the **Ask Gemini** box at the bottom of the panel. Replace `[paste project-facts.txt]` with the whole text of `project-facts.txt`. Don't submit yet.

**Copy: Draft a Procedure**

**Session:** new Gemini panel chat | **Grounding:** pasted project-facts.txt

```text
Goal: Propose a weekly reporting procedure for team members.
Context: Fictional Seri Maju Projects training exercise.
Source: Only the facts pasted below.
Expectations: Reply in the panel only, without editing my document. Use headings Prepare, Check, Submit for Review and Resolve Questions, with numbered steps. Label operational steps as proposed training practice. Preserve the proposed budget and unresolved start date. Do not invent approval authorities, deadlines or systems.

FACTS:
[paste project-facts.txt]
```

Replace bracketed source placeholders before submitting. Keep a human check between an AI proposal and the final output.

3. Read the prompt again before submitting. It asks for an answer in the panel and a proposed procedure, not a change to your document or to company policy.

![The Gemini panel with the drafting prompt pasted into the Ask Gemini box, not yet submitted](./images/c02-02-source-grounded-prompt.png)

*The prompt includes the actual fact sheet. It is still in the box, waiting to be submitted.*

<details markdown="1">
<summary>What should you see?</summary>

The request names the reader, source and output format. No source placeholder remains.

</details>

<!-- Reference core captured 18 October 2026; independent learner challenge remains pending. -->

## 2.2 Review the Draft

1. Click **Submit** (the arrow at the bottom right of the panel) and read the whole response, scrolling down the panel. If Gemini offers to edit your document instead, click **Reject all**: this lab only uses the panel.

![Gemini's response in the panel; its Check section lists only two of the three statuses](./images/c02-02-unreviewed-response.png)

*This is still an unreviewed proposal. Its Check section mentions Complete and In Progress but leaves out Not Started.*

![The rest of the response; the boxed Submit for Review step gives no usable submission route](./images/c02-02-response-checks.png)

*"Route submissions according to the project structure" doesn't tell a reader where to send anything.*

2. Compare every instruction in the response with `project-facts.txt` and `reporting-guidance.txt`. At the end of the document, type `AI draft review` and today's date, then record what the response got right and each repair it needs. Check at least these three things: does Check list all three statuses, is the submission route specific, and did it use anything other than the pasted facts?

**Copy: Typed Values**

Labels for sections 2.2 and 2.3, in the order you type them:

```text
AI draft review
```


![The AI draft review typed at the end of the Authoring Log](./images/c02-02-human-review.png)

*The review records the missing status, the vague routing instruction and the source-boundary issue.*

**No Gemini?** Skip steps 1 and 2. Copy the reference draft provided below and review it the same way.

<details markdown="1">
<summary>What should you see?</summary>

The draft distinguishes known project facts from a proposed training procedure. The budget and start date remain unresolved.

</details>

<!-- Reference core captured 18 October 2026; independent learner challenge remains pending. -->

## 2.3 Insert the Checked Text

1. Click at the end of the purpose statement at the top of the document (above **Authoring Log**) and press **Enter** twice. Type `Weekly reporting procedure - proposed training practice`, then write the checked procedure under four labels: Prepare, Check, Submit for Review and Resolve Questions, with eight numbered steps. Use the response only where your review in 2.2 found it correct, and fix the repairs you recorded, except the missing status in step 4: leave that for section 2.4. The reference wording is provided below if you want to compare.

**Copy: Typed Values**

```text
Weekly reporting procedure - proposed training practice
```



**Copy: Reference Checked Draft**

Use this in section 2.3 to compare with your own checked procedure, or as the draft to review if Gemini isn't available. Step 4 is repaired later, in section 2.4.

```text
Weekly reporting procedure - proposed training practice
Prepare
1. Identify your task in Planning, Procurement or Site Coordination. Preserve the source task ID and owner; flag missing information for clarification rather than inventing it.
2. Gather the current task update and a short exception note. Use fictional training data only; exclude live construction records and purchasing commitments.
Check
3. Compare project context with the fact sheet: the pilot runs four weeks from an agreed start date and requires a Friday update. RM 12000 remains proposed, not approved.
4. Confirm that operational instructions are labelled proposed training practice. If a fact or instruction has no evidence, retain an unresolved question.
Submit for Review
5. Prepare the weekly status update for Friday review. The submission channel, review recipient and cut-off time are unresolved; request agreement before treating a draft route as operational.
6. Check that the brief, task register, weekly update and project hub remain the four intended outputs. This training draft does not authorise sending or publication.
Resolve Questions
7. Record ambiguous statuses, missing owners and unsupported commitments as questions requiring clarification. Do not turn uncertainty into a completed task or an approved decision.
8. Recheck the entry against its sources after clarification. Until evidence is supplied, preserve the unresolved value and keep the draft distinguishable from an approved record.
```


![The checked procedure inserted under the purpose statement, with eight numbered steps](./images/c02-02-checked-draft.png)

*The checked procedure sits in the reader-facing part of the document. The Gemini response and your review stay in the Authoring Log.*

2. Keep `project-facts.txt` open in another tab so a reviewer can compare commitments.
3. Under step 8, type `Questions for the Sponsor` and the two unresolved decisions provided below.

**Copy: Typed Values**

```text
Questions for the Sponsor
- Is the proposed RM 12000 budget approved? Open decision; sponsor approval is not evidenced.
- What is the agreed pilot start date? Open decision; no calendar date or approval authority is inferred.
```

![Questions for the Sponsor with the two open decisions at the end of the procedure](./images/c02-02-open-decisions.png)

*The draft ends with two open sponsor questions. It doesn't invent an approval or a calendar date.*

<details markdown="1">
<summary>What should you see?</summary>

The procedure and its outstanding questions are readable without the Gemini conversation.

</details>

<!-- Reference core captured 18 October 2026; independent learner challenge remains pending. -->

## 2.4 Develop an Executable Procedure and Test Its Logic

1. At the end of the document (in the Authoring Log), type `Procedure plan - eight steps across four sections` and the sources line provided below. Click **Copy table** above the procedure-plan table below, then paste it on a blank line outside any table in Google Docs using **Ctrl+V**. This inserts the 5-column, 9-row scaffold at once. Fill one row for each of the eight procedure steps.

**Copy: Procedure Plan**

Section 2.4, step 1. Type the label and sources line, then build the table and fill the Input, Action, Output and Check cells yourself.

```text
Procedure plan - eight steps across four sections
Sources: project-facts.txt (facts); reporting-guidance.txt v1 (proposed guidance). Workflow details below are proposed practice.
```

| Step | Input | Action | Output | Check |
|---|---|---|---|---|
| 1 Prepare | | | | |
| 2 Prepare | | | | |
| 3 Check | | | | |
| 4 Check | | | | |
| 5 Submit | | | | |
| 6 Submit | | | | |
| 7 Resolve | | | | |
| 8 Resolve | | | | |


![The procedure plan label and the first seven rows of the plan table](./images/c02-02-plan-first-steps.png)

*Each step has an input, an action, an output and a check. Source labels in brackets show where each action comes from.*

![The last rows of the plan complete eight steps across the four sections](./images/c02-02-plan-final-steps.png)

*Steps 6 to 8 cover routing questions, missing information and rechecking after clarification.*

2. Check the plan against `reporting-guidance.txt` and the fact sheet. Mark each factual instruction with its source in brackets, such as `(facts)` or `(guidance)`, and mark workflow details you designed as `(proposed)`. Then fix procedure step 4 so that it lists all three statuses (Not Started, In Progress and Complete), the repair your AI draft review asked for.

**Copy: Walkthrough and Distinction Labels**

```text
Before:
After:
Preserved checks:
```


**Copy: Walkthrough and Distinction Labels**

```text
4. Check the three proposed guidance categories: Not Started means work has not begun; In Progress means work has begun without owner-confirmed completion; Complete means the owner has confirmed the agreed output is ready for review. Preserve an unfamiliar label as a clarification query rather than inventing a mapping.
```


![Procedure step 4 now names all three proposed guidance statuses](./images/c02-02-status-repair.png)

*The arrow marks the repaired step 4. An unfamiliar label becomes a clarification query rather than a guessed status.*

3. Below the plan, type `Example weekly submission - fictional supplied record` and write a submission for task T001 from `Tasks.csv`: its TaskID, owner, status and exception note.

**Copy: Walkthrough and Distinction Labels**

Section 2.4, steps 3 to 7.

```text
Example weekly submission - fictional supplied record
```


4. Below the example, type `Missing-owner route - proposed practice` and describe what happens for test card T-TEST-A provided below . The route must stop anyone from guessing an owner and say what needs clarifying.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Walkthrough A: TaskID T-TEST-A, owner missing, status In Progress, exception “awaiting owner confirmation”. Walkthrough B: TaskID T-TEST-B, owner Siti Aminah, status Blocked. These are separate fictional procedure test cases; do not add them to the task workbook.
```


**Copy: Walkthrough and Distinction Labels**

```text
Missing-owner route - proposed practice
```


![The T001 example submission and the missing-owner route for T-TEST-A](./images/c02-02-normal-and-exception.png)

*The supplied T001 record and the missing-owner test card are kept separate. No owner is invented.*

5. Rewrite procedure step 5 (Submit for Review) to make it clearer, using Gemini or by hand. In the Authoring Log, type `Before:` and `After:` lines with the old and new wording, and a `Preserved checks:` line listing what the rewrite kept.

**Copy: Walkthrough and Distinction Labels**

```text
5. Prepare a review-ready draft containing task ID, recorded owner, one supported status and an exception note when needed. The fact sheet requires Friday reporting. Before sending, obtain agreement on the submission channel, review recipient and cut-off time; if any is missing, retain the draft and record a routing query. This exercise sends nothing.
```

| Record type | Observable distinction |
|---|---|
| Complete submission | |
| Unresolved question | |


![The rewritten step 5 in the procedure](./images/c02-02-clarity-rewrite.png)

*The new step 5 keeps the draft and records a routing query while the channel, recipient and cut-off are unresolved.*

6. Do two paper walkthroughs. Under `Paper walkthrough A - normal supplied T001`, follow the procedure with T001 and note where it gives a clear next action. Under `Paper walkthrough B - incomplete card T-TEST-A`, do the same with the missing-owner card. Record any ambiguity and the repair you made.

**Copy: Walkthrough and Distinction Labels**

```text
Paper walkthrough A - normal supplied T001
```


**Copy: Walkthrough and Distinction Labels**

```text
Paper walkthrough B - incomplete card T-TEST-A
```


![Paper walkthroughs A and B with the observed ambiguity and its repair](./images/c02-02-paper-walkthroughs.png)

*Walkthrough A found that "request agreement" didn't say what to do with the draft while waiting. Step 5 was repaired.*

7. Type `Submission distinction` and insert a 2-column, 3-row table with the headings Record type and Observable distinction. Fill the rows Complete submission and Unresolved question. Keep both project decisions unresolved.

**Copy: Walkthrough and Distinction Labels**

```text
Submission distinction
```


![A two-row table separates a complete submission from an unresolved question](./images/c02-02-submission-distinction.png)

*A complete submission can be review-ready while its route is unresolved. An unresolved question keeps the draft and asks for evidence.*

<details markdown="1">
<summary>What should you see?</summary>

An eight-step plan with inputs, outputs and checks, a repaired step 4, a T001 example, a missing-owner route, two walkthroughs with a recorded repair, and the submission distinction table. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- Reference core captured 18 October 2026; independent learner challenge remains pending. -->

## Independent Practice

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Write a new **Late or Incomplete Submission** subsection without using the earlier drafting prompt. Give a reader a clear action, an exception record and a review check.

2. Test it with both card examples, one containing a missing owner and one an unfamiliar status. Do not silently convert “Blocked” into Complete or invent a new reporting deadline.

3. Ask a reviewer to execute the written steps verbally. Revise one ambiguity and save the source comparison in the Authoring Log.

### Evidence to Hand Over

- Eight-step procedure with inputs, outputs and checks.
- Normal and exception walkthroughs with a recorded repair.
- Independent late/incomplete subsection that preserves uncertainty.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A shorter rewrite loses a required check | Compare the before-and-after input/action/output table and restore the missing check. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

You created a source-constrained draft. Structure and navigation will make it usable as a longer document.

**Check yourself:** Can you identify one instruction that is a proposed procedure step rather than a source fact?
