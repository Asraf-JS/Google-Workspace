# 07 - Summarise with Pivot Tables: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Pivot Review
```

```text
=SUM(Amount)/COUNTA(OrderID)
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
PO025, challenge copy only: PJ-A | Planning | IT01 | Quantity 2 | UnitCost 45 | Delivered | week 4 | Additional practice line. Amount is quantity times cost. Extend both formulas and pivot source range; do not alter the baseline workbook.
```

## Captured Author-Run Reference

Use native **Insert > Pivot table**, not a typed summary. Baseline source **Orders A1:K25** contains24records. Keep source edits for the named whole-workbook **Pivot Coverage** copy only. These cards support guided casework, not an independent learner submission.

### Calculated field — Average line amount, Summarise by Custom

```text
=SUM(Amount)/COUNTA(OrderID)
```

### Pivot Checks A1:E5 — expectations first, actual columns blank

```text
Project	Expected average	Source average	Pivot average	Difference
PJ-A	122.5
PJ-B	150.5
PJ-C	121.75
All	131.583333333333
```

### Pivot Checks C2:E5 — source/native comparison formulas

```text
=SUMIF(Orders!$B$2:$B$25,A2,Orders!$J$2:$J$25)/COUNTIF(Orders!$B$2:$B$25,A2)	='Pivot Calculations'!C2	=D2-C2
=SUMIF(Orders!$B$2:$B$25,A3,Orders!$J$2:$J$25)/COUNTIF(Orders!$B$2:$B$25,A3)	='Pivot Calculations'!C3	=D3-C3
=SUMIF(Orders!$B$2:$B$25,A4,Orders!$J$2:$J$25)/COUNTIF(Orders!$B$2:$B$25,A4)	='Pivot Calculations'!C4	=D4-C4
=SUM(Orders!$J$2:$J$25)/COUNTA(Orders!$A$2:$A$25)	='Pivot Calculations'!C5	=D5-C5
```

### Pivot Checks A8:D18 — category counts and total

```text
Project / status	Source count	Pivot count	Difference
PJ-A / Cancelled	=COUNTIFS(Orders!$B$2:$B$25,"PJ-A",Orders!$G$2:$G$25,"Cancelled")	='Pivot Counts'!B3	=C9-B9
PJ-A / Delivered	=COUNTIFS(Orders!$B$2:$B$25,"PJ-A",Orders!$G$2:$G$25,"Delivered")	='Pivot Counts'!C3	=C10-B10
PJ-A / Pending	=COUNTIFS(Orders!$B$2:$B$25,"PJ-A",Orders!$G$2:$G$25,"Pending")	='Pivot Counts'!D3	=C11-B11
PJ-B / Cancelled	=COUNTIFS(Orders!$B$2:$B$25,"PJ-B",Orders!$G$2:$G$25,"Cancelled")	='Pivot Counts'!B4	=C12-B12
PJ-B / Delivered	=COUNTIFS(Orders!$B$2:$B$25,"PJ-B",Orders!$G$2:$G$25,"Delivered")	='Pivot Counts'!C4	=C13-B13
PJ-B / Pending	=COUNTIFS(Orders!$B$2:$B$25,"PJ-B",Orders!$G$2:$G$25,"Pending")	='Pivot Counts'!D4	=C14-B14
PJ-C / Cancelled	=COUNTIFS(Orders!$B$2:$B$25,"PJ-C",Orders!$G$2:$G$25,"Cancelled")	='Pivot Counts'!B5	=C15-B15
PJ-C / Delivered	=COUNTIFS(Orders!$B$2:$B$25,"PJ-C",Orders!$G$2:$G$25,"Delivered")	='Pivot Counts'!C5	=C16-B16
PJ-C / Pending	=COUNTIFS(Orders!$B$2:$B$25,"PJ-C",Orders!$G$2:$G$25,"Pending")	='Pivot Counts'!D5	=C17-B17
All records	=COUNTA(Orders!A2:A25)	='Pivot Counts'!E6	=C18-B18
```

### Pivot Checks A21:F25 — manual amounts before comparison

```text
OrderID	Quantity	UnitCost	Manual amount	Formula amount	Difference
PO001	2	45	90
PO004	8	18	144
PO005	10	25	250
PO008	6	12	72
```

### Pivot Checks E22:F25 — row comparison formulas

```text
=B22*C22	=E22-D22
=B23*C23	=E23-D23
=B24*C24	=E24-D24
=B25*C25	=E25-D25
```

### Pivot Checks A27:D28 — actual drilldown reconciliation

```text
Control	Manual sum	Native detail sum	Difference
PJ-A Delivered	=SUM(D22:D25)	=SUM('Detail1-PJ-A-Delivered'!J2:J5)	=C28-B28
```

### Pivot Checks A31:D33 — two-row aggregation practice

```text
Practice row	Quantity	UnitCost	Row amount
First line	2	45	=B32*C32
Second line	4	12	=B33*C33
```

### Pivot Checks A35:B38 — aggregation comparison

```text
Metric	Result
Expected row total	138
Sum of row products	=SUM(D32:D33)
Product of sums	=SUM(B32:B33)*SUM(C32:C33)
```

### Scenario Orders A26:K26 — after inserting row 26

```text
PO025	PJ-A	Planning	IT01	2	45	Delivered	4	Additional practice line	=E26*F26	=IF(G26="Cancelled",0,J26)
```

### Scenario Orders J28:K28 — repaired source totals

```text
=SUM(J2:J26)	=SUM(K2:K26)
```

### Coverage Controls A1:D7 — expanded source/pivot reconciliation

```text
Coverage control	Source formula	Expanded pivot	Difference
All amount	=SUM(Orders!J2:J26)	='Pivot Review'!E6	=C2-B2
Delivered amount	=SUMIF(Orders!G2:G26,"Delivered",Orders!J2:J26)	='Pivot Review'!C6	=C3-B3
All count	=COUNTA(Orders!A2:A26)	='Pivot Counts'!E6	=C4-B4
Delivered count	=COUNTIF(Orders!G2:G26,"Delivered")	='Pivot Counts'!C6	=C5-B5
PJ-A Delivered amount	=SUMIFS(Orders!J2:J26,Orders!B2:B26,"PJ-A",Orders!G2:G26,"Delivered")	='Pivot Review'!C3	=C6-B6
PJ-A Delivered count	=COUNTIFS(Orders!B2:B26,"PJ-A",Orders!G2:G26,"Delivered")	='Pivot Counts'!C3	=C7-B7
```

### Coverage Controls A10:B14 — scenario scope note

```text
Scenario scope	Record
Source	Orders A1:K26 includes PO025, amount 90
Pivots	Pivot Review SUM Amount; Pivot Counts COUNTA OrderID; both A1:K26
Earlier sheets	Copied baseline checks and calculated pivot still target24rows; historical comparison only
Authoritative expanded checks	Coverage Controls A1:D7; six differences 0; independent learner challenge pending
```

### Pivot Notes A1:B10 — baseline handover

```text
Analysis note	Definition / evidence
Baseline source	Orders A1:K25;24records; Cancelled retained
Amount pivot	Pivot Review: Project rows, Status columns, SUM Amount; no final filter
Filter test	Delivered only 1478; removed filter restores 3158
Count pivot	Pivot Counts: same source/groups, COUNTA OrderID;24total/12Delivered
Calculated field	Pivot Calculations: Average line amount =SUM(Amount)/COUNTA(OrderID), Custom; all 131.5833333
Drilldown	Actual Detail1-PJ-A-Delivered contains PO001/004/005/008; amounts 90/144/250/72 sum 556
Aggregation trap	Two rows2x45 and4x12: SUM row products 138; product of sums 342
Coverage experiment	Separate Pivot Coverage workbook only: confirmed A1:K26 gives 3248/25; Delivered 1568/13
Validation limit	Guided author reference; independent learner diagnosis/presentation and75minute timing pending
```

### Native pivot definitions

| Tab | Source | Rows | Columns | Values | Final filter |
|---|---|---|---|---|---|
| Pivot Review | Orders A1:K25 | Project | Status | SUM of Amount | None; Delivered-only1478 test then removed |
| Pivot Counts | Orders A1:K25 | Project | Status | COUNTA of OrderID | None |
| Pivot Calculations | Orders A1:K25 | Project | None | SUM of Amount plus Average line amount, Custom | None |
| Scenario Pivot Review | Orders A1:K26 | Project | Status | SUM of Amount | None |
| Scenario Pivot Counts | Orders A1:K26 | Project | Status | COUNTA of OrderID | None |

Use **Select data range > Range > OK** to confirm range edits. Inspect recalculation, not just input text. Expected baseline 3158/1478/24/12; scenario 3248/1568/25/13. PJ-A Delivered changes 556/4 to 646/5. Do not include summary rows 27–28 in the scenario pivot source.

The two-row trap has row products 90 and 48, sum 138; multiplying the summed quantities 6 by summed costs 57 returns 342. These metrics have different meanings. The original ambiguous multiplication prompt has been replaced by the actually verified average field; retain SUM of row Amount for authoritative totals.

Earlier copied scenario checks/calculated pivots remain 24-row references. Only the expanded source summaries and Coverage Controls A1:D7 establish 25-row coverage. Independent Delivered pivot/output, learner diagnosis/presentation and timing remain pending.
