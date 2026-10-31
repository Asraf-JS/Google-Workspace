# 04 - Clean and Organise Records

The teams send updates in all sorts of shapes: a team name with stray spaces, a status in lowercase, the same row twice. Aina wants them tidied before they reach the register, without losing what was actually sent, and she's nervous about sorting since someone once sorted one column and scrambled every task's status. In this lab you clean text with TRIM and Find and replace, sort whole records safely, freeze the heading row and name a range. Then you make the classic sorting mistake on purpose, so you'll recognise it.

**Estimated time:** 50 minutes, planned as 5 explanation, 30 guided build and 15 independent practice. Not yet timed with learners.

**Your result:** in `GW - Sheets - Task Register`, a **Dirty Text Practice** tab cleaned with TRIM, a **Sorting Practice** copy of **Tasks** with a frozen header and a named range, and a cleaned, sorted intake on **Cleaning Intake**, with its raw copy kept and a **Sort Safety Test** that shows what a one-column sort breaks.

> **You'll practise:** importing a CSV, TRIM and LEN, Find and replace within a range, sorting with a header row and two sort keys, freezing rows, named ranges and Undo.

---

## What You Will Learn

- Clean text with a formula, and keep the original next to it
- Sort whole records so every field stays with its row
- Freeze a heading row and name a range

## Before You Begin

> **Download:** [DirtyText.csv](../../shared/sample-files/DirtyText.csv) and save it on your computer. It holds three fictional records with untidy team names.

Open `GW - Sheets - Task Register` from **GW - Sheets Foundation - Practice**. You change practice tabs only. **Tasks** stays exactly as it is.

**What you build in this lab:**

**Dirty Text Practice**: raw > TRIM > lengths | **Sorting Practice**: whole-record sort > frozen header > **PlannedCosts** | **Cleaning Intake Raw** > **Cleaning Intake**: clean > fix status > sort > checks | **Sort Safety Test**

## Topics

**Keep the raw, clean beside it.** You never tidy the cells you were sent. You add a cleaned column next to them with a formula, so anyone can compare what arrived with what you made of it.

**Invisible spaces.** `" Planning "` and `"Planning"` look the same, but a sort, a filter or a COUNTIF treats them as different. `=TRIM(B2)` removes spaces at the start and end. `=LEN(B2)` counts characters, so it shows you spaces you can't see.

**A record is a whole row.** T001's owner, costs and status belong together. Sort the whole table and they move together. Sort one column on its own and the values move without their rows, so every task gets someone else's status.

---

## 4.1 Import the Messy Text

1. In `GW - Sheets - Task Register`, click **File**, then **Import**. Click **Upload**, then **Browse**, and choose `DirtyText.csv`.
2. Set **Import location** to **Insert new sheet(s)**. Leave **Separator type** on **Detect automatically**. Untick **Convert text to numbers, dates, and formulas**. Click **Import data**.
3. Double-click the new tab's name, type `Dirty Text Practice` and press **Enter**.
4. Click **B2** and look at the formula bar. There should be a space before and after **Planning**.

![Dirty Text Practice with three records, and B2 showing Planning with spaces in the formula bar](./images/c04-04-01-raw-dirty-text.png)

*The spaces are hard to see. Click in the formula bar after Planning to check the trailing one.*

If the import isn't available in your account, or the spaces are missing, type them back: click **B2**, type an apostrophe, a space, `Planning` and a space (`' Planning `), then press **Enter**. Do the same for **B4** with one space after `Site Coordination` (`'Site Coordination `). The apostrophe tells Sheets to keep the text exactly as typed; it doesn't become part of the value.

**Check:** **Dirty Text Practice** has **TaskID**, **Team** and **Status** in **A1:C4**, and **B2** has a space on each side of **Planning**.

---

## 4.2 Clean It With TRIM

1. Click **D1** and type `CleanTeam`. Click **D2**, type `=TRIM(B2)` and press **Enter**.

![D2 showing Planning from =TRIM(B2)](./images/c04-04-02-first-trim-formula.png)

*D2 shows Planning without the spaces. B2 is untouched.*

2. Click the name box, type `D2:D4`, press **Enter**, then press **Ctrl+D**.
3. Copy the block below, click **E1** and press **Ctrl+V**. It adds a clean status column and two length headings.

```text
CleanStatus	Raw length	Clean length
Complete
In Progress
Not Started
```

4. Click **F2** and type `=LEN(B2)`. Click **G2** and type `=LEN(D2)`. Click the name box, type `F2:G4`, press **Enter**, then press **Ctrl+D**.

