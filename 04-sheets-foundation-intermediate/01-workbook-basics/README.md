# 01 - Create and Navigate a Workbook

In this chapter you will create a native Sheet, rename tabs and enter a small set of records.

> **Prompts and values:** use the [copy-paste page](./prompts.md) for the exact values used below.

**Target allocation:** 40 minutes: 10 explanation/demonstration, 10 guided build and casework, 15 independent challenge, 5 verification and repair. The active portion is 30 minutes by design. These are unmeasured targets awaiting a learner pilot.

**Your result:** A named native workbook with an intact source and a separate practice tab.

> **Status:** author reference with 26 current-stage application captures through 1.4. Native conversion, navigation, separate practice tabs, address map, reconstruction and Drive reopen checked. The instructor completed the XLSX upload manually after the browser extension blocked it; automated upload, independent challenge and learner timing remain unverified.

## What You Will Learn

- Create and name a native Sheet.
- Navigate tabs, cells and ranges.
- Keep the input records intact.

## Before You Begin

Read the [case input](./prompts.md) and use a separate named casework copy for destructive tests or altered datasets. Keep the baseline unchanged for later chapters. Record source facts, proposed practice and unresolved questions separately.

Download [TaskRegister.xlsx](../../shared/sample-files/TaskRegister.xlsx). This workbook starts at row 1 so cell references in the course match exactly.

## 1.1 Open a Native Copy

1. In the training account, create a Drive folder named `GW - Sheets Foundation - Practice`. Keep the starter file separate from later native practice.

![Create the empty Foundation practice folder](./images/c04-01-01-empty-foundation-practice-folder.jpg)

2. Upload **TaskRegister.xlsx** into this folder and confirm its **Microsoft Excel** type. In this author run the instructor uploaded the file manually: the extension still rejected file upload after its file-URL setting and browser restart. The captured uploaded file is real; the automated upload step is not claimed as passed.

![Inspect the uploaded original Excel file](./images/c04-01-02-uploaded-original-xlsx.jpg)

3. Open the uploaded file in Sheets. While its **.XLSX / Microsoft Excel format** badge is visible, choose **File > Save as Google Sheets**. This creates a separate native file; the original Excel file remains in the folder.

![Use Save as Google Sheets while the XLSX badge is visible](./images/c04-01-03-excel-format-save-as-google-sheets.jpg)

4. Name the new native file `GW - Sheets - Task Register`. Confirm the XLSX badge is absent and **Tasks** and **Summary** are present. Do not rename the original XLSX instead.

![Name the separate native workbook with only its starter tabs](./images/c04-01-04-named-native-copy-two-tabs.jpg)

<details markdown="1">
<summary>What should you see?</summary>

The native workbook has Tasks and Summary tabs, with 12 task records.

</details>

<!-- VERIFIED: guided/casework UI and bounded source comparison; manual upload handoff, independent challenge and learner timing remain separate. -->

## 1.2 Navigate the Register

1. Open **Tasks**. Click the name box, enter `A1:H13` and press **Enter** to select all eight headers and twelve records.

![Select the complete twelve-record source range](./images/c04-01-05-select-full-source-range.jpg)

2. Enter **D5** in the name box and press **Enter**. Read **Aina Rahman** from the formula bar; the corresponding row is **T004** in column A. A cell address locates the value now; TaskID identifies the record if rows later move.

![Read the owner in D5 and identify T004](./images/c04-01-06-d5-owner-and-task-record.jpg)

3. Open **Summary** and return to **Tasks**. Summary contains the supplied starter headings/categories; do not build later formulas or charts yet.

![Inspect the supplied Summary tab before later calculations](./images/c04-01-07-summary-tab-before-calculations.jpg)

<details markdown="1">
<summary>What should you see?</summary>

You can identify a cell address, a rectangular range and a worksheet tab.

</details>

<!-- VERIFIED: guided/casework UI and bounded source comparison; manual upload handoff, independent challenge and learner timing remain separate. -->

## 1.3 Manage a Practice Tab

1. Open the **Tasks** tab menu and choose **Duplicate**. Rename **Copy of Tasks** to `Navigation Practice` using its tab label or **Rename** command.

![Name the Tasks duplicate Navigation Practice](./images/c04-01-08-named-navigation-practice-duplicate.jpg)

2. On **Navigation Practice**, enter `Practice only` in **J1**, commit the entry, and widen column J using its header boundary. Keep this experiment on the duplicate.

![Enter Practice only and widen its column on the duplicate](./images/c04-01-09-practice-only-label-and-resized-column.jpg)

