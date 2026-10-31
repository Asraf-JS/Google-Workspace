# 02 - Plan and Draft with Gemini

Your working document now holds the project's sources. Aina Rahman wants the procedure itself: the steps a team member follows each Friday to send in their update. In this lab you ask Gemini for a first draft and check it against the sources. Then you put a checked version in the document and test it the way a contributor would, once with a normal task and once with a task whose owner is missing.

**Estimated time:** 55 minutes, planned as 10 explanation and demonstration, 30 guided build and testing, and 15 independent practice. Not yet timed with learners.

**Your result:** a checked eight-step procedure with two open questions for the sponsor, and an Authoring Log that shows how you reviewed and tested it.

> **You'll practise:** asking Gemini for a draft grounded in your sources, checking the reply line by line, replacing a step in a document, and testing a procedure by walking through it with real cases.

---

## What You Will Learn

- Write an AI request that names the reader, the source and the format you want
- Review an AI draft against the sources before you use any of it
- Test a procedure with a normal case and a missing-information case, and repair what the test finds

## Before You Begin

> **Download:** [Tasks.csv](../../shared/sample-files/Tasks.csv), the fictional task list you use in 2.5. Save it with the source files from Lab 01.

Open your `GW - Reporting Procedure - Working` document from Lab 01. Every step in this lab happens in that document.

**How the document comes together:**

Purpose statement > **Procedure** (Prepare, Check, Submit for Review, Resolve Questions) > **Questions for the Sponsor** > **Authoring Log**: Lab 01 evidence > AI draft review > procedure plan > test cases > walkthroughs > step 5 rewrite > submission distinction

The reader-facing procedure goes above the Authoring Log. Everything you use to check and test it goes at the end of the Authoring Log.

> **No Gemini?** Skip 2.1. In 2.2, review the supplied procedure from 2.3 against the sources instead of a Gemini reply, and call your notes `Reference draft review`. Everything after that is the same.

## Topics

**An AI draft is a proposal.** Gemini writes fluently, so a draft can read well and still leave out a status, or give an instruction like "route submissions according to the project structure" that doesn't tell anyone where to send anything. You check every instruction against the sources before any of it goes into the procedure.

**Testing a procedure on paper.** A procedure works if a person can follow it and always knows the next action. The quickest test is a *paper walkthrough*: take one real case and go through the steps in order, noting where you get stuck. You do one for a normal task and one for a task with missing information, then repair the step that caused trouble.

---

## 2.1 Ask Gemini for a Draft

The prompt below follows the course's GCSE pattern: **G**oal, **C**ontext, **S**ource and **E**xpectations. The fact sheet is pasted in, so Gemini works from the same facts you do.

1. In your working document, click **Ask Gemini** (the star button at the top right). The Gemini panel opens on the right.
2. Copy the prompt below and paste it into the **Ask Gemini** box. Don't submit it yet.

**Session:** new Gemini panel chat | **Grounding:** pasted project-facts.txt

```text
Goal: Propose a weekly reporting procedure for team members.
Context: Fictional Seri Maju Projects training exercise.
Source: Only the facts pasted below.
Expectations: Reply in the panel only, without editing my document. Use headings Prepare, Check, Submit for Review and Resolve Questions, with numbered steps. Label operational steps as proposed training practice. Preserve the proposed budget and unresolved start date. Do not invent approval authorities, deadlines or systems.

FACTS:
FICTIONAL TRAINING MATERIAL
All organisations, people and project details below are fictional.

Organisation: Seri Maju Projects
Location: Petaling Jaya, Malaysia
Project: Project Reporting Pilot
Project coordinator: Aina Rahman
Project sponsor: Farid Hassan
Pilot teams: Planning, Procurement and Site Coordination
Pilot duration: four weeks from an agreed start date
Start date: not yet agreed
Budget ceiling: RM 12000
Budget status: proposed, not approved
Purpose: test a consistent weekly project reporting process
Required outputs: a project brief, task register, weekly status update and project hub
Reporting cadence: one status update every Friday during the pilot
Known risk: teams may use different definitions of task status
Known constraint: use fictional training data only
Success measure: all three teams submit their weekly update on time for the final two weeks
Unresolved decision: sponsor approval of the budget and the pilot start date
Out of scope: live construction records, purchasing commitments and external publication
```

