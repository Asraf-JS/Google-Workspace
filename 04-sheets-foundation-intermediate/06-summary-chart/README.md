# 06 - Summarise and Visualise

The sponsor doesn't want to read twelve rows. Aina needs two answers on one screen: how many tasks are in each status, and how the planned budget splits across the teams, with a chart for each. And she needs to trust them, so you'll check that the summary adds up to the register and see how a chart can mislead without a single formula being wrong.

**Estimated time:** 55 minutes, planned as 5 explanation, 35 guided build and 15 independent practice. Not yet timed with learners.

**Your result:** in `GW - Sheets - Task Register`, a **Summary** tab with status counts, team planned costs, two labelled charts, reconciliation checks and two findings, plus a **Chart Range Tests** copy and a **Summary Test Log**.

> **You'll practise:** COUNTIF and SUMIF with fixed and relative references, inserting and editing column charts, checking a summary against its source, and (if your account has it) asking Gemini to explain a formula.

---

## What You Will Learn

- Count and total by category with COUNTIF and SUMIF
- Build a clear, labelled chart from the right range
- Check that a summary and its chart still match the register

## Before You Begin

Open `GW - Sheets - Task Register` from **GW - Sheets Foundation - Practice**. You need **Tasks** with all twelve records and the supplied **Summary** tab, which has the three status names in **A2:A4** and an empty **TaskCount** column.

**What you build in this lab:**

**Summary**: status counts > team planned costs > status chart > cost chart > checks > findings | **Chart Range Tests** | **Summary Test Log**

## Topics

**COUNTIF and SUMIF.** `=COUNTIF(range, criterion)` counts the cells in a range that match. `=SUMIF(range, criterion, sum_range)` adds up the matching rows' values from another column. The range stays fixed with `$`; the criterion, such as **A2**, moves as you fill down.

**A chart is only as honest as its range.** Include the **Total** row and the chart shows a fourth bar of 12, as if there were 24 tasks. Misspell a category and its bar drops to zero. The chart looks fine either way, so you check the numbers behind it.

**Two ways to the same number.** If the summary's total matches a total taken straight from **Tasks**, the summary hasn't lost or double-counted anything.

---

## 6.1 Count the Statuses

1. Click the **Summary** tab. Click **B2**, type `=COUNTIF(Tasks!$F$2:$F$13,A2)` and press **Enter**. It shows **4**.

![B2 on Summary showing 4 from the COUNTIF formula](./images/c04-06-01-first-countif.png)

*The status range is fixed with $; A2 tells it which status to count.*

2. Click the name box, type `B2:B4`, press **Enter**, then press **Ctrl+D**.
3. Click **A5** and type `Total`. Click **B5**, type `=SUM(B2:B4)` and press **Enter**.

![Summary with 4, 4, 4 and a total of 12 in A1:B5](./images/c04-06-02-status-total.png)

*Four tasks in each status, twelve in total.*

**Check:** **B2:B4** show **4**, **4**, **4** and **B5** shows **12**. Click **B3**: its formula ends in **A3**.

---

## 6.2 Total the Planned Cost by Team

1. Click **D1** (it says **Fictional training data**) and press **Ctrl+X**. Click **G1** and press **Ctrl+V**. That frees up columns **D** and **E**.
2. Copy the block below, click **D1** and press **Ctrl+V**.

```text
Team	Planned cost (RM)
Planning
Procurement
Site Coordination
```

3. Click **E2**, type `=SUMIF(Tasks!$B$2:$B$13,D2,Tasks!$G$2:$G$13)` and press **Enter**. It shows **2800**.

![E2 showing 2800 from the SUMIF formula](./images/c04-06-03-first-sumif.png)

*It finds Planning in the Team column and adds those rows' planned costs.*

4. Click the name box, type `E2:E4`, press **Enter**, then press **Ctrl+D**. Double-click the right edges of the **D** and **E** headings so everything fits.

![Summary with both summaries: status counts and team planned costs](./images/c04-06-04-two-summaries.png)

*2,800 + 4,000 + 3,600 = 10,400, the same as the planned total on Tasks.*

**Check:** **E2:E4** show **2800**, **4000** and **3600**. These are planned amounts, not money spent.

---

## 6.3 Chart the Status Counts

