# 07 - Run an AI Pilot

In this chapter you will apply a repeatable prompt workflow to a small task and compare the checked result with a manual baseline.

> **Prompts:** the [prompts page](./prompts.md) has every value and prompt for this chapter, each with a Copy button.

**Estimated time:** 50 minutes, planned as 10 explanation and demonstration, 20 guided build and casework, 15 independent practice and 5 verification and repair, with 40 active minutes by design. Not yet timed with learners.

**Your result:** A supervised pilot with checked outputs and a transparent timing comparison.

> **Status:** guided author reference with 15 staged captures. Predefined rubric, checked A/B attempts and a targeted author rerun are recorded. Human manual baseline, complete active-effort timing, independent challenge, reviewer agreement and classroom timing remain unvalidated.

---

## What You Will Learn

- Define a small repeatable task.
- Compare manual and AI-assisted work fairly.
- Measure the checked outcome rather than raw speed.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use the fictional source pack and review log. This is a supervised manual workflow, not a deployed unattended automation.

## 7.1 Define the Pilot

1. In **GW - AI - Practice** create a Google Doc named `GW - AI - Pilot Evaluation`. Use the same three original fictional sources for every attempt. Set the acceptance rule before generation: all five topics pass, each consequential claim has source support, and no approval, date, supplier or gain is invented.
2. Copy the rubric from Part 3 of the prompts page into the Doc. The date criterion includes both the unagreed calendar start and the unresolved sponsor decision. Record prior familiarity and attempt order. A rejected first draft is not an accepted output.
3. A participant should first write and check a manual FAQ, logging drafting and checking separately. Its source-based reference is not a human manual baseline. Human manual and classroom timings remain unmeasured; no productivity percentage can be calculated.

> **Reference run:** **Author boundary:** this reference was prepared by an AI agent with extensive source familiarity.

![The Pilot Evaluation Doc with the acceptance rule, scoring criteria and study limits written before generation](./images/c06-07-01-predefined-protocol.png)

*The rubric is fixed before any answer exists.*

## 7.2 Run the Assisted Attempt

1. Open a fresh Gemini conversation in the approved account. Record the visible mode. Paste the Attempt A prompt from Part 4 of the prompts page, followed by all three labelled originals. Do not paste only the question list.

> **Reference run:** The author used Flash.

![A fresh Gemini chat with the model set to Flash](./images/c06-07-02-fresh-flash-session-a.png)

*Record the visible model before pasting the prompt.*

2. Submit once and record generation waiting separately. While waiting, retain the expected source facts and a clearly unscored ledger.

> **Reference run:** The author reference below is a source check, not a timed human attempt.

![The source reference and an attempt ledger with every score pending](./images/c06-07-03-source-reference-and-pending-ledger.png)

*Nothing is scored while generation is running.*

3. Read the complete response before scoring. A source label is only a pointer: compare the quoted passage with the actual original.

> **Reference run:** the observed Set A used five extractive entries with S1 quotes.

![The Set A response: five numbered answers, each with a source and quote](./images/c06-07-04-set-a-response.png)

*A source label is a pointer. Check the quote against the original.*

## 7.3 Evaluate the Outcome

1. Apply the predefined rubric (Part 3 of the [prompts page](./prompts.md)) without changing it after seeing the response. Score each of the five topics pass or repair.

> **Reference run:** Set A preserved the purpose/duration, teams, cadence/success and budget status. Its date quote retained “not yet agreed” but omitted the unresolved sponsor-decision statement required by the scorecard: **4/5, repair required**. This is an omission against that contract, not an invented date.
2. If a topic needs repair, correct only that answer from the original sources, then recheck the corrected version against the rubric. Keep the original model response and mark your repair as yours, not a regenerated answer.

> **Reference run:** the author correction: retain A1–A4 and replace A5 with the no-agreed-date statement plus S1's exact unresolved-decision line. Recheck the corrected reference: **5/5**. Keep the original model response and distinguish the author's repair from a regenerated answer.

![The Set A claim audit with one topic marked Repair, and the author correction](./images/c06-07-06-set-a-audit-and-repair.png)

*The original response stays as it was; the repair is recorded separately.*

3. Include prompting, source checking and repair in active effort. Keep generation wait, sign-in, setup and interruptions separate. Complete human timing is still required before a manual/assisted comparison.

> **Reference run:** The author observed Set A complete within about 98 seconds of submission; that interval included other work and is an upper bound, not exact server latency or human effort.

