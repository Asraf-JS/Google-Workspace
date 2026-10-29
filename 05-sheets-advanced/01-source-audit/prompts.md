# 01 - Audit the Source Register: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
GW - Sheets Advanced - Analysis
```

```text
Source Snapshot
```

```text
Analysis
```

## Part 2: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Separate intake anomalies: duplicate PO001 with changed quantity; missing OrderID; ItemCode IT99; Quantity “four”; valid zero quantity; valid Cancelled status. Do not inject these into Orders. Other fields can be copied from a source row only in Audit Intake and labelled as practice.
```

## Part 3: Captured Source-Audit Reference

The supplied source has 24 unique OrderIDs PO001–PO024, six unique Rates keys IT01–IT06, Quantity total 140 and unit-price checksum552 (not spend). All 24 Quantity/UnitCost/Week entries are numeric, all 24 item keys map, statuses are 12 Delivered/6 Pending/6 Cancelled. Source tables retain their supplied values and formats; Analysis is empty. Manual upload handoff was required; native conversion and audit were executed in the application.

### Baseline row diagnostics — Audit Checks A1:G25

Paste this bounded card into the named diagnostic tab, not Orders. It supplies the exact formulas observed in the author run; inspect representative formulas and explain the anchored population.

```text
OrderID	ID occurrences	Qty numeric	Cost numeric	Item key matches	Allowed status	Week numeric
=Orders!A2	=COUNTIF(Orders!$A$2:$A$25,A2)	=ISNUMBER(Orders!E2)	=ISNUMBER(Orders!F2)	=COUNTIF(Rates!$A$2:$A$7,Orders!D2)	=OR(Orders!G2="Delivered",Orders!G2="Pending",Orders!G2="Cancelled")	=ISNUMBER(Orders!H2)
=Orders!A3	=COUNTIF(Orders!$A$2:$A$25,A3)	=ISNUMBER(Orders!E3)	=ISNUMBER(Orders!F3)	=COUNTIF(Rates!$A$2:$A$7,Orders!D3)	=OR(Orders!G3="Delivered",Orders!G3="Pending",Orders!G3="Cancelled")	=ISNUMBER(Orders!H3)
=Orders!A4	=COUNTIF(Orders!$A$2:$A$25,A4)	=ISNUMBER(Orders!E4)	=ISNUMBER(Orders!F4)	=COUNTIF(Rates!$A$2:$A$7,Orders!D4)	=OR(Orders!G4="Delivered",Orders!G4="Pending",Orders!G4="Cancelled")	=ISNUMBER(Orders!H4)
=Orders!A5	=COUNTIF(Orders!$A$2:$A$25,A5)	=ISNUMBER(Orders!E5)	=ISNUMBER(Orders!F5)	=COUNTIF(Rates!$A$2:$A$7,Orders!D5)	=OR(Orders!G5="Delivered",Orders!G5="Pending",Orders!G5="Cancelled")	=ISNUMBER(Orders!H5)
=Orders!A6	=COUNTIF(Orders!$A$2:$A$25,A6)	=ISNUMBER(Orders!E6)	=ISNUMBER(Orders!F6)	=COUNTIF(Rates!$A$2:$A$7,Orders!D6)	=OR(Orders!G6="Delivered",Orders!G6="Pending",Orders!G6="Cancelled")	=ISNUMBER(Orders!H6)
=Orders!A7	=COUNTIF(Orders!$A$2:$A$25,A7)	=ISNUMBER(Orders!E7)	=ISNUMBER(Orders!F7)	=COUNTIF(Rates!$A$2:$A$7,Orders!D7)	=OR(Orders!G7="Delivered",Orders!G7="Pending",Orders!G7="Cancelled")	=ISNUMBER(Orders!H7)
=Orders!A8	=COUNTIF(Orders!$A$2:$A$25,A8)	=ISNUMBER(Orders!E8)	=ISNUMBER(Orders!F8)	=COUNTIF(Rates!$A$2:$A$7,Orders!D8)	=OR(Orders!G8="Delivered",Orders!G8="Pending",Orders!G8="Cancelled")	=ISNUMBER(Orders!H8)
=Orders!A9	=COUNTIF(Orders!$A$2:$A$25,A9)	=ISNUMBER(Orders!E9)	=ISNUMBER(Orders!F9)	=COUNTIF(Rates!$A$2:$A$7,Orders!D9)	=OR(Orders!G9="Delivered",Orders!G9="Pending",Orders!G9="Cancelled")	=ISNUMBER(Orders!H9)
=Orders!A10	=COUNTIF(Orders!$A$2:$A$25,A10)	=ISNUMBER(Orders!E10)	=ISNUMBER(Orders!F10)	=COUNTIF(Rates!$A$2:$A$7,Orders!D10)	=OR(Orders!G10="Delivered",Orders!G10="Pending",Orders!G10="Cancelled")	=ISNUMBER(Orders!H10)
=Orders!A11	=COUNTIF(Orders!$A$2:$A$25,A11)	=ISNUMBER(Orders!E11)	=ISNUMBER(Orders!F11)	=COUNTIF(Rates!$A$2:$A$7,Orders!D11)	=OR(Orders!G11="Delivered",Orders!G11="Pending",Orders!G11="Cancelled")	=ISNUMBER(Orders!H11)
=Orders!A12	=COUNTIF(Orders!$A$2:$A$25,A12)	=ISNUMBER(Orders!E12)	=ISNUMBER(Orders!F12)	=COUNTIF(Rates!$A$2:$A$7,Orders!D12)	=OR(Orders!G12="Delivered",Orders!G12="Pending",Orders!G12="Cancelled")	=ISNUMBER(Orders!H12)
=Orders!A13	=COUNTIF(Orders!$A$2:$A$25,A13)	=ISNUMBER(Orders!E13)	=ISNUMBER(Orders!F13)	=COUNTIF(Rates!$A$2:$A$7,Orders!D13)	=OR(Orders!G13="Delivered",Orders!G13="Pending",Orders!G13="Cancelled")	=ISNUMBER(Orders!H13)
=Orders!A14	=COUNTIF(Orders!$A$2:$A$25,A14)	=ISNUMBER(Orders!E14)	=ISNUMBER(Orders!F14)	=COUNTIF(Rates!$A$2:$A$7,Orders!D14)	=OR(Orders!G14="Delivered",Orders!G14="Pending",Orders!G14="Cancelled")	=ISNUMBER(Orders!H14)
=Orders!A15	=COUNTIF(Orders!$A$2:$A$25,A15)	=ISNUMBER(Orders!E15)	=ISNUMBER(Orders!F15)	=COUNTIF(Rates!$A$2:$A$7,Orders!D15)	=OR(Orders!G15="Delivered",Orders!G15="Pending",Orders!G15="Cancelled")	=ISNUMBER(Orders!H15)
=Orders!A16	=COUNTIF(Orders!$A$2:$A$25,A16)	=ISNUMBER(Orders!E16)	=ISNUMBER(Orders!F16)	=COUNTIF(Rates!$A$2:$A$7,Orders!D16)	=OR(Orders!G16="Delivered",Orders!G16="Pending",Orders!G16="Cancelled")	=ISNUMBER(Orders!H16)
=Orders!A17	=COUNTIF(Orders!$A$2:$A$25,A17)	=ISNUMBER(Orders!E17)	=ISNUMBER(Orders!F17)	=COUNTIF(Rates!$A$2:$A$7,Orders!D17)	=OR(Orders!G17="Delivered",Orders!G17="Pending",Orders!G17="Cancelled")	=ISNUMBER(Orders!H17)
=Orders!A18	=COUNTIF(Orders!$A$2:$A$25,A18)	=ISNUMBER(Orders!E18)	=ISNUMBER(Orders!F18)	=COUNTIF(Rates!$A$2:$A$7,Orders!D18)	=OR(Orders!G18="Delivered",Orders!G18="Pending",Orders!G18="Cancelled")	=ISNUMBER(Orders!H18)
=Orders!A19	=COUNTIF(Orders!$A$2:$A$25,A19)	=ISNUMBER(Orders!E19)	=ISNUMBER(Orders!F19)	=COUNTIF(Rates!$A$2:$A$7,Orders!D19)	=OR(Orders!G19="Delivered",Orders!G19="Pending",Orders!G19="Cancelled")	=ISNUMBER(Orders!H19)
=Orders!A20	=COUNTIF(Orders!$A$2:$A$25,A20)	=ISNUMBER(Orders!E20)	=ISNUMBER(Orders!F20)	=COUNTIF(Rates!$A$2:$A$7,Orders!D20)	=OR(Orders!G20="Delivered",Orders!G20="Pending",Orders!G20="Cancelled")	=ISNUMBER(Orders!H20)
=Orders!A21	=COUNTIF(Orders!$A$2:$A$25,A21)	=ISNUMBER(Orders!E21)	=ISNUMBER(Orders!F21)	=COUNTIF(Rates!$A$2:$A$7,Orders!D21)	=OR(Orders!G21="Delivered",Orders!G21="Pending",Orders!G21="Cancelled")	=ISNUMBER(Orders!H21)
=Orders!A22	=COUNTIF(Orders!$A$2:$A$25,A22)	=ISNUMBER(Orders!E22)	=ISNUMBER(Orders!F22)	=COUNTIF(Rates!$A$2:$A$7,Orders!D22)	=OR(Orders!G22="Delivered",Orders!G22="Pending",Orders!G22="Cancelled")	=ISNUMBER(Orders!H22)
=Orders!A23	=COUNTIF(Orders!$A$2:$A$25,A23)	=ISNUMBER(Orders!E23)	=ISNUMBER(Orders!F23)	=COUNTIF(Rates!$A$2:$A$7,Orders!D23)	=OR(Orders!G23="Delivered",Orders!G23="Pending",Orders!G23="Cancelled")	=ISNUMBER(Orders!H23)
=Orders!A24	=COUNTIF(Orders!$A$2:$A$25,A24)	=ISNUMBER(Orders!E24)	=ISNUMBER(Orders!F24)	=COUNTIF(Rates!$A$2:$A$7,Orders!D24)	=OR(Orders!G24="Delivered",Orders!G24="Pending",Orders!G24="Cancelled")	=ISNUMBER(Orders!H24)
=Orders!A25	=COUNTIF(Orders!$A$2:$A$25,A25)	=ISNUMBER(Orders!E25)	=ISNUMBER(Orders!F25)	=COUNTIF(Rates!$A$2:$A$7,Orders!D25)	=OR(Orders!G25="Delivered",Orders!G25="Pending",Orders!G25="Cancelled")	=ISNUMBER(Orders!H25)
```

