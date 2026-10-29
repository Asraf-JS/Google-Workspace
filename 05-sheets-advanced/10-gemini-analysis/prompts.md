# 10 - Use Gemini as an Analysis Partner: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Propose a Delivered Total

**Session:** new chat | **Grounding:** explicit Orders schema

```text
Goal: Propose a formula for delivered order amount.
Context: Fictional Google Sheets analysis.
Source: Orders rows 2 to 25; Status is G and Amount is J. Header row is 1.
Expectations: Reply with a formula and explanation only. Do not edit cells. Include only Status equal to Delivered. Use bounded ranges. I will test the formula against the source.
```

Replace bracketed source placeholders before submitting. Keep a human check between an AI proposal and the final output.

## Part 2: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Flawed formula proposals to audit if AI is unavailable: `=SUM(Orders!J2:J24)` described as all 24 rows; `=IFERROR(VLOOKUP("IT99",Rates!A2:D7,3,FALSE),0)` described as a confirmed zero rate; `=SUMIFS(Orders!J2:J25,Orders!G2:G25,"Delivered")` described as active amount excluding only Cancelled.
```

## Part 3: Captured Author-Run Reference

Use the isolated **GW - Sheets Advanced - AI Audit** copy. Build in guide order, record expectations before tests, and retain original proposals separately from manual repairs. Supplied deliberate flaws below are not Gemini outputs. Use the live Dashboard for refreshed values; the inserted **AI Generated Snapshot** uses static number cells.

### AI Proposals A1:D4 - Delivered verification

```text
Gemini proposal verification	Value	Control	Difference
Delivered amount (RM)	=SUMIF(Orders!G2:G25,"Delivered",Orders!J2:J25)	='Database Analysis'!D10	=B2-C2
Delivered record count	=COUNTIF(Orders!G2:G25,"Delivered")	12	=B3-C3
Acceptance	=IF(AND(D2=0,D3=0),"Matches bounded controls","Review mismatch")
```

### AI Proposals A7:D11 - threshold tests

```text
Threshold proposal tests	Actual	Expected	Difference
Pending amount >=200	=SUMIFS(Orders!$J$2:$J$25,Orders!$G$2:$G$25,"Pending",Orders!$J$2:$J$25,">=200")	0	=B8-C8
Pending count >=200	=COUNTIFS(Orders!$G$2:$G$25,"Pending",Orders!$J$2:$J$25,">=200")	0	=B9-C9
All Pending amount	=SUMIF(Orders!$G$2:$G$25,"Pending",Orders!$J$2:$J$25)	460	=B10-C10
Max Pending amount	=MAX(FILTER(Orders!J2:J25,Orders!G2:G25="Pending"))	180	=B11-C11
```

### AI Proposals A14:D21 - traced Pending subset

```text
Pending subset trace	Amount (RM)	Status	Amount >=200
=Orders!A3	=Orders!J3	=Orders!G3	=B15>=200
=Orders!A7	=Orders!J7	=Orders!G7	=B16>=200
=Orders!A11	=Orders!J11	=Orders!G11	=B17>=200
=Orders!A15	=Orders!J15	=Orders!G15	=B18>=200
=Orders!A19	=Orders!J19	=Orders!G19	=B19>=200
=Orders!A23	=Orders!J23	=Orders!G23	=B20>=200
Subset total / qualifying count	=SUM(B15:B20)	=COUNTIF(D15:D20,TRUE)
```

### AI Findings A1:B7 - checked commentary

```text
Checked findings	Author wording and supporting evidence
Finding 1	Across all 24 orders, including Cancelled, the amount is RM3158. Delivered orders alone contribute RM1478 across 12 records.
Evidence 1	Dashboard B6:B8 sum 3158; C6:C8 sum 1478; G6:G8 sum 24 and G6=12. These are different populations.
Finding 2	Among Delivered orders, PJ-B has the largest amount at RM578, compared with PJ-A RM556 and PJ-C RM344.
Evidence 2	Dashboard A6:A8 identifies projects; C6:C8 contains 556/578/344. Ranking is descriptive, not a cause or forecast.
Rejected inference	These figures do not establish efficiency, future delivery performance, cost savings or ROI.
Acceptance rule	Retain a finding only when the claimed population, units and cited cells agree. Generated prose is a proposal, not the source.
```

### AI Visual Test A1:B11 - actual source and refresh audit

```text
Generated visual audit	Prediction before source change
AI claim	Gemini said the generated chart followed Dashboard A5:B8 directly and used no separate data.
Actual insertion	Insert created a new [Chart 1] tab with chart 1111393157 and a separate A3:B6 table. The chosen AI Visual Test tab was not used as the destination.
Actual source	Chart editor Setup shows A3:B6 on the generated tab. B4:B6 contain numbers 980/1204/974, not source-link formulas.
Test input	In this AI Audit workbook only, temporarily change Orders E2 Quantity 2 to 3 at cost 45, then restore 2.
Live prediction	PO001 Amount 135, Dashboard PJ-A1025 and all amount 3203: +45.
Snapshot prediction	Generated B4 stays 980 and its chart stays at baseline because the inserted values are static.
Acceptance rule	Use the checked live Dashboard for refreshed values; label a generated static result as a snapshot. AI prose alone cannot prove refresh.

