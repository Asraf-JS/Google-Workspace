# 12 - Review and Handover

In this chapter you will explain assumptions, refresh steps and known data limitations.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 50 minutes: 10 explanation/demonstration, 20 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 40 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A restored baseline and an update-tested workbook handover.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Explain the workbook update path.
- Identify future maintenance work.
- Leave a checked final state.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use your baseline workbook and separate capstone copy.

## 12.1 Review the Baseline

1. Clear temporary test entries and restore all source values changed during exercises.
2. Confirm the 24-record count and control totals.
3. Inspect filter states and remove or name any view that could mislead the next reader.

<details markdown="1">
<summary>What should you see?</summary>

The baseline is consistent and temporary tests no longer affect it.

</details>

<!-- VERIFY: execute 12.1 in the target account and reconcile control names. Capture images/c05-12-01.jpg only from the real app. -->

## 12.2 Write the Handover

1. Record where the source lives, what one row represents and which columns users may edit.
2. Describe formula, validation, pivot and chart ranges that must include a new row.
3. Document unmapped keys and other unresolved data issues rather than converting them to zero.

<details markdown="1">
<summary>What should you see?</summary>

A future editor can update the analysis without silently omitting records.

</details>

<!-- VERIFY: execute 12.2 in the target account and reconcile control names. Capture images/c05-12-02.jpg only from the real app. -->

## 12.3 Demonstrate One Update

1. On the capstone copy, add one new fictional order line and walk through the documented update steps.
2. Check the resulting calculations and visuals, then clearly label that copy as an extension test.
3. Keep the original baseline for future class recovery.

<details markdown="1">
<summary>What should you see?</summary>

The handover has been tested on an actual extension in a separate copy.

</details>

<!-- VERIFY: execute 12.3 in the target account and reconcile control names. Capture images/c05-12-03.jpg only from the real app. -->

## 12.4 Make the Analysis Operable by Another Analyst

1. Create a **Runbook** with source location, row grain, accepted inputs, editable fields, formula columns, exception handling and release controls.

2. Create a range inventory for validation, conditional formatting, SUMIFS, lookups, database functions, pivots, chart sources and weekly summaries used in your workbook.

3. On a separately named extension copy add PO025 and follow only the runbook to extend the analysis. Record every instruction that needed interpretation.

4. Reconcile the 25-record scenario by count, all-orders total, Delivered total and project/week contribution, then compare with the preserved 24-record baseline.

5. Test the unknown-key route without overwriting the supplied Rates mapping. Record the issue and leave a visible unresolved disposition.

6. Give a partner the runbook and ask them to locate a source, run a check and explain a failed key. If alone, use a fresh read-through with previous working tabs closed.

7. Repair one handover gap and issue a manifest identifying the maintained baseline, scenario test and current fixed summary.

<details markdown="1">
<summary>What should you see?</summary>

Complete range inventory and a runbook tested on PO025. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 12.4 and independent challenge; capture images/c05-12-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Use the different PO026 line on the card in another disposable copy and update the analysis without returning to the lesson steps.

2. Verify how Pending amount and exception flags change, including any new-row coverage failure. Record and repair the cause.

3. Hand over the runbook, controls, open issues and manifest. Another analyst must be able to reproduce both a successful update and an unresolved-key outcome.

## Evidence to Hand Over

- Complete range inventory and a runbook tested on PO025.
- Independent PO026 update with reconciled controls and exception coverage.
- Recorded handover repair, open-issue route and clear scenario manifest.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| The next analyst must guess a range extension | Record exact current bounds, the new-row action and the expected checks in the runbook. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

You can maintain and hand over a checked analysis rather than a collection of unexplained formulas.

**Check yourself:** Which assumption would you check first if a future total unexpectedly drops?
