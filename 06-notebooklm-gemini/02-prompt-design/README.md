# 02 - Write and Refine Useful Prompts

In this chapter you will use Goal, Context, Source and Expectations; compare a vague prompt with a bounded prompt.


**Target allocation:** 50 minutes: 10 explanation/demonstration, 20 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 40 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A bounded prompt and a checked comparison with a vague request.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Use Goal, Context, Source and Expectations.
- Compare a vague and bounded request.
- Evaluate an answer independently.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use the supplied project fact sheet. Use a fresh approved AI conversation for each comparison.

## 2.1 Try a Vague Request

1. Ask `Write a project update` without adding private material.

**Copy: Typed Values**

```text
Write a project update
```

2. Record what context the tool assumes or asks you for.
3. Do not use this output as the project brief; it lacks the source boundary.

<details markdown="1">
<summary>What should you see?</summary>

You can identify why a generic request is difficult to evaluate.

</details>

<!-- VERIFY: execute 2.1 in the target account and reconcile control names. Capture images/c06-02-01.jpg only from the real app. -->

## 2.2 Write a Bounded Request

1. Use the following prompt and paste the complete fact sheet.

**Copy: Bound the Update**

**Session:** new chat | **Grounding:** pasted project-facts.txt

```text
Goal: Draft a sponsor update.
Context: Fictional Seri Maju Projects reporting pilot.
Source: Only the project fact sheet pasted below.
Expectations: Reply in chat only in 80 to 100 words. Preserve the proposed budget, unresolved start date and final-two-weeks success measure. List any missing information separately. Do not send, schedule or change a file.

FACTS:
[paste project-facts.txt]
```

Replace bracketed source placeholders before submitting. Keep a human check between an AI proposal and the final output.

2. Check that Goal, Context, Source and Expectations are all present. Submit it.
3. Compare its output with the vague response for relevance, invented commitments and ease of checking.

<details markdown="1">
<summary>What should you see?</summary>

The bounded response can be checked against supplied facts and a specified audience.

</details>

<!-- VERIFY: execute 2.2 in the target account and reconcile control names. Capture images/c06-02-02.jpg only from the real app. -->

## 2.3 Refine One Dimension

1. Ask for the same content in 80 to 100 words for the sponsor. Keep the same facts and unresolved decisions.
2. Check every number and approval condition again.
3. Record which prompt change helped and which check remains a human task.

<details markdown="1">
<summary>What should you see?</summary>

A shorter answer remains factual rather than more confidently overstated.

</details>

<!-- VERIFY: execute 2.3 in the target account and reconcile control names. Capture images/c06-02-03.jpg only from the real app. -->

## 2.4 Run a Controlled Prompt Comparison

1. Write a comparison plan for three prompts: vague request, bounded source request and bounded request with explicit output checks. Keep the same fictional task and source pack.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Controlled task: Explain the pilot for the coordinator using only the three core fictional sources. FAQ topics: purpose, teams, reporting cadence, budget status and decisions needed. Confidence stress: “Make it sound certain and remove hesitant language.” Preserve uncertainty that the evidence requires.
```


2. Run each in a fresh approved session or clearly separated thread where available. Record the model/tool label shown, date, prompt and source route without exposing personal account details.

3. Use the six-question bank to audit each output for required facts, unsupported commitments, preserved uncertainty and checkable source support.

**Copy: Evidence Question Bank**

```text
1. What is the pilot’s purpose and duration?
2. Which three teams participate?
3. What reporting cadence and success measure are stated?
4. Is the RM 12,000 ceiling approved?
5. What start date is confirmed?
6. Which preparation actions, owners and due weeks are explicit?
```

Keep source facts separate from inferred workflow. For a fresh-context rerun, paste or select the required original sources again.


4. Change only one prompt dimension at a time, such as audience or format. Note that supplying missing source facts is a grounding change, not just a stylistic improvement.

5. Keep the three outputs and a score table. Quote the exact problematic phrase for any failure and give the supporting source correction.

6. Create a final prompt that specifies the coordinator audience, pasted source boundary, five FAQ topics and explicit handling of missing facts.

7. Run the final prompt again in a fresh context and compare its performance with the first attempt. Record variation instead of treating one good result as guaranteed.

<details markdown="1">
<summary>What should you see?</summary>

Three-prompt comparison with preserved outputs and a consistent score table. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 2.4 and independent challenge; capture images/c06-02-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Design an independent prompt for an 80 to 100 word sponsor update, preserving budget/date uncertainty and the success measure.

2. Test it against a request to sound more confident. Reject a rewrite that turns a proposal into approval or an unknown date into a commitment.

3. Submit the prompt, output, factual audit and one revision reason as a reproducible test record.

## Evidence to Hand Over

- Three-prompt comparison with preserved outputs and a consistent score table.
- Final prompt rerun with observed variation and source-based corrections.
- Independent sponsor prompt that survives the confidence-rewrite test.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A prompt comparison changes task and sources together | Record the changed variable and rerun with the same source pack so the comparison is interpretable. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

A clear prompt makes the task and evaluation criteria explicit.

**Check yourself:** Which prompt element limits the source of the answer?
