# 02 - Enter and Format Reliable Data

In Lab 01 you typed three costs as plain numbers, such as `600`, and they look plain on **Entry Practice**. On **Tasks** the same costs show as **RM 600**. Aina wants the practice tab to look like the real register, but she's been caught out before by a "cost" that looked right and wasn't a number at all, so a total came out wrong. In this lab you format the costs and headings, and you learn to tell what a cell holds from what it shows.

**Estimated time:** 45 minutes, planned as 5 explanation, 25 guided build and 15 independent practice. Not yet timed with learners.

**Your result:** **Entry Practice** in `GW - Sheets - Task Register` with ringgit costs, headings that match **Tasks** and readable task names, plus a small **Type tests** block that shows why a typed `RM 600` doesn't add up.

> **You'll practise:** reading the formula bar, applying a custom number format, copying formatting with **Paste special** and **Paint format**, wrapping text, and spotting text that only looks like a number.

---

## What You Will Learn

- Tell a cell's value from its display format
- Format numbers as ringgit without changing them
- Make a table readable without merging cells

## Before You Begin

Open `GW - Sheets - Task Register` from **GW - Sheets Foundation - Practice**. You need **Entry Practice** from Lab 01, with the headings and three records in **A1:H4**.

If you skipped Lab 01, download [TaskRegister.xlsx](../../shared/sample-files/TaskRegister.xlsx), follow Lab 01 sections 1.1, 1.2 and 1.7, then come back.

**What you change in this lab:**

**Entry Practice**: costs > headings > task names > **Type tests** > **Workbook Guide**: formatting check

You don't change **Tasks**. You only copy from it.

## Topics

**What a cell holds and what it shows.** Click a cell and look at the formula bar: that's the value. The cell itself shows the value through a format. `600` formatted as ringgit shows **RM 600**, but it's still the number 600, so it adds up. If someone types the letters `RM 600`, the cell holds text. It looks the same, but a total skips it.

**A quick clue.** Sheets lines up numbers on the right of a cell and text on the left. A "cost" sitting on the left is worth a second look.

**Weeks aren't dates.** **DueWeek** is a week number in the pilot (1 to 4), not a calendar date. The pilot's start date isn't agreed yet, so a value like `next Monday` can't become a real date. Leave it as a question.

---

## 2.1 Compare a Value With How It Looks

1. Click the **Tasks** tab, then click **G2**. The cell shows **RM 600**. Look at the formula bar: it shows `600`.
2. Click the **Entry Practice** tab, then click **G2**. The cell shows **600**, and so does the formula bar.

<!-- CAPTURE: Tasks!G2 selected, formula bar 600, cell RM 600. Then Entry Practice!G2 selected, both 600. -->

Same value, different format. You're about to give **Entry Practice** the same format, without retyping anything.

**Check:** you can say what **G2** holds on both tabs (600) and why they look different (only **Tasks** has a ringgit format).

---

## 2.2 Show the Costs as Ringgit

1. On **Entry Practice**, click the name box, type `G2:H4` and press **Enter**. Both cost columns for your three records are selected.
2. Click **Format**, then **Number**, then **Custom number format**.
3. In the box at the top, delete anything already there, then copy and paste this format:

```text
"RM "#,##0
```

4. Click **Apply**.

<!-- CAPTURE: Custom number formats dialog with "RM "#,##0 typed, then Entry Practice G2:H4 showing RM 600, RM 550 and so on. -->

5. Click **G2** again. The cell shows **RM 600**, and the formula bar still shows `600`.

**Check:** **G2:H4** on **Entry Practice** show **RM** amounts, such as **RM 600** and **RM 0**, and the formula bar shows plain numbers.

---

## 2.3 Make the Headings and Task Names Readable

You copy the look of the **Tasks** headings rather than rebuilding it. **Paste special > Format only** brings across the colours and font, and leaves the words in your cells alone.

1. Click the **Tasks** tab. Click the name box, type `A1:H1` and press **Enter**. Press **Ctrl+C**.
2. Click the **Entry Practice** tab and click **A1**.
3. Click **Edit**, then **Paste special**, then **Format only** (or press **Ctrl+Alt+V**). The headings take the **Tasks** colours.

<!-- CAPTURE: Edit > Paste special menu with Format only, then Entry Practice row 1 in the Tasks header style. -->

4. Click the name box, type `C2:C4` and press **Enter**. Click **Format**, then **Wrapping**, then **Wrap**. Long task names now break onto a second line instead of running into the next column.
5. If a row looks cramped, drag the line under its row number down a little.

<!-- CAPTURE: Entry Practice with Tasks-style headings, RM costs and wrapped task names. -->

Don't merge cells to make headings look neater. A merged cell sits across two columns, so sorting and filtering can't treat each field separately. You'll rely on that in later labs.

**Check:** **Entry Practice** row 1 matches the **Tasks** headings, the task names in **C2:C4** are fully visible, and no cells are merged.

---

## 2.4 Spot Text That Looks Like a Number

