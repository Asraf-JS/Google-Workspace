# 11 - Complete the Analysis Capstone: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

Use the exact staged inputs and formulas below. Predict each test before entering its actual calculation.


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Capstone questions: Largest Delivered amount by project; Pending records with Amount >=200 and their IDs; highest all-orders Amount by practice week. Scenario PO025: PJ-A, Planning, IT01, Quantity 2, UnitCost 45, Delivered, week 4. No actual budget or profit data is supplied.
```

## Captured Author-Run Reference

Build the isolated **GW - Sheets Advanced - Capstone** copy in guide order. Source baseline is Orders A1:K25 and Rates A1:D7. Paste only the current stage; later blocks would reveal objects not created yet. Independent reviewer/spoken work and classroom timing remain pending.

### Capstone Spec A1:B11 - define before calculating

```text
Analysis specification	Fictional training decision analysis
Source and scope	Orders A1:K25: header plus 24 records; Rates A1:D7: header plus 6 items. Amount in RM; practice weeks 1 to 4. No real purchasing data.
Question 1	Which project has the largest Delivered order amount? Sum Amount J by Project B where Status G equals Delivered; exclude Pending and Cancelled.
Question 2	Which Pending records have Amount>=200? Require both criteria and retain OrderIDs. Report zero matches explicitly if none qualify. Threshold200 is inclusive.
Question 3	Which supplied practice week has highest all-orders Amount? Sum J by numeric Week H, including Cancelled. These are practice periods, not real calendar dates.
Control expectations	Baseline 24 records; all Amount 3158; Delivered Amount 1478. Six unique item rates; source totals are not profit or approved budget.
Evidence methods	SUMIFS/COUNTIFS and qualifying-ID traces; independent native Pivot Review/source-row reconciliation; source-cell checks.
Ranking rule	Rank within the specified population. Report ties rather than claiming an unsupported unique winner.
Scenario isolation	Keep baseline analysis unchanged. PO025 scenario and lookup-key tests remain separate; label synthetic boundary fixtures.
Limits and audience	Fictional project reporting reviewer. No cost/outcome/budget approval data, so no profitability, savings, performance or purchasing approval conclusion.
Reviewer boundary	Author source challenges may be prepared; actual independent human review and 80-minute classroom timing remain unverified.
```

### Capstone Calculations A1:C9 - initial ranking

```text
Project	Delivered Amount (RM)	Delivered records
PJ-A	=SUMIFS(Orders!$J$2:$J$25,Orders!$B$2:$B$25,A2,Orders!$G$2:$G$25,"Delivered")	=COUNTIFS(Orders!$B$2:$B$25,A2,Orders!$G$2:$G$25,"Delivered")
PJ-B	=SUMIFS(Orders!$J$2:$J$25,Orders!$B$2:$B$25,A3,Orders!$G$2:$G$25,"Delivered")	=COUNTIFS(Orders!$B$2:$B$25,A3,Orders!$G$2:$G$25,"Delivered")
PJ-C	=SUMIFS(Orders!$J$2:$J$25,Orders!$B$2:$B$25,A4,Orders!$G$2:$G$25,"Delivered")	=COUNTIFS(Orders!$B$2:$B$25,A4,Orders!$G$2:$G$25,"Delivered")
Total Delivered	=SUM(B2:B4)	=SUM(C2:C4)