1. Click the name box, type `A1:B4` and press **Enter**. Leave out row 5: the total isn't a status.
2. Click **Insert**, then **Chart**. In the **Chart editor**, on the **Setup** tab, set **Chart type** to **Column chart**. Sheets may suggest a pie chart first. Check **Data range** says **A1:B4**.

![The Chart editor Setup tab with Column chart and A1:B4](./images/c04-06-05-column-chart-setup.png)

*Use row 1 as headers and column A as labels are both ticked.*

3. Click the **Customise** tab, open **Chart and axis titles** and set the **Chart title** text to `Task count by status`.

![The Customise tab with the chart title set to Task count by status](./images/c04-06-06-status-title.png)

*A title that says what's being counted.*

4. Close the editor. Drag the chart by its blank top area so it sits below the summaries without covering any cells.

![The status chart below the summaries, with three bars of 4](./images/c04-06-07-linked-status-chart.png)

*Three categories, each at 4. No Total bar.*

**Check:** the chart is titled **Task count by status** and has exactly three bars, each at **4**.

---

## 6.4 Ask Gemini to Explain a Formula

If your account doesn't have Gemini, skip to step 3 and explain the formula to a partner instead.

1. Click **Ask Gemini** (the star at the top right). Copy the prompt below, paste it into the box and press **Enter**.

Session: the **Ask Gemini** panel in this workbook. Grounding: this formula only.

```text
Explain this formula in the panel only: =COUNTIF(Tasks!$F$2:$F$13,A2). Explain the anchored range and the relative criterion cell, including what changes when filled to B3. Use only this formula and this fictional workbook. Do not edit cells, create charts, or apply changes.
```

![The Gemini panel with the formula prompt typed](./images/c04-06-08-formula-prompt.png)

*The prompt asks for an explanation only, not changes.*

2. Read the reply. Don't click **Insert** or anything else that changes the sheet.

