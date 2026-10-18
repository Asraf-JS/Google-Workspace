# 04 - Combine and Clean Text

In this chapter you will use LEFT, RIGHT, MID and concatenation; check AI categorisation against explicit rules.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 60 minutes: 15 explanation/demonstration, 17 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 45 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** Text extraction and labels with checked category mappings.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Extract parts of identifiers.
- Combine readable labels.
- Check AI categories against a visible mapping.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use Orders and Rates. The supplied IDs follow PO plus three digits; this is a training convention.

## 4.1 Extract Identifier Parts

1. On a separate Text Practice tab copy OrderID and ItemCode from a few rows.
2. Use `=LEFT(A2,2)` for the prefix and `=RIGHT(A2,3)` for the numeric text.
3. Use `=MID(A2,3,3)` to extract the same three characters and compare the results. Keep leading zeros as text.

<details markdown="1">
<summary>What should you see?</summary>

PO001 yields prefix PO and sequence text 001 rather than a newly assigned key.

</details>

<!-- VERIFY: execute 4.1 in the target account and reconcile control names. Capture images/c05-04-01.jpg only from the real app. -->

## 4.2 Combine and Clean Text

1. Copy a space-padded team name from DirtyText.csv into a spare cell and use TRIM to clean it.
2. Use CONCATENATE or & to build a label from an order ID and project code, for example `=A2&" - "&B2` on Orders.
3. Check the underlying separate fields remain available for filtering and analysis.

<details markdown="1">
<summary>What should you see?</summary>

The readable label does not replace the source columns or destroy identifier zeros.

</details>

<!-- VERIFY: execute 4.2 in the target account and reconcile control names. Capture images/c05-04-02.jpg only from the real app. -->

## 4.3 Check Categorisation

1. Read the six-item Rates table and its Category column.
2. If Gemini is available, ask it to propose categories for the item names using only Equipment, Stationery and Print and the supplied mapping.
3. Compare every proposed category with Rates. Use the mapping as the reference; record ambiguous or unmapped inputs.

<details markdown="1">
<summary>What should you see?</summary>

AI suggestions have been checked against an explicit six-item rule rather than accepted by appearance.

</details>

<!-- VERIFY: execute 4.3 in the target account and reconcile control names. Capture images/c05-04-03.jpg only from the real app. -->

## 4.4 Build a Reversible Text Normalisation Pipeline

1. Import DirtyText.csv into **Text Audit** and preserve its raw columns. Add Normalised team, Normalised status and Decision columns.

2. Apply TRIM for spaces and use explicit case handling only where it preserves the known vocabulary. Record any non-breaking or unusual spaces that the observed function does not remove.

3. Build an identifier test table from the card. Apply LEFT, RIGHT and MID, then compare extracted values with the expected identifier pattern.

4. Flag malformed or unknown keys rather than allowing a correctly extracted substring to prove a valid mapping. Retain leading zeros as text.

5. Build a display label from OrderID and Project using CONCATENATE or & while retaining the original separate key fields.

6. Use the Rates mapping to assign the six known item categories. If AI proposes categories, compare every proposal with that mapping and retain unmapped keys as explicit exceptions.

7. Write a pipeline note showing raw → normalised → validated → category/display output. Name which transformations are reversible and which require the raw source for audit.

<details markdown="1">
<summary>What should you see?</summary>

Raw/clean text audit and identifier extraction tests. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 4.4 and independent challenge; capture images/c05-04-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Independently process the mixed identifier intake into accepted keys and an exception list. Do not rely on string length alone for validity.

2. Demonstrate that IT99 is syntactically plausible but absent from the supplied mapping, and that a blank key is not a category.

3. Have a reviewer reconstruct one clean value’s origin from your raw and transformation columns. Repair any missing trace.

## Evidence to Hand Over

- Raw/clean text audit and identifier extraction tests.
- Separate syntax and mapping validation with explicit exceptions.
- Traceable category/display outputs and an independent mixed-intake result.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Text extraction succeeds on a bad identifier | Validate the complete pattern and reference mapping separately from substring extraction. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Text functions reshape fields while source keys and mappings preserve meaning.

**Check yourself:** Why should an ID suffix such as 001 remain text?