Ranking	Project	Amount (RM)
Largest Delivered	=INDEX(A2:A4,MATCH(MAX(B2:B4),B2:B4,0))	=MAX(B2:B4)
Number tied at maximum	=COUNTIF(B2:B4,MAX(B2:B4))
```

### Capstone Calculations A11:B14 - actual Pending exceptions

```text
Pending exception test	Baseline result
Matching record count	=COUNTIFS(Orders!$G$2:$G$25,"Pending",Orders!$J$2:$J$25,">=200")
Matching amount (RM)	=SUMIFS(Orders!$J$2:$J$25,Orders!$G$2:$G$25,"Pending",Orders!$J$2:$J$25,">=200")
Qualifying OrderIDs	=IFNA(FILTER(Orders!A2:A25,Orders!G2:G25="Pending",Orders!J2:J25>=200),"No qualifying baseline records")
```

### Capstone Trace A1:C2 - baseline spill formula

```text
Delivered leader OrderID	Project	Amount (RM)
=FILTER({Orders!A2:A25,Orders!B2:B25,Orders!J2:J25},Orders!G2:G25="Delivered",Orders!B2:B25='Capstone Calculations'!B8)
```

### Capstone Calculations D1:E5 - native pivot comparison

```text
Native pivot (RM)	Difference
='Pivot Review'!C3	=B2-D2
='Pivot Review'!C4	=B3-D3
='Pivot Review'!C5	=B4-D4
='Pivot Review'!C6	=B5-D5
```

### Capstone Calculations A18:D22 - baseline controls

```text
Baseline controls	Calculation	Independent control	Difference
All Amount	=SUM(Orders!J2:J25)	='Pivot Review'!E6	=B19-C19
Delivered Amount	=B5	='Pivot Review'!C6	=B20-C20
Record count	=COUNTA(Orders!A2:A25)	='Pivot Counts'!E6	=B21-C21
Rate key count	=COUNTUNIQUE(Rates!A2:A7)	=COUNTA(Rates!A2:A7)	=B22-C22
```

### Capstone Tests A1:E2 - actual nonqualifier

```text
Baseline OrderID	Status	Amount (RM)	Amount>=200	Both criteria
=Orders!A11	=Orders!G11	=Orders!J11	=C2>=200	=AND(B2="Pending",C2>=200)
```

### Capstone Tests A6:D10 - predict synthetic outcomes first

```text
Synthetic case only	Status	Amount (RM)	Expected qualifies
Below threshold	Pending	199.99	False
At threshold	Pending	200	True
Above threshold	Pending	250	True
Wrong status	Delivered	250	False
```

### Capstone Tests E6:E10 - actual boundary tests afterward

```text
Actual qualifies
=AND(B7="Pending",C7>=200)
=AND(B8="Pending",C8>=200)
=AND(B9="Pending",C9>=200)
=AND(B10="Pending",C10>=200)
```

### Capstone Tests A13:D15 - synthetic controls

```text
Synthetic control	Actual	Expected	Difference
Qualifying records	=COUNTIF(E7:E10,TRUE)	2	=B14-C14
Qualifying amount (RM)	=SUMIFS(C7:C10,B7:B10,"Pending",C7:C10,">=200")	450	=B15-C15
```

### Capstone Key Test A8:D8 - conflicting fixture after duplicating Rates

```text
IT01	Conflicting training fixture	99	Equipment
```

### Capstone Key Test F1:J4 - guarded lookup tests

```text
Test key	Match count	Raw exact lookup	Guarded rate	Disposition
IT01	=COUNTIF($A$2:$A$8,F2)	=IFNA(VLOOKUP(F2,$A$2:$D$8,3,FALSE),"Missing rate")	=IF(G2<>1,"Review key",VLOOKUP(F2,$A$2:$D$8,3,FALSE))	=IF(G2=1,"Use mapped rate",IF(G2=0,"Missing mapping","Duplicate/conflict"))
IT99	=COUNTIF($A$2:$A$8,F3)	=IFNA(VLOOKUP(F3,$A$2:$D$8,3,FALSE),"Missing rate")	=IF(G3<>1,"Review key",VLOOKUP(F3,$A$2:$D$8,3,FALSE))	=IF(G3=1,"Use mapped rate",IF(G3=0,"Missing mapping","Duplicate/conflict"))
IT02	=COUNTIF($A$2:$A$8,F4)	=IFNA(VLOOKUP(F4,$A$2:$D$8,3,FALSE),"Missing rate")	=IF(G4<>1,"Review key",VLOOKUP(F4,$A$2:$D$8,3,FALSE))	=IF(G4=1,"Use mapped rate",IF(G4=0,"Missing mapping","Duplicate/conflict"))
```

### Capstone Key Test F7:F10 - observed first-match test notes

```text
Fixture only: baseline Rates and Orders unchanged.
Reversing conflicting IT01 rates changed the raw lookup from 45 to 99.
Match count stayed 2; the guarded result remained Review key.
Fixture order restored 45 then 99. Keep the conflict visible for resolution; do not choose a rate automatically.
```

### Capstone Calculations A25:D31 - chronological baseline weeks

```text
Practice week	All Amount (RM)	Independent weekly control	Difference
1	=SUMIFS(Orders!$J$2:$J$25,Orders!$H$2:$H$25,A26)	='Dashboard Data'!B16	=B26-C26
2	=SUMIFS(Orders!$J$2:$J$25,Orders!$H$2:$H$25,A27)	='Dashboard Data'!C16	=B27-C27
3	=SUMIFS(Orders!$J$2:$J$25,Orders!$H$2:$H$25,A28)	='Dashboard Data'!D16	=B28-C28
4	=SUMIFS(Orders!$J$2:$J$25,Orders!$H$2:$H$25,A29)	='Dashboard Data'!E16	=B29-C29
Weekly total	=SUM(B26:B29)	=B19	=B30-C30
Largest week	=INDEX(A26:A29,MATCH(MAX(B26:B29),B26:B29,0))	=MAX(B26:B29)
```

### Capstone Executive A1:D21 - baseline output

```text
Procurement capstone - baseline