![Gemini's reply, showing the B3 formula and explaining the fixed range and moving criterion](./images/c04-06-09-anchored-relative-explanation.png)

*Gemini's wording will differ from the screenshot.*

3. Click **B3** and compare the formula bar with the explanation: `=COUNTIF(Tasks!$F$2:$F$13,A3)`. The range is the same; the criterion moved from **A2** to **A3**. Close the panel.

**Check:** you can say which part of the formula stayed fixed when you filled down, and which part moved, using **B3** to prove it.

---

## 6.5 Watch a Change Flow Through

You change one status on **Tasks** for a moment, to see the summary and chart follow it, then put it back.

1. Click the **Tasks** tab. Find **T003**: its status in **F4** is **Not Started**.

![T003 on Tasks with Not Started in F4](./images/c04-06-10-original-t003-status.png)

*Note the original value before you change it.*

2. Use the dropdown in **F4** to choose **Complete**.

![F4 changed to Complete](./images/c04-06-11-temporary-complete.png)

*Only T003 changes.*

3. Click the **Summary** tab. The counts are now **5**, **4**, **3**, still **12** in total, and the chart's bars have changed.

![Summary with 5, 4 and 3, and the chart showing the new heights](./images/c04-06-12-status-change-chart.png)

*The summary and chart follow the register by themselves.*

4. Go back to **Tasks** and set **F4** to **Not Started** again.

![F4 back to Not Started](./images/c04-06-13-status-restored-source.png)

*T003 is back as it was.*

5. Click the **Summary** tab: **4**, **4**, **4**, and three equal bars.

![Summary back to 4, 4, 4 with three equal bars](./images/c04-06-14-status-baseline-restored.png)

*Check both the numbers and the chart.*

**Check:** **Tasks** **F4** says **Not Started**, and the summary is back to **4**, **4**, **4**.

---

## 6.6 Chart the Costs and Reconcile

1. On **Summary**, click the name box, type `D1:E4` and press **Enter**. Click **Insert**, **Chart**, and set **Chart type** to **Column chart**. Check **Data range** says **D1:E4**.

![The Chart editor with Column chart and D1:E4](./images/c04-06-15-cost-chart-source.png)

*A separate chart for money; counts and ringgit don't share an axis.*

2. On **Customise**, set the chart title to `Planned cost by team (RM)`. Close the editor and drag the chart beside the status chart.

![The cost chart titled Planned cost by team (RM)](./images/c04-06-16-cost-units-title.png)

*The title names the unit.*

3. Copy the block below, click **G2** and press **Ctrl+V**.

```text
Summary Checks	Summary	Source	Difference
Task count
Planned cost (RM)
```

4. Type these formulas, pressing **Enter** after each:
   - **H3**: `=B5`
   - **I3**: `=COUNTA(Tasks!A2:A13)`
   - **J3**: `=H3-I3`
   - **H4**: `=SUM(E2:E4)`
   - **I4**: `=SUM(Tasks!G2:G13)`
   - **J4**: `=H4-I4`

![Summary Checks in G2:J4, with 12 against 12 and 10400 against RM10,400, both differences 0](./images/c04-06-17-reconciliation-checks.png)

*Both differences are zero, so the summary hasn't lost or double-counted anything.*

**Check:** **J3** and **J4** both show **0**.

---

## 6.7 Break the Chart on a Copy

Now see two ways a chart can mislead, on a copy you can throw away.

1. Click the arrow on the **Summary** tab and choose **Duplicate**. Rename the copy `Chart Range Tests`.

![The Chart Range Tests tab, a copy of Summary](./images/c04-06-18-named-chart-copy.png)

*The copy's formulas still read from Tasks.*

2. On **Chart Range Tests**, click the status chart, click the three dots at its top right and choose **Edit chart**. Click the grid icon in **Data range**, change it to `A1:B5` and click **OK**. The chart gains a fourth bar, **Total**, at **12**.

![The status chart on the copy with a fourth bar for Total at 12](./images/c04-06-19-total-row-fault.png)

*Now the bars add up to 24, as if there were twice as many tasks.*

3. Change the data range back to `A1:B4` the same way. Three bars again.

![The status chart repaired to A1:B4](./images/c04-06-20-chart-range-repaired.png)

*Fix the range itself. Hiding the label or renaming the bar wouldn't fix the numbers.*

4. Close the editor. Click **A4** and type `Not Startd` (a typo). **B4** drops to **0**, **B5** to **8** and **J3** shows **-4**.

![Not Startd in A4, B4 at 0, B5 at 8 and J3 at -4](./images/c04-06-21-misspelt-category-fault.png)

*The four tasks are still on Tasks; the label just doesn't match them any more. The reconciliation catches it.*

5. Correct **A4** to `Not Started`. **B4** returns to **4**, **B5** to **12** and **J3** to **0**.

![A4 corrected, with B4 back at 4 and J3 at 0](./images/c04-06-22-category-repaired.png)

*Fix the label, not the number: never type 4 over the formula.*

**Check:** on **Chart Range Tests**, the chart has three bars, **A4** says **Not Started** and **J3** shows **0**.

---

## 6.8 Write Findings and Test a Cost Change

1. Click the **Summary** tab. In **A7** and **A8**, write two findings, one sentence each, that the summary supports. Start each with `Finding:`.

![Two findings in A7 and A8 on Summary](./images/c04-06-23-supported-findings.png)

*Say only what the numbers show.*

2. Click the **Tasks** tab and click **G4**: T003's planned cost is **RM500**, and its variance in **I4** is **-RM500**.

![G4 on Tasks holding 500, with I4 at -RM500](./images/c04-06-24-original-planned-cost.png)

*Note the original value first.*

3. Type `600` in **G4** and press **Enter**. **I4** becomes **-RM600**.

![G4 changed to 600 and I4 at -RM600](./images/c04-06-25-temporary-cost-source.png)

*The variance formula updated by itself.*

4. Click the **Summary** tab. Planning is now **2900**, both planned totals are **10500** and **J4** is still **0**. The Planning bar is a little taller.

![Summary with Planning at 2900, planned totals 10500 and J4 at 0](./images/c04-06-26-cost-propagation.png)

*The findings in A7:A8 don't update themselves, so they're now out of date. That's why you put the value back.*

5. Go back to **Tasks**, type `500` in **G4** and press **Enter**. **I4** is **-RM500** again.

![G4 back at 500](./images/c04-06-27-planned-cost-restored.png)

*T003 is as it was.*

6. Click the **Summary** tab and check everything is back: **4**, **4**, **4**; **2800**, **4000**, **3600**; **10400**; both differences **0**.

![Summary restored, with both charts and zero differences](./images/c04-06-28-two-charts-restored.png)

*The charts and findings agree with the register again.*

<details markdown="1">
<summary>What should you see?</summary>

Findings along these lines:

- `Finding: 4 tasks in each status; 12 tasks in total.`
- `Finding: Procurement has the largest planned total: RM4,000 of RM10,400.`

Neither says anything about whether tasks are on time or money was saved: the summary doesn't show that.

</details>

---

## 6.9 Log the Tests

1. Click **+** (Add sheet). Rename the new tab `Summary Test Log`.
2. Copy the block below, click **A1** and press **Ctrl+V**. Check each line against what you saw.

```text
Check	Target / change	Expected and observed	Restored final state
Status change	Tasks F4: Not Started to Complete	Summary B2:B4 and chart: 5 / 4 / 3; total 12	F4 Not Started; counts 4 / 4 / 4
Chart range fault	Chart Range Tests status chart A1:B5	Fourth category Total = 12; double-count risk	Range A1:B4; three categories
Spelling fault	Chart Range Tests A4: Not Startd	B4 zero, B5 8, J3 -4; zero-height category	A4 Not Started; formula B4 4; total 12
Cost change	Tasks G4: 500 to 600	I4 -600; Planning 2900; source and summary 10500	G4 500; I4 -500; Planning 2800; totals 10400
Formula check	Summary B3 COUNTIF	Fixed Tasks F2:F13; relative A3; result 4	Panel-only explanation; no Insert applied
Reconciliation	Summary H3:J4 versus Tasks	Task count 12 versus 12; planned 10400 versus 10400	Both differences zero
Scope	Lab 06 guided sections	All temporary changes were reversed	Baseline source values restored
```

3. Select columns **A** to **D**, turn on **Format**, **Wrapping**, **Wrap**, and widen the columns until each line is readable.

![Summary Test Log with seven checks in A1:D8](./images/c04-06-29-test-log.png)

*The screenshot's Scope row is worded differently from yours.*

**Check:** **Summary Test Log** has seven rows, and every test in it was put back.

---

## Independent Practice

Try these without looking back at the steps.

1. **A one-screen dashboard.** Add a tab called `Dashboard`. Copy both charts from **Summary** onto it (click a chart, **Ctrl+C**, then **Ctrl+V** on **Dashboard**), and add your two findings underneath with the cells they come from.
2. **Find the fault.** Ask a partner to break one thing on your **Chart Range Tests** without telling you: a chart range, a status name or a team name. Use the checks in **G2:J4** and the charts to find what they changed, then fix the cause, not just the look.
3. **Review.** Swap with a partner and check each other's **Summary**: are the units right on both charts, do the bars add up to twelve tasks, and do the differences show zero? Record one thing you corrected, or why nothing needed changing.

<details markdown="1">
<summary>What should you see?</summary>

A misspelt team name, such as `Procuremnt` in **D3**, makes **E3** show **0**, and **J4** shows **-4000**. A chart range that includes row 5 adds a **Total** bar. A misspelt status shows up in **J3**. In each case the fix is the label or the range, never a typed number.

</details>

### Evidence to Hand Over

- **Summary** with status counts, team planned costs, two titled charts, zero differences in **J3:J4** and two findings
- **Chart Range Tests** repaired after both faults
- **Summary Test Log** with seven checks
- Your **Dashboard**, and the fault your partner set and how you found it

## Troubleshooting

| Problem | What to try |
|---|---|
| The chart has a Total bar | Edit the chart and set **Data range** to `A1:B4`. |
| A count is 0 but the tasks exist | The label doesn't match exactly. Check spelling and spaces in the **A** or **D** cell. |
| Filling down changed the range | Add `$` signs to the range part, such as `Tasks!$F$2:$F$13`, and fill again. |
| Sheets made a pie chart | Open **Edit chart** and change **Chart type** to **Column chart**. |
| Typing the range in the chart editor didn't change the chart | Use the grid icon next to **Data range**, change it there and click **OK**. |
| Gemini offered to insert a formula | Don't. Close the panel; you only wanted an explanation. |

## Lesson Summary

You counted statuses with COUNTIF and totalled costs by team with SUMIF, charted both with clear titles, and proved the summary matches the register. You watched a change on **Tasks** flow through to the summary and chart, and saw a wrong range and a misspelt label mislead without any formula being wrong. In Lab 07 you prepare the summary for sharing and printing.

**Check yourself:** why should the Total row normally be left out of this chart?
