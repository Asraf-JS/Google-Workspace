# 11 - Complete the Analysis Capstone

In this chapter you will answer a new project question, substantiate the finding and deliver a checked dashboard.


**Target allocation:** 80 minutes: 15 explanation/demonstration, 37 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 65 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A source-traceable capstone analysis and checked presentation.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Answer a new analysis question.
- Reconcile a result independently.
- Communicate assumptions and limitations.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Create a challenge copy. Use the same 24-order source and six-item Rates table; do not import real purchasing data.

## 11.1 Define and Calculate

1. Answer: which project has the largest Delivered amount, and which Pending records have Amount at least 200?
2. Write the population and criteria before choosing formulas or a pivot.
3. Calculate the result and retain a visible trace to qualifying order IDs.

<details markdown="1">
<summary>What should you see?</summary>

The ranking and exception list are based on explicit delivered/pending definitions.

</details>

<!-- VERIFY: execute 11.1 in the target account and reconcile control names. Capture images/c05-11-01.jpg only from the real app. -->

## 11.2 Challenge the Result

1. Reconcile the delivered total to 1,478 and all-orders total to 3,158.
2. If no baseline pending row qualifies, record zero matches explicitly. Inspect a non-qualifying baseline row and use a separate synthetic row to test the positive boundary without altering the baseline.
3. Test a duplicate or missing lookup key on a disposable copy and explain its effect without changing the baseline workbook.

<details markdown="1">
<summary>What should you see?</summary>

Your result survives an independent check and identifies meaningful data assumptions.

</details>

<!-- VERIFY: execute 11.2 in the target account and reconcile control names. Capture images/c05-11-02.jpg only from the real app. -->

## 11.3 Present the Analysis

1. Show one clear chart or table with project names and currency units.
2. State the source population, result and one limitation. Do not equate order amount with profit or budget approval.
3. Explain which sources and calculations must update for a future record.

<details markdown="1">
<summary>What should you see?</summary>

A reviewer can trace the finding to source records and understand its limits.

</details>

<!-- VERIFY: execute 11.3 in the target account and reconcile control names. Capture images/c05-11-03.jpg only from the real app. -->

## 11.4 Complete a Decision Analysis With Independent Evidence

1. Write a one-page analysis specification for the card’s three questions, naming population, metric, threshold and exclusions.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Capstone questions: Largest Delivered amount by project; Pending records with Amount >=200 and their IDs; highest all-orders Amount by practice week. Scenario PO025: PJ-A, Planning, IT01, Quantity 2, UnitCost 45, Delivered, week 4. No actual budget or profit data is supplied.
```


2. Build answers with formulas and a pivot or filtered-source reconciliation. Retain the contributing OrderIDs for the exception list.

3. Compare project Delivered amounts and identify the largest using checked numbers. Do not infer profitability or project performance from order amount alone.

4. For Pending Amount >=200, first report the actual baseline match count, including zero if none qualify. Inspect a non-qualifying baseline row and use a separate synthetic positive/boundary test. Keep synthetic tests outside the baseline analysis.

5. Run a separate PO025 scenario and describe its effect on ranking, delivered totals and week 4. Do not overwrite the baseline result.

6. Prepare an executive table/chart and an audit appendix showing source range, assumptions, controls and unresolved data issues.

7. Ask a reviewer to challenge one answer and prove it from the source rows and a second calculation method.

<details markdown="1">
<summary>What should you see?</summary>

Three-question specification and independently reconciled results. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 11.4 and independent challenge; capture images/c05-11-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Independently compare all-orders and active populations and explain how excluding Cancelled changes the question and results.

2. Stress-test an unknown rate key and a duplicate lookup key in a scenario copy. Demonstrate the warning/disposition rather than forcing a numeric answer.

3. Deliver a three-minute recommendation limited to what the data supports, plus one next question requiring additional evidence.

## Evidence to Hand Over

- Three-question specification and independently reconciled results.
- Separate added-row and key-quality scenarios with audit evidence.
- Executive output, reviewer challenge response and a bounded recommendation.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A recommendation claims savings or profitability | Return to dataset meaning and request missing cost/outcome evidence before making that claim. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

The capstone combines reliable data, explicit calculations and a defensible explanation.

**Check yourself:** Would the same result follow if Cancelled records were included?


## Zero-Match Check

The supplied baseline has no Pending record with Amount at least 200. Record that result explicitly. Use a separately labelled synthetic case to prove the positive branch; do not edit baseline records just to obtain a highlight.
