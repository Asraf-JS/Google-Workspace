# 06 - Complete the Formula Clinic

In this chapter you will debug supplied defects, explain the correction and reconcile a checked sample.


**Target allocation:** 65 minutes: 15 explanation/demonstration, 22 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 50 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** Three repaired defects with independent baseline reconciliations.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Diagnose formula defects.
- Test zero and missing values.
- Reconcile source totals independently.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use a challenge copy of your advanced workbook. Keep the baseline original untouched.

## 6.1 Create Three Test Defects

1. On the challenge copy, remove FALSE from a copied VLOOKUP, shift one multiplication reference to the next row, and shorten one SUM range by a row.
2. Record the intended formula behaviour before fixing anything.
3. Inspect the formula bar, not just the visible result, for each defect.

<details markdown="1">
<summary>What should you see?</summary>

You have three clearly identified test defects; a plausible number is not assumed correct.

</details>

<!-- VERIFY: execute 6.1 in the target account and reconcile control names. Capture images/c05-06-01.jpg only from the real app. -->

## 6.2 Repair and Test

1. Restore exact matching and the correct same-row multiplication. Extend the total to every source row.
2. Test a temporary zero quantity and check that its amount becomes a valid zero. Restore the quantity.
3. Test an unknown item code in a separate practice cell and confirm it remains an explicit missing match.

<details markdown="1">
<summary>What should you see?</summary>

The repair handles ordinary rows, valid zero and a missing key distinctly.

</details>

<!-- VERIFY: execute 6.2 in the target account and reconcile control names. Capture images/c05-06-02.jpg only from the real app. -->

## 6.3 Reconcile and Explain

1. Sum line amounts from all 24 rows and reconcile to 3,158. Filter Delivered rows and reconcile their amount to 1,478.
2. Compare the conditional summary with a manually inspected subset.
3. Write one sentence per defect explaining the cause and why your test detects it.

<details markdown="1">
<summary>What should you see?</summary>

The baseline is restored and both independent control totals agree.

</details>

<!-- VERIFY: execute 6.3 in the target account and reconcile control names. Capture images/c05-06-03.jpg only from the real app. -->

## 6.4 Run an Independent Formula Fault Clinic

1. Create a defect register for wrong match mode, shifted row reference and omitted total row. Include expected behaviour, observed symptom, hypothesis and proof.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Extra fault choices, clinic copy only: change a numeric quantity to text “four”; insert a duplicate lookup key; replace a blank/missing-rate outcome with 0; shorten one delivered summary range by two rows. Diagnose the cause before restoring from Source Snapshot.
```


2. Preserve faulty and repaired formulas side by side on the clinic copy so a reviewer can see the specific change.

3. Use a small manually calculated subset to distinguish a logic error from a display-format difference. Do not repair by typing the desired result.

4. Add the duplicate-key and numeric-text cases from the card as separate tests. Decide whether each problem belongs in source cleaning, lookup validation or formula logic.

5. For every repair, test one normal input and one boundary/exception input. Record actual results and any unresolved issue.

6. Reconcile baseline all-orders and Delivered totals after restoration, plus a record-count control. Keep cancelled rows in the source.

7. Write a brief troubleshooting decision path: inspect source → define population → inspect references → test boundary → reconcile result.

<details markdown="1">
<summary>What should you see?</summary>

Defect register with preserved faulty/repaired formulas and test evidence. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 6.4 and independent challenge; capture images/c05-06-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Ask a partner to introduce a defect on a separate clinic copy without telling you its cell; if alone, use the card and hide your defect note before diagnosis.

2. Locate it through controls, isolate the cause, repair it and run a regression check on a previously correct population.

3. Present the evidence trail in two minutes, including why your chosen control would catch the defect on a future refresh.

## Evidence to Hand Over

- Defect register with preserved faulty/repaired formulas and test evidence.
- Normal/boundary checks for every repair and restored baseline controls.
- Independent diagnosis, regression check and an explainable troubleshooting path.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| The total is corrected but the defect remains | Require a formula/source repair and a new input test rather than a hard-coded total. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

A useful formula check tests meaning and boundaries rather than merely the absence of an error message.

**Check yourself:** Which of your checks would catch a missing final row?
