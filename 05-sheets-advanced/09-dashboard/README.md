# 09 - Build a Dashboard

In this chapter you will choose charts, sparklines and filter views; distinguish source-linked charts from generated analysis snapshots.


**Target allocation:** 70 minutes: 15 explanation/demonstration, 27 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 55 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A compact source-linked dashboard with a tested update path.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Choose source-linked visuals.
- Use a sparkline for a defined time sequence.
- Explain how a dashboard refreshes.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use the checked advanced workbook with all-orders and delivered controls reconciled.

## 9.1 Build a Compact View

1. Create a Dashboard tab. Link a small project summary to the checked analysis or create a fresh pivot from the same source.
2. Add a chart comparing Amount by Project and label whether cancelled orders are included.
3. Add a separate status count view with clear labels. Keep detailed source records in Orders.

<details markdown="1">
<summary>What should you see?</summary>

The dashboard identifies the question and population behind each number.

</details>

<!-- VERIFY: execute 9.1 in the target account and reconcile control names. Capture images/c05-09-01.jpg only from the real app. -->

## 9.2 Show the Weekly Sequence

1. On Analysis create week labels 1, 2, 3 and 4 and calculate Amount totals for each with SUMIFS.
2. On Dashboard create a labelled sparkline using the four weekly result cells, for example `=SPARKLINE(Analysis!B16:E16)` after placing the totals there.

**Copy: Typed Values**

```text
=SPARKLINE(Analysis!B16:E16)
```

3. Check that the sequence is chronological and its totals reconcile to all-orders Amount.

<details markdown="1">
<summary>What should you see?</summary>

The sparkline describes the four supplied practice weeks, not an invented real calendar period.

</details>

<!-- VERIFY: execute 9.2 in the target account and reconcile control names. Capture images/c05-09-02.jpg only from the real app. -->

## 9.3 Test a Refresh

1. Temporarily change one source quantity. Check the line amount, summary, chart and sparkline.
2. Inspect whether a pivot has updated and whether its source still includes all rows.
3. Restore the source quantity. Document any manual refresh step and keep filters visible or clearly named.

<details markdown="1">
<summary>What should you see?</summary>

The dashboard returns to the reconciled baseline after restoration.

</details>

<!-- VERIFY: execute 9.3 in the target account and reconcile control names. Capture images/c05-09-03.jpg only from the real app. -->

## 9.4 Design a Dashboard With a Visible Refresh Contract

1. Write a dashboard brief specifying audience, population, units, three useful questions and the source range. Do not mix all-orders and active totals without labels.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Audience questions: Which project has the largest Delivered amount? How much Amount remains Pending? Which practice week has the largest all-orders Amount? PO025 extension: PJ-A, Planning, IT01, Quantity 2, UnitCost 45, Delivered, week 4.
```


2. Add KPI cells for record count, all-orders Amount, ActiveAmount and Delivered Amount. Reconcile each to the corresponding checked analysis.

3. Show project amount comparison, status count and weekly sequence with explicit filter scope. Keep week order numeric and label it as practice week.

4. Create a visible **Checks** block comparing KPI totals with source controls and indicating any mismatch. It must recalculate from cells rather than contain typed “OK” text.

5. On a scenario copy change PO001 Quantity from its baseline to 4. Predict the amount delta and check the source line, summary, chart and weekly sequence.

6. Restore the quantity and prove all affected values return. Record which components follow source-cell changes and which depend on range extension for new rows.

7. Prepare a refresh contract listing source bounds, pivot bounds, formula bounds, chart ranges, filter scope and snapshot/export steps.

<details markdown="1">
<summary>What should you see?</summary>

Defined dashboard with distinct populations, units and recalculating controls. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 9.4 and independent challenge; capture images/c05-09-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Build an independent dashboard view answering the three audience questions on the card, with at least one visible reconciliation check.

2. Append PO025 only on a challenge copy and repair source-range coverage across KPIs, pivots, charts and the weekly sequence.

3. Ask a reviewer to identify the population and a stale component using the labels/checks, then revise any misleading element.

## Evidence to Hand Over

- Defined dashboard with distinct populations, units and recalculating controls.
- Source-change/restoration trace across line, summary and visuals.
- Independent new-row coverage test and a usable refresh contract.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A dashboard looks current but omits the new line | Trace range coverage through every KPI and visual rather than checking only one total. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

A dashboard is useful when its totals, populations and update path are understandable.

**Check yourself:** Which dashboard objects depend on which source calculations?
