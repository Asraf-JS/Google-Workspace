# 04 - Clean and Organise Records

In this chapter you will find and replace, trim text, sort whole records and freeze the header row.


**Target allocation:** 50 minutes: 10 explanation/demonstration, 20 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 40 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A cleaned text example, whole-record sort and named cost range.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Clean text without altering source evidence.
- Sort whole records.
- Keep headers visible while scrolling.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use Tasks and download [DirtyText.csv](../../shared/sample-files/DirtyText.csv). Keep cleaning practice separate from the original register.

## 4.1 Clean a Small Import

1. Import DirtyText.csv into a new spreadsheet or separate practice tab. Check its three column headings.
2. In D1 type `CleanTeam`; in D2 enter `=TRIM(B2)` and fill to D4.

**Copy: Typed Values**

```text
CleanTeam
```


**Copy: Typed Values**

```text
=TRIM(B2)
```

3. Compare B and D. Correct the lowercase status complete to the canonical Complete in a separate cleaned status column.

<details markdown="1">
<summary>What should you see?</summary>

The trailing/leading spaces are removed in the cleaned output while original text remains inspectable.

</details>

<!-- VERIFY: execute 4.1 in the target account and reconcile control names. Capture images/c04-04-01.jpg only from the real app. -->

## 4.2 Sort Whole Records

1. Return to Tasks and select A1:I13, including the variance column if you created it.
2. Use Data, Sort range, Advanced range sorting options. Mark that the range has a header row and sort by Team, then TaskID.
3. Locate T001 after sorting and check its owner, costs and variance still belong to that same record.

<details markdown="1">
<summary>What should you see?</summary>

The task row stays intact. Sorting one column in isolation would break the record relationships.

</details>

<!-- VERIFY: execute 4.2 in the target account and reconcile control names. Capture images/c04-04-02.jpg only from the real app. -->

## 4.3 Freeze and Name a Range

1. Use View, Freeze and freeze one row. Scroll down and verify the header stays visible.
2. Select G2:G13 and use the named-range control to name it `PlannedCosts`.

**Copy: Typed Values**

```text
PlannedCosts
```

3. In a spare labelled cell enter `=SUM(PlannedCosts)` and compare it with the earlier planned total.

**Copy: Typed Values**

```text
=SUM(PlannedCosts)
```


<details markdown="1">
<summary>What should you see?</summary>

The named range sums to 10,400 and the frozen header remains visible.

</details>

<!-- VERIFY: execute 4.3 in the target account and reconcile control names. Capture images/c04-04-03.jpg only from the real app. -->

## 4.4 Clean an Intake and Prove That Records Stay Together

1. Import or type the five-row cleaning intake provided below into a new **Cleaning Intake** tab. Preserve a raw copy before editing.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Cleaning intake (TaskID | Team | Status): C001 |  Planning  | complete; C002 | Procurement | In Progress; C003 | Site Coordination | Blocked; C002 | Procurement | In Progress; C004 | Planning | Not Started. C001 has surrounding team spaces. The duplicate is identical; Blocked remains unresolved. These are separate practice records.
```


2. Create CleanTeam, CleanStatus and Disposition columns. Use TRIM where appropriate, standardise obvious case differences and flag ambiguous statuses for clarification.

3. Identify the duplicate TaskID and compare its other fields before deciding whether it is a repeated identical record or a conflicting update. Do not delete a row solely because the name appears twice.

4. Use **Find and replace** restricted to the cleaned-status column for a known spelling repair. Preview the target scope and keep the raw source unchanged.

5. Sort the complete intake range by Team and TaskID. Before and after sorting compare three TaskID-to-owner or status relationships against the raw copy.

6. On a disposable copy, sort just one data column to demonstrate how relationships can break. Undo immediately and prove restoration with those three checks.

7. Create a named range for the cleaned numeric test costs if supplied, or use the existing PlannedCosts range. Inspect its exact bounds and compare its SUM with an explicit-range SUM.

<details markdown="1">
<summary>What should you see?</summary>

Preserved raw intake, justified clean values and explicit exceptions. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 4.4 and independent challenge; capture images/c04-04-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Produce a clean intake and an exception list independently. Keep unresolved category and conflicting-duplicate decisions visible.

2. Add one new numeric row only to a named-range practice copy and inspect whether the named range includes it. Repair its bounds and compare the two total methods.

3. Hand over the raw copy, clean result and three row-identity checks so another person can verify the cleaning without trusting your description.

## Evidence to Hand Over

- Preserved raw intake, justified clean values and explicit exceptions.
- Whole-record sorting evidence and a restored isolated-column demonstration.
- Named-range boundary test and independently reconciled total.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A clean-looking row is associated with the wrong task | Compare complete TaskID relationships before and after the sort, not only totals. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Cleaning, whole-record sorts and visible headers make the data safer to analyse.

**Check yourself:** What must stay together when sorting a register?
