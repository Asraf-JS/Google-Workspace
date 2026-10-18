# 03 - Calculate and Copy Formulas

In this chapter you will use arithmetic, SUM, AVERAGE and COUNT; explain relative and absolute references.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 65 minutes: 15 explanation/demonstration, 22 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 50 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** Copied variance formulas, reconciled totals and a tested fixed reference.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Write arithmetic and aggregation formulas.
- Copy relative references correctly.
- Anchor a shared assumption.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use Tasks A1:H13. The workbook has no prefilled answer formulas.

## 3.1 Calculate Variance

1. In I1 type `Variance`. In I2 enter `=H2-G2`.
2. Fill I2 through I13 using the fill handle or copy and paste.
3. Inspect I2, I7 and I13 in the formula bar. Each formula should reference its own row. Negative variance means actual cost is below planned cost.

<details markdown="1">
<summary>What should you see?</summary>

T001 has variance -50. The formula in I13 uses H13 and G13.

</details>

<!-- VERIFY: execute 3.1 in the target account and reconcile control names. Capture images/c04-03-01.jpg only from the real app. -->

## 3.2 Summarise the Columns

1. In K1:L4 enter labels Planned Total, Actual Total and Variance Total in K2:K4.
2. Enter `=SUM(G2:G13)` in L2, `=SUM(H2:H13)` in L3 and `=SUM(I2:I13)` in L4.
3. In K6:L7 add Average Planned and Numeric Cost Count, using `=AVERAGE(G2:G13)` and `=COUNT(G2:G13)`.

<details markdown="1">
<summary>What should you see?</summary>

Planned total is RM 10,400, actual total RM 6,800 and variance total -RM 3,600. There are 12 numeric planned costs.

</details>

<!-- VERIFY: execute 3.2 in the target account and reconcile control names. Capture images/c04-03-02.jpg only from the real app. -->

## 3.3 Anchor an Assumption

1. On Navigation Practice, type `Practice multiplier` in K9 and 1.1 in L9. This is a hypothetical calculation, not a tax rate.
2. In J2 enter `=G2*$L$9` and fill through J13.
3. Inspect a later formula. Change L9 to 1.2, observe the results and restore 1.1.

<details markdown="1">
<summary>What should you see?</summary>

The multiplier reference remains $L$9 while each row's G reference moves.

</details>

<!-- VERIFY: execute 3.3 in the target account and reconcile control names. Capture images/c04-03-03.jpg only from the real app. -->

## 3.4 Test Calculations With Zeros, Blanks and Reference Errors

1. Create a **Calculation Tests** tab with Planned, Actual and Variance in A:C. Enter the four pairs on the card, leaving the designated blank empty.

2. Calculate Actual minus Planned for each complete numeric pair. Record separately why a blank Actual requires interpretation rather than automatically meaning confirmed zero expenditure.

3. Compare a real numeric zero with a blank and with text. Use COUNT and SUM in clearly labelled test cells to inspect numeric participation.

4. Create one deliberately wrong same-row calculation on the practice tab. Predict its result, inspect the formula bar and repair the reference.

5. Rebuild the practice multiplier calculation with both a relative and an absolute multiplier reference in two columns. Fill each down and compare the second and final rows.

6. Change the multiplier once, record the effect and restore it. Keep this hypothetical exercise separate from tax, policy or approved rates.

7. Reconcile SUM of row variances with total actual minus total planned in Tasks. If they differ, locate a specific row or range error rather than adjusting the total manually.

<details markdown="1">
<summary>What should you see?</summary>

Four-case calculation test with a documented blank-information limitation. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 3.4 and independent challenge; capture images/c04-03-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Create an independent three-row estimate table with at least one zero actual cost and one positive variance. Calculate and explain the results without copying a finished answer column.

2. Shorten one total range on the practice table, then use a second calculation to detect and repair the omission.

3. Write a short explanation of negative variance, numeric zero, blank information and a fixed reference, each supported by an actual test cell.

## Evidence to Hand Over

- Four-case calculation test with a documented blank-information limitation.
- Reference-error and omitted-range diagnosis with repaired formulas.
- Reconciled baseline totals and independent estimate table.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A plausible total hides a copied-row error | Inspect row references and compare sum of variances against the difference of totals. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

You calculated and reconciled the register using visible source values and references.

**Check yourself:** Which part of a copied formula should move, and which should stay fixed?
