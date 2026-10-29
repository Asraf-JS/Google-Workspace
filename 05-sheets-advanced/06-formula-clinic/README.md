# 06 - Complete the Formula Clinic

In this chapter you will debug supplied defects, explain the correction and reconcile a checked sample.

> **Prompts:** the [prompts page](./prompts.md) has every value and prompt for this chapter, each with a Copy button.

**Estimated time:** 65 minutes, planned as 15 explanation and demonstration, 22 guided build and casework, 20 independent practice and 8 verification and repair, with 50 active minutes by design. Not yet timed with learners.

**Your result:** Three repaired defects with independent baseline reconciliations.

> **Status:** author reference with 31 staged application captures through 6.4. Three defects are observed and repaired in a separate workbook copy. Zero, missing, numeric-text, duplicate-key and final-row tests are verified; original source remains unchanged. Independent diagnosis, partner/reviewer and learner timing remain pending.

---

## What You Will Learn

- Diagnose formula defects.
- Test zero and missing values.
- Reconcile source totals independently.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use a challenge copy of your advanced workbook. Keep the baseline original untouched.

## 6.1 Create Three Test Defects

1. Click **File > Make a copy** of the existing Advanced workbook. Name it GW - Sheets Advanced - Formula Clinic in the practice folder. Keep sharing/comments unchecked. Verify the new workbook title and different file URL before editing.

![The Copy document dialog naming GW - Sheets Advanced - Formula Clinic, with sharing and comments unchecked](./images/c05-06-01-copy-workbook-with-private-settings.png)

*Make a private copy for the clinic. The maintained workbook stays untouched.*

![The Formula Clinic copy open, still matching the original](./images/c05-06-02-separate-clinic-workbook-before-faults.png)

*Check the title before introducing any fault.*

2. Create **Clinic Register** and paste the register card (Part 2 of the [prompts page](./prompts.md)) to record intended behaviour, fault and detecting test before mutation. Known IT01=45 is not sufficient to detect omitted match mode; missing IT99 must remain explicit. First line is 2×45=90; final order contributes 64 to 3158.

