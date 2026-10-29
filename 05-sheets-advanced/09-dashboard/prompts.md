# 09 - Build a Dashboard: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
=SPARKLINE(Analysis!B16:E16)
```

## Part 2: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Audience questions: Which project has the largest Delivered amount? How much Amount remains Pending? Which practice week has the largest all-orders Amount? PO025 extension: PJ-A, Planning, IT01, Quantity 2, UnitCost 45, Delivered, week 4.
```

## Part 3: Captured Author-Run Reference

Use separate **Dashboard Data**, **Dashboard**, and **Dashboard Contract** tabs. Earlier Analysis B16:E16 is occupied. Formulas below describe the final baseline; build them in guide order and record predictions before changing source. All input data is fictional.

### Dashboard Data A1:D4 - project view

```text
Project	All Amount incl Cancelled (RM)	Delivered Amount (RM)	Pending Amount (RM)
PJ-A	=SUM(Analysis!B4:D4)	=Analysis!B4	=Analysis!C4
PJ-B	=SUM(Analysis!B5:D5)	=Analysis!B5	=Analysis!C5
PJ-C	=SUM(Analysis!B6:D6)	=Analysis!B6	=Analysis!C6
```

### Dashboard Data A7:B10 - status counts

```text
Status	Record count
Delivered	=COUNTIF(Orders!$G$2:$G$25,A8)
Pending	=COUNTIF(Orders!$G$2:$G$25,A9)
Cancelled	=COUNTIF(Orders!$G$2:$G$25,A10)
```

### Dashboard Data A15:E16 - numeric weeks

```text
Practice week	1	2	3	4
All orders Amount (RM)	=SUMIFS(Orders!$J$2:$J$25,Orders!$H$2:$H$25,B$15)	=SUMIFS(Orders!$J$2:$J$25,Orders!$H$2:$H$25,C$15)	=SUMIFS(Orders!$J$2:$J$25,Orders!$H$2:$H$25,D$15)	=SUMIFS(Orders!$J$2:$J$25,Orders!$H$2:$H$25,E$15)
```

### Dashboard Data A18:D19 - weekly control

```text
Control	Source all Amount	Weekly sum	Difference
Week coverage	=SUM(Orders!J2:J25)	=SUM(B16:E16)	=C19-B19
```

### Dashboard Data A22:D28 - first test predictions

```text
Refresh test	Baseline	Predicted quantity 3	Restore target
PO001 Quantity	2	3	2
PO001 Amount	90	135	90
PJ-A all Amount	980	1025	980
Week 1 Amount	728	773	728
All Amount	3158	3203	3158
Record count	24	24	24
```

### Dashboard A5:D8 - project links

```text
Project	All Amount (RM)	Delivered (RM)	Pending (RM)
='Dashboard Data'!A2	='Dashboard Data'!B2	='Dashboard Data'!C2	='Dashboard Data'!D2
='Dashboard Data'!A3	='Dashboard Data'!B3	='Dashboard Data'!C3	='Dashboard Data'!D3
='Dashboard Data'!A4	='Dashboard Data'!B4	='Dashboard Data'!C4	='Dashboard Data'!D4
```

### Dashboard F5:G8 - status links

```text
Status	Record count
='Dashboard Data'!A8	='Dashboard Data'!B8
='Dashboard Data'!A9	='Dashboard Data'!B9
='Dashboard Data'!A10	='Dashboard Data'!B10
```

### Dashboard A12:E16 - weekly links and sparkline

```text
Practice week	1	2	3	4
All orders Amount (RM)	='Dashboard Data'!B16	='Dashboard Data'!C16	='Dashboard Data'!D16	='Dashboard Data'!E16

Practice-week trend	=SPARKLINE('Dashboard Data'!B16:E16)
Weekly total (RM)	=SUM(B13:E13)
```

### Dashboard A18:B22 - KPIs

```text
Key metrics	Value
All record count	=COUNTA(Orders!A2:A25)
All Amount (RM)	=SUM('Dashboard Data'!B2:B4)
Active Amount (RM)	=SUM(Orders!K2:K25)
Delivered Amount (RM)	=SUM('Dashboard Data'!C2:C4)
```

### Dashboard D18:E23 - live Checks

