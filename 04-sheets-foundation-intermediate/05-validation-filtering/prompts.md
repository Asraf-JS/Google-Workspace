# 05 - Validate and Filter the Register: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Incomplete tasks
```

```text
Done
```

## Part 2: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Rule test values: status Complete, In Progress, Not Started, Done and blank; DueWeek 0, 1, 4, 5 and 1.5. DueWeek is a relative index for this training exercise, not an approved calendar schedule.
```

## Part 3: Captured Rule and View Reference

- Tasks status range **F2:F13**; single-selection dropdown Complete / In Progress / Not Started, **Reject the input**. Spare N2 has the copied validation and is empty after the rejected Done test.
- Rule Tests status inputs **B2:B6** use that same strict rule. B2:B4 retain Complete / In Progress / Not Started; attempted Done in B5 was rejected, and clearing B6 was allowed. A2:A6 retain the attempted test values; observations are separate in D.
- Entry Rule Practice **E2:E4**: custom formula **=AND(ISNUMBER(E2),E2=INT(E2),E2>=1,E2<=4)**, reject invalid input. Help text: Enter a whole practice week from 1 to 4. This is not a calendar date. Test E4 with 0/1/4/5/1.5, then clearing. Observed reject/accept/accept/reject/reject/clearing allowed. Restore E4 to 1. The bounded rule does not cover the copied notes below the three-record table.
- Tasks **I15 SUM costs / J15 =SUM(G2:G13)** displays 10400 before and during either view. Ordinary SUM includes hidden rows.
- **Incomplete tasks**, Tasks A1:I13: exclude Complete; eight IDs T002,T003,T005,T006,T008,T009,T011,T012.
- **Planning incomplete tasks**, same range: Team Planning and Status excluding Complete; two IDs T002,T003.
- Both views were reopened and checked, then closed with all 12 rows visible. Entry guide and view observations are in Rule Tests A18:B24/A27:E31.

Source Tasks A1:L13 values/formulas and the original Entry Practice records remain unchanged. Testing clearing does not guarantee all required fields are complete. Independent Procurement/new-row coverage challenges and classroom timing remain pending.

## Part 4: Rule Tests Layout

Section 5.4. Columns are separated by tabs, so you can paste each block into its first cell. Leave **Validated input** (column B) empty until you test it, and change **Pending** to what you actually observe.

Status test plan, A1:E6 (step 1):

```text
Status test	Validated input	Expected	Observed	Repair / next action
Complete		Accept	Pending	None if accepted
In Progress		Accept	Pending	None if accepted
Not Started		Accept	Pending	None if accepted
Done		Reject	Pending	Use a canonical status
Blank		Test clearing	Pending	Check required fields separately
```

Week test plan, A9:E15 (step 5). Column B names the cell you test on Entry Rule Practice:

```text
Week test	Copy cell	Expected	Observed	Repair / next action
0	E4	Reject	Pending	Use integer 1 through 4
1	E4	Accept	Pending	None if accepted
4	E4	Accept	Pending	None if accepted
5	E4	Reject	Pending	Use integer 1 through 4
1.5	E4	Reject	Pending	Use a whole week
Blank	E4	Test clearing	Pending	Check required fields separately
```

Entry guide, A18:A24 (step 12). Write your own instruction for each row in column B:

```text
Entry guide
Status
DueWeek
Invalid input
Blank fields
Unclear category
Rule coverage
```

View check, A27:E31 (step 20):

```text
View check	Range	Visible IDs	Ordinary SUM	Observed IDs / restore
Incomplete tasks
Planning incomplete tasks
Closed views
Scope
```