![Dirty Text Practice with CleanTeam, CleanStatus and the raw and clean lengths in D1:G4](./images/c04-04-03-cleaned-text-length-checks.png)

*Planning drops from 10 characters to 8: two spaces removed. Procurement stays at 11.*

**Check:** **F2:F4** show **10**, **11**, **18** and **G2:G4** show **8**, **11**, **17**.

---

## 4.3 Sort Whole Records

You sort a copy of **Tasks**, so the register itself stays in its original order.

1. Click the arrow on the **Tasks** tab and choose **Duplicate**. Rename **Copy of Tasks** to `Sorting Practice`.
2. On **Sorting Practice**, click the name box, type `A1:I13` and press **Enter**. That's every column of every record, including **Variance**.

![Sorting Practice with A1:I13 selected](./images/c04-04-04-isolated-sort-range.png)

*Select every column in the table, not just the one you're sorting by.*

3. Click **Data**, **Sort range**, then **Advanced range sorting options**.
4. Tick **Data has header row**. Set **Sort by** to **Team**, **A to Z**.
5. Click **Add another sort column**. Set **then by** to **TaskID**, **A to Z**. Check the second column really says **TaskID**: Sheets sometimes picks a different one. Click **Sort**.

![The Sort range box with Data has header row ticked, Team then TaskID, both A to Z](./images/c04-04-05-team-taskid-sort-options.png)

*Team first, then TaskID within each team.*

6. Find **T001**. It still has **Aina Rahman**, **RM600**, **RM550** and **-RM50**, the same as on **Tasks**.

![T001 on Sorting Practice with all its fields intact](./images/c04-04-06-intact-sorted-record.png)

*The register was already in this order, so nothing moved. You'll see a sort that does move rows in 4.7.*

**Check:** every row on **Sorting Practice** matches the same TaskID on **Tasks**, field for field.

---

## 4.4 Freeze the Header and Name a Range

1. On **Sorting Practice**, click **View**, **Freeze**, **1 row**. The copy may already have row 1 frozen from Excel; choosing it again does no harm.

![The View > Freeze menu with 1 row highlighted](./images/c04-04-07-freeze-one-row-menu.png)

*One row is all you need: the headings.*

2. Click the name box, type `A35` and press **Enter**. The sheet scrolls down, and row 1 stays at the top.

![Sorting Practice scrolled to row 35, with the heading row still visible](./images/c04-04-08-frozen-header-scrolled.png)

*The headings stay put while the rows scroll underneath.*

3. Click the name box, type `G2:G13` and press **Enter**. Click **Data**, then **Named ranges**. Type `PlannedCosts` and click **Done**. The panel shows **'Sorting Practice'!G2:G13**.

![The Named ranges panel showing PlannedCosts as Sorting Practice!G2:G13](./images/c04-04-09-plannedcosts-exact-bounds.png)

*A name for the twelve planned costs. Close the panel when you've checked the range.*

4. Copy the block below, click **K9** and press **Ctrl+V**.

```text
Named planned total
Explicit planned total
Difference
```

5. In **L9**, type `=SUM(PlannedCosts)`. In **L10**, type `=SUM(G2:G13)`. In **L11**, type `=L9-L10`. Double-click the right edge of the column **K** heading so the labels fit.

![K9:L11 showing RM10,400, RM10,400 and RM0](./images/c04-04-10-named-explicit-totals.png)

*The name and the cell range give the same total.*

**Check:** row 1 stays visible when you scroll, and **L9:L11** show **RM10,400**, **RM10,400** and **RM0**.

---

## 4.5 Set Up the Intake

Five records have come in from the teams, with an untidy team name, a lowercase status, a duplicate and a status that isn't one of the three allowed.

1. Click **+** (Add sheet). Rename the new tab `Cleaning Intake Raw`.
2. Copy the block below, click **A1** and press **Ctrl+V**.

```text
TaskID	Team	Status
C001	Planning	complete
C002	Procurement	In Progress
C003	Site Coordination	Blocked
C002	Procurement	In Progress
C004	Planning	Not Started
```

