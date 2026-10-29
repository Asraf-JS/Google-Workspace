# 02 - Build Conditional Calculations: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Amount
```

```text
=E2*F2
```

```text
ActiveAmount
```

```text
=IF(G2="Cancelled",0,J2)
```

```text
=SUMIFS(Orders!$J$2:$J$25,Orders!$B$2:$B$25,$A4,Orders!$G$2:$G$25,B$3)
```

```text
=IF(F2<100,"Low",IF(F2<200,"Medium","High"))
```

## Part 2: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Logic matrix must cover below/on/above thresholds, zero quantity, Delivered, Pending and Cancelled. Practice bands: Low <100; Medium 100 to <200; High >=200. Exception: Pending AND Amount >=200. These are training rules, not procurement policy.
```

## Part 3: Captured Conditional-Calculation Reference

Preserve the supplied K1 fictional-data label in M1 before using K for ActiveAmount. Original A:I inputs, Rates, Source Snapshot and intake audit remain intact. J2=E2*F2 and K2=IF(G2="Cancelled",0,J2), filled to 25; source totals 3158 and 1938. Spot checks J2/J13/J25 are 90/32/64.

Amount grid B4:D6:556/64/360;578/276/350;344/120/510. D6 uses $A6 and D$3. Count grid B9:D11:4/2/2 for each project. B9 seed:

```text
=COUNTIFS(Orders!$B$2:$B$25,$A9,Orders!$G$2:$G$25,B$8)
```

### Population control card — Analysis A13:D18

Write each population definition before calculating the final two columns.

```text
Population	Definition	Amount (RM)	Record count
All orders	All 24 supplied order lines; include every status.	=SUM(Orders!J2:J25)	=COUNTA(Orders!A2:A25)
Active	Delivered and Pending; exclude Cancelled from ActiveAmount only.	=SUM(Orders!K2:K25)	=COUNTIF(Orders!G2:G25,"<>Cancelled")
Delivered only	Only the Delivered status; excludes Pending and Cancelled.	=SUMIF(Orders!G2:G25,"Delivered",Orders!J2:J25)	=COUNTIF(Orders!G2:G25,"Delivered")
Cancelled	Valid source lines retained; not active for this question.	=SUMIF(Orders!G2:G25,"Cancelled",Orders!J2:J25)	=COUNTIF(Orders!G2:G25,"Cancelled")
Pending	Only Pending, regardless of amount.	=SUMIF(Orders!G2:G25,"Pending",Orders!J2:J25)	=COUNTIF(Orders!G2:G25,"Pending")
```

### Reconciliation card — Analysis A21:D26

```text
Check	Summary	Source	Difference
Amount grid	=SUM(B4:D6)	=C14	=B22-C22
Count grid	=SUM(B9:D11)	=D14	=B23-C23
Active = Delivered + Pending	=C16+C18	=C15	=B24-C24
All = Active + Cancelled	=C15+C17	=C14	=B25-C25
Status population	=SUM(D16:D18)	=D14	=B26-C26
```

B28 baseline check **=COUNTIFS(Orders!G2:G25,"Pending",Orders!J2:J25,">=200")** gives 0. All 3158/24, Active 1938/18, Delivered 1478/12, Cancelled 1220/6, Pending 460/6. Every reconciliation difference 0.

### Manual subset inputs — Subset Checks A1:H7

Record the six manually checked products before G/H formula comparisons. Inputs match the named source OrderIDs; all amounts use training RM.

```text
Project	Status	OrderID	Quantity	UnitCost	Manual Amount	Formula Amount	Difference
PJ-A	Delivered	PO001	2	45	90
PJ-A	Delivered	PO004	8	18	144
PJ-A	Delivered	PO005	10	25	250
PJ-A	Delivered	PO008	6	12	72
PJ-B	Pending	PO010	10	18	180
PJ-B	Pending	PO014	8	12	96
```

G2 **=D2*E2**, H2 **=G2-F2**, fill to 7. The two subsets total 556 and 276; their counts 4 and 2 also match the maintained grids.

### Logic matrix input/expectations — Logic Tests A1:J22

Actual columns G/I/J are deliberately empty on this input card. D calculates Quantity times a known UnitCost. Zero Quantity is numeric 0; it is not an unresolved rate lookup. Expected flags are Boolean TRUE/FALSE.

```text
TestID	Quantity	UnitCost	Amount	Status	Expected band	Actual band	Expected flag	Actual flag	Pass
LT01	0	100	=B2*C2	Delivered	Low		FALSE
LT02	0	100	=B3*C3	Pending	Low		FALSE
LT03	0	100	=B4*C4	Cancelled	Low		FALSE
LT04	1	99	=B5*C5	Delivered	Low		FALSE
LT05	1	99	=B6*C6	Pending	Low		FALSE
LT06	1	99	=B7*C7	Cancelled	Low		FALSE
LT07	1	100	=B8*C8	Delivered	Medium		FALSE
LT08	1	100	=B9*C9	Pending	Medium		FALSE
LT09	1	100	=B10*C10	Cancelled	Medium		FALSE
LT10	1	101	=B11*C11	Delivered	Medium		FALSE
LT11	1	101	=B12*C12	Pending	Medium		FALSE
LT12	1	101	=B13*C13	Cancelled	Medium		FALSE
LT13	1	199	=B14*C14	Delivered	Medium		FALSE
LT14	1	199	=B15*C15	Pending	Medium		FALSE
LT15	1	199	=B16*C16	Cancelled	Medium		FALSE
LT16	1	200	=B17*C17	Delivered	High		FALSE
LT17	1	200	=B18*C18	Pending	High		TRUE
LT18	1	200	=B19*C19	Cancelled	High		FALSE
LT19	1	201	=B20*C20	Delivered	High		FALSE
LT20	1	201	=B21*C21	Pending	High		TRUE
LT21	1	201	=B22*C22	Cancelled	High		FALSE
```

G2 **=IF(D2<100,"Low",IF(D2<200,"Medium","High"))**; I2 **=AND(E2="Pending",D2>=200)**; J2 **=AND(F2=G2,H2=I2)**. Fill each to 22. Expected 21 passes/0 mismatches, 2 positive flags, 3 zero-quantitycases, 6High/9Medium/6Low. Synthetic Pending 200/201 exercise the positive flag branch; baseline remains 0.

### Repaired mixed-reference scenario

Duplicate Analysis as Mixed Reference Tests. On that copy only, remove the column anchor from B4's $A4 criterion, then refill across/down. C4 incorrectly uses B4 as project criterion and gives 0; total 1478, discrepancy-1680 from 3158. Restore $A4 and refill: grid 3158, difference 0; D6 uses $A6 and D$3. The actual fault snapshot was retained before repair. The maintained Analysis grid was never damaged.

Independent project threshold summary, filtered-source reconciliation, threshold 250 change/restoration and reviewer/learner-timing checks remain pending. Practice bands and flags are fictional training rules, not procurement policy.
