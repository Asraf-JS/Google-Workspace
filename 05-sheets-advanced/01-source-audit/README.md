# 01 - Audit the Source Register

In this chapter you will check types, blanks, duplicates and keys before analysis.


**Target allocation:** 45 minutes: 10 explanation/demonstration, 15 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 35 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** An audited source, preserved snapshot and empty Analysis workspace.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Inspect dataset grain and keys.
- Check types and baseline controls.
- Preserve the source before analysis.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Download [ProcurementRegister.xlsx](../../shared/sample-files/ProcurementRegister.xlsx). It contains 24 fictional order lines and a six-item rate table, separate from the pilot budget.

## 1.1 Prepare the Workbook

1. Upload the workbook and save a native Google Sheets copy named `GW - Sheets Advanced - Analysis`.

**Copy: Typed Values**

```text
GW - Sheets Advanced - Analysis
```

2. Open Orders. Confirm headers in A1:I1 and records PO001 to PO024 in rows 2:25.
3. Open Rates and confirm six unique item codes in A2:A7.

<details markdown="1">
<summary>What should you see?</summary>

Each Orders row is one fictional order line, not a project subtotal or a real purchase commitment.

</details>

<!-- VERIFY: execute 1.1 in the target account and reconcile control names. Capture images/c05-01-01.jpg only from the real app. -->

## 1.2 Audit Key Fields

1. Check OrderID values for blanks and duplicates. Use a temporary COUNTIF diagnostic if needed.
2. Inspect Quantity and UnitCost: they must be numeric. Week is a practice index, not a date.
3. Compare the status vocabulary Delivered, Pending and Cancelled. Keep cancelled records visible for analysis.

<details markdown="1">
<summary>What should you see?</summary>

The baseline has 24 unique order IDs and the expected categories.

</details>

<!-- VERIFY: execute 1.2 in the target account and reconcile control names. Capture images/c05-01-02.jpg only from the real app. -->

## 1.3 Protect the Analysis Trail

1. Duplicate Orders as `Source Snapshot` before adding calculations.

**Copy: Typed Values**

```text
Source Snapshot
```

2. Create a new tab called `Analysis` for summaries.

**Copy: Typed Values**

```text
Analysis
```

3. Record the source range and meaning of an order line in a note outside the working table.

<details markdown="1">
<summary>What should you see?</summary>

The original supplied values can be compared with later analysis without guessing what changed.

</details>

<!-- VERIFY: execute 1.3 in the target account and reconcile control names. Capture images/c05-01-03.jpg only from the real app. -->

## 1.4 Quarantine Bad Rows and Write a Data Contract

1. Create **Audit Intake** and preserve the six anomaly records from the copy-paste card separately from Orders. Add Issue, Evidence and Disposition columns.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Separate intake anomalies: duplicate PO001 with changed quantity; missing OrderID; ItemCode IT99; Quantity “four”; valid zero quantity; valid Cancelled status. Do not inject these into Orders. Other fields can be copied from a source row only in Audit Intake and labelled as practice.
```


2. Define one row’s grain, OrderID uniqueness, valid ItemCode mapping, allowed status vocabulary and numeric Quantity/UnitCost requirements in a **Data Contract** section.

3. Use COUNTIF to inspect duplicate IDs and an exact lookup or manual comparison for unknown item keys. Keep a repeated record distinct from a conflicting duplicate.

4. Use ISNUMBER or equivalent inspected checks to distinguish numeric 4 from text “four”. Document whether zero is valid for the stated training rule.

5. Compare cancelled and pending records with the contract. A cancelled row is not automatically corrupt or removable from an all-orders population.

6. Create an exception register with a proposed next action for each anomaly: clarify, correct with evidence, retain as valid or quarantine pending evidence.

7. Recheck the original 24 unique IDs and six Rates keys after the audit. Keep intake anomalies out of baseline controls.

<details markdown="1">
<summary>What should you see?</summary>

Data contract and six-row anomaly audit with preserved raw values. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 1.4 and independent challenge; capture images/c05-01-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Independently decide whether each anomaly should enter the analysis, remain pending or be retained as a valid case. Justify every decision against the contract.

2. Write a release condition for the source: what must be true before conditional calculations and lookups can be trusted?

3. Have a reviewer challenge one disposition and resolve it using source evidence or an explicit unresolved label.

## Evidence to Hand Over

- Data contract and six-row anomaly audit with preserved raw values.
- Baseline uniqueness/type/key checks and a justified quarantine policy.
- Independent release conditions and a recorded challenged decision.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A cancelled row is removed as dirty data | Separate data validity from the inclusion rule of the analysis question. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

An analysis begins with data meaning, types and source coverage.

**Check yourself:** What does one row represent, and which field identifies it?
