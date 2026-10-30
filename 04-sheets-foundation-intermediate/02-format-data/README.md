# 02 - Enter and Format Reliable Data

In this chapter you will use dates, numbers, currency, wrapping and sensible column widths.


**Target allocation:** 45 minutes: 10 explanation/demonstration, 15 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 35 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A readable register with numeric currency values and sensible dimensions.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Apply formats to typed numbers.
- Use wrapping and fitted dimensions.
- Distinguish appearance from the stored value.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use your original Tasks tab. If needed, reopen a fresh native copy of [TaskRegister.xlsx](../../shared/sample-files/TaskRegister.xlsx).

## 2.1 Inspect Values and Types

1. Click G2 and inspect the formula bar. The value is numeric 600, not text containing RM.
2. Select G2:H13. Apply a currency format suitable for Malaysian ringgit, with no decimals for this exercise.
3. Select E2:E13 and use a whole-number format. DueWeek is a practice week index, not a calendar date.

<details markdown="1">
<summary>What should you see?</summary>

Costs show their currency while remaining numeric. Week values still range from 1 to 4.

</details>

<!-- VERIFY: execute 2.1 in the target account and reconcile control names. Capture images/c04-02-01.jpg only from the real app. -->

## 2.2 Improve Readability

1. Select A1:H1 and apply a consistent header style with readable contrast.
2. Widen Task and Owner so text is legible. Use text wrapping for the task descriptions if needed.
3. Fit row heights after wrapping. Keep each data column separate; do not merge cells inside the register.

<details markdown="1">
<summary>What should you see?</summary>

Headers, names and cost figures are readable without cutting off text.

</details>

<!-- VERIFY: execute 2.2 in the target account and reconcile control names. Capture images/c04-02-02.jpg only from the real app. -->

## 2.3 Inspect Formatting Effects

1. On Navigation Practice, enter a sample date in J2 and apply a date format; keep it outside the baseline register.
2. Compare a numeric value displayed as currency with a typed text value such as RM 600.
3. Undo the practice entries if they are no longer useful. Confirm that formatting the original costs did not change their values.

<details markdown="1">
<summary>What should you see?</summary>

You can explain why number formatting does not convert arbitrary text into a number.

</details>

<!-- VERIFY: execute 2.3 in the target account and reconcile control names. Capture images/c04-02-03.jpg only from the real app. -->

## 2.4 Diagnose Display, Type and Readability Problems

1. On **Entry Practice** create a **Type Tests** block outside the copied records. Enter numeric 600, text `RM 600`, a relative week 2 and a local practice date in separate labelled cells.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Formatting intake: PlannedCost “RM 600” supplied as text; DueWeek “next Monday” with no agreed calendar start; a long Task description clipped in a narrow column. Treat type, missing date evidence and presentation as three different issues.
```


2. Inspect each formula-bar value and its display. Apply currency to the number and compare it with the text; formatting alone does not turn arbitrary text into a usable numeric input.

3. Add a temporary `=SUM(...)` check over the numeric and text cost cells. Record which value contributes and why the visually similar entries behave differently.

4. Use **Format**, **Number** to give costs a consistent RM display and DueWeek a whole-number display. Keep practice dates outside the source week column.

5. Apply wrapping, column widths and header contrast to the copied three-row table. Make each complete task description readable without merging source cells.

6. Use **Paste special**, **Values only** and **Format only** in separate practice cells. Compare the result to a normal paste and note which operation transfers each property.

7. Inspect the original Tasks numeric count and source values again. Formatting must not alter the twelve records or create a confirmed calendar date.

<details markdown="1">
<summary>What should you see?</summary>

Type-test block with observed calculation behaviour. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 2.4 and independent challenge; capture images/c04-02-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Repair the card’s three proposed entries in a separate intake table. Preserve raw input and record the clean value or clarification needed.

2. Prepare a readable three-record handout view with consistent currency and whole-week display. Prove the underlying numeric values remain numeric.

3. Give a partner two visually similar cost cells and ask them which one can be calculated reliably. Use formula-bar and SUM evidence in your explanation.

## Evidence to Hand Over

- Type-test block with observed calculation behaviour.
- Raw-to-clean intake table and readable entry-practice layout.
- Independent numeric evidence and unchanged 12-row source.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Currency looks correct but totals are wrong | Inspect numeric type and formula-bar value before changing more display formats. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Typed values and readable formatting prepare the register for calculation.

**Check yourself:** Why should you avoid merging cells inside a dataset?
