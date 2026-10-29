# 06 - Complete the Formula Clinic: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

Use the bounded formulas and test cards below on the separate clinic copy. Record expected behaviour before introducing a fault. Restore every temporary source change.


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Extra fault choices, clinic copy only: change a numeric quantity to text “four”; insert a duplicate lookup key; replace a blank/missing-rate outcome with 0; shorten one delivered summary range by two rows. Diagnose the cause before restoring from Source Snapshot.
```

## Captured Author-Run Reference

Create a whole-workbook copy named **GW - Sheets Advanced - Formula Clinic**. Keep sharing/comments unchecked. Use the new copy for every mutation below. These are guided reference cards, not a completed independent challenge.

### Clinic Register A1:D4 — record before faults

```text
Defect	Expected behaviour	Planned fault	Test that should detect it
Match mode	Known IT01 returns 45; unknown IT99 must be an explicit missing match	Remove FALSE from Lookup Practice N2	Test IT99; sorted approximate lookup may return an unrelated rate
Shifted row	Orders J2 multiplies its own Quantity 2 by UnitCost 45 =90	Change J2 from E2*F2 to E2*F3	Compare first-row product and inspect references
Omitted row	All 24 Orders amounts sum 3158; final PO024 contributes64	Change J27 SUM range to J2:J24	Inspect final-row coverage and compare full control total
```

### Clinic Checks A1:D3 — expected values before actuals

```text
Check	Expected	Observed	Pass
Known IT01 rate	45
Unknown IT99	Unmapped item
```

### Clinic Checks A5:D9 — population expectations

```text
Population control	Expected	Observed	Difference
All orders amount	3158
Delivered amount	1478
All order count	24
Delivered count	12
```

### Clinic Checks A12:F16 — manual amounts before formulas

```text
OrderID	Quantity	UnitCost	Manual amount	Formula amount	Difference
PO001	2	45	90
PO004	8	18	144
PO005	10	25	250
PO008	6	12	72
```

### Clinic Checks A18:D19 — reconciliation formulas

```text
Manual subset sum	556	=SUM(D13:D16)	=C18-B18
Analysis PJ-A Delivered	=SUM(D13:D16)	=Analysis!B4	=C19-B19
```

### Clinic Register A7:B10 — causes after repairs

```text
Cause	Why the control detects it
Match mode	Removing FALSE leaves approximate matching: a known IT01 still looked correct 45, but unknown IT99 incorrectly returned 8. Exact matching keeps absence explicit.
Shifted row	E2*F3 uses the next item price 12, so Quantity 2 gives 24 instead of 90. Inspecting same-row inputs catches a plausible numeric error.
Omitted row	SUM(J2:J24) excludes PO024 amount 64. After repairing J2, it gives 3094 instead of 3158; a final-row coverage test catches the omission.
```

### Clinic Comparisons A1:E4 — live isolated expressions

```text
Defect	Faulty expression	Isolated faulty result	Repaired expression	Repaired result
Match mode	=FORMULATEXT(C2)	=VLOOKUP("IT99",Rates!$A$2:$D$7,3)	=FORMULATEXT(E2)	=IFNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE),"Unmapped item")
Shifted row	=FORMULATEXT(C3)	=Orders!E2*Orders!F3	=FORMULATEXT(E3)	=Orders!E2*Orders!F2
Omitted row	=FORMULATEXT(C4)	=SUM(Orders!J2:J24)	=FORMULATEXT(E4)	=SUM(Orders!J2:J25)
```

### Clinic Comparisons A7:D10 — expectations before tests

```text
Test	Expected observation	Restore	Classification
Numeric text: Orders E3=four	J3 and total show #VALUE!	E3=4; J3=48; total=3158	Source type error; do not hide as zero
Duplicate IT03 in copied Rates	First rate=30; count=2; review duplicate	Keep duplicate confined to test tab	Source key validation
Final row: Orders E25=0	J25=0; total=3094	E25=8; J25=64; total=3158	Range boundary test
```

### Clinic Duplicate Rates A8:D8 — append only on the test tab

```text
IT03	Duplicate cable rate	99	Equipment
```

### Clinic Comparisons A13:D14 — duplicate diagnostic

```text
Key	First exact rate	Key count	Decision
IT03	=VLOOKUP(A14,'Clinic Duplicate Rates'!$A$2:$D$8,3,FALSE)	=COUNTIF('Clinic Duplicate Rates'!$A$2:$A$8,A14)	=IF(C14>1,"Review duplicate","Unique")
```

### Clinic Comparisons A17:D23 — test log, actual columns blank

```text
Test	Expected	Observed during test	Restored or retained state
Known and missing key	45 / Unmapped item
Zero quantity E2	J2=0; total=3068
Numeric text E3	#VALUE! in J3 and total
Duplicate IT03	Count=2; review duplicate
Final row E25=0	J25=0; total=3094
Restored baseline	3158 / 1478 / 24 / 12
```

### Clinic Comparisons A26:B31 — troubleshooting path

```text
Troubleshooting step	Evidence to check
1 Inspect source	Numeric types and unique keys before changing formulas
2 Define population	All 24 orders=3158; Delivered 12=1478; keep Cancelled
3 Inspect references	Exact FALSE; same-row product; include J25
4 Test boundaries	Normal, missing, zero, text, duplicate and final row
5 Reconcile	Manual PJ-A Delivered=556; record expected versus actual
```

### Actual fault and repair sequence

| Target on clinic copy | Fault | Repair / restore |
|---|---|---|
| Lookup Practice N2 | =VLOOKUP(D2,Rates!$A$2:$D$7,3) | =VLOOKUP(D2,Rates!$A$2:$D$7,3,FALSE) |
| Lookup Practice D2 | IT99 to expose approximate result 8 | IT01; exact result 45 |
| Orders J2 | =E2*F3 returns 24 | =E2*F2 returns 90 |
| Orders J27 | =SUM(J2:J24); combinedfault3028, after rowrepair3094 | =SUM(J2:J25) returns 3158 |
| Orders E2 | 0 gives valid zero line amount; total 3068 | 2; total 3158 |
| Orders E3 | four gives #VALUE! in J3 and total | 4; J3=48; total 3158 |
| Orders E25 | 0 gives J25=0 and total 3094 | 8; J25=64; total 3158 |

### Filtered population helpers outside the source range

Create the filter on **Orders A1:K25**, select Status **Delivered** only, and add the helpers outside that range:

```text
Visible Amount	Visible Count
=SUBTOTAL(109,J2:J25)	=SUBTOTAL(103,A2:A25)
```

Paste in **N26:O27**. With the Delivered filter active, expect 1478/12. Remove the filter after recording the result; the helpers then show 3158/24. SUM over the source remains an all-record total. Keep Cancelled records.

In Clinic Checks **E13** use **=B13*C13** and F13 **=E13-D13**, then fill both through row 16. The manual amounts must be recorded before these comparisons. Expected differences are 0; subset sum 556.

The numeric-text and duplicate-key cases classify source type/uniqueness problems separately from formula logic. Do not replace missing or invalid values with 0. Independent hidden-fault diagnosis, partner presentation, reviewer work and learner duration remain pending.
