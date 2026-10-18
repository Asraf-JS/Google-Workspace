# 05 - Match Records and Handle Errors

In this chapter you will compare exact-match VLOOKUP, HLOOKUP and INDEX/MATCH; distinguish a missing key from bad input.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 80 minutes: 15 explanation/demonstration, 37 guided build and casework, 20 independent challenge, 8 verification and repair. The active portion is 65 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** Exact-match lookup examples and an explicit missing-item result.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Use exact-match lookups.
- Compare vertical and horizontal lookup layouts.
- Distinguish missing keys from broken formulas.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use Orders and Rates. Rates A2:D7 has unique item codes and numeric unit costs.

## 5.1 Look Up a Rate

1. In a spare Orders column labelled `LookupRate`, enter `=VLOOKUP(D2,Rates!$A$2:$D$7,3,FALSE)` and fill down.
2. Compare each looked-up rate with the original F column.
3. In another labelled practice column use `=INDEX(Rates!$C$2:$C$7,MATCH(D2,Rates!$A$2:$A$7,0))` and reconcile the same result.

<details markdown="1">
<summary>What should you see?</summary>

IT01 returns 45 and IT06 returns 8. Both formulas use exact matches.

</details>

<!-- VERIFY: execute 5.1 in the target account and reconcile control names. Capture images/c05-05-01.jpg only from the real app. -->

## 5.2 Practise a Horizontal Lookup

1. On Analysis G1:L1 enter IT01 through IT06. In G2:L2 enter their unit costs 45, 12, 30, 18, 25 and 8.
2. Put IT03 in F4 and enter `=HLOOKUP(F4,$G$1:$L$2,2,FALSE)` in G4.
3. Change F4 to IT06, check 8, then restore IT03.

<details markdown="1">
<summary>What should you see?</summary>

The horizontal lookup returns 30 for IT03 and uses the same explicit matching principle.

</details>

<!-- VERIFY: execute 5.2 in the target account and reconcile control names. Capture images/c05-05-02.jpg only from the real app. -->

## 5.3 Handle an Expected Missing Key

1. In a spare test cell use item code IT99. Observe the lookup's missing-match error.
2. Wrap only the intended missing-match case, for example `=IFNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE),"Unmapped item")`.
3. Deliberately misspell a function in another spare cell, observe the different error and repair it. Discuss how a blanket IFERROR can hide defects as well as expected missing matches.

<details markdown="1">
<summary>What should you see?</summary>

An unknown item is labelled Unmapped item. A broken formula is repaired rather than treated as a zero price.

</details>

<!-- VERIFY: execute 5.3 in the target account and reconcile control names. Capture images/c05-05-03.jpg only from the real app. -->

## 5.4 Challenge Exact Lookups With Missing and Duplicate Keys

1. Create a **Lookup Tests** table containing all six known ItemCodes, IT99, a blank and a space-padded key. Preserve raw input next to any normalised key.

2. For each known key compare exact VLOOKUP with INDEX/MATCH and the supplied Rates value. Count and investigate disagreements instead of hiding them.

3. Create **Rates Duplicate Test** as a disposable Rates copy. Append a second IT03 with a different UnitCost. Observe which result a first-match lookup returns.

4. Add a key-count diagnostic so multiple matches are flagged before accepting a looked-up amount. Record that lookup success does not prove uniqueness.

5. Reorder a copied Rates table and compare exact versus omitted-match-mode VLOOKUP. Keep approximate-match experiments clearly separated from the authoritative mapping.

6. Compare a missing-key error, a bad function name and a bad range reference. Apply IFNA to the intended missing-match case and explain how broad IFERROR could conceal other defects.

7. Reconcile a known item’s lookups across vertical, horizontal and INDEX/MATCH methods and write the range/column assumptions of each.

<details markdown="1">
<summary>What should you see?</summary>

Known/missing/blank/padded-key test matrix with exact-method reconciliation. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 5.4 and independent challenge; capture images/c05-05-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Design an independent lookup output with Rate, MatchCount and Decision for the mixed intake. A zero rate, unknown key and duplicate key must remain distinguishable.

2. Move a column only on a disposable mapping copy and inspect which lookup formula needs repair. Explain why the original column-index assumption failed.

3. Hand over a rejected-key list and source-mapping check, leaving baseline Rates unchanged.

## Evidence to Hand Over

- Known/missing/blank/padded-key test matrix with exact-method reconciliation.
- Duplicate-key and column-move diagnosis on labelled copies.
- Independent lookup result that never silently turns unknown rates into zero.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| A lookup returns a plausible but wrong rate | Inspect exact-match mode, key uniqueness, whitespace and the lookup column position. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

Reliable lookups depend on clean keys, explicit match behaviour and deliberate error handling.

**Check yourself:** Does an exact-match lookup prove that a matched source value is populated?