## 7.4 Run a Small, Interpretable AI Evaluation

1. Start a fresh conversation and paste the Attempt B prompt (Part 5 of the prompts page) with the unchanged brief, mode and source pack. It asks the same five questions in a different order: budget, date, cadence/success, teams, purpose/duration. This is a reordered repeat, not an unseen task or a human baseline. Keep attempt order and familiarity visible.

![A second fresh Flash chat for Set B](./images/c06-07-05-fresh-flash-session-b.png)

*Set B uses the same sources and brief in a new conversation.*

2. Record a design issue before the repair trial: the original visible date question did not explicitly ask for every scorecard detail. The score remains recorded, but do not blame the omission solely on the model. Keep A and B unchanged; prepare the explicit acceptance-check block for a separate Set A rerun C.

![The note explaining the prompt design issue before rerun C](./images/c06-07-07-targeted-revision-before-rerun.png)

*The date question didn't ask for every scorecard detail, so the omission isn't only the model's.*

3. Inspect the entire Set B answer and its original supporting passages, including facts beyond its short excerpts. Score it with the same rubric.

> **Reference run:** It retained the unapproved budget, sponsor identity and unresolved date/decision, plus all other required facts. First-review result: **5/5; no correction needed**. Do not infer that reordering caused the difference.

![The Set B response with the questions in a different order](./images/c06-07-08-set-b-response.png)

*Same five topics, reordered.*

![The rest of the Set B response with its supporting passages](./images/c06-07-09-set-b-source-tail.png)

*Read the whole answer, including facts beyond the short quotes.*

![The Set B review table with every criterion checked](./images/c06-07-10-set-b-audit.png)

*Score Set B with the same rubric as Set A.*

4. Run C in another fresh Flash conversation using Set A and the same sources, adding only the explicit output acceptance block. Apply the same rubric when a complete answer exists. No cause was established and no retry was submitted. Keep C unscored; this does not demonstrate a successful repair. This is an author repair attempt, not an independent learner challenge.

> **Reference run:** C remained generating after more than seven minutes, then returned to the new-chat composer with the prompt restored and no answer.

![Rerun C still generating, with no answer](./images/c06-07-11-targeted-rerun-wait.png)

*A pending response can't be scored.*

![The note recording rerun C as not yet assessed](./images/c06-07-12-targeted-rerun-unscored.png)

*Keep C unscored rather than filling in an expected result.*

![Gemini back at the new-chat composer with the prompt restored and no answer](./images/c06-07-15-rerun-returned-to-composer.png)

*The rerun returned no response, so it stays unscored.*

5. Save the final review and timing ledger. Report the actual sample size, prompt-contract mismatch, order/familiarity effects and unmeasured phases. B and C generation waits overlapped; do not add those intervals as sequential task duration. A complete participant comparison must include all active drafting, prompting, checking and correction for each accepted output. The maintained FAQ below is author-checked text, not a substitute for C's missing response.

![The maintained checked FAQ, marked as an author reference](./images/c06-07-13-maintained-checked-faq.png)

*This checked text is not an unedited model response or a human baseline.*

![The final ledger: human baseline not run, A repaired, B accepted, C unscored](./images/c06-07-14-final-ledger-and-limits.png)

*The ledger reports what was actually run and what wasn't.*

6. Recommend a narrow next trial: have a participant complete the aligned manual and assisted tasks using the same sources and acceptance rule, with phase timing and reviewer checks. Repeat on an equivalent task with a different order. Keep the checked outputs, defects and repairs; avoid company-wide ROI claims from this demonstration.

See the [author results and maintained FAQ](./author-reference.md).

## Independent Practice

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Independently revise the prompt or review process based on the first results and rerun one previously failed case.

2. Show whether quality improved and what extra checking effort was required. If no failure occurred, test a missing-fact or conflicting-source case.

3. Recommend one narrowly defined next trial and specify the evidence required before changing a real workflow.

### Evidence to Hand Over

- Predefined acceptance rubric and comparable manual/assisted attempts.
- Timing ledger separating active effort, wait and rework, with quality scores.
- Independent process revision, rerun and bounded next-trial recommendation.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A time-saving claim excludes review effort | Compare accepted outputs and include prompting, checking and correction as active work. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

A useful AI pilot measures a checked workflow under stated conditions.

**Check yourself:** Which review work must be included in the assisted task time?
