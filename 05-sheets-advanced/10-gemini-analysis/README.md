# 10 - Use Gemini as an Analysis Partner

In this chapter you will generate and inspect formula proposals and chart summaries; test exceptions before accepting.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 55 minutes: 10 explanation/demonstration, 25 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 45 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A checked AI formula proposal and evidence-based findings.

> **Status:** author reference with 41 staged application captures through 10.4. Gemini formula proposals and findings were checked; its generated-chart direct-link claim was disproved by a source-change test. Boundary, copied-reference, missing-key and isolated new-row cases are verified. Independent PO025 pivot/chart coverage, reviewer and learner timing remain pending.

## What You Will Learn

- Ask AI for a bounded formula proposal.
- Verify a generated finding.
- Distinguish a source-linked result from a generated snapshot.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use the native checked workbook and usable Gemini in Sheets access. If unavailable, critique the supplied examples manually and record the AI objective as incomplete.

## 10.1 Request a Formula Proposal

1. Open **Ask Gemini** in the checked workbook. Confirm that its prompt box is available. If access is unavailable, use the supplied manual critique route and record the AI objective as incomplete.

![gemini available](./images/c05-10-01-gemini-available.jpg)

2. Use **File > Make a copy** to create **GW - Sheets Advanced - AI Audit** in the practice folder. Leave sharing and comment-copy options unchecked. Use this copy for the remaining tests; keep the maintained workbook intact.

![isolated ai audit copy](./images/c05-10-02-isolated-ai-audit-copy.jpg)

3. In a new Gemini conversation, paste the Part 2 prompt. Review the actual entered text before Submit: Orders rows **2:25**, Status **G**, Amount **J**, exact status **Delivered**, bounded ranges, formula/explanation only and **no cell edits**.

![bounded formula prompt](./images/c05-10-03-bounded-formula-prompt.jpg)

4. Read the response before using Insert. In this run Gemini proposed **=SUMIF(Orders!G2:G25,"Delivered",Orders!J2:J25)** and displayed **1,478**. Inspect the formula's actual bounds, sum field and criterion; its explanation alone is insufficient.

![gemini sumif proposal](./images/c05-10-04-gemini-sumif-proposal.jpg)

5. Create **AI Proposals**, with column A at 250 pixels and B:D at 210. Enter the proposal in **B2**, compare with **='Database Analysis'!D10** in C2 and calculate B2-C2 in D2. Add a Delivered record-count check in row 3. Actual/control values are **1,478 /1,478** and **12 /12**, with both differences 0. Row 4 uses a formula to report whether both controls match.

![proposal tested against controls](./images/c05-10-05-proposal-tested-against-controls.jpg)

## 10.2 Check an Interpretation

1. Open Dashboard and start a new Gemini conversation. Use the supplied findings prompt, grounding it in **Dashboard A5:D8** and **F5:G8**. Request two descriptive findings with populations, RM units and cell references; exclude web research, cell edits, causes, forecasts and invented benefit percentages.

![two findings grounding prompt](./images/c05-10-06-two-findings-grounding-prompt.jpg)

2. Allow the response to finish rendering before judging it. The following image records an early, partial render, not a completed answer or a demonstrated AI error. Do not accept a heading or confident opening sentence as evidence that all findings are present.

![gemini incomplete findings response](./images/c05-10-07-gemini-incomplete-findings-response.jpg)

3. Check the first finding against the source: **24 records =12 Delivered +6 Pending +6 Cancelled**; all-orders Amount is **3,158**, Delivered-only Amount **1,478**, and Pending Amount **460**. Confirm the cited summary cells, rather than copying prose without verification.

![first finding populations and totals](./images/c05-10-08-first-finding-populations-and-totals.jpg)

4. A follow-up can request a concise Delivered-only project comparison. The captured stage below shows that request while its response is rendering. The completed response, checked against A6:A8/C6:C8, ranks **PJ-B578**, **PJ-A556**, then **PJ-C344**. These are descriptive amounts, not evidence of efficiency or future performance.

![follow-up comparison request while response renders](./images/c05-10-09-delivered-project-finding.jpg)

