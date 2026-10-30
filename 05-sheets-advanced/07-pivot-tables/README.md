# 07 - Summarise with Pivot Tables

In this chapter you will group project costs and status; inspect filters, calculated fields and source coverage.


**Target allocation:** 75 minutes: 15 explanation/demonstration, 32 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 60 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A native pivot with checked filters and a calculated-field demonstration or recorded limitation.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Create a native pivot summary.
- Choose filters and aggregation deliberately.
- Check a calculated field against row calculations.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use Orders A1:K25 after calculating Amount in J and ActiveAmount in K. A recovery route is to repeat Advanced Chapter 2 on the supplied workbook.

## 7.1 Build the Pivot

1. Select Orders A1:K25 and use Insert, Pivot table. Place it on a new tab named `Pivot Review`.

**Copy: Typed Values**

```text
Pivot Review
```


**Copy: Typed Values**

```text
=SUM(Quantity*UnitCost)
```

2. Add Project as rows and Status as columns. Add Amount as values, summarised by SUM.
3. Inspect totals and confirm the grand total is 3,158.

<details markdown="1">
<summary>What should you see?</summary>

The pivot shows all projects and statuses. It has not discarded cancelled records without a stated filter.

</details>

<!-- VERIFY: execute 7.1 in the target account and reconcile control names. Capture images/c05-07-01.jpg only from the real app. -->

## 7.2 Filter and Compare

1. Filter the pivot to Delivered only and check the total becomes 1,478.
2. Compare the result with the earlier SUMIFS or filtered source calculation.
3. Remove the pivot filter and verify the all-orders total returns.

<details markdown="1">
<summary>What should you see?</summary>

Filtered and unfiltered results answer different documented questions.

</details>

<!-- VERIFY: execute 7.2 in the target account and reconcile control names. Capture images/c05-07-02.jpg only from the real app. -->

## 7.3 Inspect a Calculated Field

1. Create a separate practice pivot using the same source. Group by Project.
2. Add a calculated field for average line amount, using `=SUM(Amount)/COUNTA(OrderID)` and **Summarise by**, **Custom** if supported by the target UI. Compare with a source calculation. Retain SUM of the row-level Amount as the authoritative total.
3. If that calculated-field expression is rejected, retain the working Amount source column and record the limitation for the trainer; do not replace it with an unrelated metric.

<details markdown="1">
<summary>What should you see?</summary>

The calculated-field demonstration is reconciled to the existing row calculation, or explicitly recorded as unavailable.

</details>

<!-- VERIFY: execute 7.3 in the target account and reconcile control names. Capture images/c05-07-03.jpg only from the real app. -->

## 7.4 Reconcile Pivot Semantics and New-Row Coverage

1. Create a second pivot counting OrderID by Project and Status. Compare its population count with the 24-row source and its category counts with COUNTIFS.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
PO025, challenge copy only: PJ-A | Planning | IT01 | Quantity 2 | UnitCost 45 | Delivered | week 4 | Additional practice line. Amount is quantity times cost. Extend both formulas and pivot source range; do not alter the baseline workbook.
```


2. Double-click a populated pivot value where supported to inspect its contributing source rows. Reconcile the amount from those rows independently.

3. Use a safe calculated field such as `=SUM(Amount)/COUNTA(OrderID)` with **Summarise by**, **Custom**, where the target UI supports it. Label this as average line amount and compare with a source calculation.

4. Do not replace SUM of row Amount with SUM(Quantity)*SUM(UnitCost). Calculate both on a small two-row practice table and explain the different meanings.

5. On a separate pivot challenge copy append the supplied PO025 record. Inspect whether the fixed pivot source range includes it.

6. Extend the source range and inspect both the count and amount pivots. Compare them with a repaired formula summary.

7. Record pivot source range, filters, aggregation and calculated-field definition in an analysis note. If the calculated field is unavailable, retain source Amount and document that specific UI check as pending.

<details markdown="1">
<summary>What should you see?</summary>

Amount and count pivots reconciled to formulas and contributing source rows. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 7.4 and independent challenge; capture images/c05-07-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Build a fresh pivot independently answering Delivered amount by Project, with a count of contributing order lines.

2. On the challenge copy include PO025 and show the source row, count, total and changed project contribution. Leave the baseline pivot unchanged.

3. Explain one aggregation trap and use contributing rows to prove the correct result.

## Evidence to Hand Over

- Amount and count pivots reconciled to formulas and contributing source rows.
- Safe calculated-field comparison or documented unavailable route.
- Separate new-record pivot with repaired coverage and demonstrated aggregation semantics.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A pivot total is wrong even though the row appears | Inspect aggregation, filters, source range and calculated-field meaning separately. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Native pivots summarise a defined source. Their filters and formulas need the same checks as ordinary calculations.

**Check yourself:** Why must the pivot's source range include every record and calculated column?