```text
Checks	Difference
Count via pivot	=B19-'Pivot Counts'!E6
All source amount	=B20-SUM(Orders!J2:J25)
Active via analysis	=B21-Analysis!C15
Delivered via DSUM	=B22-'Database Analysis'!D10
Check status	=IF(COUNTIF(E19:E22,0)=4,"All checks pass","Review mismatch")
```

### Dashboard A24:C27 - audience answers

```text
Audience question	Answer	Amount (RM)
Top Delivered project	=INDEX(A6:A8,MATCH(MAX(C6:C8),C6:C8,0))	=MAX(C6:C8)
Pending Amount	Pending	=SUM(D6:D8)
Peak practice week	=INDEX(B12:E12,1,MATCH(MAX(B13:E13),B13:E13,0))	=MAX(B13:E13)
```

### Dashboard Contract A1:B10 - brief

```text
Dashboard brief	Definition
Audience	Fictional project reporting reviewer; training evidence, not company policy
Source / units	Orders A1:K25;24 records; Amount and cost values in RM
Population	All includes Cancelled; Active excludes Cancelled; Delivered is a separate status subset
Questions	Largest Delivered project? Pending Amount? Largest all-orders practice week?
Practice sequence	Numeric weeks 1,2,3,4; no invented real calendar dates
Chart / filter scope	Dashboard A5:B8 linked to checked all-project totals; saved source views do not filter these SUMIFS totals
Scenario prediction	Copy only: PO001 Quantity 2 to 4 adds 90; line 180/PJ-Aall1070/Week1 818/all 3248/active 2028/Delivered1568/count 24
Expected ranking change	Largest Delivered project changes from PJ-B578 to PJ-A646; peakweek remains3at850
Validation limit	Guided author casework; independent new-row coverage, reviewer and70minute learner timing pending
```

### Dashboard Contract A12:B25 - refresh bounds

```text
Refresh contract	Observed bounds and action
Source bounds	Orders A1:K25: header plus 24 records. This run changes existing E2 only.
Formula bounds	SUMIFS/COUNTIF use rows 2:25. Dashboard Data project links use Analysis rows 4:6; weekly B16:E16.
Pivot bounds	Existing Pivot Review / Pivot Counts source Orders A1:K25. Existing-row changes updated automatically in both captured tests.
Chart bounds	Dashboard A5:B8, header plus three projects; column chart includes Cancelled.
Sparkline bounds	Dashboard B15 uses Dashboard Data B16:E16, numeric practice weeks 1 to 4.
Filter scope	Dashboard has no filter. Source saved filter views do not filter these SUMIFS totals. Exit source views after inspection.
Snapshot and export	Static exports or generated analysis snapshots need regeneration and verification after source changes. No generated snapshot was tested here.
New-row coverage	New rows require checking every source, formula, pivot and chart bound; PO025 extension is independent work, not executed.
Maintained refresh test	Quantity 2 to 3 added RM45: line 135, PJ-A1025, week 1773, total 3203. Restored 2 and baseline 3158.
Copy refresh test	Dashboard Refresh copy: quantity 2 to 4 added RM90: line 180, PJ-A1070, week 1818, total 3248, active 2028, Delivered 1568.
Copy audience result	Top Delivered changed from PJ-B578 to PJ-A646. Pending 460 and peak week 3 at 850 stayed unchanged. All four Checks differences 0.
Final restoration	Both workbooks restored to quantity 2, line 90, total 3158, active 1938, Delivered 1478, count 24.
Refresh limit	No manual refresh was required for these existing-row value tests. This does not prove automatic new-row coverage. Independent reviewer and learner timing pending.
```

### Controlled refresh tests

Maintained workbook E2:2 to 3, observe +45 then restore 2. Separate whole-workbook copy E2:2 to 4, observe +90 then restore 2. Never perform the copy test on maintained source. Copy-test expected KPIs: 24 /3248 /2028 /1568; chart PJ-A1070; Week 1818; Delivered leader PJ-A646. Final baseline: 24 /3158 /1938 /1478; weeks 728/754/850/826; Delivered leader PJ-B578, Pending 460, peak week 3 at 850. Independent PO025 extension is not covered by existing-row refresh.
