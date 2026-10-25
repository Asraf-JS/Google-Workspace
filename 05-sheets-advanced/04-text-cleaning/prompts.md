# 04 - Combine and Clean Text: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
=LEFT(A2,2)
```

```text
=RIGHT(A2,3)
```

```text
=MID(A2,3,3)
```

```text
=A2&" - "&B2
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Identifier intake: PO001; PO024; PO1; blank; IT01; IT06; IT99; “ IT03 ”. Order IDs require PO plus three digits; mapped item keys are the six supplied Rates codes. Do not treat every extracted suffix as a valid key.
```

## Captured Author-Run Reference

Fictional training material. Expectations precede actual formulas; actual results are recorded separately. Preserve spaces using single-cell entry where noted. This is not independent learner validation.

### Text Practice A1:C4

```text
OrderID	Project	ItemCode
PO001	PJ-A	IT01
PO002	PJ-A	IT02
PO024	PJ-C	IT06
```

### Text Practice source-padded team A8

Enter one ordinary space, then `Planning`, then one ordinary space. The raw value must have length10; enter this cell separately from a multi-cell paste.

### Gemini proposal-only prompt

```text
Fictional training task. Return a category proposal table only; do not edit the spreadsheet. Use only Equipment, Stationery, Print and this explicit Rates mapping: IT01 Display adapter = Equipment; IT02 Training notebook = Stationery; IT03 Cable pack = Equipment; IT04 Marker set = Stationery; IT05 Desk sign = Print; IT06 Quick guide = Print. Propose a category for each of these six ItemCodes and names. Mark an unmapped or ambiguous input for review rather than inventing a category.
```

### Category Checks A1:E7 — actual proposal observations, blank comparison columns

```text
ItemCode	Item	Gemini proposal	Rates category	Matches reference
IT01	Display adapter	Equipment
IT02	Training notebook	Stationery
IT03	Cable pack	Equipment
IT04	Marker set	Stationery
IT05	Desk sign	Print
IT06	Quick guide	Print
```

### Text Audit A1:C4 — raw CSV, restore B2/B4 single-cell spaces

```text
TaskID	Raw team	Raw status
T001	 Planning 	complete
T002	Procurement	In Progress
T003	Site Coordination 	Not Started
```

### Whitespace expectations A12:H15 — blank actual columns

```text
Case	Raw value	Expected length after TRIM	TRIM output	Observed length	Matches expected	Decision	First code point
Ordinary padding	 Planning 	8
Trailing space	Site Coordination 	17
NBSP padding	 Planning 	10
```

### Identifier expectations A1:L9 — blank actual columns

```text
Case	Raw key	Kind	Expected outcome	Normalised	Prefix	RIGHT 3	MID 3	Pattern OK	Reference OK	Decision	Matches expected
ID01	PO001	Order	Accepted order
ID02	PO024	Order	Accepted order
ID03	PO1	Order	Malformed
ID04		Item	Blank
ID05	IT01	Item	Equipment
ID06	IT06	Item	Print
ID07	IT99	Item	Unmapped
ID08	 IT03 	Item	Equipment
```

### Identifier controls A12:D21

```text
Control	Actual	Expected	Difference
Cases	=COUNTA(A2:A9)	8	=B13-C13
Expected decisions matched	=COUNTIF(L2:L9,TRUE)	8	=B14-C14
Accepted orders	=COUNTIF(K2:K9,"Accepted order")	2	=B15-C15
Mapped item categories	=COUNTIF(K2:K9,"Equipment")+COUNTIF(K2:K9,"Stationery")+COUNTIF(K2:K9,"Print")	3	=B16-C16
Malformed	=COUNTIF(K2:K9,"Malformed")	1	=B17-C17
Blank	=COUNTIF(K2:K9,"Blank")	1	=B18-C18
Unmapped	=COUNTIF(K2:K9,"Unmapped")	1	=B19-C19
Pattern passes	=COUNTIF(I2:I9,TRUE)	6	=B20-C20
Reference matches	=COUNTIF(J2:J9,TRUE)	5	=B21-C21
```

### Pipeline Notes A1:B10

```text
Pipeline stage	Evidence and reversibility
Raw source	DirtyText.csv raw values retained in Text Audit A:C; Orders and Rates unchanged. CSV block paste trimmed spaces; affected raw cells restored individually before cleaning.
Normalised	Text Audit D uses TRIM. E uses explicit case handling only for complete / in progress / not started. Whitespace and case changes are not invertible without the raw source.
Unusual whitespace	The literal NBSP case keeps length10 after TRIM and code point160. Retain it for review; do not silently replace unusual characters.
Validated	Identifier Tests checks complete ^PO[0-9]{3}$ or ^IT[0-9]{2}$ patterns and reference membership separately. PO1 malformed; blank remains blank; IT99 syntactically valid but unmapped.
Category output	Known item categories come from exact Rates mapping. Six Gemini proposals were compared individually; they repeated the supplied mapping, not an independent test on unseen items.
Display output	Text Practice combines OrderID and Project only for display. Separate keys and original zeros remain; LEFT/RIGHT/MID outputs are text, not new identifiers.
Reconstruction	Clean Planning traces to Text Audit B2 with raw length10, TRIM D2 length8. Preserve raw B2 to recover discarded spaces; do not attempt to reverse TRIM from clean text alone.
Author evidence	Three raw/clean rows, three space cases, eight expected-versus-actual identifier cases and six AI/reference comparisons checked. Maintained Orders/Analysis/Rates/Source Snapshot unchanged.
Pending checks	Independent mixed-intake attempt and reviewer reconstruction not performed. File-import route and classroom60-minute timing remain unverified.
```

### Seed formulas — fill each stated column down

**Text Practice D2:D4**

```text
=LEFT(A2,2)
```

**Text Practice E2:E4**

```text
=RIGHT(A2,3)
```

**Text Practice F2:F4**

```text
=MID(A2,3,3)
```

**Text Practice G2:G4**

```text
=A2&" - "&B2
```

**Text Audit D2:D4**

```text
=TRIM(B2)
```

**Text Audit E2:E4**

```text
=IF(LOWER(TRIM(C2))="complete","Complete",IF(LOWER(TRIM(C2))="in progress","In Progress",IF(LOWER(TRIM(C2))="not started","Not Started","Review")))
```

**Text Audit F2:F4**

```text
=IF(AND(OR(D2="Planning",D2="Procurement",D2="Site Coordination"),E2<>"Review"),"Accepted","Review")
```

**Text Audit G2:G4**

```text
=LEN(B2)
```

**Text Audit H2:H4**

```text
=LEN(D2)
```

**Text Audit D13:D15**

```text
=TRIM(B13)
```

**Text Audit E13:E15**

```text
=LEN(D13)
```

**Text Audit F13:F15**

```text
=E13=C13
```

**Text Audit H13:H15**

```text
=UNICODE(LEFT(B13,1))
```

**Identifier Tests E2:E9**

```text
=TRIM(B2)
```

**Identifier Tests F2:F9**

```text
=LEFT(E2,2)
```

**Identifier Tests G2:G9**

```text
=RIGHT(E2,3)
```

**Identifier Tests H2:H9**

```text
=MID(E2,3,3)
```

**Identifier Tests I2:I9**

```text
=IF(C2="Order",REGEXMATCH(E2,"^PO[0-9]{3}$"),IF(C2="Item",REGEXMATCH(E2,"^IT[0-9]{2}$"),FALSE))
```

**Identifier Tests J2:J9**

```text
=IF(I2,IF(C2="Order",COUNTIF(Orders!$A$2:$A$25,E2)=1,COUNTIF(Rates!$A$2:$A$7,E2)=1),FALSE)
```

**Identifier Tests K2:K9**

```text
=IF(E2="","Blank",IF(NOT(I2),"Malformed",IF(NOT(J2),"Unmapped",IF(C2="Order","Accepted order",VLOOKUP(E2,Rates!$A$2:$D$7,4,FALSE)))))
```

**Identifier Tests L2:L9**

```text
=K2=D2
```

**Category Checks D2:D7**

```text
=VLOOKUP(A2,Rates!$A$2:$D$7,4,FALSE)
```

**Category Checks E2:E7**

```text
=C2=D2
```

Raw whitespace cases include literal NBSP (U+00A0) padding; if copying changes it, verify the first code point160 and raw length10. Do not substitute ordinary spaces and claim the same test. Independent mixed intake, reviewer reconstruction, native file import and learner timing remain pending.
