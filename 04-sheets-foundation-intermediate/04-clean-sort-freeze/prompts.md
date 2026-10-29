# 04 - Clean and Organise Records: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
CleanTeam
```

```text
=TRIM(B2)
```

```text
PlannedCosts
```

```text
=SUM(PlannedCosts)
```

## Part 2: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Cleaning intake (TaskID | Team | Status): C001 |  Planning  | complete; C002 | Procurement | In Progress; C003 | Site Coordination | Blocked; C002 | Procurement | In Progress; C004 | Planning | Not Started. C001 has surrounding team spaces. The duplicate is identical; Blocked remains unresolved. These are separate practice records.
```

## Part 3: Exact DirtyText.csv Records

For manual entry, treat each CSV field below as a separate cell and preserve the spaces inside its quotation marks. Do not paste the entire comma-separated block into one cell.

```csv
"TaskID","Team","Status"
"T001"," Planning ","complete"
"T002","Procurement","In Progress"
"T003","Site Coordination ","Not Started"
```

## Part 4: Manual Raw-Entry Fallback

CSV import remains unverified in the captured browser session. If entry trims the surrounding spaces, use a leading apostrophe in the cell editor to preserve the literal raw text; do not include that prefix in the intended stored value. DirtyText.csv raw team values are ` Planning `, `Procurement`, and `Site Coordination `, with lengths 10,11,18. TRIM produces Planning/Procurement/Site Coordination, lengths 8,11,17. Keep raw A:C and cleaned D:E separate.

Cleaning Intake Raw A1:C6 contains the five supplied C records. The reference explicitly preserves two spaces before and after C001's Planning. Duplicate it as Cleaning Intake. D2:D6 uses TRIM of B on each row; E initially copies raw status. Restrict Find and replace complete→Complete to E2:E6, matching case and entire cell; one replacement. Both C002 records are identical and retained. C003 Blocked is unresolved, with no invented mapping.

Sort A1:F6 by CleanTeam then TaskID, with the header option: C001,C004,C002,C002,C003. Inspect C001/C002/C003 status relationships before and after. In a disposable Sort Safety Test copy, sorting only E2:E6 A→Z makes C001 Blocked and C003 Not Started; Undo restores Complete and Blocked respectively. C002 remains In Progress through this test.

PlannedCosts bounds: **'Sorting Practice'!G2:G13**, twelve numeric cells. SUM(PlannedCosts)=10400, explicit SUM of that range=10400, difference 0. No new-row expansion test is claimed. Tasks A1:L13 values/formulas remain unchanged. Independent challenge and learner timing remain pending.