3. Read the **Expectations** line once. It asks for a reply in the panel, not a change to your document, and tells Gemini to keep the budget and start date open.

![The Gemini panel with the drafting prompt pasted into the Ask Gemini box, not yet submitted](./images/c02-02-source-grounded-prompt.png)

*The prompt, with the fact sheet, is in the box and not yet submitted.*

4. Click **Submit** (the arrow at the bottom right of the panel).
5. If Gemini offers to edit your document, click **Reject all**. This lab only uses the reply in the panel.

**Check:** Gemini's reply is in the panel, and your document hasn't changed.

---

## 2.2 Review the Reply Against the Sources

Now you check the reply before using any of it. The table shows what the sources actually say about the three things most likely to go wrong, so you don't need to open the files.

| What to check in the reply | Source file | What the source says |
|---|---|---|
| Status definitions | reporting-guidance.txt | Not Started: work has not begun. In Progress: work has begun without owner-confirmed completion. Complete: the owner has confirmed the agreed output is ready for review. |
| Submission details | Both files | Friday reporting is known. Neither file gives a submission channel, review recipient or cut-off time, so those stay open. |
| Project facts | project-facts.txt | RM 12000 is proposed, not approved. The start date is not agreed. The pilot lasts four weeks from an agreed start, with an update every Friday. |

Here's one finding written out, for an invented reply that called the budget approved:

> **Gemini wrote:** The RM 12000 budget is approved.<br>
> **Source says:** project-facts.txt records the budget as proposed, not approved.<br>
> **Decision:** Change it to "The RM 12000 budget is proposed, not approved."

If the reply already matches the source, the decision is **no repair needed**.

1. Read your whole reply in the panel, scrolling down to the end.

   This example reply shows the kind of problem to look for. Yours will be worded differently and may not have the same problems.

   ![Example reply, view 1 of 2: its Check section includes Complete and In Progress but omits Not Started](./images/c02-02-unreviewed-response.png)

   *In this example, the Check section leaves out Not Started.*

   ![The same example reply, view 2 of 2 after scrolling: Submit for Review contains a vague routing instruction](./images/c02-02-response-checks.png)

   *Further down the same reply, "Route submissions according to the project structure" gives no usable destination.*

2. Press **Ctrl+End** to go to the end of the document, press **Enter**, and type `AI draft review` and today's date.
3. Under it, write three findings, one each for **statuses**, **submission details** and **project facts**. Use the three labels from the example: `Gemini wrote:`, `Source says:` and `Decision:`.

![The AI draft review typed at the end of the Authoring Log](./images/c02-02-human-review.png)

*This review records the problems in the example reply. Yours records what you found in your own reply, including anything that needs no repair.*

**Check:** your AI draft review has three findings, and each one names its source file and either a repair or **no repair needed**.

---

## 2.3 Insert the Checked Procedure

Everyone continues from the same checked procedure, so the rest of the lab works the same for every learner. You still use your review: it tells you whether this version avoids the problems Gemini had.

1. Scroll to the top. Click at the end of the purpose statement, just above **Authoring Log**, and press **Enter**.
2. Copy the procedure below and press **Ctrl+V**. The title and four section labels are included.

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

*The procedure sits in the reader-facing part, above the Authoring Log.*

3. Click at the end of step 8 and press **Enter**. Copy the block below and press **Ctrl+V**.

```text
Questions for the Sponsor
- Is the proposed RM 12000 budget approved? Open decision; sponsor approval is not evidenced.
- What is the agreed pilot start date? Open decision; no calendar date or approval authority is inferred.
```