Delivered-only comparison	Amount (RM)	Records
='Capstone Calculations'!A2	='Capstone Calculations'!B2	='Capstone Calculations'!C2
='Capstone Calculations'!A3	='Capstone Calculations'!B3	='Capstone Calculations'!C3
='Capstone Calculations'!A4	='Capstone Calculations'!B4	='Capstone Calculations'!C4


Audience question	Answer	Amount (RM)
Largest Delivered project	='Capstone Calculations'!B8	='Capstone Calculations'!C8
Pending records >=200	='Capstone Calculations'!B12	='Capstone Calculations'!B13
Highest practice week	='Capstone Calculations'!B31	='Capstone Calculations'!C31

Population controls	Value		Live checks
All Amount (RM)	='Capstone Calculations'!B19		=IF(AND(COUNTIF('Capstone Calculations'!E2:E5,0)=4,COUNTIF('Capstone Calculations'!D19:D22,0)=4,COUNTIF('Capstone Calculations'!D26:D30,0)=5),"All baseline checks pass","Review mismatch")
Delivered Amount (RM)	='Capstone Calculations'!B5
All record count	='Capstone Calculations'!B21

Source population	24 fictional Orders, rows 2:25. RM. All-orders includes Cancelled; Delivered comparison excludes Pending and Cancelled.
Interpretation limit	Order amount is not profit, efficiency, savings or budget approval. No outcome/cost evidence supports those conclusions.
Future refresh	Extend source/formula/pivot/visual bounds for new records; check qualifying IDs and weekly totals. Keep scenario results separate.
```

### PO025 Plan A1:B9 - write predictions before adding source row

```text
PO025 scenario plan	Predictions before adding the new source record
Isolation	Duplicate Orders as PO025 Orders. Keep baseline Orders, Capstone Calculations and Capstone Executive unchanged. Use separate scenario analysis/results.
Exact scenario record	PO025; PJ-A; Planning; IT01; Quantity 2; UnitCost 45; Delivered; practice week 4. New Amount 90 and ActiveAmount 90.
Baseline comparison	Delivered projects 556/578/344: PJ-B578 leads. All-week totals 728/754/850/826: week 3 at 850 leads.
Predicted new totals	25 records; all Amount 3248; Delivered 1568; Active 2028. Pending>=200 remains 0 matches.
Predicted ranking	PJ-A Delivered 646 becomes largest, ahead of PJ-B578/PJ-C344. Week 4 becomes 916 and exceeds week 3 at 850.
Coverage and controls	Add row 26 before copied totals. Check all relevant source/formula bounds 2:26; reconcile source totals, project sums, ID traces and practice weeks.
Interpretation	An extra fictional Delivered order changes the descriptive ranking, not profit, efficiency or a purchasing approval decision.
Review boundary	Author source challenges will be documented; independent human reviewer and spoken recommendation remain pending.
```

### PO025 Orders A26:K26 - insert a row above 26 first

```text
PO025	PJ-A	Planning	IT01	2	45	Delivered	4	Capstone PO025 scenario - fictional	=E26*F26	=IF(G26="Cancelled",0,J26)
```

### PO025 Orders J27:K28 - repaired scenario totals

```text
Scenario All Amount	Scenario Active Amount
=SUM(J2:J26)	=SUM(K2:K26)
```

### PO025 Analysis A1:F6 - expanded coverage after stale-bound test

```text
Scenario coverage	Expanded result	Baseline control	Delta vs baseline	Expected delta	Difference
All Amount (RM)	=SUM('PO025 Orders'!J2:J26)	='Capstone Calculations'!B19	=B2-C2	90	=D2-E2
Delivered Amount (RM)	=SUMIF('PO025 Orders'!G2:G26,"Delivered",'PO025 Orders'!J2:J26)	='Capstone Calculations'!B5	=B3-C3	90	=D3-E3
Active Amount (RM)	=SUM('PO025 Orders'!K2:K26)	=Analysis!C15	=B4-C4	90	=D4-E4
Record count	=COUNTA('PO025 Orders'!A2:A26)	='Capstone Calculations'!B21	=B5-C5	1	=D5-E5
Week 4 all Amount (RM)	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26,4)	='Capstone Calculations'!B29	=B6-C6	90	=D6-E6
```

### PO025 Analysis A9:E13 - scenario projects

```text
Project	Scenario Delivered	Baseline Delivered	Delta	Independent ID sum
PJ-A	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!B2:B26,A10,'PO025 Orders'!G2:G26,"Delivered")	='Capstone Calculations'!B2	=B10-C10	=SUM(FILTER('PO025 Orders'!J2:J26,'PO025 Orders'!G2:G26="Delivered",'PO025 Orders'!B2:B26=A10))
PJ-B	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!B2:B26,A11,'PO025 Orders'!G2:G26,"Delivered")	='Capstone Calculations'!B3	=B11-C11	=SUM(FILTER('PO025 Orders'!J2:J26,'PO025 Orders'!G2:G26="Delivered",'PO025 Orders'!B2:B26=A11))
PJ-C	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!B2:B26,A12,'PO025 Orders'!G2:G26,"Delivered")	='Capstone Calculations'!B4	=B12-C12	=SUM(FILTER('PO025 Orders'!J2:J26,'PO025 Orders'!G2:G26="Delivered",'PO025 Orders'!B2:B26=A12))
Delivered total	=SUM(B10:B12)	=SUM(C10:C12)	=B13-C13	=SUM(E10:E12)
```

### PO025 Analysis A16:E20 - scenario weeks

```text
Practice week	Scenario all Amount	Baseline all Amount	Delta	Independent ID sum
1	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26,A17)	='Capstone Calculations'!B26	=B17-C17	=SUM(FILTER('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26=A17))
2	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26,A18)	='Capstone Calculations'!B27	=B18-C18	=SUM(FILTER('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26=A18))
3	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26,A19)	='Capstone Calculations'!B28	=B19-C19	=SUM(FILTER('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26=A19))
4	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26,A20)	='Capstone Calculations'!B29	=B20-C20	=SUM(FILTER('PO025 Orders'!J2:J26,'PO025 Orders'!H2:H26=A20))
```

### PO025 Analysis A23:C29 - ranking and exception controls

```text
Scenario ranking	Answer	Amount RM
Delivered project leader	=INDEX(A10:A12,MATCH(MAX(B10:B12),B10:B12,0))	=MAX(B10:B12)
Highest practice week	=INDEX(A17:A20,MATCH(MAX(B17:B20),B17:B20,0))	=MAX(B17:B20)

Pending >=200 count	=COUNTIFS('PO025 Orders'!G2:G26,"Pending",'PO025 Orders'!J2:J26,">=200")
Pending >=200 Amount	=SUMIFS('PO025 Orders'!J2:J26,'PO025 Orders'!G2:G26,"Pending",'PO025 Orders'!J2:J26,">=200")
Unique order IDs	=COUNTUNIQUE('PO025 Orders'!A2:A26)
```

### Capstone Trace E1:G2 - scenario source-ID spill

```text
Scenario leader OrderID	Project	Amount RM
=FILTER({'PO025 Orders'!A2:A26,'PO025 Orders'!B2:B26,'PO025 Orders'!J2:J26},'PO025 Orders'!G2:G26="Delivered",'PO025 Orders'!B2:B26='PO025 Analysis'!B24)
```

### Capstone Trace E8:H10 - scenario trace controls

```text
Scenario trace control	Actual	Expected	Difference
Delivered leader total	=SUM(G2:G6)	='PO025 Analysis'!C24	=F9-G9
Delivered leader count	=COUNTA(E2:E6)	5	=F10-G10
```

### PO025 Comparison A1:D17 - executive comparison

```text
Procurement capstone scenario comparison	Baseline	PO025 scenario	Change
All-order Amount (RM)	='Capstone Calculations'!B19	='PO025 Analysis'!B2	=C2-B2
Delivered Amount (RM)	='Capstone Calculations'!B5	='PO025 Analysis'!B3	=C3-B3
Active Amount (RM)	=Analysis!C15	='PO025 Analysis'!B4	=C4-B4
Order count	='Capstone Calculations'!B21	='PO025 Analysis'!B5	=C5-B5
Delivered project leader	='Capstone Calculations'!B8	='PO025 Analysis'!B24	PJ-B to PJ-A
Leader Delivered Amount (RM)	='Capstone Calculations'!C8	='PO025 Analysis'!C24	Different project populations
Highest practice week	='Capstone Calculations'!B31	='PO025 Analysis'!B25	Week 3 to week 4
Largest week all Amount (RM)	='Capstone Calculations'!C31	='PO025 Analysis'!C25	Different week populations
Pending >=200 record count	='Capstone Calculations'!B12	='PO025 Analysis'!B27	=C10-B10
Pending >=200 Amount (RM)	='Capstone Calculations'!B13	='PO025 Analysis'!B28	=C11-B11
Expanded range checks	Baseline preserved	=IF(COUNTIF('PO025 Analysis'!F2:F6,0)=5,"All scenario checks pass","Review mismatch")	Row 26 included

Source populations	Baseline Orders A1:K25; scenario PO025 Orders A1:K26. Delivered uses Status=Delivered; weekly/all totals include Cancelled.
Interpretation limit	Fictional order Amount is not profit, savings, budget approval or evidence of project performance.
Refresh contract	Include row 26 in scenario source, project, weekly, trace and control ranges; baseline remains 24 orders.
Review status	Author-prepared source challenge only. Independent reviewer, spoken delivery and learner timing remain pending.
```

### Capstone Audit A1:B19 - final audit, add scenario observations only after testing

```text
Audit appendix - baseline	Evidence, assumptions and boundaries
Source bounds	Orders A1:K25,24 fictional records; Rates A1:D7,6 unique item keys. Source values and baseline totals are preserved.
Question populations	Delivered-only project ranking; Pending AND Amount>=200 exception IDs; all-status Amount by numeric practice week.
Baseline answers	PJ-B Delivered 578; no qualifying Pending IDs/count 0/amount 0; practice week 3 highest all-orders amount 850.
Independent reconciliation	New SUMIFS totals 556/578/344 match native Pivot Review Delivered cellsC3:C5. Delivered 1478 and all 3158 reconcile to pivot/source controls.
Source trace	Capstone Trace retains PJ-B Delivered PO009/PO012/PO013/PO016 with amounts 240/32/270/36, sum 578.
Zero-match proof	Source PO010 is Pending 180 and does not meet>=200. Separate synthetic Pending 200 and 250 qualify; synthetic figures are excluded from baseline answers.
Lookup assumptions	Exact matching requires one authorised rate per key. Disposable duplicateIT01 and missingIT99 tests return Review key rather than forcing a price.
First-match effect	Reversing the two conflicting fixture rates changes raw VLOOKUP45->99; match count stays 2 and guarded result stays Review key. Fixture order restored.
Interpretation limits	No actual budget/profit/cost-outcome evidence. Order amount alone does not establish profitability, savings, project performance or purchasing approval.
Refresh contract	New records require explicit source/formula/pivot/visual bounds, qualifying-ID traces and weekly reconciliation. Check outputs after extension rather than relying on old baseline expectations.
PO025 scenario observed	Separate PO025 Orders A1:K26: 25 records, all 3248, active 2028, Delivered 1568. PJ-A646 leads; week 4 reaches 916 and leads. Baseline unchanged.
Review status	Author evidence prepared. No independent human reviewer, spoken recommendation or 80-minute learner pilot has been completed.

Author challenge - baseline leader	Why PJ-B? PO009/012/013/016 contribute240+32+270+36=578; SUMIFS and native Pivot Review both give 578.
Author challenge - genuine zero	Pending>=200 has 0 baseline records. PO010 isPending180 and fails; separate synthetic Pending 200 qualifies, while Delivered 250 fails.
Author challenge - week shift	Baseline week 4 is 826; PO025 adds 90:916>week 3 850. Expanded SUMIFS and SUM(FILTER) agree; source includes row 26.
Scenario trace	PJ-A orders PO001/004/005/008/025 contribute90+144+250+72+90=646. Compare separately with unchanged baseline leader 578.
Human review still pending	These are author-prepared source challenge responses. No independent reviewer or spoken delivery was performed; 80-minute classroom target is unmeasured.
```

### Intermediate experiments - do these in order

Before PO025 is added, build PO025 Analysis A1:D6 with the same final controls but source bounds ending at 25, labels Original bound result and Difference, and no expected-scenario delta columns. Baseline results 3158/1478/1938/24/826. After inserting row 26, inspect these unchanged ranges before expanding to 26. They still match the old baseline while omitting PO025. Only then paste the expanded control block and expected deltas 90/90/90/1/90.

On the duplicated Capstone Key Test only, reverse conflicting IT01 values C2=99 and C8=45 after recording initial 45. Raw H2 changes 99; guarded I2 stays Review key. Then restore C2=45 and C8=99. Keep the conflict labelled; do not repair actual Rates automatically.

For the baseline audit at 11.3, write rows 1:13 with row 12 describing the planned isolated PO025 test. After actual scenario testing, update row 12 to observed results and add the author-prepared challenge responses at 15:19. These are not evidence of an independent human review.

Baseline Delivered leader PJ-B 578 has IDs PO009/012/013/016. Scenario leader PJ-A 646 has PO001/004/005/008/025. Weekly source includes Cancelled: baseline 728/754/850/826; scenario 728/754/850/916. Amount is not profit, savings or approval. A tie needs explicit handling rather than choosing the first INDEX/MATCH result.