### Baseline controls — Audit Checks A28:B48

```text
Baseline check	Observed
Source rows	=COUNTA(Orders!A2:A25)
Unique OrderIDs	=COUNTUNIQUE(Orders!A2:A25)
Blank OrderIDs	=COUNTBLANK(Orders!A2:A25)
Non-unique ID rows	=COUNTIF(B2:B25,">1")
Numeric Quantity	=COUNT(Orders!E2:E25)
Numeric UnitCost	=COUNT(Orders!F2:F25)
Valid item mappings	=COUNTIF(E2:E25,1)
Allowed status rows	=COUNTIF(F2:F25,TRUE)
Numeric Week index	=COUNT(Orders!H2:H25)
Quantity total	=SUM(Orders!E2:E25)
UnitCost sum (not spend)	=SUM(Orders!F2:F25)
Delivered records	=COUNTIF(Orders!G2:G25,"Delivered")
Pending records	=COUNTIF(Orders!G2:G25,"Pending")
Cancelled records	=COUNTIF(Orders!G2:G25,"Cancelled")
Status population	=SUM(B40:B42)
Rates keys	=COUNTA(Rates!A2:A7)
Unique Rates keys	=COUNTUNIQUE(Rates!A2:A7)
Blank Rates keys	=COUNTBLANK(Rates!A2:A7)
Minimum Week	=MIN(Orders!H2:H25)
Maximum Week	=MAX(Orders!H2:H25)
```