Observed result	With Orders E2=3, Dashboard PJ-A=1025 and all amount=3203, but generated B4=980 and chart unchanged. Static values disproved the direct-link claim.
Restoration	Orders E2 restored to 2 and Dashboard baseline 3158. Generated tab renamed AI Generated Snapshot and labelled. Regenerate/recheck it after source changes; use the checked Dashboard as live output.
```

### AI Test Matrix A1:B10 - expectations before prompting

```text
Prewritten test matrix	Expected outcome before casework prompt
Delivered population	Orders rows 2:25 Status=Delivered: Amount 1478, record count 12.
Pending >=200	Status=Pending AND Amount>=200. Six Pending amounts 48/16/180/96/48/72: no qualifying records, Amount 0 and count 0.
Boundary fixture	Pending 199.99/200/200.01 and Delivered 250: qualifying Pending count 2, amount 400.01. A >200 rule would wrongly omit 200.
Unknown ItemCode	IT99 has no mapping in Rates A2:D7. Missing rate must remain distinct from a confirmed numeric zero. IT01 known UnitCost 45.
Bounds test	Original 24-record all Amount 3158. Rows 2:24 omit PO024 Amount 64 and give 3094.
New-row test	Separate author test row TEST025 at row 26, Quantity 2*UnitCost 45=90, Delivered: expanded all 3248/Delivered1568. Original rows 2:25 exclude it.
Population labels	Active excludes only Cancelled and totals 1938; Delivered alone totals 1478. A numerically valid formula can answer the wrong question.
Copied references	With statuses Delivered/Pending, fixed source ranges and relative criteria should produce 1478/460. Verify copied formulas rather than assuming anchors.
Scope	Use this isolated AI Audit workbook and separate fixtures. Maintained workbook unchanged; independent PO025 challenge and learner timing pending.
```

### AI Boundary Cases A1:D5 - separate inputs

```text
Boundary fixture	Status	Amount (RM)	Expected qualifies
Below threshold	Pending	199.99	False
At threshold	Pending	200	True
Above threshold	Pending	200.01	True
Wrong status	Delivered	250	False
```

### AI Boundary Cases A8:E10 - boundary results

```text
Boundary metric	Actual >=200	Expected	Difference	Incorrect >200
Qualifying count	=COUNTIFS(B2:B5,"Pending",C2:C5,">=200")	2	=B9-C9	=COUNTIFS(B2:B5,"Pending",C2:C5,">200")
Qualifying amount	=SUMIFS(C2:C5,B2:B5,"Pending",C2:C5,">=200")	400.01	=ROUND(B10-C10,2)	=SUMIFS(C2:C5,B2:B5,"Pending",C2:C5,">200")
```

### AI Boundary Cases A15:E18 - final copied formulas

```text
Copy-reference test	Anchored source	Drifting source	Expected	Anchored difference
Delivered	=SUMIF(Orders!$G$2:$G$25,A16,Orders!$J$2:$J$25)	=SUMIF(Orders!G2:G25,A16,Orders!J2:J25)	1478	=B16-D16
Delivered	=SUMIF(Orders!$G$2:$G$25,A17,Orders!$J$2:$J$25)	=SUMIF(Orders!G3:G26,A17,Orders!J3:J26)	1478	=B17-D17
Pending	=SUMIF(Orders!$G$2:$G$25,A18,Orders!$J$2:$J$25)	=SUMIF(Orders!G4:G27,A18,Orders!J4:J27)	460	=B18-D18
```

### AI Repairs A1:E4 - deliberately flawed originals

```text
Supplied deliberate flaws	Original formula text (not Gemini output)	Actual	Expected claim	Verdict
All 24 records	=SUM(Orders!J2:J24)	=SUM(Orders!J2:J24)	3158	=IF(C2=D2,"Pass","Fail: excludes PO024 amount64")
IT99 confirmed zero rate	=IFERROR(VLOOKUP("IT99",Rates!A2:D7,3,FALSE), 0)	=IFERROR(VLOOKUP("IT99",Rates!A2:D7,3,FALSE), 0)	Missing rate	=IF(C3=D3,"Pass","Fail: missing mapping hidden as zero")
Active amount	=SUMIFS(Orders!J2:J25,Orders!G2:G25,"Delivered")	=SUMIFS(Orders!J2:J25,Orders!G2:G25,"Delivered")	1938	=IF(C4=D4,"Pass","Fail: Delivered is not Active")
```

### AI Repairs A7:E12 - checked manual replacements

```text
Manual repairs	Corrected formula text	Actual	Expected	Verdict
All 24 records	=SUM(Orders!$J$2:$J$25)	=SUM(Orders!$J$2:$J$25)	3158	=IF(C8=D8,"Pass","Review")
IT99 missing mapping	=IFNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE),"Missing rate")	=IFNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE),"Missing rate")	Missing rate	=IF(C9=D9,"Pass","Review")
Active excluding Cancelled	=SUMIFS(Orders!$J$2:$J$25,Orders!$G$2:$G$25,"<>Cancelled")	=SUMIFS(Orders!$J$2:$J$25,Orders!$G$2:$G$25,"<>Cancelled")	1938	=IF(C10=D10,"Pass","Review")
Known IT01 rate	=VLOOKUP("IT01",Rates!$A$2:$D$7,3,FALSE)	=VLOOKUP("IT01",Rates!$A$2:$D$7,3,FALSE)	45	=IF(C11=D11,"Pass","Review")
Missing-key diagnosis	=ISNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE))	=ISNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE))	True	=IF(C12=D12,"Missing confirmed","Review")
```

### AI Row Test A26:K26 - isolated TEST025 fixture

```text
TEST025	PJ-A	Planning	IT01	2	45	Delivered	4	Author range-coverage fixture	=E26*F26	=IF(G26="Cancelled",0,J26)
```

### AI Row Checks A1:D4 - original bounded controls

```text
New-row coverage baseline	Original bound result	Expected baseline	Difference
All Amount	=SUM('AI Row Test'!J2:J25)	3158	=B2-C2
Delivered Amount	=SUMIF('AI Row Test'!G2:G25,"Delivered",'AI Row Test'!J2:J25)	1478	=B3-C3
Record count	=COUNTA('AI Row Test'!A2:A25)	24	=B4-C4
```

### AI Row Checks A7:F10 - coverage comparison

```text
Coverage after append	Bounded 2:25	Expanded 2:26	Expected 25 records	Bounded shortfall	Expanded difference
All Amount	=B2	=SUM('AI Row Test'!J2:J26)	3248	=B8-D8	=C8-D8
Delivered Amount	=B3	=SUMIF('AI Row Test'!G2:G26,"Delivered",'AI Row Test'!J2:J26)	1568	=B9-D9	=C9-D9
Record count	=B4	=COUNTA('AI Row Test'!A2:A26)	25	=B10-D10	=C10-D10
```

### AI Row Checks A13:B17 - independent controls

```text
Independent controls	Value
Old 3158 plus new line	=3158+'AI Row Test'!J26
Unique test IDs	=COUNTUNIQUE('AI Row Test'!A2:A26)
Maintained Orders total	=SUM(Orders!J2:J25)
New row ID	='AI Row Test'!A26
```

### AI Test Matrix A12:B21 - final audit

```text
Observed casework results	Evidence and decision
Gemini threshold proposal	Fixed SUMIFS/COUNTIFS passed: amount 0 and count 0. Six Pending records sum 460, maximum 180.
Boundary proof	Pending 199.99/200/200.01 plus Delivered 250: >=200 gives count 2 and amount 400.01; >200 incorrectly gives 1 and 200.01.
Copy proof	Native Fill down: anchored 1478/1478/460; drifting1478/1388/412. Check source bounds and $ anchors after copying.
Supplied deliberate flaws	Truncated total 3094 versus 3158; IT99 wrapper 0 masks missing mapping; Delivered 1478 mislabelled Active 1938. These supplied examples are not Gemini outputs.
Manual corrections	All-range3158; exact IFNA lookup Missing rate with knownIT01=45; Active excluding Cancelled 1938. All match controls.
New-row proof	AI Row Test retains TEST025 at row 26, amount 90. Original 2:25 gives 3158/1478/24; expanded 2:26 gives 3248/1568/25 and zero differences.
Stale-control warning	Old baseline differences remain 0 after append because expected values are old. Use current population expectations to check coverage.
Generated visual proof	Gemini claimed a direct Dashboard link; actual chart uses generated A3:B6 number values. Source 2->3 changed live PJ-A980->1025 but snapshot stayed 980. Source restored 2.
Final state and limits	Maintained Orders and Dashboard restored; isolated fixture retained. Use live Dashboard for refreshed values and label generated snapshots. Independent PO025/pivot/chart extension, reviewer and 55-minute learner timing pending.
```

### Findings prompt

```text
Use only Dashboard A5:D8 and F5:G8 in this fictional workbook. A5:D8 has Project, All Amount (RM), Delivered (RM), Pending (RM): PJ-A980/556/64; PJ-B1204/578/276; PJ-C974/344/120. Status counts are Delivered 12/Pending6/Cancelled6. Give two descriptive findings with populations, RM values and supporting cell addresses. Do not use web research, edit cells, infer causes, forecast outcomes or invent ROI/benefit percentages. Distinguish all orders including Cancelled from Delivered only.
```

### Generated-chart prompt

```text
Generate a column chart comparing All Amount (RM), including Cancelled orders, by Project using only Dashboard A5:B8 in this fictional workbook. Show a chart preview first; do not change existing cells or the existing Dashboard chart. Title: Generated project amount - incl. Cancelled (RM). Tell me whether the chart follows Dashboard A5:B8 or uses separate generated data. I will test source refresh before accepting it.
```

The captured response claimed a direct Dashboard link, but actual Insert created its own tab/table A3:B6 with static numbers. Source E2:2->3 changed live PJ-A980->1025 and all 3158->3203; generated B4 stayed 980. Restore E2=2. The result is retained as **AI Generated Snapshot**. This observed behaviour is specific to the captured output; inspect and test future outputs rather than assuming their refresh mode.

### Pending threshold prompt

```text
Fictional training analysis. Propose formulas and a brief explanation only; do not edit cells. Orders has header row 1, Status in G, Amount in J,24 records in rows 2:25. Return SUMIFS for total Amount where Status equals Pending AND Amount is at least 200, and COUNTIFS for the qualifying record count. Fix all source row/column references with $ so copying the formula cannot shift source bounds. Include the exact >= boundary. I will test the proposals against a prewritten source audit and separate boundary fixture. Do not infer that a zero result proves there are no missing records.
```

### Native Fill-down setup

Enter A16:A18 as Delivered / Delivered / Pending. Enter only B16 **=SUMIF(Orders!$G$2:$G$25,A16,Orders!$J$2:$J$25)** and C16 **=SUMIF(Orders!G2:G25,A16,Orders!J2:J25)**. Select B16:C18 and Ctrl+D. Do not paste the final lower-row formulas before the copying test. Anchored results 1478/1478/460; drifting1478/1388/412.

### Test boundaries

TEST025 is added only to duplicated AI Row Test at row 26 after inserting a row above the copied totals. Keep actual Orders unchanged. Baseline 2:25 gives 3158/1478/24; expanded 2:26 gives 3248/1568/25. Old expected-baseline comparisons can still show 0 while the new row is omitted. This author fixture does not complete the independent PO025 pivot/chart-extension challenge.

Use IFNA to distinguish a missing exact lookup from a numeric zero; the IT99 test does not establish a confirmed zero rate. Supplied flawed formulas are deliberate case inputs, not actual Gemini responses in this run. Final findings are grounded in the maintained 24-record baseline. No causality, forecast or ROI is established.
