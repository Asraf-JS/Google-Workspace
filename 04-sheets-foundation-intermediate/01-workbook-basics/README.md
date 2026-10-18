# 01 - Create and Navigate a Workbook

In this chapter you will create a native Sheet, rename tabs and enter a small set of records.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 40 minutes: 10 explanation/demonstration, 10 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 30 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A named native workbook with an intact source and a separate practice tab.

> **Status:** expanded review draft, revision 0.4. Complete the casework and independent challenge as well as the guided steps. The expanded route, screenshots and timing have not yet been validated in the learner application.

## What You Will Learn

- Create and name a native Sheet.
- Navigate tabs, cells and ranges.
- Keep the input records intact.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Download [TaskRegister.xlsx](../../shared/sample-files/TaskRegister.xlsx). This workbook starts at row 1 so cell references in the course match exactly.

## 1.1 Open a Native Copy

1. Create a Drive folder named `GW - Sheets Foundation - Practice` and upload TaskRegister.xlsx.
2. Open it in Sheets and use File, Save as Google Sheets if it is still in Excel format.
3. Name the native file `GW - Sheets - Task Register`.

<details markdown="1">
<summary>What should you see?</summary>

The native workbook has Tasks and Summary tabs, with 12 task records.

</details>

<!-- VERIFY: execute 1.1 in the target account and reconcile control names. Capture images/c04-01-01.jpg only from the real app. -->

## 1.2 Navigate the Register

1. Open Tasks. Click the name box and enter `A1:H13` to select the full source table.
2. Select D5 and read the owner from the formula bar. Identify the corresponding task ID in column A.
3. Open Summary and return to Tasks. Practise moving between the tabs without changing their data.

<details markdown="1">
<summary>What should you see?</summary>

You can identify a cell address, a rectangular range and a worksheet tab.

</details>

<!-- VERIFY: execute 1.2 in the target account and reconcile control names. Capture images/c04-01-02.jpg only from the real app. -->

## 1.3 Manage a Practice Tab

1. Duplicate Tasks and name the copy `Navigation Practice`.
2. On the duplicate, enter `Practice only` in J1 and resize the column.
3. Return to the original Tasks tab. Check that the source A1:H13 remains unchanged.

<details markdown="1">
<summary>What should you see?</summary>

Experiments are on a clearly named copy; the baseline input is preserved.

</details>

<!-- VERIFY: execute 1.3 in the target account and reconcile control names. Capture images/c04-01-03.jpg only from the real app. -->

## 1.4 Build a Workbook Map and Reconstruct a Small Register

1. Create a **Workbook Guide** tab. Write a purpose for Tasks, Summary and Navigation Practice, and identify which contains the maintained 12-record source.

2. Use the name box to visit A2, D5, F8 and H13 on Tasks. For each, record the cell address, column meaning, visible value and corresponding TaskID in the guide.

3. On a new **Entry Practice** tab type the eight source headers in A1:H1. Recreate the first three task records from Tasks using values, preserving each field’s position.

4. Check each recreated row against the original by TaskID, not by appearance. Correct one copying error if found and record the check.

5. Practise selecting a cell, a whole row, a whole column and A1:H4. Record which selection would be appropriate for formatting a header versus moving a complete record.

6. Reorder Entry Practice next to Navigation Practice, then close and reopen the workbook from Drive. Use the guide to locate the original source.

7. Compare the original XLSX and the native spreadsheet by type, title and location. Add a note telling the next learner which one to edit.

<details markdown="1">
<summary>What should you see?</summary>

Workbook Guide with four address-to-record checks. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFY: execute expanded section 1.4 and independent challenge; capture images/c04-01-04.jpg only after real application success. -->

## Independent Challenge

Close the earlier step lists for the first attempt. Use the case input and your own reasoning. If you need help, record the hint and repeat the affected check independently.

1. Without using Recent, reopen the native file and locate the owner and actual cost for T008 using its record identity.

2. Create a two-row **New Entry Form** practice table with blank inputs and clear field labels. Do not append unfinished rows to Tasks.

3. Explain and demonstrate a cell address, a range, a tab and the source file identity. Have a partner use the guide or test it yourself after closing the workbook.

## Evidence to Hand Over

- Workbook Guide with four address-to-record checks.
- Recreated three-row entry table and a corrected/verified copy record.
- Independent source retrieval and a labelled new-entry practice area.

Record the defect or uncertainty you investigated, the evidence used, the repair or reasoned no-change decision, and the final state. Restore temporary changes or keep them in a clearly named scenario copy.

## Troubleshooting

| Symptom | What to check |
|---|---|
| An address is mistaken for a permanent task identity | Use TaskID to identify a record because sorting can move it to another row. |
| An input or earlier result is missing | Reopen the input named in Before You Begin; do not substitute private company data |
| A menu or feature is unavailable | Confirm the account and the shared access notes; record the missing step and ask the trainer for its fallback |
| The result differs from the checkpoint | Compare the exact source range, wording and conditions before repeating the action |

## Lesson Summary

You can navigate and manage a native workbook. Next, make its data readable without changing its meaning.

**Check yourself:** What is the difference between a spreadsheet file and a worksheet tab?