3. C001's team arrived with spaces round it. Click **B2**, type `'  Planning  ` (an apostrophe, two spaces, Planning, two spaces) and press **Enter**.

![Cleaning Intake Raw with five records in A1:C6, and B2 showing spaces round Planning](./images/c04-04-11-preserved-intake-raw.png)

*This tab stays exactly as received from now on.*

4. Click the arrow on the **Cleaning Intake Raw** tab and choose **Duplicate**. Rename the copy `Cleaning Intake`. You work on this one.
5. On **Cleaning Intake**, click **D1** and type `CleanTeam`. In **E1** type `CleanStatus`, and in **F1** type `Disposition`.
6. Click **D2** and type `=TRIM(B2)`. Click the name box, type `D2:D6`, press **Enter**, then **Ctrl+D**.
7. Click the name box, type `C2:C6`, press **Enter** and press **Ctrl+C**. Click **E2**, then **Edit**, **Paste special**, **Values only**. The statuses are copied as they arrived, including lowercase **complete**.
8. Compare the two **C002** rows field by field, and check whether **Blocked** is one of the three allowed statuses (**Complete**, **In Progress**, **Not Started**). Then copy the block below, click **F2** and press **Ctrl+V**.

```text
Case repair pending
Identical duplicate; retain both
Clarify: not a canonical status
Identical duplicate; retain both
Retain
```

![Cleaning Intake with CleanTeam, CleanStatus and Disposition in D1:F6](./images/c04-04-12-cleaning-exceptions-before-repair.png)

*Both C002 rows are kept because they're identical. Blocked is left as it is and flagged: nobody has said what it should become.*

**Check:** **Cleaning Intake Raw** is unchanged, and **Cleaning Intake** has five rows with **CleanTeam**, **CleanStatus** and **Disposition** filled in.

---

## 4.6 Fix One Status With Find and Replace

1. On **Cleaning Intake**, click the name box, type `E2:E6` and press **Enter**.
2. Press **Ctrl+H** to open **Find and replace**. In **Find**, type `complete`. In **Replace with**, type `Complete`.
3. Check **Search** says **Specific range** and **'Cleaning Intake'!E2:E6**. Tick **Match case** and **Match entire cell contents**. Leave the other boxes unticked.

![Find and replace set to complete, Complete, Specific range, Match case and Match entire cell contents](./images/c04-04-13-replace-cleaned-status-scope.png)

*Limiting it to E2:E6 keeps the raw Status column out of it.*

4. Click **Replace all**. The box says **Replaced one instance of complete with Complete**. Click **Done**.

![Find and replace reporting one replacement](./images/c04-04-14-one-status-replaced.png)

*One replacement: only C001's clean status. C2 still says complete.*

5. Click **F2** and type `Case standardised; raw retained`.
6. Copy the block below, click **A9** and press **Ctrl+V**. It records each TaskID's status before you sort.

```text
ID check	Raw status	Clean status	Disposition
C001	complete	Complete	Case standardised
C002 (both)	In Progress	In Progress	Both identical copies retained
C003	Blocked	Blocked	Clarify; no invented mapping
```

![The before-sort check in A9:D12, below the intake](./images/c04-04-15-before-sort-identity-checks.png)

*Look at each line against the intake above it before you move on.*

**Check:** **E2** shows **Complete**, **C2** still shows **complete**, and **A9:D12** match the intake.

---

## 4.7 Sort the Intake

1. Click the name box, type `A1:F6` and press **Enter**. That's the raw columns, the clean columns and the dispositions, but not the check table below.
2. Click **Data**, **Sort range**, **Advanced range sorting options**. Tick **Data has header row**.
3. Set **Sort by** to **CleanTeam**, **A to Z**. Click **Add another sort column** and set it to **TaskID**, **A to Z**. Click **Sort**.

![The Sort range box for A1:F6, with CleanTeam then TaskID](./images/c04-04-16-intake-whole-record-sort.png)

*Sorting by CleanTeam means stray spaces can't affect the order.*

4. The order is now **C001**, **C004**, **C002**, **C002**, **C003**. Check each row still has its own status and disposition.

![Cleaning Intake sorted, with C001, C004, C002, C002, C003 in column A](./images/c04-04-17-sorted-intake-identities.png)

*Every field moved with its row. The TRIM formulas moved too, and each still points at its own row.*

5. Copy the block below, click **A14** and press **Ctrl+V**. Then type the raw and clean status you now see for each TaskID in **B15:C17**.

```text
ID after sort	Raw status	Clean status	Outcome
C001			Same ID; case repair only
C002 (both)			Both identical copies retained
C003			Unresolved; clarify
```

6. Copy the block below, click **A19** and press **Ctrl+V**. Then type `=SUM(PlannedCosts)` in **B19**, `=SUM('Sorting Practice'!G2:G13)` in **B20** and `=B19-B20` in **B21**.

```text
Named total
Explicit total
Difference
```

![The after-sort check in A14:D17 and the totals in A19:B21](./images/c04-04-18-intake-checks-and-cost-reconciliation.png)

*Same statuses as before the sort, and the named range still adds up from another tab.*

**Check:** rows 15 to 17 match rows 10 to 12, and **B21** shows **RM0**.

---

## 4.8 See What a One-Column Sort Breaks

Now make the mistake on purpose, on a copy you can throw away.

1. Click the arrow on the **Cleaning Intake** tab and choose **Duplicate**. Rename the copy `Sort Safety Test`.
2. On **Sort Safety Test**, click the name box, type `E2:E6` and press **Enter**. Only the clean status column is selected.

![Sort Safety Test with only E2:E6 selected](./images/c04-04-19-disposable-single-column-selection.png)

*This is the mistake: one column selected on its own.*

3. Click **Data**, **Sort range**, **Sort range by column E (A to Z)**.

![E2:E6 sorted on its own: C001 now shows Blocked and C003 shows Not Started](./images/c04-04-20-broken-single-column-relationships.png)

*C001 now says Blocked and C003 says Not Started. The C002 rows look fine by chance, so checking only them would miss it.*

4. Press **Ctrl+Z** straight away, before you do anything else.

![E2:E6 restored after Undo, with C001 Complete and C003 Blocked](./images/c04-04-21-immediate-undo-restoration.png)

*Undo puts every status back on its own row.*

5. Copy the block below, click **A24** and press **Ctrl+V**. Type what you saw in **C25:D27**: the status after the bad sort and after Undo.

```text
ID check	Correct	Bad sort	After Undo
C001	Complete
C002 (both)	In Progress
C003	Blocked
```

6. Click **A29** and type `Final state`. In **B29**, type `Disposable test restored; raw intake and original Tasks retained.`

![The bad-sort record in A24:D27 and the final state in row 29](./images/c04-04-22-restored-identity-evidence.png)

*The record shows what broke and that Undo fixed it.*

<details markdown="1">
<summary>What should you see?</summary>

| ID check | Correct | Bad sort | After Undo |
|---|---|---|---|
| C001 | Complete | Blocked | Complete |
| C002 (both) | In Progress | In Progress | In Progress |
| C003 | Blocked | Not Started | Blocked |

</details>

---

## Independent Practice

Try these without looking back at the steps.

1. **Does a named range grow?** On **Sorting Practice**, type a new task in row 14 with TaskID `T013` and a planned cost of `200`. Compare **L9** (`=SUM(PlannedCosts)`) with a new `=SUM(G2:G14)`. Explain the difference, then open **Data** > **Named ranges** and extend **PlannedCosts** to **G2:G14**. Finally, put things back: delete row 14, set **PlannedCosts** to **G2:G13** again and check **L11** shows **RM0**.
2. **List what's still open.** On **Cleaning Intake**, in **H1**, start a short list of the records that still need a decision from the teams, and why.
3. **Hand it over.** Give a partner your **Cleaning Intake Raw**, **Cleaning Intake** and the check tables. Without your help, they should be able to say what you changed, what you kept, and why both C002 rows are still there.

<details markdown="1">
<summary>What should you see?</summary>

With T013 added, `=SUM(PlannedCosts)` still shows **RM10,400**, while `=SUM(G2:G14)` shows **RM10,600**. A named range doesn't grow by itself when you add a row below it. After you extend it to **G2:G14**, both show **RM10,600**. Your open list should include **C003**: **Blocked** isn't one of the three statuses.

</details>

### Evidence to Hand Over

- **Dirty Text Practice** with the raw text, TRIM results and length checks
- **Sorting Practice** sorted by Team and TaskID, with a frozen header and **PlannedCosts** reconciling at **RM0**
- **Cleaning Intake Raw** unchanged, and **Cleaning Intake** cleaned and sorted with the before and after checks
- **Sort Safety Test** with the bad-sort record and its final state
- Your open list and the result of the named-range test

## Troubleshooting

| Problem | What to try |
|---|---|
| The spaces round **Planning** disappeared | Type the value again with an apostrophe in front, such as `' Planning `. |
| The sort mixed up the heading row | Undo, then tick **Data has header row** before sorting. |
| Only one column moved | Undo straight away with **Ctrl+Z**, then select the whole table and sort again. |
| **Replace all** changed more than one cell | Undo. Select **E2:E6** first, and check **Search** says **Specific range**. |
| The second sort column isn't TaskID | Open its list and choose **TaskID**: Sheets picks the next column by default. |
| The named range total is wrong | **Data** > **Named ranges**: check the sheet name and both ends of the range. |

## Lesson Summary

You cleaned text with TRIM while keeping what was sent, fixed one status with a narrowly aimed Find and replace, sorted whole records by two keys, froze the headings and named a range. You also saw a one-column sort scramble the statuses, and Undo put them back. In Lab 05 you stop bad data getting in at all, with entry rules.

**Check yourself:** what must stay together when you sort a register?
