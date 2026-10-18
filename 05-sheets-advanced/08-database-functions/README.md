# 08 - Query Structured Criteria

In this chapter you will use DSUM, DCOUNT and DAVERAGE with a visible criteria range and reconcile against a manual subset.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 60 minutes: 15 explanation/demonstration, 17 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 45 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A visible criteria area and reconciled database function results.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Build a visible database criteria range.
- Use DSUM, DCOUNT and DAVERAGE.
- Reconcile criteria-based results.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use Orders A1:J25, including Amount. Keep criteria outside the source table.

## 8.1 Build the Criteria

1. On Analysis type Status in A10 and Delivered in A11. Match the Orders header exactly.
2. In C10 type `Delivered amount`. In D10 enter `=DSUM(Orders!A1:J25,"Amount",A10:A11)`.
3. Compare the result with the delivered control total.

<details markdown="1">
<summary>What should you see?</summary>

DSUM returns 1,478 using the visible Delivered criterion.

</details>

<!-- VERIFY: execute 8.1 in the target account and reconcile control names. Capture images/c05-08-01.jpg only from the real app. -->

## 8.2 Count and Average

1. In C11 type `Delivered numeric quantity records`; in D11 enter `=DCOUNT(Orders!A1:J25,"Quantity",A10:A11)`.
2. In C12 type `Average delivered unit cost`; in D12 enter `=DAVERAGE(Orders!A1:J25,"UnitCost",A10:A11)`.
3. Discuss why DCOUNT of the text OrderID field would not count order IDs like a text-aware count.

<details markdown="1">
<summary>What should you see?</summary>

DCOUNT counts numeric Quantity entries in qualifying records. The average is of unit costs, not a quantity-weighted price.

</details>

<!-- VERIFY: execute 8.2 in the target account and reconcile control names. Capture images/c05-08-02.jpg only from the real app. -->

## 8.3 Check Criteria Semantics

1. Filter the source to Delivered and manually inspect a small sample contributing to each result.
2. Add Project as a second criteria header beside Status and use PJ-A on the same criteria row to mean both conditions.
3. Compare with SUMIFS for the same project/status pair. Restore or clearly label the expanded criteria.

<details markdown="1">
<summary>What should you see?</summary>

The database function and ordinary conditional formula agree when their criteria describe the same subset.

</details>

<!-- VERIFY: execute 8.3 in the target account and reconcile control names. Capture images/c05-08-03.jpg only from the real app. -->

## 8.4 Prove AND, OR and Overlapping Criteria

1. Create three separate criteria blocks with exact source headers: Delivered AND PJ-A; Delivered OR Pending; and Delivered OR PJ-A. Label each natural-language population.

2. Use same-row criteria for the AND block and separate criteria rows for OR blocks. Keep blocks spatially separate from result cells.

3. Calculate DSUM, DCOUNT of numeric Quantity and DAVERAGE of UnitCost for each block. Record how blanks or text could affect the latter two metrics.

4. For the AND block reconcile amount with SUMIFS and list matching OrderIDs using a filter view.

5. For Delivered OR Pending reconcile with the sum of two disjoint status totals. For Delivered OR PJ-A inspect the overlap so a record satisfying both conditions is not counted twice.

6. Compare an unweighted mean UnitCost with a quantity-weighted cost measure on a small explicit test. State which question each answers.

7. Deliberately misspell one criteria header on a disposable block. Record the observed error or result and repair it using the exact source heading.

<details markdown="1">
<summary>What should you see?</summary>

Three labelled criteria blocks with source-ID reconciliation. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 8.4 and independent challenge; capture images/c05-08-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Write a new analysis question requiring two conditions and design its database criteria without copying a finished block.

2. Create a second version that uses OR instead of AND, predict the population difference and verify it through contributing IDs.

3. Explain the numeric field counted by DCOUNT, the average’s denominator and one overlap risk.

## Evidence to Hand Over

- Three labelled criteria blocks with source-ID reconciliation.
- AND/OR and overlap proof, plus weighted/unweighted meaning comparison.
- Independent question and corrected criteria-header test.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| An OR total double-counts overlapping rows | Compare the contributing ID sets and count each qualifying source record once. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Database functions are useful when their header matching, criteria logic and field meaning are explicit.

**Check yourself:** Why is an average unit cost different from a quantity-weighted average?