![Questions for the Sponsor with the two open decisions at the end of the procedure](./images/c02-02-open-decisions.png)

*The procedure ends with the two open decisions. It doesn't invent an approval or a date.*

4. Read step 4 of the procedure. It doesn't mention the three statuses, which is the same gap as the example reply. You fix it in 2.4.
5. In your AI draft review, add one line: `Reference draft:` and one thing it gets right that your Gemini reply got wrong, or one thing both got right.

**Check:** above **Authoring Log** you have the procedure title, four section labels, eight steps and **Questions for the Sponsor**.

---

## 2.4 Add the Procedure Plan and Fix Step 4

The plan lays each step out as input, action, output and check, so you can see whether every step has a way to tell it's done. It's supplied to save typing. The source tags in brackets show where each action comes from: `(facts)` is the fact sheet, `(guidance)` the reporting guidance and `(proposed)` a working detail you're suggesting.

1. Press **Ctrl+End**, then **Enter** twice.
2. Click **Copy heading and table** below, go back to the document and press **Ctrl+V**.

<p data-copy-with-table><strong>Procedure plan - eight steps across four sections</strong><br>Sources: project-facts.txt (facts); reporting-guidance.txt v1 (proposed guidance). Workflow details are proposed practice.</p>

| Step | Input | Action | Output | Check |
|---|---|---|---|---|
| 1 Prepare | Supplied task record | Identify task; retain ID and owner (guidance) | Task or clarification query | No invented ID or owner |
| 2 Prepare | Current task information | Gather status and exception note (guidance) | Draft update | Fictional data only; gaps retained |
| 3 Check | Fact sheet | Check duration, cadence and budget (facts) | Context checked | Four relative weeks; Friday; RM 12000 proposed; start unagreed |
| 4 Check | Guidance v1 | Check all three status meanings (guidance) | Supported status or meaning query | No guessed mapping of unfamiliar labels |
| 5 Submit | Draft and unresolved routing | Prepare Friday review; request routing agreement (facts / proposed) | Review-ready draft retained | Channel, recipient and cut-off agreed before sending |
| 6 Submit | Intended project outputs | Check brief, register, update and hub (facts) | Scope check | No sending or publication authority |
| 7 Resolve | Missing or unsupported information | Record gap and ask for clarification (guidance / proposed) | Query and exception note | No invented decision |
| 8 Resolve | Evidence after clarification | Recheck entry against its source (proposed) | Checked entry or open query | Unresolved values stay visible |

![The procedure plan label and the first seven rows of the plan table](./images/c02-02-plan-first-steps.png)

*Each row has an input, an action, an output and a check.*

![The last rows of the plan complete eight steps across the four sections](./images/c02-02-plan-final-steps.png)

*Rows 6 to 8 cover the outputs, missing information and rechecking after clarification.*

3. Read row 4 of the plan. It says step 4 should check all three status meanings, which the procedure's step 4 doesn't do yet.
4. Scroll up to the procedure (not the plan). Select the whole of step 4, from `4.` to the end of its paragraph.
5. Copy the replacement below and press **Ctrl+V** to paste over the selection.

**Replacement for procedure step 4**

```text
4. Check the three proposed guidance categories: Not Started means work has not begun; In Progress means work has begun without owner-confirmed completion; Complete means the owner has confirmed the agreed output is ready for review. Preserve an unfamiliar label as a clarification query rather than inventing a mapping.
```

![Procedure step 4 now names all three proposed guidance statuses](./images/c02-02-status-repair.png)

*The arrow marks the new step 4. A status label that isn't one of the three becomes a question, not a guess.*

**Check:** the plan table is at the end of the Authoring Log, and the procedure's step 4 names all three statuses. The procedure still has eight steps.

---

## 2.5 Write the Two Test Cases

To test the procedure you need two cases: a normal task from the task list, and a test card with missing information. Here is the T001 row from `Tasks.csv`:

