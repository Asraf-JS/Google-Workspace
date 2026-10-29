# 05 - Match Records and Handle Errors: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
LookupRate
```

```text
=VLOOKUP(D2,Rates!$A$2:$D$7,3,FALSE)
```

```text
=INDEX(Rates!$C$2:$C$7,MATCH(D2,Rates!$A$2:$A$7,0))
```

```text
=HLOOKUP(F4,$G$1:$L$2,2,FALSE)
```

```text
=IFNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE),"Unmapped item")
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Lookup challenge: Known IT01 and IT06; unknown IT99; blank; space-padded IT03. Duplicate-test mapping adds IT03 with UnitCost 99 only on a disposable copy. Baseline IT03 remains 30. Keep the supplied six-key Rates source intact.
```

## Captured Author-Run Reference

Fictional training material. Use separate practice/copy tabs, preserve raw keys and record expectations before actual results. This is not independent learner validation.

### Lookup Practice N1:Q2 — seed formulas, fill row 2 through 25

```text
LookupRate	IndexMatchRate	VLookup difference	Index difference
=VLOOKUP(D2,Rates!$A$2:$D$7,3,FALSE)	=INDEX(Rates!$C$2:$C$7,MATCH(D2,Rates!$A$2:$A$7,0))	=N2-F2	=O2-F2
```

### Horizontal Lookup G1:L2 reference

```text
IT01	IT02	IT03	IT04	IT05	IT06
45	12	30	18	25	8
```

### Lookup Errors A1:D3 — repaired introductory state

```text
Case	Observed output	Meaning	Action
Missing key	=IFNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE),"Unmapped item")	Expected missing match	Label as unmapped, not zero
Bad function	=VLOOKUP("IT03",Rates!$A$2:$D$7,3,FALSE)	Formula defect	Repair function name
```

### Lookup Tests A1:K10 — expectations, blank actual columns

```text
Case	Raw key	Normalised key	Expected result	Match count	VLOOKUP	INDEX MATCH	Rates check	Matches expected	Decision	Raw lookup
LK01	IT01		45
LK02	IT02		12
LK03	IT03		30
LK04	IT04		18
LK05	IT05		25
LK06	IT06		8
LK07	IT99		Unmapped item
LK08			Blank
LK09	 IT03 		30
```

### Lookup Tests A13:D19 controls

```text
Control	Actual	Expected	Difference
Cases	=COUNTA(A2:A10)	9	=B14-C14
Expected results matched	=COUNTIF(I2:I10,TRUE)	9	=B15-C15
Disagreements	=COUNTIF(I2:I10,FALSE)	0	=B16-C16
Accepted key cases	=COUNTIF(J2:J10,"Accepted")	7	=B17-C17
Unmapped key cases	=COUNTIF(J2:J10,"Unmapped item")	1	=B18-C18
Blank key cases	=COUNTIF(J2:J10,"Blank")	1	=B19-C19
```

### Rates Duplicate Test A8:D8 — copy only

```text
IT03	Cable pack duplicate	99	Equipment
```

### Duplicate diagnostic A11:F12

```text
Test key	First VLOOKUP	INDEX MATCH	Match count	Decision	Expected first rate
IT03	=VLOOKUP(A12,$A$2:$D$8,3,FALSE)	=INDEX($C$2:$C$8,MATCH(A12,$A$2:$A$8,0))	=COUNTIF($A$2:$A$8,A12)	=IF(D12<>1,"Review duplicate","Accepted")	30
```

### Descending-copy experiment A10:F11

```text
Test key	Exact FALSE	Omitted mode	Expected exact	Exact matches	Comparison
IT03	=VLOOKUP(A11,$A$2:$D$7,3,FALSE)	=VLOOKUP(A11,$A$2:$D$7,3)	30	=B11=D11	Descending keys violate the ascending-order requirement of approximate lookup. Record this output; do not use it as a rate mapping.
```

### Actual error comparison A6:E9 — before repair

```text
Error experiment	Raw result	IFNA only	IFERROR blanket	Interpretation
Missing key	=VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE)	=IFNA(B7,"Unmapped item")	=IFERROR(B7,"Fallback")	Expected missing match; not a zero rate
Bad function name	=VLOKUP("IT03",Rates!$A$2:$D$7,3,FALSE)	=IFNA(B8,"Unmapped item")	=IFERROR(B8,"Fallback")	IFNA exposes function defect; IFERROR hides it
Return column outside range	=VLOOKUP("IT03",Rates!$A$2:$B$7,3,FALSE)	=IFNA(B9,"Unmapped item")	=IFERROR(B9,"Fallback")	Third return column is outside the two-column range
```

### Lookup Notes A1:B11

```text
Topic	Verified result and assumptions
Preserved baseline	Orders, Analysis, Rates and Source Snapshot remain unchanged. Lookup Practice is an Orders copy; Horizontal Lookup avoids the occupied Analysis F/G area.
Vertical lookup	VLOOKUP uses Rates A2:D7, keys in the first column, return column 3, FALSE for exact match. All 24 copied Orders rows reconcile to original UnitCost.
INDEX MATCH	INDEX returns Rates C2:C7 and MATCH searches the aligned A2:A7 range with 0. All 24 copied rows reconcile; exact matching still returns a first match, not a uniqueness guarantee.
Horizontal lookup	G1:L1 contains the six keys and G2:L2 their rates. HLOOKUP uses row 2 and FALSE. IT03 returned 30, IT06 returned 8, then IT03 was restored; three methods agree at 30.
Input matrix	Nine expected cases include all six known keys, IT99, blank and padded IT03. Raw key retained beside TRIM. Nine comparisons pass; seven accepted cases, one unmapped, one blank.
Duplicate copy	Rates Duplicate Test appends IT03 with UnitCost 99. First VLOOKUP and INDEX MATCH return 30, but COUNTIF=2 means Review duplicate. Baseline IT03 remains 30. Retain the labelled experimental copy.
Reordered copy	Rates Reordered sorts only A2:D7 descending. Exact lookup of IT03 returns 30; omitted match mode returned 45 in this actual test. Approximate mode assumes ascending keys; that experiment is not authoritative mapping.
Error distinction	Raw missing IT99 gives NA, misspelled VLOKUP gives NAME, and return column 3 on range A:B gives REF. IFNA handles only NA; IFERROR hid all three behind the same fallback text.
Repair and final state	Function and range defects were repaired to return 30. One raw expected missing-key NA remains as a labelled demonstration; Unmapped item is not zero. Conflicting and reordered mappings exist only in scenario tabs.
Pending independent work	Independent Rate/MatchCount/Decision output, zero-rate distinction, column-move diagnosis, rejected-key handover, reviewer and classroom 80-minute timing remain pending. These author cases are not independent learner validation.
```

### Lookup Tests seed formulas — fill each column from row 2 through 10

**C2:C10**

```text
=TRIM(B2)
```

**E2:E10**

```text
=IF(C2="",0,COUNTIF(Rates!$A$2:$A$7,C2))
```

**F2:F10**

```text
=IF(C2="","Blank",IFNA(VLOOKUP(C2,Rates!$A$2:$D$7,3,FALSE),"Unmapped item"))
```

**G2:G10**

```text
=IF(C2="","Blank",IFNA(INDEX(Rates!$C$2:$C$7,MATCH(C2,Rates!$A$2:$A$7,0)),"Unmapped item"))
```

**H2:H10**

```text
=IF(C2="","Blank",IF(E2=0,"Unmapped item",IF(E2>1,"Duplicate",SUMIF(Rates!$A$2:$A$7,C2,Rates!$C$2:$C$7))))
```

**I2:I10**

```text
=AND(D2=F2,D2=G2,D2=H2)
```

**J2:J10**

```text
=IF(C2="","Blank",IF(E2=0,"Unmapped item",IF(E2>1,"Duplicate","Accepted")))
```

**K2:K10**

```text
=IF(B2="","Blank",IFNA(VLOOKUP(B2,Rates!$A$2:$D$7,3,FALSE),"Unmapped item"))
```

### Horizontal comparison formulas

**Horizontal Lookup G4**

```text
=HLOOKUP(F4,$G$1:$L$2,2,FALSE)
```

**Horizontal Lookup H4**

```text
=VLOOKUP(F4,Rates!$A$2:$D$7,3,FALSE)
```

**Horizontal Lookup I4**

```text
=INDEX(Rates!$C$2:$C$7,MATCH(F4,Rates!$A$2:$A$7,0))
```

**Horizontal Lookup J4**

```text
=AND(G4=H4,H4=I4)
```

Enter padded Lookup Tests B10 individually as one ordinary space, IT03, then one ordinary space. Keep B9 truly empty. Error comparison formulas intentionally create errors; capture and inspect them before repairing B8/B9 to exact VLOOKUP on Rates A2:D7. Independent zero-rate/column-move/output and reviewer checks remain pending.
