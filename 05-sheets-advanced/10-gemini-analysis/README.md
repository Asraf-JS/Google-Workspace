# 10 - Use Gemini as an Analysis Partner

In this chapter you will generate and inspect formula proposals and chart summaries; test exceptions before accepting.


**Target allocation:** 55 minutes: 10 explanation/demonstration, 25 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 45 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A checked AI formula proposal and evidence-based findings.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Ask AI for a bounded formula proposal.
- Verify a generated finding.
- Distinguish a source-linked result from a generated snapshot.

## Before You Begin

Read the case input beside the relevant steps. Use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Use the native checked workbook and usable Gemini in Sheets access. If unavailable, critique the supplied examples manually and record the AI objective as incomplete.

## 10.1 Request a Formula Proposal

1. Open Ask Gemini. Paste the following prompt describing the actual source columns and range.

**Copy: Propose a Delivered Total**

**Session:** new chat | **Grounding:** explicit Orders schema

```text
Goal: Propose a formula for delivered order amount.
Context: Fictional Google Sheets analysis.
Source: Orders rows 2 to 25; Status is G and Amount is J. Header row is 1.
Expectations: Reply with a formula and explanation only. Do not edit cells. Include only Status equal to Delivered. Use bounded ranges. I will test the formula against the source.
```

Replace bracketed source placeholders before submitting. Keep a human check between an AI proposal and the final output.

2. Read the proposed formula before applying it. Check its row bounds, exact status spelling and use of Amount.
3. Test the formula in a spare labelled cell and compare with the known Delivered total of 1,478.

<details markdown="1">
<summary>What should you see?</summary>

The proposal is accepted only after it matches the actual schema and control total.

</details>

<!-- VERIFY: execute 10.1 in the target account and reconcile control names. Capture images/c05-10-01.jpg only from the real app. -->

## 10.2 Check an Interpretation

1. Ask for two findings using the checked project/status summary, without web research.
2. For each finding, identify the cells that support it. Reject unsupported causal claims, forecasts or benefit percentages.
3. Write a final finding in your own words with its population and units.

<details markdown="1">
<summary>What should you see?</summary>

Each retained finding is traceable to values rather than AI confidence.

</details>

<!-- VERIFY: execute 10.2 in the target account and reconcile control names. Capture images/c05-10-02.jpg only from the real app. -->

## 10.3 Inspect Generated Visuals

1. If asking Gemini to generate a chart, inspect where its data was written and what range the chart references.
2. Temporarily change a source quantity and observe whether that generated analysis follows the original source.
3. Restore the quantity. Label a static/generated analysis snapshot appropriately or use your already checked source-linked chart.

<details markdown="1">
<summary>What should you see?</summary>

The final dashboard does not imply automatic refresh where it has not been demonstrated.

</details>

<!-- VERIFY: execute 10.3 in the target account and reconcile control names. Capture images/c05-10-03.jpg only from the real app. -->

## 10.4 Evaluate AI Proposals Against Known Test Cases

1. Prepare a test matrix before prompting: Delivered total, Pending >=200, unknown ItemCode and a new record outside the original bounds.

**Case input to analyse**

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Flawed formula proposals to audit if AI is unavailable: `=SUM(Orders!J2:J24)` described as all 24 rows; `=IFERROR(VLOOKUP("IT99",Rates!A2:D7,3,FALSE),0)` described as a confirmed zero rate; `=SUMIFS(Orders!J2:J25,Orders!G2:G25,"Delivered")` described as active amount excluding only Cancelled.
```


2. Ask Gemini for a formula and explanation using the actual headers and range. If unavailable, use the deliberately flawed proposals on the card for the same audit.

3. Inspect every proposed formula’s population, field, match mode, bounds and copied-reference behaviour before using it.

4. Run the proposal in labelled spare cells against known controls and a manually verified subset. Record pass/fail and the cause of each failure.

5. Request a correction for one identified defect, or repair it manually. Keep the original proposal alongside the checked replacement so improvement is demonstrable.

6. For any generated chart inspect its data source and test a source-cell change. Record whether it follows the maintained data, separate generated cells or a static snapshot.

7. Write a final two-finding commentary grounded in checked values, rejecting causal claims, forecasts and unsupported ROI.

<details markdown="1">
<summary>What should you see?</summary>

Prewritten test matrix and observed proposal results. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 10.4 and independent challenge; capture images/c05-10-04.jpg only after real application success. -->

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