5. Create **AI Findings**, with A260/B1040 pixels and wrapping enabled. Write two findings in your own words, their supporting cell addresses and the claims that the source cannot establish. Keep the all-orders and Delivered populations distinct. Do not use the AI response as a substitute for source cells.

![findings traced to cells](./images/c05-10-10-findings-traced-to-cells.jpg)

## 10.3 Inspect Generated Visuals

1. From Dashboard, start a new Gemini conversation and request a **column chart** using only **Dashboard A5:B8**, including Cancelled orders. Ask for a preview, an explicit data-source statement and no changes to existing cells or the existing dashboard chart. The reference title is **Generated project amount - incl. Cancelled (RM)**.

![generated chart request](./images/c05-10-11-generated-chart-request.jpg)

2. Inspect the chart card and proposed category values **980 /1,204 /974** before insertion. A correct preview does not demonstrate a live connection.

![generated chart preview and claim](./images/c05-10-12-generated-chart-preview-and-claim.jpg)

3. Choose **Preview**. In this actual response Gemini claimed that the chart followed Dashboard A5:B8 directly and used no separate generated data. Treat that as a claim to test. Close the preview before deciding where to retain the result.

![preview before insertion](./images/c05-10-13-preview-before-insertion.jpg)

4. Create a separate **AI Visual Test** tab, reopen Gemini and select the chart card's **Insert**. In this run, Insert created its own new **[Chart 1] Generated project amount - incl. Cancelled (RM)** tab, regardless of the selected blank destination. The app reported that source data was at the bottom of the new sheet. Its generated table is **A3:B6**.

![generated chart created new source tab](./images/c05-10-14-generated-chart-created-new-source-tab.jpg)

5. Double-click the inserted chart and inspect **Chart editor > Setup**. Its actual data range is **A3:B6 on the generated tab**, not Dashboard A5:B8. Inspect generated **B4:B6**: they contain the numbers 980/1204/974 rather than formulas linking to Dashboard. This is already evidence against the direct-link claim, but perform the change test as well.

![actual generated chart range](./images/c05-10-15-actual-generated-chart-range.jpg)

6. In AI Visual Test A1:B8, record the AI claim, observed table/range and predictions before editing. Changing this copy's **Orders E2 from 2 to 3**, at UnitCost 45, should produce line Amount 135, live PJ-A1025 and total 3203. Predict that the generated number table and its chart will remain at 980/1204/974.

![visual refresh predictions](./images/c05-10-16-visual-refresh-predictions.jpg)

7. Change **Orders E2 to 3** in the AI Audit copy. Inspect the PO001 line Amount **135**. Do not alter the maintained workbook.

![source quantity three](./images/c05-10-17-source-quantity-three.jpg)

8. Inspect the checked **Dashboard**: PJ-A all Amount becomes **1,025**, Week 1 becomes 773 and total Amount becomes **3,203**. The source-linked chart updates.

![linked dashboard refreshes](./images/c05-10-18-linked-dashboard-refreshes.jpg)

9. Return to the generated tab. **B4 remains 980** and its chart retains the original values. The observed change test contradicts Gemini's direct-refresh statement. Preserve this transient evidence before restoration.

![generated snapshot stays stale](./images/c05-10-19-generated-snapshot-stays-stale.jpg)

10. Restore the AI Audit copy's **Orders E2 to 2**, returning PO001 Amount to 90.

![source restored](./images/c05-10-20-source-restored.jpg)

11. Check Dashboard returns to **24 records /3,158 all Amount /1,938 ActiveAmount /1,478 Delivered**, with all four difference checks 0.

![live dashboard restored](./images/c05-10-21-live-dashboard-restored.jpg)

12. Rename the generated tab **AI Generated Snapshot** and label its static nature visibly beside the table. Retain the generated result as a teaching snapshot; use the checked live Dashboard for refreshed analysis. Regenerate and recheck a snapshot after source changes.

![snapshot labelled after test](./images/c05-10-22-snapshot-labelled-after-test.jpg)

13. Complete AI Visual Test A10:B11 with the observed live 1025 versus static 980 result and source restoration. Record the actual source range and refresh behaviour, rather than relying on the original AI description.

![visual refresh audit result](./images/c05-10-23-visual-refresh-audit-result.jpg)