3. Return to **Tasks** and inspect **A1:H13**. The reference source was compared with its initial native cell data and remained unchanged, including all twelve records.

![Return to the unchanged original Tasks tab](./images/c04-01-10-original-tasks-after-practice-edit.jpg)

<details markdown="1">
<summary>What should you see?</summary>

Experiments are on a clearly named copy; the baseline input is preserved.

</details>

<!-- VERIFIED: guided/casework UI and bounded source comparison; manual upload handoff, independent challenge and learner timing remain separate. -->

## 1.4 Build a Workbook Map and Reconstruct a Small Register

1. Use **Add Sheet**, rename it **Workbook Guide**, and record the purpose of Tasks, Summary and Navigation Practice. Identify **Tasks!A1:H13** as the maintained twelve-record source. Widen the authored guide columns so the map is readable.

![Record the purpose and source status of each tab](./images/c04-01-11-workbook-guide-tab-purposes.jpg)

2. On **Tasks**, use the name box to visit **A2, D5, F8 and H13**. Inspect the value and the corresponding TaskID each time before recording the check in Workbook Guide. The reference values are below; zero actual cost is a value, not a blank.

![Visit A2 and identify T001](./images/c04-01-12-source-address-a2.jpg)

![Visit D5 and identify the owner of T004](./images/c04-01-13-source-address-d5.jpg)

![Visit F8 and identify the status of T007](./images/c04-01-14-source-address-f8.jpg)

![Visit H13 and identify the zero actual cost of T012](./images/c04-01-15-source-address-h13.jpg)

| Address | Column meaning | Visible value | TaskID |
|---|---|---|---|
| A2 | TaskID | T001 | T001 |
| D5 | Owner | Aina Rahman | T004 |
| F8 | Status | Complete | T007 |
| H13 | ActualCost | 0 (displayed RM 0 in Tasks) | T012 |

![Record all four address-to-record checks](./images/c04-01-16-four-address-record-checks-in-guide.jpg)

3. Add **Entry Practice**. Enter the eight source headers in **A1:H1**, then recreate **T001, T002 and T003** as values in **A2:H4**, preserving field positions. Widen the task-text column if needed; do not copy the entire Tasks tab for this reconstruction exercise.

![Recreate the first three records with all eight fields](./images/c04-01-17-three-record-entry-practice-reconstruction.jpg)

4. Compare all eight fields by **TaskID** against **Tasks**. The reference three rows matched, so no copying error was invented or introduced. Record that result. The observed readability issue was clipped task text; widening the Entry Practice task column repaired the display without changing values.

5. Practise **B2** (one cell), **2:2** (whole row), **C:C** (whole column) and **A1:H4** (small table) through the name box. Record that **A1:H1** targets the header only, while a complete record must keep all its fields together. Selection alone does not move data.

![Select a single cell](./images/c04-01-18-select-one-cell.jpg)

![Select the complete second row](./images/c04-01-19-select-complete-row.jpg)

![Select the Task column](./images/c04-01-20-select-whole-column.jpg)

![Select the header and three reconstructed records](./images/c04-01-21-select-header-and-three-records.jpg)

![Record reconstruction and selection checks](./images/c04-01-22-reconstruction-and-selection-checks-recorded.jpg)

6. Use the Entry Practice tab menu **Move right** to place it after **Navigation Practice**. Close the native workbook, return to the practice folder in Drive and reopen the file by its name and type. This tests retrieval from the folder rather than using Recent.

![Move Entry Practice after Navigation Practice](./images/c04-01-23-entry-practice-reordered-after-navigation.jpg)

![Compare the native file and original XLSX in the same Drive folder](./images/c04-01-24-native-and-original-file-types-in-folder.jpg)

7. In **Workbook Guide**, record both identities: **TaskRegister.xlsx — Microsoft Excel**, retained as supplied source; **GW - Sheets - Task Register — Google Sheets**, the course working file. Both are in **My Drive / GW - Sheets Foundation - Practice**. Tell the next learner to open Workbook Guide, then Tasks, and identify records by TaskID. Confirm the map and checks survived reopening.

![Record which file to edit after reopening from Drive](./images/c04-01-25-reopened-workbook-source-identity-and-edit-instructions.jpg)

![Inspect the completed Workbook Guide after reopening](./images/c04-01-26-complete-workbook-guide-after-reopen.jpg)

<details markdown="1">
<summary>What should you see?</summary>

Workbook Guide with four address-to-record checks. The result must be supported by the recorded checks; an attractive output or an AI assurance is insufficient.

</details>

<!-- VERIFIED: guided/casework UI and bounded source comparison; manual upload handoff, independent challenge and learner timing remain separate. -->

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
