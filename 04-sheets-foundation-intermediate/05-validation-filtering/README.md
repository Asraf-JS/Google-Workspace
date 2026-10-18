# 05 - Validate and Filter the Register

In this chapter you will add a status dropdown, identify invalid entries and create a filter view.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 50 minutes: 10 explanation/demonstration, 20 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 40 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A status dropdown and two named filter views.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Restrict status values.
- Create and name a filter view.
- Check hidden rows before interpreting totals.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use the original Tasks table, with all 12 baseline records still present.

## 5.1 Add a Status Dropdown

1. Select F2:F13. Open Data, Data validation and add a dropdown rule.
2. Use Complete, In Progress and Not Started as the three values. Set the rule to reject invalid data where that option is available.
3. Inspect one existing cell and confirm that its current status is retained.

<details markdown="1">
<summary>What should you see?</summary>

The original values remain valid and future entries use the same vocabulary.

</details>

<!-- VERIFY: execute 5.1 in the target account and reconcile control names. Capture images/c04-05-01.jpg only from the real app. -->

## 5.2 Create a Filter View

1. Select A1:I13 and open the filter-view option under Data. Create a new filter view.
2. Name it `Incomplete tasks` and use the Status filter to exclude Complete.
3. Count visible task IDs, then close the filter view and confirm that all 12 return.

<details markdown="1">
<summary>What should you see?</summary>

Eight tasks are visible in the incomplete view. Closing it restores the full dataset.

</details>

<!-- VERIFY: execute 5.2 in the target account and reconcile control names. Capture images/c04-05-02.jpg only from the real app. -->

## 5.3 Test a Rule Safely

1. Copy the validation rule to a spare test cell outside the register and try `Done`.
2. Check whether the rule rejects it or shows a warning, and discuss the difference.
3. Clear the spare test cell. Open your named filter view again to confirm it remains available.

<details markdown="1">
<summary>What should you see?</summary>

You know the rule's actual behaviour and have not changed the baseline statuses.

</details>

<!-- VERIFY: execute 5.3 in the target account and reconcile control names. Capture images/c04-05-03.jpg only from the real app. -->

## 5.4 Design and Verify Entry Rules and Focused Views

1. Create a **Rule Tests** tab with test value, expected accept/reject, observed result and repair columns. Plan tests before changing the rules.

2. Test the three canonical statuses and invalid **Done** using spare validated cells. Record rejection versus warning behaviour.

3. On an Entry Practice copy add DueWeek validation for whole practice weeks 1 through 4. Inspect the available custom-formula or number rule and test 0, 1, 4, 5 and 1.5.

4. Decide how blanks should be handled for a partially entered record. Test actual behaviour and document it; do not claim validation guarantees every required field is filled.

5. Create a second named filter view for Planning tasks not Complete. Count visible TaskIDs and compare them with a manual source scan.

6. Open and close each named view, confirming that all source rows return. Compare an ordinary SUM before and during filtering and record whether hidden rows still contribute.

7. Write a short entry guide explaining canonical statuses, relative weeks, the invalid-input message and what to do with an unclear category.

<details markdown="1">
<summary>What should you see?</summary>

Expected-versus-observed rule matrix including week boundaries and blanks. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 5.4 and independent challenge; capture images/c04-05-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Independently build a small entry test with one valid row, one invalid status and one out-of-range week. Demonstrate the rules rather than merely listing them.

2. Create a named view answering “Which Procurement tasks are not complete?” and list its TaskIDs as evidence.

3. Check whether each new practice row lies inside the rule and view ranges. Repair a missing bound on the practice copy and retest.

## Evidence to Hand Over

- Expected-versus-observed rule matrix including week boundaries and blanks.
- Two useful named views with independently checked visible records.
- Entry guide and a repaired coverage/range test.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A new row accepts invalid values | Inspect rule coverage as well as the dropdown definition; retest the actual new row. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Validation prevents inconsistent entries and filter views support focused inspection.

**Check yourself:** Does hiding a row delete it or remove it from an ordinary SUM?