Now you see the problem Aina warned about, on purpose, in a corner of **Entry Practice** away from your records.

1. Copy the block below, click **J1** on **Entry Practice** and press **Ctrl+V**. It adds four labels in **J1:J4**.

```text
Type tests
Number
Text
Total
```

2. Click **K2** and type `600`, then press **Enter**.
3. In **K3**, type `RM 600` (the letters R and M, a space, then 600) and press **Enter**.
4. In **K4**, type `=SUM(K2:K3)` and press **Enter**. The total is **600**, not 1200: the sum skipped **K3**.
5. Look at where the values sit: **600** in **K2** is on the right of its cell, and **RM 600** in **K3** is on the left. That's the text clue.
6. Click **G2**, click **Paint format** (the paint roller on the toolbar), then click **K2**. **K2** takes the ringgit format. **K2** and **K3** now look almost the same, but only **K2** is counted.

<!-- CAPTURE: Type tests block with K2 formatted RM 600, K3 text RM 600 left-aligned, K4 total 600. -->

7. Fix **K3**: click it, type `600` and press **Enter**. The total changes to **1200**.

<details markdown="1">
<summary>What should you see?</summary>

Before the fix, **K4** shows **600**: only the number in **K2** is added. After you retype **K3** as `600`, **K4** shows **1200**. Formatting can't turn typed text into a number; retyping the value as a number can.

</details>

---

## 2.5 Check Tasks and Record What You Did

1. Click the **Tasks** tab. Click **G2** and check the formula bar still shows `600`. Check the twelve tasks are still in rows 2 to 13.
2. Click the **Workbook Guide** tab. Copy the block below, click **A31** and press **Ctrl+V**. Row 30 stays empty as a gap.

```text
Formatting check	Result
Entry Practice costs	G2:H4 show RM amounts; the formula bar still shows plain numbers.
Headings and task names	Row 1 copied from Tasks with Paste special > Format only; C2:C4 wrapped; no merged cells.
Type tests	RM 600 typed as text was skipped by SUM; retyped as 600 it was counted.
Tasks	Unchanged: 12 records, costs are still numbers.
```

<!-- CAPTURE: Workbook Guide rows 31 to 35 with the formatting check. -->

**Check:** **Workbook Guide** has the formatting check in **A31:B35**, and **Tasks** is unchanged.

---

## Independent Practice

A Site Coordination lead has sent a new task on a card, typed the way people often do. Try this without looking back at the steps.

1. On **Entry Practice**, copy the block below, click **A7** and press **Ctrl+V**. Row 7 is a label, and row 8 is the card exactly as supplied.

```text
Intake card - as supplied
T013	Site Coordination	Prepare the weekly sponsor summary and check every team's figures before Friday	Bala Kumar	next Monday	Not Started	RM 600	0
```

2. In row 10, type `Clean entry`. In row 11, type a cleaned-up version of the same task, all eight fields:
   - **PlannedCost** as a number, formatted as ringgit
   - **DueWeek** left empty, because nobody has agreed which week "next Monday" means
   - the long task name wrapped so it's readable
3. In **J7**, type the question you'd send back to the lead about the due week.
4. Show a partner **G8** and **G11**. Ask them which one a total would count, and how they can tell without a formula.

<details markdown="1">
<summary>What should you see?</summary>

**G8** holds the text `RM 600` and sits on the left of its cell. **G11** holds the number 600, shows **RM 600** and sits on the right. **E11** is empty, and **J7** asks something like "Which pilot week is next Monday? The start date isn't agreed yet." Row 8 stays as supplied, so anyone can see what you started from.

</details>

### Evidence to Hand Over

- **Entry Practice** with ringgit costs, **Tasks**-style headings and wrapped task names
- The **Type tests** block, with **K4** showing **1200** after the fix
- The intake card as supplied (row 8), your clean entry (row 11) and your question in **J7**
- The formatting check in **Workbook Guide**

## Troubleshooting

| Problem | What to try |
|---|---|
| The total is smaller than you expect | One of the cells is probably text. Click each one: a value on the left of its cell, or with letters in the formula bar, isn't a number. Retype it as a plain number. |
| The format box showed an error | Copy the format again, including both quotation marks: `"RM "#,##0` |
| **Paste special > Format only** also changed your words | You pressed **Ctrl+V** instead. Press **Ctrl+Z**, then use **Edit > Paste special > Format only**. |
| `=SUM(K2:K3)` shows as text in the cell | There's a space or an apostrophe before the `=`. Click the cell, delete it and type the formula again. |
| You formatted **Tasks** by mistake | Press **Ctrl+Z** until the change is gone. Formatting only changes the look, so the values are safe. |

## Lesson Summary

You formatted costs as ringgit without changing them, copied the heading style from **Tasks**, wrapped long task names without merging cells, and saw why a typed `RM 600` breaks a total. In Lab 03 you start calculating with these numbers.

**Check yourself:** why should you avoid merging cells inside a table of records?