> **Source: Tasks.csv, row T001**<br>
> TaskID: T001 | Team: Planning | Task: Confirm reporting fields | Owner: Aina Rahman | DueWeek: 1 | Status: Complete

And here is the test card. It's a made-up case for testing only, so it doesn't go in the task list:

> **Test card T-TEST-A:** owner missing, status In Progress, exception note "awaiting owner confirmation".

1. Below the plan table, outside it, type `Example weekly submission - fictional supplied record`.
2. On the next line, write T001's submission in this form, using the values from the row above: `TaskID: ... | Owner: ... | Status: ... | Exception note: ...`. T001 has no exception, so write `none recorded`.
3. Press **Enter** twice and type `Missing-owner route - proposed practice`.
4. Under it, write two or three sentences saying what the procedure tells a contributor to do with T-TEST-A. Use steps 1 and 7 of the procedure.

<details markdown="1">
<summary>What should you see?</summary>

The T001 line matches the row: `TaskID: T001 | Owner: Aina Rahman | Status: Complete | Exception note: none recorded`.

The missing-owner route keeps the task ID, the In Progress status and the exception note, flags the missing owner for clarification and doesn't name anyone as owner. Who to ask, and by when, is still to be agreed, so the route leaves that open too.

</details>

![The T001 example submission and the missing-owner route for T-TEST-A](./images/c02-02-normal-and-exception.png)

*The reference wrote a little more for each case. What matters is that T001 matches the task list and no owner is invented for T-TEST-A.*

**Check:** your T001 line matches the row above, and your missing-owner route asks for clarification without naming an owner.

---

## 2.6 Walk Through the Procedure

Now play the contributor. Go through the eight steps with each case and notice where the procedure stops telling you what to do next.

1. Below the missing-owner route, type `Paper walkthrough A - normal supplied T001`.
2. Read steps 1 to 8 in order as if you were Aina reporting T001. Under the heading, type `Worked:` and the steps that gave you a clear next action.
3. Type `Observed ambiguity:` and any step where you weren't sure what to do. Look closely at step 5: the route isn't agreed yet, so what are you supposed to do with your finished draft?
4. Type `Paper walkthrough B - incomplete card T-TEST-A` and repeat steps 2 and 3 with the test card.

![Paper walkthroughs A and B with the observed ambiguity and its repair](./images/c02-02-paper-walkthroughs.png)

*Walkthrough A found that step 5 says "request agreement" but not what to do with the draft while you wait. The reference document already shows the repair you make in 2.7, and its rewrite record sits above the walkthroughs; yours comes after them.*

**Check:** both walkthroughs have a **Worked:** line and an **Observed ambiguity:** line, and walkthrough A mentions step 5.

---

## 2.7 Repair Step 5

Step 5 asks for agreement on the route but doesn't say what happens to the draft in the meantime. The repair keeps the draft and records a question until the route is agreed.

1. Scroll up to the procedure and copy the current text of step 5. You need it for the record.
2. Press **Ctrl+End**, then **Enter**. Type `Clarity rewrite - Submit for Review, step 5`, then on the next line `Before:` and paste the old wording after it.
3. Go back to the procedure and select the whole of step 5. Copy the replacement below and press **Ctrl+V** to paste over it.

**Replacement for procedure step 5**

```text
5. Prepare a review-ready draft containing task ID, recorded owner, one supported status and an exception note when needed. The fact sheet requires Friday reporting. Before sending, obtain agreement on the submission channel, review recipient and cut-off time; if any is missing, retain the draft and record a routing query. This exercise sends nothing.
```

![The rewritten step 5 in the procedure](./images/c02-02-clarity-rewrite.png)

*The new step 5 keeps the draft and records a routing query while the route is still open.*

4. Back in the rewrite record, type `After:` and paste the new wording. Then type `Preserved checks:` and list what the new step still requires: Friday reporting, task ID, owner, status and the exception note.
5. Under **Observed ambiguity** in walkthrough A, add `Repair: step 5 now says to keep the draft and record a routing query.`