![The Clinic Register with each defect's intended behaviour, planned fault and detecting test](./images/c05-06-03-record-intended-behaviour-and-fault-predictions.png)

*Predictions are written before anything is broken.*

3. On the copy Lookup Practice N2 remove FALSE. With known IT01 it still returns 45. Temporarily test D2=IT99: the omitted mode returns 8 from the sorted mapping, an incorrect rate for an absent key. Preserve that observation, then restore D2=IT01.

![N3 showing VLOOKUP without FALSE, still returning the right rate for a known key](./images/c05-06-04-omitted-match-mode-still-looks-correct-for-known-key.png)

*Omitting the match mode can still look correct.*

![D2 set to IT99 and N2 returning 8 instead of a missing-match result](./images/c05-06-05-unknown-key-exposes-approximate-rate-8.png)

*An unknown key exposes the approximate match: it returns an unrelated rate.*

4. On copy Orders J2 use =E2*F3. The numeric 24 is plausible but wrong because the next row's cost is 12.

![J2 using =E2*F3 and showing 24 instead of 90](./images/c05-06-06-shifted-multiplication-uses-next-row-unit-cost.png)

*The shifted reference uses the next row's unit cost. The result looks plausible.*

5. Shorten copy Orders J27 to =SUM(J2:J24). With both amount and range faults present, observe 3028. Do not attribute this combined discrepancy solely to the last row.

![J27 using =SUM(J2:J24) and showing 3,028](./images/c05-06-07-shortened-total-excludes-final-order.png)

*Two faults together give 3,028. Don't blame the whole gap on one cause.*

## 6.2 Repair and Test

1. Restore exact FALSE in Lookup Practice N2; IT01 returns 45.

![N3 with FALSE restored in the VLOOKUP](./images/c05-06-08-restore-exact-match-mode-for-known-rate.png)

*Exact match mode is back.*

2. Restore Orders J2=E2*F2=90. The shortened total is now 3094, isolating the missing 64.

![The row reference repaired; J27 still shows 3,094](./images/c05-06-09-repair-row-reference-total-still-misses-64.png)

*With J2 fixed, the remaining gap is exactly PO024's 64.*

3. Restore J27=SUM(J2:J25)=3158.

![J27 restored to =SUM(J2:J25) and showing 3,158](./images/c05-06-10-restore-full-24-row-sum-to-3158.png)

*The full 24-row total is back to 3,158.*

4. Temporarily set Orders E2=0. J2/K2 become a legitimate numeric 0, all-orders total 3068. Save the observed test before restoring E2=2, J2=90 and total 3158.

![E2 set to 0 and J2 showing RM 0.00](./images/c05-06-11-zero-quantity-produces-valid-zero-amount.png)

*A numeric zero gives a valid zero amount.*

![E2 restored and J27 back at 3,158](./images/c05-06-12-restore-quantity-and-total-after-zero-test.png)

*Restore the source value straight after the test.*

5. In Clinic Checks compare known IT01 VLOOKUP result 45 and unknown IT99 IFNA result Unmapped item against prior expectations. Both checks pass. Unmapped item is not a zero price.

![Clinic Checks: known IT01 is 45 and unknown IT99 is Unmapped item](./images/c05-06-13-known-and-unknown-rates-remain-distinct.png)

*Unmapped item is not a zero price.*

## 6.3 Reconcile and Explain

1. Clinic Checks independently calculates SUM(Orders!J2:J25)=3158, SUMIF status Delivered=1478, COUNTA OrderID=24 and COUNTIF Delivered=12. Compare each to its stated population control.

![The population controls: all orders, Delivered amount and both counts, all differences 0](./images/c05-06-14-restored-all-and-delivered-controls-before-filter-check.png)

*Each control matches its stated population.*

2. On copy Orders create a bounded A1:K25 filter and select Delivered only from Status. Use outside-table N27=SUBTOTAL(109,J2:J25) and O27=SUBTOTAL(103,A2:A25). The actual filtered result is 1478 and 12 visible records. Keep helpers outside the filtered source; source SUM is not a filtered subtotal. Remove filter after the observation, leaving 3158/24 in the helper cells.

![Orders filtered to Delivered only, 12 of 24 rows displayed](./images/c05-06-15-filtered-delivered-source-records.png)

*The filter hides rows. It doesn't remove them.*

![SUBTOTAL helpers outside the table showing 1,478 and 12](./images/c05-06-16-filtered-delivered-subtotal-1478-and-count-12.png)

*SUBTOTAL counts only the visible rows.*

3. Inspect PJ-A Delivered IDs PO001/PO004/PO005/PO008 and record manual 2×45=90,8×18=144,10×25=250,6×12=72 before formula comparison.

![The four PJ-A Delivered orders with manual amounts, before any formulas](./images/c05-06-17-manual-delivered-subset-before-formula-comparison.png)

*Record the manual amounts first.*

4. Calculate each product and its difference against the manually recorded amount. All four differences 0; manual subtotal 556 matches Analysis B4 PJ-A Delivered 556. These are author-supported manual checks, not independent learner validation.

![Formula amounts matching the manual amounts, and the subset total matching Analysis at 556](./images/c05-06-18-manual-subset-and-conditional-summary-agree-at-556.png)

*Manual and formula results agree.*

5. Explain the match-mode, row-reference and range-coverage causes and their detecting tests in Clinic Register.

![The causes table in the Clinic Register](./images/c05-06-19-record-causes-and-detecting-controls.png)

*Each cause names the control that detects it.*

## 6.4 Run the Formula Fault Clinic

1. Create **Clinic Comparisons A1:E4** from the side-by-side card (Part 2 of the prompts page). Put live faulty expressions in C and repaired expressions in E; use **FORMULATEXT(C2)** and **FORMULATEXT(E2)** in B/D and fill through row 4. Wrap A1:E4. Observe **8 versus Unmapped item**, **24 versus 90**, and **3094 versus 3158**. These are isolated re-evaluations against the restored baseline; the earlier combined-fault total was 3028.

![Clinic Comparisons with each faulty and repaired expression side by side](./images/c05-06-20-side-by-side-comparisons.png)

*FORMULATEXT shows the exact expression next to its result.*

2. Before changing inputs, paste the numeric-text, duplicate-key and final-row expectations (Part 2 of the prompts page) into A7:D10. A source type error must remain visible; do not replace it with zero.

![The regression test expectations, written before the tests](./images/c05-06-21-regression-expectations.png)

*Expectations come first.*

3. On clinic-copy **Orders**, temporarily enter literal **four** in E3. J3's **=E3*F3** produces **#VALUE!**, which propagates to J27. Inspect the error before repairing its source.

![E3 holding the text "four" and J3 showing #VALUE!](./images/c05-06-22-numeric-text-error.png)

*A text quantity produces an error. Don't hide it as zero.*

4. Restore **E3=4**. J3 returns 48 and the all-orders total returns 3158. This is source cleaning, not a reason to wrap the multiplication in IFERROR(...,0).

![E3 restored to 4 and J3 back at 48](./images/c05-06-23-numeric-source-restored.png)

*Fix the source value, not the formula.*

5. Duplicate baseline **Rates** as **Clinic Duplicate Rates**. Verify the new tab has the six original keys before altering it. Keep maintained Rates unchanged.

![Clinic Duplicate Rates with the six original keys](./images/c05-06-24-duplicate-sandbox-before.png)

*Check the copy before changing it.*

6. Append **IT03 / Duplicate cable rate /99 /Equipment** at A8:D8 on that test tab only. Original IT03 remains 30.

![A duplicate IT03 row appended at row 8 of the copy](./images/c05-06-25-duplicate-key-in-sandbox.png)

*The duplicate exists only on this test tab.*

7. In **Clinic Comparisons A13:D14**, run the duplicate diagnostic card from Part 2 of the prompts page over the seven data rows. Exact VLOOKUP returns the first rate 30, COUNTIF returns 2, and the decision is **Review duplicate**. Neither 30 nor 99 becomes an approved repair. Retain the clearly named scenario tab.

![The duplicate diagnostic: first exact rate 30, key count 2, Review duplicate](./images/c05-06-26-duplicate-detected.png)

*A count above one blocks automatic acceptance.*

8. Temporarily change **Orders E25 to 0**. J25 becomes 0 and the repaired full-range total J27 changes to 3094. The shortened range would not respond to this last-row change. Inspect J27 in the formula bar; scroll down if it is below the viewport.

![E25 set to 0 and J27 showing 3,094](./images/c05-06-27-final-row-boundary.png)

*The full range responds to a change in the last row.*

9. Restore **E25=8**. J25 returns 64 and J27 returns 3158. Keep the full **=SUM(J2:J25)** formula.

![E25 restored and J27 back at 3,158](./images/c05-06-28-final-row-restored.png)

*The full SUM formula stays.*

10. Record actual observations in **A17:D23** after each experiment. Distinguish captured historical results from formulas that recalculate with the current baseline. The normal/missing lookup, normal/zero multiplication and normal/final-row total tests all have recorded outcomes.

![The regression log with expected, observed and restored states](./images/c05-06-29-regression-results.png)

*Observations are recorded after each experiment.*

11. Write the troubleshooting path in A26:B31 (labels in Part 2 of the prompts page): inspect source → define population → inspect references → test boundary → reconcile. Explain which control detects each defect and why a plausible numeric result is insufficient.

![The five-step troubleshooting path and the evidence for each step](./images/c05-06-30-troubleshooting-path.png)

*Use the same path for any formula fault.*

12. Return to **Clinic Checks**. Confirm all-orders 3158, Delivered 1478, total count 24, Delivered count 12, and manually inspected PJ-A Delivered 556. All differences are 0; known/missing checks are TRUE. Remove any active source filter and retain Cancelled records. Orders N27/O27 SUBTOTAL helpers now show 3158/24.

![Clinic Checks with every control difference at 0](./images/c05-06-31-final-reconciliation.png)

*The clinic ends with the baseline fully reconciled.*

> **Validation boundary:** guided 6.1–6.3 and author casework 6.4 were executed through learner UI with bounded native-cell evidence. Original maintained ranges are unchanged; temporary clinic inputs are restored. The copied workbook also retains earlier labelled teaching scenarios, including a raw missing-key error from Lab 5. This is not independent learner diagnosis or proof of the planned 65-minute classroom allocation. Complete the independent challenge separately.

## Independent Practice

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Ask a partner to introduce a defect on a separate clinic copy without telling you its cell; if alone, use the card and hide your defect note before diagnosis.

2. Locate it through controls, isolate the cause, repair it and run a regression check on a previously correct population.

3. Present the evidence trail in two minutes, including why your chosen control would catch the defect on a future refresh.

### Evidence to Hand Over

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
