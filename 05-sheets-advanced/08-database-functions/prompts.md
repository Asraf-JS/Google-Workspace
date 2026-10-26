# 08 - Query Structured Criteria: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Delivered amount
```

```text
=DSUM(Orders!A1:J25,"Amount",A10:A11)
```

```text
Delivered numeric quantity records
```

```text
=DCOUNT(Orders!A1:J25,"Quantity",A10:A11)
```

```text
Average delivered unit cost
```

```text
=DAVERAGE(Orders!A1:J25,"UnitCost",A10:A11)
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Criteria cases: Status=Delivered AND Project=PJ-A; Status=Delivered OR Status=Pending; Status=Delivered OR Project=PJ-A. The last case overlaps. DCOUNT uses numeric Quantity; OrderID is text and must not be treated as a numeric record count.
```

## Captured Author-Run Reference

Use a separate **Database Analysis** tab because the earlier Analysis cells are occupied. Maintained source is **Orders A1:J25**. Predict results before actual formulas. These cards show the final corrected source-derived mean352/18; the historical first-pass prediction23 in screenshots is investigated in the guide. Independent learner work remains a separate task.

### Database Analysis A10:B11 — criteria

```text
Status	Project
Delivered	PJ-A
```

### Database Analysis C10:D12 — original Delivered formulas

```text
Delivered amount	=DSUM(Orders!A1:J25,"Amount",A10:A11)
Delivered numeric quantity records	=DCOUNT(Orders!A1:J25,"Quantity",A10:A11)
Average delivered unit cost	=DAVERAGE(Orders!A1:J25,"UnitCost",A10:A11)
```

### Database Analysis C14:E15 — amount control

```text
Control	Source SUMIF	Difference
Delivered amount	=SUMIF(Orders!G2:G25,"Delivered",Orders!J2:J25)	=D10-D15
```

### Database Analysis C17:D20 — field-aware counts

```text
Count comparison	Result
DCOUNT text OrderID	=DCOUNT(Orders!A1:J25,"OrderID",A10:A11)
DCOUNTA populated OrderID	=DCOUNTA(Orders!A1:J25,"OrderID",A10:A11)
COUNTIF Delivered source rows	=COUNTIF(Orders!G2:G25,"Delivered")
```

### Database Analysis C23:D26 — AND metrics

```text
Delivered AND PJ-A	Result
Amount	=DSUM(Orders!A1:J25,"Amount",A10:B11)
Numeric quantity records	=DCOUNT(Orders!A1:J25,"Quantity",A10:B11)
Average unit cost	=DAVERAGE(Orders!A1:J25,"UnitCost",A10:B11)
```

### Database Analysis C28:E29 — SUMIFS comparison

```text
AND comparison	SUMIFS	Difference
Delivered AND PJ-A	=SUMIFS(Orders!J2:J25,Orders!G2:G25,"Delivered",Orders!B2:B25,"PJ-A")	=D24-D29
```

### Database Semantics A1:B3 — AND

```text
Delivered AND PJ-A
Status	Project
Delivered	PJ-A
```

### Database Semantics A7:A10 — disjoint OR

```text
Delivered OR Pending
Status
Delivered
Pending
```

### Database Semantics A14:B17 — overlapping OR

```text
Delivered OR PJ-A
Status	Project
Delivered
	PJ-A