### Raw practice intake — Audit Intake A1:I7

Rows 2–7 are practice copies of source PO001–PO006. Changes: PO001 Quantity 2→3; PO002 ID removed; PO003 practice ID QA003 and ItemCode IT99; PO004 practice ID QA004 and Quantity text four; PO005 practice ID QA005 and numeric Quantity 0; PO006 practice ID QA006 and status Cancelled. Other fields are copied only as fictional practice context. Do not insert these into Orders or replace the blank with PO002.

```text
OrderID	Project	Team	ItemCode	Quantity	UnitCost	Status	Week	Description
PO001	PJ-A	Planning	IT01	3	45	Delivered	1	Display adapter for briefing
	PJ-A	Procurement	IT02	4	12	Pending	1	Training notebook for pilot team
QA003	PJ-A	Site Coordination	IT99	6	30	Cancelled	1	Cable pack for review session
QA004	PJ-A	Planning	IT04	four	18	Delivered	1	Marker set for briefing
QA005	PJ-A	Procurement	IT05	0	25	Delivered	1	Desk sign for pilot team
QA006	PJ-A	Site Coordination	IT06	2	8	Cancelled	1	Quick guide for review session
```

### Training contract — Data Contract A1:B14

```text
Data Contract	Fictional training rule — source audit
Grain	One order line. One OrderID identifies that line; not a project subtotal or a purchase approval.
Maintained source	Orders!A1:I25, 24 supplied lines. Rates!A1:D7, six supplied item mappings. Intake rows are separate practice copies.
OrderID	Required and unique for each order line. Do not invent a missing identifier or overwrite a conflicting duplicate.
ItemCode	Must match exactly one Rates!A2:A7 key. An unknown code needs clarification, not an approximate match.
Quantity	Numeric, non-negative whole number. Zero is valid for this stated training rule; text four is not numeric 4.
UnitCost	Numeric and non-negative. Values use the supplied training currency; a sum of unit prices is not spend.
Status	Exactly Delivered, Pending or Cancelled. Keep valid cancelled lines in an all-orders population.
Week	Numeric practice index 1 to 4 in this baseline, not a calendar date.
Repeated record	Same ID and all nine fields identical: a repeated copy, not an additional order. Preserve provenance and do not double-count.
Conflicting duplicate	Same ID with changed Quantity or any other field: quarantine pending an evidenced correction. Do not choose a winner by guesswork.
Raw evidence	Preserve Audit Intake A2:I7 exactly. Record proposed corrections separately; no repairs to Orders during this audit.
Analysis scope	Questions may later select statuses. Record that population rule; do not label Cancelled as corrupt merely to exclude it.
Authority boundary	Training contract and proposed dispositions only. No purchasing, approval, sharing or real policy decisions.
```