## 10.4 Evaluate AI Proposals Against Known Test Cases

1. Create **AI Test Matrix** before the next formula request. Record expected outcomes: Delivered 1478/12; Pending Amount>=200 gives 0 amount/0 records; missing IT99 is not a confirmed zero rate; rows 2:24 total 3094 rather than 3158; ActiveAmount 1938 differs from Delivered 1478. Plan separate threshold, copied-reference and new-row fixtures. The copy-paste page supplies the full matrix.

![prewritten proposal test matrix](./images/c05-10-24-prewritten-proposal-test-matrix.jpg)

2. Ask Gemini for SUMIFS and COUNTIFS using actual Orders Status G and Amount J, exact **Pending**, **>=200** and absolute source bounds **$2:$25**. Request formulas/explanation only and no edits. Review the entered prompt before Submit.

![pending threshold formula prompt](./images/c05-10-25-pending-threshold-formula-prompt.jpg)

3. Inspect the proposed **SUMIFS** and corresponding COUNTIFS. The captured SUMIFS card is visible while the COUNTIFS card continues below it; both complete formulas are provided on the copy-paste page. Check the actual comparison operator and anchors before testing.

```text
=SUMIFS(Orders!$J$2:$J$25,Orders!$G$2:$G$25,"Pending",Orders!$J$2:$J$25,">=200")
```

![gemini fixed threshold formulas](./images/c05-10-26-gemini-fixed-threshold-formulas.jpg)

4. In AI Proposals rows 7:11, execute both proposals and compare with the prewritten expectations. Both threshold results are 0. Separate controls confirm all Pending Amount 460 and maximum Pending Amount 180. A zero threshold result does not, by itself, establish that source coverage is complete.

![threshold proposals tested on source](./images/c05-10-27-threshold-proposals-tested-on-source.jpg)

5. Trace the six Pending records in AI Proposals A14:D21 by linking the actual source cells. IDs are **PO002 /PO006 /PO010 /PO014 /PO018 /PO022**, with amounts **48 /16 /180 /96 /48 /72**. They sum to 460; none meets >=200. This checks the actual contributing population.

![six pending records manually traced](./images/c05-10-28-six-pending-records-manually-traced.jpg)

6. Create **AI Boundary Cases**. Enter four explicitly fictional fixtures: Pending 199.99, Pending 200, Pending 200.01 and Delivered 250. Predict TRUE only for the two Pending amounts at/above200 before adding result formulas.

![isolated boundary inputs](./images/c05-10-29-isolated-boundary-inputs.jpg)

7. Compare the two rules in rows 8:10. Correct **>=200** gives **2 records /400.01 amount**; incorrect **>200** gives **1 /200.01**. The Delivered 250 line is excluded by the status condition. Actual-minus-expected differences for the correct rule are 0.

![exact threshold versus greater than](./images/c05-10-30-exact-threshold-versus-greater-than.jpg)

8. Set up the copied-reference test at A15:E18. Put statuses **Delivered /Delivered /Pending** in A16:A18. Enter anchored and unanchored SUMIF formulas only in B16/C16. Leave the lower actual cells blank initially; their temporary differences are not completed test results.

![formula copy before fill](./images/c05-10-31-formula-copy-before-fill.jpg)

9. Select **B16:C18** and use **Fill down (Ctrl+D)**. Anchored results remain **1478 /1478 /460**. Unanchored results become **1478 /1388 /412** because the source ranges move. Select C17 and inspect the formula bar: G3:G26/J3:J26 has dropped PO001. Repeating Delivered isolates the source-range drift; the Pending row also loses PO002 after the second shift.

![copied reference drift exposed](./images/c05-10-32-copied-reference-drift-exposed.jpg)

10. Create **AI Repairs** and retain the three deliberately flawed examples from the case card. Label them **supplied examples, not Gemini outputs**. Keep original formula text beside executed results: the truncated total returns **3094**, the IT99 error wrapper returns **0**, and the Delivered formula mislabelled Active returns **1478**. Each fails its stated claim.

![supplied flaws executed and rejected](./images/c05-10-33-supplied-flaws-executed-and-rejected.jpg)