```

### Database Semantics D1:G4 — AND expectations, actuals blank

```text
Metric	Expected	Actual	Difference
Amount	556
Numeric quantity count	4
Mean unit cost	25
```

### Database Semantics D7:G10 — corrected OR expectations, actuals blank

```text
Metric	Expected	Actual	Difference
Amount	1938
Numeric quantity count	18
Mean unit cost	=352/18
```

### Database Semantics D14:G17 — overlap expectations, actuals blank

```text
Metric	Expected	Actual	Difference
Amount	1902
Numeric quantity count	16
Mean unit cost	23.1875
```

### Database Semantics A21:D25 — inclusion–exclusion

```text
Population arithmetic	Amount	Count	Meaning
Delivered	=SUMIF(Orders!G2:G25,"Delivered",Orders!J2:J25)	=COUNTIF(Orders!G2:G25,"Delivered")	First set
PJ-A	=SUMIF(Orders!B2:B25,"PJ-A",Orders!J2:J25)	=COUNTIF(Orders!B2:B25,"PJ-A")	Second set
Overlap: Delivered AND PJ-A	=F2	=F3	Remove one duplicated membership
Union: Delivered OR PJ-A	=B22+B23-B24	=C22+C23-C24	One count per qualifying source row
```

### Database Semantics D28:G32 — independent source controls

```text
Disjoint status control	Source formula	Database result	Difference
Delivered plus Pending amount	=SUMIF(Orders!G2:G25,"Delivered",Orders!J2:J25)+SUMIF(Orders!G2:G25,"Pending",Orders!J2:J25)	=F8	=F29-E29
Delivered plus Pending count	=COUNTIF(Orders!G2:G25,"Delivered")+COUNTIF(Orders!G2:G25,"Pending")	=F9	=F30-E30
UnitCost sum in OR population	=SUMIF(Orders!G2:G25,"Delivered",Orders!F2:F25)+SUMIF(Orders!G2:G25,"Pending",Orders!F2:F25)	=DSUM(Orders!A1:J25,"UnitCost",A8:A10)	=F31-E31
Mean from source cost sum / count	=E31/E30	=F10	=F32-E32
```

### Database IDs A23:F26 — ID counts and amounts

```text
Population	Expected count	Actual count	Unique IDs	Sum by listed IDs	Database amount
AND	4	=COUNTA(A2:A5)	=COUNTUNIQUE(A2:A5)	=SUM(ARRAYFORMULA(SUMIF(Orders!A2:A25,A2:A5,Orders!J2:J25)))	='Database Semantics'!F2
Disjoint OR	18	=COUNTA(C2:C19)	=COUNTUNIQUE(C2:C19)	=SUM(ARRAYFORMULA(SUMIF(Orders!A2:A25,C2:C19,Orders!J2:J25)))	='Database Semantics'!F8
Overlapping OR	16	=COUNTA(E2:E17)	=COUNTUNIQUE(E2:E17)	=SUM(ARRAYFORMULA(SUMIF(Orders!A2:A25,E2:E17,Orders!J2:J25)))	='Database Semantics'!F15
```

### Database Tests A1:D5 — isolated type cases

```text
OrderID	Quantity	UnitCost	Status
T01	2	10	Delivered
T02		20	Delivered
T03	four		Delivered
T04	0	unknown	Delivered
```

### Database Tests A8:E14 — expectations before actuals

```text
Metric	Expected	Actual	Difference	Meaning
Numeric Quantity	2			Includes numeric2 and valid0; excludes blank/text
Populated Quantity	3			Nonblank count includes text four
Numeric UnitCost	2			Only numeric10 and20
Mean UnitCost	15			Two numeric costs; blank/text excluded
Numeric OrderID	0			Text IDs are not numeric values
Populated OrderID	4			Four populated text IDs
```

### Database Tests C9:D14 — six actual formulas

```text
=DCOUNT($A$1:$D$5,"Quantity",$F$1:$F$2)	=C9-B9
=DCOUNTA($A$1:$D$5,"Quantity",$F$1:$F$2)	=C10-B10
=DCOUNT($A$1:$D$5,"UnitCost",$F$1:$F$2)	=C11-B11
=DAVERAGE($A$1:$D$5,"UnitCost",$F$1:$F$2)	=C12-B12
=DCOUNT($A$1:$D$5,"OrderID",$F$1:$F$2)	=C13-B13
=DCOUNTA($A$1:$D$5,"OrderID",$F$1:$F$2)	=C14-B14
```

### Database Tests A18:A20 — correct header test

```text
Disposable header test
Status
Delivered
```

### Database Tests D18:E19 — header test formula

```text
Observed amount	Criterion requirement
=DSUM(Orders!A1:J25,"Amount",A19:A20)	Match the exact source header Status
```

### Database Tests A22:B23 — actual fault observation

```text
Header observation	Interpretation
Statuz returned0; restored Status returns1478	No visible error does not prove correct criteria
```

### Database Tests A26:D28 — weighted-price inputs

```text
Practice line	Quantity	UnitCost	Line cost
Small line	2	10	=B27*C27
Large line	8	30	=B28*C28
```

### Database Tests A31:D34 — mean interpretation checks

```text
Question	Expected	Observed	Difference
Mean price per line	20	=AVERAGE(C27:C28)	=C32-B32
Price per unit across quantities	26	=SUM(D27:D28)/SUM(B27:B28)	=C33-B33
Total line cost	260	=SUM(D27:D28)	=C34-B34
```

### Database Notes A1:B13 — corrected handover

```text
Database analysis note	Definition / evidence
Source boundary	Orders A1:J25;24baseline records; maintained values/formats preserved
Practice placement	Separate Database Analysis tab avoids existing Analysis A10:D12 work
Delivered	DSUM1478; DCOUNT Quantity12; DAVERAGE UnitCost23; text OrderID DCOUNT0 versus DCOUNTA12
AND	Status and Project on same row: Delivered AND PJ-A gives556/4/25
Disjoint OR	Status alternatives on separate rows: Delivered OR Pending gives1938/18/19.55555556
Overlapping OR	Separate Delivered row and PJ-A row:1902/16/23.1875; each matching record once
Overlap proof	Delivered1478 + PJ-A980 - overlap556 =1902; counts12+8-4=16
Source IDs	FILTER lists reconcile4/18/16 unique IDs and amounts556/1938/1902; saved views DB8 Delivered and DB8 Delivered AND PJ-A
Field types	Test table: numeric Quantity count2 includes zero; populated Quantity3 includes text; numeric UnitCost mean15 ignores blank/text
Mean meaning / header test	Two-row unweighted20 versus quantity-weighted26; Statuz criterion returned0 before Status repair1478
Validation boundary	Guided author casework; independent learner question/OR diagnosis/reviewer and60minute timing pending
Prediction repair	Initial expected mean23 was wrong: Delivered cost sum276 plus Pending76 =352 across18 numeric costs; corrected expectation352/18 matches DAVERAGE
```

### AND F2:G4

```text
=DSUM(Orders!$A$1:$J$25,"Amount",$A$2:$B$3)	=F2-E2
=DCOUNT(Orders!$A$1:$J$25,"Quantity",$A$2:$B$3)	=F3-E3
=DAVERAGE(Orders!$A$1:$J$25,"UnitCost",$A$2:$B$3)	=F4-E4
```

### Disjoint OR F8:G10

```text
=DSUM(Orders!$A$1:$J$25,"Amount",$A$8:$A$10)	=F8-E8
=DCOUNT(Orders!$A$1:$J$25,"Quantity",$A$8:$A$10)	=F9-E9
=DAVERAGE(Orders!$A$1:$J$25,"UnitCost",$A$8:$A$10)	=F10-E10
```

### Overlapping OR F15:G17

```text
=DSUM(Orders!$A$1:$J$25,"Amount",$A$15:$B$17)	=F15-E15
=DCOUNT(Orders!$A$1:$J$25,"Quantity",$A$15:$B$17)	=F16-E16
=DAVERAGE(Orders!$A$1:$J$25,"UnitCost",$A$15:$B$17)	=F17-E17
```

### Database IDs AND — A2

```text
=FILTER(Orders!A2:A25,Orders!G2:G25="Delivered",Orders!B2:B25="PJ-A")
```

### Database IDs Disjoint OR — C2

```text
=FILTER(Orders!A2:A25,((Orders!G2:G25="Delivered")+(Orders!G2:G25="Pending"))>0)
```

### Database IDs Overlapping OR — E2

```text
=FILTER(Orders!A2:A25,((Orders!G2:G25="Delivered")+(Orders!B2:B25="PJ-A"))>0)
```

### Filter views and test boundaries

Select **Orders A1:J25 > Data > Create filter view**. Save **DB8 - Delivered** after selecting Delivered in Status. Create a separate **DB8 - Delivered AND PJ-A** with both Status Delivered and Project PJ-A; its IDs are PO001/PO004/PO005/PO008. Exit the view after inspection. Do not delete excluded source rows.

Database Tests criteria are **F1:F2 = Status / Delivered**. Preserve genuine blanks B3/C4, text four/unknown and numeric zero B5 in that isolated table. DCOUNT counts numbers; DCOUNTA counts populated fields; DAVERAGE's denominator includes only numeric values of the selected field.

For the disposable header test, capture D19 with exact Status, then temporarily change A19 to Statuz. The observed result was0; restore Status and verify1478. Do not treat an error-free numeric result as proof of correct criteria.

The disjoint-OR mean is352/18 =19.55555556, not23. Final expected E10 is **=352/18**, while actual F10 remains DAVERAGE. Delivered UnitCost sum276 plus Pending76 explains the mean. Keep prediction errors distinct from formula/source defects.

Final populations: Delivered1478/12/23; Delivered AND PJ-A556/4/25; Delivered OR Pending1938/18/19.55555556; Delivered OR PJ-A1902/16/23.1875. Amount/numeric Quantity count/mean UnitCost are different metrics. Independent question, learner diagnosis and timing remain pending.