### Intake diagnostics — Intake Checks A1:J7

```text
Case	Intake row	OrderID	Source ID count	Intake ID count	Rate key count	Qty numeric	Qty rule	Cost rule	Status rule
Case 1	2	='Audit Intake'!A2	=IF(C2="",0,COUNTIF(Orders!$A$2:$A$25,C2))	=IF(C2="",0,COUNTIF('Audit Intake'!$A$2:$A$7,C2))	=COUNTIF(Rates!$A$2:$A$7,'Audit Intake'!D2)	=ISNUMBER('Audit Intake'!E2)	=IF(ISNUMBER('Audit Intake'!E2),AND('Audit Intake'!E2>=0,MOD('Audit Intake'!E2,1)=0),FALSE)	=AND(ISNUMBER('Audit Intake'!F2),'Audit Intake'!F2>=0)	=OR('Audit Intake'!G2="Delivered",'Audit Intake'!G2="Pending",'Audit Intake'!G2="Cancelled")
Case 2	3	='Audit Intake'!A3	=IF(C3="",0,COUNTIF(Orders!$A$2:$A$25,C3))	=IF(C3="",0,COUNTIF('Audit Intake'!$A$2:$A$7,C3))	=COUNTIF(Rates!$A$2:$A$7,'Audit Intake'!D3)	=ISNUMBER('Audit Intake'!E3)	=IF(ISNUMBER('Audit Intake'!E3),AND('Audit Intake'!E3>=0,MOD('Audit Intake'!E3,1)=0),FALSE)	=AND(ISNUMBER('Audit Intake'!F3),'Audit Intake'!F3>=0)	=OR('Audit Intake'!G3="Delivered",'Audit Intake'!G3="Pending",'Audit Intake'!G3="Cancelled")
Case 3	4	='Audit Intake'!A4	=IF(C4="",0,COUNTIF(Orders!$A$2:$A$25,C4))	=IF(C4="",0,COUNTIF('Audit Intake'!$A$2:$A$7,C4))	=COUNTIF(Rates!$A$2:$A$7,'Audit Intake'!D4)	=ISNUMBER('Audit Intake'!E4)	=IF(ISNUMBER('Audit Intake'!E4),AND('Audit Intake'!E4>=0,MOD('Audit Intake'!E4,1)=0),FALSE)	=AND(ISNUMBER('Audit Intake'!F4),'Audit Intake'!F4>=0)	=OR('Audit Intake'!G4="Delivered",'Audit Intake'!G4="Pending",'Audit Intake'!G4="Cancelled")
Case 4	5	='Audit Intake'!A5	=IF(C5="",0,COUNTIF(Orders!$A$2:$A$25,C5))	=IF(C5="",0,COUNTIF('Audit Intake'!$A$2:$A$7,C5))	=COUNTIF(Rates!$A$2:$A$7,'Audit Intake'!D5)	=ISNUMBER('Audit Intake'!E5)	=IF(ISNUMBER('Audit Intake'!E5),AND('Audit Intake'!E5>=0,MOD('Audit Intake'!E5,1)=0),FALSE)	=AND(ISNUMBER('Audit Intake'!F5),'Audit Intake'!F5>=0)	=OR('Audit Intake'!G5="Delivered",'Audit Intake'!G5="Pending",'Audit Intake'!G5="Cancelled")
Case 5	6	='Audit Intake'!A6	=IF(C6="",0,COUNTIF(Orders!$A$2:$A$25,C6))	=IF(C6="",0,COUNTIF('Audit Intake'!$A$2:$A$7,C6))	=COUNTIF(Rates!$A$2:$A$7,'Audit Intake'!D6)	=ISNUMBER('Audit Intake'!E6)	=IF(ISNUMBER('Audit Intake'!E6),AND('Audit Intake'!E6>=0,MOD('Audit Intake'!E6,1)=0),FALSE)	=AND(ISNUMBER('Audit Intake'!F6),'Audit Intake'!F6>=0)	=OR('Audit Intake'!G6="Delivered",'Audit Intake'!G6="Pending",'Audit Intake'!G6="Cancelled")
Case 6	7	='Audit Intake'!A7	=IF(C7="",0,COUNTIF(Orders!$A$2:$A$25,C7))	=IF(C7="",0,COUNTIF('Audit Intake'!$A$2:$A$7,C7))	=COUNTIF(Rates!$A$2:$A$7,'Audit Intake'!D7)	=ISNUMBER('Audit Intake'!E7)	=IF(ISNUMBER('Audit Intake'!E7),AND('Audit Intake'!E7>=0,MOD('Audit Intake'!E7,1)=0),FALSE)	=AND(ISNUMBER('Audit Intake'!F7),'Audit Intake'!F7>=0)	=OR('Audit Intake'!G7="Delivered",'Audit Intake'!G7="Pending",'Audit Intake'!G7="Cancelled")
```