11. Add manual repairs below the originals. Full bounded SUM returns **3158**; exact **IFNA(VLOOKUP(...,FALSE),"Missing rate")** preserves the missing IT99 mapping; Active excluding only Cancelled returns **1938**. Known IT01 returns 45, while ISNA on the missing IT99 lookup is TRUE. A missing mapping is not evidence of a numeric zero. Keep the original and repaired formulas together for comparison.

![original and corrected formulas](./images/c05-10-34-original-and-corrected-formulas.jpg)

12. Duplicate **Orders** within the AI Audit workbook and rename that tab **AI Row Test**. Inspect the duplicated baseline before adding any new record. This fixture is separate from maintained Orders and from the independent PO025 challenge.

![isolated orders copy before extension](./images/c05-10-35-isolated-orders-copy-before-extension.jpg)

13. Create **AI Row Checks** before inserting the test row. Use original bounds **2:25** for all Amount, Delivered Amount and record count. Baseline values are **3158 /1478 /24**, with matching expected values and zero differences. Select B2 to inspect its exact original range.

![coverage controls before new row](./images/c05-10-36-coverage-controls-before-new-row.jpg)

14. On AI Row Test select row 26 and **Insert 1 row above**, preserving the totals below it. Enter **TEST025 /PJ-A /Planning /IT01 /2 /45 /Delivered /4 /Author range-coverage fixture**, then line Amount **=E26*F26** and ActiveAmount **=IF(G26="Cancelled",0,J26)**. The new line contributes90. This is authorised guided casework, not the independent PO025 attempt.

![new record outside original bounds](./images/c05-10-37-new-record-outside-original-bounds.jpg)

15. Return to AI Row Checks. The original formulas still end at 25 and return 3158/1478/24, omitting the new row. The old difference cells still show 0 because their expected values are also the old baseline. Matching a stale expected value is not proof of current population coverage.

![original bounds omit new record](./images/c05-10-38-original-bounds-omit-new-record.jpg)

16. Add the expanded **2:26** comparisons at A7:F10. Expected current values are **3248 /1568 /25**. Original bounds are short by **90 /90 /1**, while all expanded differences are 0. Independent controls verify old 3158+new90=3248,25 unique IDs, TEST025 at row 26 and maintained Orders still 3158. Retain the isolated fixture; this does not test new-row pivot/chart coverage.

![expanded range repairs coverage](./images/c05-10-39-expanded-range-repairs-coverage.jpg)

17. Complete AI Test Matrix A12:B21 with pass/fail decisions, corrections, copied-reference evidence, the stale-control warning, the generated snapshot's actual refresh behaviour and validation limits. Keep correct Gemini proposals distinct from the deliberately flawed supplied examples.

![proposal audit handover](./images/c05-10-40-proposal-audit-handover.jpg)

18. Finish with the two source-grounded findings in AI Findings. Native bounded checks confirm the AI Audit copy's maintained Orders/Analysis/Rates/Source Snapshot, earlier pivot definitions and Dashboard are restored to their pre-test state. The isolated TEST025 fixture remains separate. Do not infer causes, forecasts or ROI from the checked amounts.

![final source grounded findings](./images/c05-10-41-final-source-grounded-findings.jpg)

> **Validation boundary:** guided 10.1-10.3 and author casework 10.4 were executed through learner UI, with native read-only evidence. Gemini's formula proposals passed these cases, but its generated-chart direct-link claim was disproved by the actual source-change test. Independent PO025 coverage across pivots/charts, human reviewer and the planned 55-minute learner allocation remain unverified.


## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Design an independent prompt that includes the population, fields, intended output and tests, then run or manually review its result.

2. Challenge it with IT99 and PO025 in separate test contexts. Keep missing mapping distinct from zero and inspect new-row coverage.

3. Produce a short audit comparing original proposal, correction, evidence and remaining limitation.

## Evidence to Hand Over

- Prewritten test matrix and observed proposal results.
- Original/corrected formula trace with independent verification.
- Generated-chart source check or stated unavailable route, and supported final findings.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| The AI explanation sounds right while the formula differs | Audit the actual formula and contributing rows, not its prose description. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

AI can propose analysis; source tests establish whether it is suitable.

**Check yourself:** What evidence would establish that a generated chart follows the maintained source?