**Check:** the procedure's step 5 is the new wording, it still has eight steps, and your rewrite record has **Before**, **After** and **Preserved checks** lines.

---

## 2.8 Tell a Submission From a Question

The last check: a draft can be complete and ready for review while it still can't be sent, because the route is open. This table puts the two cases side by side.

1. Press **Ctrl+End**, then **Enter** twice.
2. Click **Copy heading and table** below, go back and press **Ctrl+V**.

<p data-copy-with-table><strong>Submission distinction</strong></p>

| Record type | Observable distinction |
|---|---|
| Complete submission | ID, recorded owner, supported status and any exception note are checked. Keep the draft unsent until channel, recipient and cut-off are agreed. |
| Unresolved question | Record the gap, source and clarification needed. Retain the draft; do not guess a missing value. |

![A two-row table separates a complete submission from an unresolved question](./images/c02-02-submission-distinction.png)

*A complete submission can be ready for review while its route is still open.*

3. Below the table, type one sentence saying which row each of your two cases belongs to: T001 and T-TEST-A.

<details markdown="1">
<summary>What should you see?</summary>

T001 is a complete submission: every field is there and checked, but it stays unsent until the route is agreed. T-TEST-A is an unresolved question, because its owner is missing.

Your document now has the eight-step procedure with a repaired step 4 and step 5, the two sponsor questions, and in the Authoring Log your AI draft review, the plan, both test cases, both walkthroughs, the rewrite record and this table.

</details>

**Check:** your sentence puts T001 in the first row and T-TEST-A in the second.

<!-- Reference core captured 18 October 2026; the revised route, independent challenge and reviewer pilot remain pending. -->

---

## Independent Practice

Work without the steps above. Use the procedure and the sources, and write your own wording.

1. Under **Resolve Questions** in the procedure, add a short subsection called `Late or Incomplete Submission`. Give a contributor one clear action, what to record and how a reviewer checks it.
2. Test it with this second test card. It has a status that isn't one of the three in the guidance:

   > **Test card T-TEST-B:** owner Siti Aminah, status Blocked.

   Write `Paper walkthrough C - T-TEST-B` in the Authoring Log and note what your subsection tells the contributor to do. Don't change "Blocked" into one of the three statuses, and don't invent a deadline.
3. Ask a partner to read your subsection aloud and say what they'd do. Fix one thing they found unclear, and note the change under your walkthrough.

### Evidence to Hand Over

- The eight-step procedure with the repaired steps 4 and 5 and the two sponsor questions.
- Your AI draft review with three findings.
- The T001 example, the missing-owner route and both walkthroughs, with the step 5 repair recorded.
- Your Late or Incomplete Submission subsection and walkthrough C.

Be ready to point to one instruction in your procedure that is proposed practice rather than a source fact.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Gemini changed my document instead of replying in the panel | Press **Ctrl+Z** until the change is gone, or click **Reject all**. The prompt asks for a panel reply only. |
| The Ask Gemini button isn't there | Your account may not have Gemini. Follow **No Gemini?** under Before You Begin. |
| The procedure landed inside the Authoring Log | Select it, press **Ctrl+X**, click at the end of the purpose statement and press **Ctrl+V**. |
| My pasted table appeared inside another cell | Press **Ctrl+Z** once. Click a blank line below the table, outside it, and paste again. |
| The procedure now has nine steps | You pasted a replacement without selecting the old step. Delete the old step 4 or 5. |
| I'm not sure what to write in a walkthrough | Read one step at a time and ask: do I know what to do next? Write down any step where the answer is no. |

## Lesson Summary

You asked Gemini for a draft and checked it against the sources, then built a checked procedure with the sponsor's open decisions. You tested it with a normal task and a missing-owner case, found the gap in step 5 and repaired it. In Lab 03 you give the procedure headings and navigation so it works as a longer document.

**Check yourself:** what can a contributor do with a complete draft while the submission route is still unagreed?