Supporting comparison cells: B11 **=Orders!E2** gives 2; E11 **='Audit Intake'!E2** gives 3; H11 **=Orders!E2='Audit Intake'!E2** givesFALSE. E13 **=SUMPRODUCT(--(Orders!A2:I2='Source Snapshot'!A2:I2))** gives 9 identical fields in the preserved copy. A repeated copy is not an additional order; the conflicting PO001 intake remains quarantined.

### Proposed exception register — Audit Intake J1:L7

These are guided author-reference dispositions, not completed independent decisions or messages to a source owner.

```text
Issue	Evidence	Disposition
Conflicting duplicate OrderID	Practice PO001: source ID count 1; Orders Quantity 2 vs intake 3, equality FALSE. Other fields copied from PO001.	Quarantine pending evidenced correction. Clarify with the source owner; do not overwrite Orders or count both.
Missing OrderID	Raw intake A3 is empty. This is a labelled copy of PO002 with only its ID removed; do not infer that missing ID.	Clarify the required key; quarantine pending evidence. Do not invent an ID or silently fill PO002.
Unknown ItemCode	IT99 has zero exact matches in Rates A2:A7. Other fields are practice copies of PO003. Cancelled itself is allowed.	Clarify the intended item key and rate with evidence. Keep raw IT99; quarantine pending evidence.
Non-numeric Quantity	Quantity is the text four: ISNUMBER is FALSE and the non-negative whole-number rule is FALSE. Other fields copied from PO004.	Clarify the intended numeric quantity with evidence; propose correction separately. Do not replace raw text by guessing 4.
Valid zero Quantity	Quantity 0 is numeric and passes the explicit non-negative whole-number rule. Other fields copied from PO005 under a practice ID.	Retain as a valid training example. No insertion into baseline Orders; zero does not prove a delivery or spend.
Valid Cancelled status	Cancelled passes the status contract; numeric Quantity 2, UnitCost 8 and key IT06 are valid. Practice copy of PO006 with status changed.	Retain as a valid all-orders training example. Later status exclusions need a stated analysis question, not a dirty-data label.
```

Independent release conditions, independent disposition reasoning, reviewer challenge and learner timing remain pending. The six intake examples never enter baseline controls. A preserved Source Snapshot is a copy, not a protected-range permission or automatic archive.
