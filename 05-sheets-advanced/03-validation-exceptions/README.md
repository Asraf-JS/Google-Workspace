# 03 - Validate Entries and Flag Exceptions

In this chapter you will use dropdowns, custom validation and formula-based conditional formatting.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 65 minutes: 15 explanation/demonstration, 22 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 50 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** Validation rules and a tested pending-order exception highlight.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Validate categorical and numeric inputs.
- Highlight exceptions using a rule.
- Test an invalid and boundary value.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use a practice copy of Orders. Restore all temporary tests before completing the chapter.

## 3.1 Validate New Entries

1. Select G2:G25 and add a dropdown for Delivered, Pending and Cancelled.
2. Add a validation rule to E2:E25 requiring a whole number at least 0. A zero quantity is permitted for this training dataset.
3. Inspect whether invalid values are rejected or warned about.

<details markdown="1">
<summary>What should you see?</summary>

The rules reflect the stated training choices and do not silently invent a positive-only restriction.

</details>

<!-- VERIFY: execute 3.1 in the target account and reconcile control names. Capture images/c05-03-01.jpg only from the real app. -->

## 3.2 Flag Pending High Amounts

1. Select A2:K25 and open Format, Conditional formatting.
2. Use a custom formula `=AND($G2="Pending",$J2>=200)` and a readable light fill.
3. Check the rule starts at source row 2 and applies across the intended rows.

<details markdown="1">
<summary>What should you see?</summary>

Only pending rows with Amount at least 200 are highlighted; delivered or cancelled rows do not qualify.

</details>

<!-- VERIFY: execute 3.2 in the target account and reconcile control names. Capture images/c05-03-02.jpg only from the real app. -->

## 3.3 Test the Rules

1. On one practice row, try an invalid status and a fractional quantity, then undo.
2. Test a pending row at amount 199 and 200 by temporarily changing its numeric inputs.
3. Restore the source values and inspect that the highlighting recalculates.

<details markdown="1">
<summary>What should you see?</summary>

You have tested both rejection behaviour and the conditional-format threshold.

</details>

<!-- VERIFY: execute 3.3 in the target account and reconcile control names. Capture images/c05-03-03.jpg only from the real app. -->

## 3.4 Create a Rule Test Harness and Reconcile Exceptions

1. Create **Validation Tests** with expected result and observed result before trying each input. Include whole zero, positive integer, negative, fractional and text quantities.

2. For whole nonnegative Quantity, inspect a custom rule such as `=AND(ISNUMBER(E2),E2>=0,MOD(E2,1)=0)` on a practice range. Decide and document how a blank should be handled separately.

3. Test rejection behaviour for each quantity and status case. Do not equate a coloured cell with an enforced validation rule.

4. Build an explicit exception flag column on a practice Orders copy using the same Pending/Amount logic as the conditional format.

5. Filter the flag and compare its qualifying OrderIDs with the highlighted rows. Check both the first and final source row for rule coverage.

6. On test records compare Pending at 199, 200 and 201, plus Delivered at 200 and Cancelled at 200. Explain which logical condition excludes each non-qualifying row.

7. Restore all temporary values and record the exact data-validation and conditional-format ranges used.

<details markdown="1">
<summary>What should you see?</summary>

Eight-case input validation matrix and five-case exception matrix. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 3.4 and independent challenge; capture images/c05-03-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Append a synthetic pending record only to the test copy and diagnose whether input validation, flag formulas and conditional formatting extend to it.

2. Repair coverage and produce a test report containing at least eight input cases and five exception cases.

3. State whether blanks and pasted values were actually tested and list any behaviour still requiring confirmation in the customer account.

## Evidence to Hand Over

- Eight-case input validation matrix and five-case exception matrix.
- Agreement between explicit flags, highlighted rows and filtered IDs.
- New-row coverage repair and restored source values.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| The colour rule flags the wrong row | Check the apply-to start row and the relative row in the custom formula. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Data rules constrain entry; conditional formatting draws attention to defined exceptions.

**Check yourself:** How does a validation rule differ from a coloured warning?


## Zero-Match Check

The supplied baseline has no Pending record with Amount at least 200. Record that result explicitly. Use a separately labelled synthetic case to prove the positive branch; do not edit baseline records just to obtain a highlight.
