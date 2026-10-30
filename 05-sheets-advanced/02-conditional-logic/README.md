# 02 - Build Conditional Calculations

In this chapter you will revise mixed references and apply IF, SUMIF, COUNTIF, SUMIFS and COUNTIFS with test cases.


**Target allocation:** 75 minutes: 15 explanation/demonstration, 32 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 60 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** Checked line amounts, a project/status summary grid and tested logic bands.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Build row calculations.
- Apply conditional totals with mixed references.
- Test a nested rule at its boundaries.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use Orders A1:I25 and the Analysis tab from Chapter 1.

## 2.1 Calculate Line Amounts

1. In Orders J1 type `Amount`; in J2 enter `=E2*F2` and fill through J25.

**Copy: Typed Values**

```text
Amount
```

2. In K1 type `ActiveAmount`; in K2 enter `=IF(G2="Cancelled",0,J2)` and fill through K25.

**Copy: Typed Values**

```text
=E2*F2
```


**Copy: Typed Values**

```text
ActiveAmount
```


**Copy: Typed Values**

```text
=IF(G2="Cancelled",0,J2)
```

3. Compare J2, J13 and J25 with quantity times unit cost. Cancelled rows remain in the dataset but contribute zero to ActiveAmount.

<details markdown="1">
<summary>What should you see?</summary>

The all-orders Amount sum is RM 3,158. ActiveAmount answers a different question from all-orders Amount.

</details>

<!-- VERIFY: execute 2.1 in the target account and reconcile control names. Capture images/c05-02-01.jpg only from the real app. -->

## 2.2 Create a Summary Grid

1. On Analysis enter Project in A3 and Delivered, Pending, Cancelled in B3:D3. Put PJ-A, PJ-B and PJ-C in A4:A6.
2. In B4 enter `=SUMIFS(Orders!$J$2:$J$25,Orders!$B$2:$B$25,$A4,Orders!$G$2:$G$25,B$3)`.

**Copy: Typed Values**

```text
=SUMIFS(Orders!$J$2:$J$25,Orders!$B$2:$B$25,$A4,Orders!$G$2:$G$25,B$3)
```

3. Fill across through D4, then down through row 6. Inspect a formula in the final row and column.

<details markdown="1">
<summary>What should you see?</summary>

Project criteria move down while status headers move across. The grid sums back to 3,158 across all statuses.

</details>

<!-- VERIFY: execute 2.2 in the target account and reconcile control names. Capture images/c05-02-02.jpg only from the real app. -->

## 2.3 Test Logic Boundaries

1. In a spare practice area label the bands Low below 100, Medium from 100 to below 200, and High from 200 upward.
2. With a test amount in F2, enter `=IF(F2<100,"Low",IF(F2<200,"Medium","High"))` in G2.

**Copy: Typed Values**

```text
=IF(F2<100,"Low",IF(F2<200,"Medium","High"))
```

3. Test 99, 100, 199 and 200 in F2 and record the classifications. Keep these hypothetical bands separate from source policy.

<details markdown="1">
<summary>What should you see?</summary>

99 is Low; 100 and 199 are Medium; 200 is High. The bands do not overlap.

</details>

<!-- VERIFY: execute 2.3 in the target account and reconcile control names. Capture images/c05-02-03.jpg only from the real app. -->

## 2.4 Reconcile Three Populations and Test Conditional Boundaries

1. Create an Analysis control block for all-orders Amount, ActiveAmount excluding Cancelled, and Delivered-only Amount. Write each population definition before calculating.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Logic matrix must cover below/on/above thresholds, zero quantity, Delivered, Pending and Cancelled. Practice bands: Low <100; Medium 100 to <200; High >=200. Exception: Pending AND Amount >=200. These are training rules, not procurement policy.
```


2. Build COUNTIFS as well as SUMIFS project/status grids. Reconcile the count grid to 24 and the amount grid to the all-orders source total.

3. For two grid intersections list qualifying OrderIDs and manually multiply their quantity and unit cost. Compare this independent subset with the formulas.

4. Create a separate **Logic Tests** table with amount, status, expected band and expected pending-high flag. Include 0, 99, 100, 199 and 200 and each status.

5. Apply the nested-IF band formula and the pending/amount condition to the test table. Compare expected and actual outcomes and investigate any mismatch.

6. On a grid copy remove one mixed-reference anchor and fill across/down. Locate the first incorrect criterion by inspecting the formula, then restore the anchor.

7. Record why a valid zero amount differs from an unknown item rate and why active, delivered and all-orders totals answer different questions.

<details markdown="1">
<summary>What should you see?</summary>

Reconciled count/amount grids for clearly defined populations. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 2.4 and independent challenge; capture images/c05-02-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Build a second summary answering count and amount for Pending orders of at least 200 by project. Keep threshold logic explicit.

2. Use a filtered source list as an independent reconciliation. A zero-match baseline is a valid result; create a separate synthetic qualifying case and a non-qualifying boundary case to test the rule.

3. Change the threshold to 250 in a labelled assumption cell, repair references so the grid follows it, then restore 200 and verify restoration.

## Evidence to Hand Over

- Reconciled count/amount grids for clearly defined populations.
- Expected-versus-actual boundary matrix and repaired mixed-reference defect.
- Independent threshold summary with supporting OrderIDs and a restored assumption.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Correct totals conceal the wrong population | Reconcile counts and contributing IDs as well as the monetary total. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Visible row calculations and explicit criteria make advanced logic checkable.

**Check yourself:** Which references in the summary grid must stay fixed when copied across and down?


## Zero-Match Check

The supplied baseline has no Pending record with Amount at least 200. Record that result explicitly. Use a separately labelled synthetic case to prove the positive branch; do not edit baseline records just to obtain a highlight.
