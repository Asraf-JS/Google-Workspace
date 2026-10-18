# 06 - Summarise and Visualise

In this chapter you will build a simple conditional total and chart; ask Gemini to explain a checked formula if available.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 55 minutes: 10 explanation/demonstration, 25 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 45 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A conditional summary and a source-linked status chart.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Calculate a conditional count and total.
- Choose and label a simple chart.
- Use AI to explain a formula without surrendering the check.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use Tasks and the starter Summary tab. Existing baseline status counts are four per category.

## 6.1 Count Statuses

1. In Summary B2 enter `=COUNTIF(Tasks!$F$2:$F$13,A2)` and fill through B4.
2. Add a total in B5 using `=SUM(B2:B4)` and label A5 Total.
3. In D1:E4 add team labels and use SUMIF over Tasks B2:B13 and G2:G13 to calculate planned cost by team.

<details markdown="1">
<summary>What should you see?</summary>

Status counts are 4/4/4 and total 12. Planned team totals are Planning 2,800, Procurement 4,000 and Site Coordination 3,600.

</details>

<!-- VERIFY: execute 6.1 in the target account and reconcile control names. Capture images/c04-06-01.jpg only from the real app. -->

## 6.2 Build a Useful Chart

1. Select Summary A1:B4, excluding the total row. Choose Insert, Chart.
2. Choose a column chart and title it `Task count by status`.
3. Inspect category labels and make sure no blank category or total has become a fourth status.

<details markdown="1">
<summary>What should you see?</summary>

The chart shows three status categories with equal counts.

</details>

<!-- VERIFY: execute 6.2 in the target account and reconcile control names. Capture images/c04-06-02.jpg only from the real app. -->

## 6.3 Explain and Check

1. If Gemini is available, paste your COUNTIF formula and ask it to explain the anchored range and relative criterion cell in the panel only.
2. Compare the explanation with the formula in B3.
3. Temporarily change T003 to Complete, observe 5/4/3 and restore it. Confirm the chart returns to baseline.

<details markdown="1">
<summary>What should you see?</summary>

Both your explanation and the chart's update behaviour have been checked against an actual input change.

</details>

<!-- VERIFY: execute 6.3 in the target account and reconcile control names. Capture images/c04-06-03.jpg only from the real app. -->

## 6.4 Build a Second Summary and Diagnose a Misleading Chart

1. Add a second chart for planned cost by team using the checked D:E summary. Label currency units and keep task counts separate from cost amounts.

2. Create a small **Summary Checks** block comparing total status counts with the number of TaskIDs and team planned totals with Tasks planned total.

3. On a chart copy deliberately include the status total row as a fourth category. Explain the double-counting risk, then repair the source range.

4. On a summary copy deliberately misspell one status label. Observe how COUNTIF and the chart respond. Repair the spelling rather than overwriting the result with a typed number.

5. Write two supported findings, one about task counts and one about planned cost distribution. Avoid claims about on-time success or realised savings.

6. Test a temporary change to one task’s planned cost. Check the row, team summary, grand total and chart; then restore the source value.

7. Record each change and restoration in a check log with expected effect, observed effect and the range or label you inspected.

<details markdown="1">
<summary>What should you see?</summary>

Two reconciled summaries/charts with distinct units. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 6.4 and independent challenge; capture images/c04-06-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Prepare an independent one-page dashboard on a new tab with two labelled charts, source links and two concise supported findings.

2. Diagnose the card’s suspicious chart and summary symptoms using the source cells. Repair the cause, not just the visual appearance.

3. Use a reviewer or fresh read-through to check units, population and total reconciliation, then record one correction or evidence for a no-change decision.

## Evidence to Hand Over

- Two reconciled summaries/charts with distinct units.
- Documented total-row and misspelt-category fault repairs.
- Independent dashboard, supported findings and restored source-change test.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A missing count is hidden by typing a result | Repair the criterion or formula so later source changes still recalculate. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

A checked summary and chart communicate the register accurately.

**Check yourself:** Why should the total row normally be excluded from this chart's categories?
