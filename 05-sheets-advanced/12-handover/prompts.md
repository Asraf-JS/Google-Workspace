# 12 - Review and Handover: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

Use the staged runbook text, exact formula blocks and native pivot actions below. Preserve the recovery baseline.


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Independent PO026, separate baseline-derived copy: PJ-B | Procurement | IT03 | Quantity 10 | UnitCost 30 | Pending | week 4 | Handover exception test. Do not combine it with PO025 unless you explicitly define and reconcile that additional scenario.
```

## Captured Author-Run Reference

Build the recovery copy **GW - Sheets Advanced - Handover Baseline** first. Copy it as a whole workbook for **GW - Sheets Advanced - PO025 Extension Test**. Paste only the current stage. Final formulas below are for the extension copy; do not overwrite the preserved24-order baseline.

### Runbook A1:B15 - version 1 before extension

```text
Runbook v1 - fictional procurement	Maintained 24-order baseline; extension work must use a separately named whole-workbook copy.
Source and grain	Orders A1:K25: one fictional order line per unique OrderID. Rates A1:D7: one authoritative row per ItemCode. RM amounts; numeric practice weeks1-4.
Accepted inputs	Projects PJ-A/PJ-B/PJ-C; Teams Planning/Procurement/Site Coordination; ItemCode must match exactly one Rates key; Quantity whole numeric >=0; Status Delivered/Pending/Cancelled; Week numeric1-4. Orders inputs require manual checks; validation practice is a separate fixed lab.
Editable fields	Orders A:I are inputs. F UnitCost is an evidenced input, not an automatic approval. Verify it against Rates. Do not type over formula columns J:K.
Formula columns	J=Quantity*UnitCost; K=IF(Status="Cancelled",0,Amount). Copy formulas to an added row and verify their actual references.
Populations	All Amount includes Cancelled. Active excludes Cancelled. Delivered excludes Pending and Cancelled. Pending>=200 requires BOTH conditions and inclusive >=.
Before update	Confirm24 unique IDs, all3158, active1938, Delivered1478, Pending460; 12/6/6 Delivered/Pending/Cancelled records. Close active filter view before interpreting all-source totals.
Source extension	On named extension copy only, insert a row above26 before totals; add PO025 PJ-A/Planning/IT01/2/45/Delivered/week4, Amount90. Extend input/formula bounds to26 and totals now at row28.
Dependent update	Use Range Inventory. Extend source-dependent analysis, weekly/count/DB ranges and both pivots. Fixed summary chart follows Dashboard A5:B8; sparkline follows weekly summary. Check source coverage rather than assuming refresh.
Expected scenario	25 unique IDs; all3248; active2028; Delivered1568; Pending460; PJA all1070/Delivered646. Week4 916; Delivered leader PJA646. Baseline remains unchanged.
Unknown/duplicate key route	Count exact Rates matches before using a rate. Count0=unmapped; count>1=conflict. Preserve unresolved warning; never replace missing with0 or overwrite Rates to hide the issue.
Exceptions and release	Resolve formula/range mismatches first. Record unknown keys as open issues. Release only a clearly labelled, checked training scenario; no purchasing/budget/performance decision is implied.
Historical practice scope	Source Snapshot and earlier Lookup/Validation/Logic/Text/Database test tabs are fixed lab evidence, not live dashboard inputs. Do not treat their old rows as updated source.
Review boundary	Author checks only. Partner review, independent PO026 challenge, spoken handover and50-minute classroom pilot remain pending.
Runbook test record	Version1 prepared before PO025 extension. Record unclear instructions and actual checks during the separate test; revise after evidence.
```

### Range Inventory A1:C14 - exact baseline bounds and update contract

```text
Component	Baseline bounds / role	Required extension action / verification
Source inputs + formulas	Orders A1:K25; J2:K25 formulas; J27/K27 totals	Insert above row26; add PO025 A26:K26; totals shift to28. Extend total SUM bounds to26. Check25 unique IDs and90 line amount.
Conditional amounts/counts	Analysis B4:D6/B9:D11; C14:D18; B28; source rows2:25	Extend all source endpoints25 to26 in active Analysis formulas; retain criteria and absolute anchors. Update population notes to25-order scenario.
Database functions	Database Analysis D10:D12/D15/D18:D20/D24:D26/D29; DB Orders A1:J25	Extend database rectangle toA1:J26 and source ranges to26; keep header/criteria rectangles unchanged. DSUM Delivered1568.
Native amount pivot	Pivot Review; source Orders A1:K25	Extend pivot source to Orders A1:K26, retain Project rows/Status columns/SUM Amount. Verify all3248/Delivered1568.
Native count pivot	Pivot Counts; source Orders A1:K25	Extend pivot source to Orders A1:K26, retain COUNTA OrderID. Verify25 total, Delivered13/Pending6/Cancelled6.
Summary source	Dashboard Data A1:D4 links Analysis; B8:B10 COUNTIF; B16:E16 weekly; B19:D19 controls	Source-dependent bounds end26. Fixed project/status/week summary shape stays; weekly728/754/850/916 and all3248. Rows22:28 are historical Lab9 predictions, not live results.
Dashboard controls	Dashboard B19/B21 and E20 source bounds2:25; summary links elsewhere	Extend source endpoints26; keep links to updated Analysis/Database Analysis/pivots. E19:E22 all0. E23 All checks pass.
Chart + sparkline	Dashboard chart uses A5:B8, sparkline B15 uses Dashboard Data B16:E16	Fixed summary ranges stay; verify chart PJA1070/PJB1204/PJC974 and weekly sparkline refresh. Update visible25-order scenario label.
Lookup mapping	Rates A2:D7 exact mapping; six unique ItemCodes	Do not extend Rates for PO025 IT01. Verify matchcount1/rate45. Unmapped IT99 stays unresolved on separate Key Handover tab.
Validation practice	Validation Practice E2:E25 whole-number Quantity>=0; G2:G25 Status list; separate fixed lab copy	Not the Orders input range. Do not claim source dropdown protection. Check accepted source inputs manually before release; document future validation deployment separately.
Conditional format practice	Validation Practice A2:K25; AND($G2="Pending",$J2>=200)	Fixed lab evidence. No Orders exception flag is implied. Active exception check is Analysis B28; separate Pending>=200 count must remain0 for PO025.
Filter views	Orders DB8 - Delivered and DB8 - Delivered AND PJ-A; inactive baseline	Keep named teaching views, close active view for all-source controls. In extension do not assume old saved-view range includes row26; verify its range if using it.
Historical snapshots/tests	Source Snapshot, drill-through Detail1, earlier Lookup/Logic/Text/Validation/Database test tabs	Preserve as fixed teaching evidence. They are outside maintained Dashboard refresh path; label release manifest accordingly, do not present old snapshots as current scenario.
```

### Extension Checks A1:C9 - predictions before appending

```text
PO025 extension controls	Original bounds2:25	Expected after PO025
Order count	=COUNTA(Orders!A2:A25)	25
All Amount (RM)	=SUM(Orders!J2:J25)	3248
Active Amount (RM)	=SUM(Orders!K2:K25)	2028
Delivered Amount (RM)	=SUMIF(Orders!G2:G25,"Delivered",Orders!J2:J25)	1568
PJ-A Delivered (RM)	=SUMIFS(Orders!J2:J25,Orders!B2:B25,"PJ-A",Orders!G2:G25,"Delivered")	646
Week4 all Amount (RM)	=SUMIFS(Orders!J2:J25,Orders!H2:H25,4)	916
Pending>=200 count	=COUNTIFS(Orders!G2:G25,"Pending",Orders!J2:J25,">=200")	0
Unique IDs	=COUNTUNIQUE(Orders!A2:A25)	25
```

### Orders A26:K26 - extension only, insert above26 first

```text
PO025	PJ-A	Planning	IT01	2	45	Delivered	4	Handover PO025 extension test - fictional	=E26*F26	=IF(G26="Cancelled",0,J26)
```

### Orders J27:K28 - extended total bounds

```text
Scenario All Amount	Scenario Active Amount
=SUM(J2:J26)	=SUM(K2:K26)
```

### Analysis B4:D6 - project/status amounts

```text
=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A4,Orders!$G$2:$G$26,B$3)	=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A4,Orders!$G$2:$G$26,C$3)	=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A4,Orders!$G$2:$G$26,D$3)
=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A5,Orders!$G$2:$G$26,B$3)	=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A5,Orders!$G$2:$G$26,C$3)	=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A5,Orders!$G$2:$G$26,D$3)
=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A6,Orders!$G$2:$G$26,B$3)	=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A6,Orders!$G$2:$G$26,C$3)	=SUMIFS(Orders!$J$2:$J$26,Orders!$B$2:$B$26,$A6,Orders!$G$2:$G$26,D$3)
```

### Analysis B9:D11 - project/status counts

```text
=COUNTIFS(Orders!$B$2:$B$26,$A9,Orders!$G$2:$G$26,B$8)	=COUNTIFS(Orders!$B$2:$B$26,$A9,Orders!$G$2:$G$26,C$8)	=COUNTIFS(Orders!$B$2:$B$26,$A9,Orders!$G$2:$G$26,D$8)
=COUNTIFS(Orders!$B$2:$B$26,$A10,Orders!$G$2:$G$26,B$8)	=COUNTIFS(Orders!$B$2:$B$26,$A10,Orders!$G$2:$G$26,C$8)	=COUNTIFS(Orders!$B$2:$B$26,$A10,Orders!$G$2:$G$26,D$8)
=COUNTIFS(Orders!$B$2:$B$26,$A11,Orders!$G$2:$G$26,B$8)	=COUNTIFS(Orders!$B$2:$B$26,$A11,Orders!$G$2:$G$26,C$8)	=COUNTIFS(Orders!$B$2:$B$26,$A11,Orders!$G$2:$G$26,D$8)
```

### Analysis C14:D18 - population amounts/counts

```text
=SUM(Orders!J2:J26)	=COUNTA(Orders!A2:A26)
=SUM(Orders!K2:K26)	=COUNTIF(Orders!G2:G26,"<>Cancelled")
=SUMIF(Orders!G2:G26,"Delivered",Orders!J2:J26)	=COUNTIF(Orders!G2:G26,"Delivered")
=SUMIF(Orders!G2:G26,"Cancelled",Orders!J2:J26)	=COUNTIF(Orders!G2:G26,"Cancelled")
=SUMIF(Orders!G2:G26,"Pending",Orders!J2:J26)	=COUNTIF(Orders!G2:G26,"Pending")
```

### Analysis B28 - Pending threshold count

```text
=COUNTIFS(Orders!G2:G26,"Pending",Orders!J2:J26,">=200")
```

### Analysis B30 - current scenario population note

```text
PO025 scenario all3248 includes Cancelled1220. Active2028 equals Delivered1568 plus Pending460. Original baseline3158/1938/1478 remains separate.
```

### Database Analysis D10:D12 - delivered database calculations

```text
=DSUM(Orders!A1:J26,"Amount",A10:A11)
=DCOUNT(Orders!A1:J26,"Quantity",A10:A11)
=DAVERAGE(Orders!A1:J26,"UnitCost",A10:A11)
```

### Database Analysis D15 - delivered independent control

```text
=SUMIF(Orders!G2:G26,"Delivered",Orders!J2:J26)
```

### Database Analysis D18:D20 - numeric/text counts

```text
=DCOUNT(Orders!A1:J26,"OrderID",A10:A11)
=DCOUNTA(Orders!A1:J26,"OrderID",A10:A11)
=COUNTIF(Orders!G2:G26,"Delivered")
```

### Database Analysis D24:D26 - Delivered AND PJ-A

```text
=DSUM(Orders!A1:J26,"Amount",A10:B11)
=DCOUNT(Orders!A1:J26,"Quantity",A10:B11)
=DAVERAGE(Orders!A1:J26,"UnitCost",A10:B11)
```

### Database Analysis D29 - AND independent control

```text
=SUMIFS(Orders!J2:J26,Orders!G2:G26,"Delivered",Orders!B2:B26,"PJ-A")
```

### Dashboard Data B8:B10 - status counts

```text
=COUNTIF(Orders!$G$2:$G$26,A8)
=COUNTIF(Orders!$G$2:$G$26,A9)
=COUNTIF(Orders!$G$2:$G$26,A10)
```

### Dashboard Data B16:E16 - numeric weeks

```text
=SUMIFS(Orders!$J$2:$J$26,Orders!$H$2:$H$26,B$15)	=SUMIFS(Orders!$J$2:$J$26,Orders!$H$2:$H$26,C$15)	=SUMIFS(Orders!$J$2:$J$26,Orders!$H$2:$H$26,D$15)	=SUMIFS(Orders!$J$2:$J$26,Orders!$H$2:$H$26,E$15)
```

### Dashboard Data B19 - source total control

```text
=SUM(Orders!J2:J26)
```

### Dashboard B19 - source count

```text
=COUNTA(Orders!A2:A26)
```

### Dashboard B21 - Active Amount

```text
=SUM(Orders!K2:K26)
```

### Dashboard E20 - all-source comparison

```text
=B20-SUM(Orders!J2:J26)
```

### Dashboard A2 - labelled scenario population

```text
PO025 extension test: all25 orders including Cancelled. Amount in RM; no dashboard filter. Historical practice tabs remain fixed.
```

### Extension Checks D2:E9 - observed values after refresh

```text
=COUNTA(Orders!A2:A26)	=D2-C2
=SUM(Orders!J2:J26)	=D3-C3
=SUM(Orders!K2:K26)	=D4-C4
=SUMIF(Orders!G2:G26,"Delivered",Orders!J2:J26)	=D5-C5
=SUMIFS(Orders!J2:J26,Orders!B2:B26,"PJ-A",Orders!G2:G26,"Delivered")	=D6-C6
=SUMIFS(Orders!J2:J26,Orders!H2:H26,4)	=D7-C7
=COUNTIFS(Orders!G2:G26,"Pending",Orders!J2:J26,">=200")	=D8-C8
=COUNTUNIQUE(Orders!A2:A26)	=D9-C9
```

### Extension Checks A12:B17 - independent reconciliation

```text
Independent cross-check	Result
All baseline3158 + new90	=3158+Orders!J26
Delivered baseline1478 + new90	=1478+Orders!J26
Native amount pivot total	='Pivot Review'!E6
Native count pivot total	='Pivot Counts'!E6
Dashboard status	=Dashboard!E23
```

### Key Handover A1:B4 - exact keys and match counts first

```text
Exact key test	Rates match count
IT01	=COUNTIF(Rates!$A$2:$A$7,A2)
IT99	=COUNTIF(Rates!$A$2:$A$7,A3)
IT02	=COUNTIF(Rates!$A$2:$A$7,A4)
```

### Key Handover C1:E4 - guarded rate/disposition afterward

```text
Guarded rate	Disposition	Amount allowed?
=IF(B2<>1,"Unresolved rate",VLOOKUP(A2,Rates!$A$2:$D$7,3,FALSE))	=IF(B2=1,"Mapped",IF(B2=0,"Open - unmapped key","Open - duplicate key"))	=IF(B2=1,"Use checked rate","Hold - no numeric amount")
=IF(B3<>1,"Unresolved rate",VLOOKUP(A3,Rates!$A$2:$D$7,3,FALSE))	=IF(B3=1,"Mapped",IF(B3=0,"Open - unmapped key","Open - duplicate key"))	=IF(B3=1,"Use checked rate","Hold - no numeric amount")
=IF(B4<>1,"Unresolved rate",VLOOKUP(A4,Rates!$A$2:$D$7,3,FALSE))	=IF(B4=1,"Mapped",IF(B4=0,"Open - unmapped key","Open - duplicate key"))	=IF(B4=1,"Use checked rate","Hold - no numeric amount")
```

### Key Handover A7:B10 - unresolved issue and source boundary

```text
Open issue K01	IT99 has no supplied Rates mapping. Fixture stays outside Orders and scenario totals.
Required evidence	A source owner must confirm the item/key/rate before a real mapping or monetary calculation. No owner response was requested in this walkthrough.
Baseline preservation	Rates A1:D7 unchanged; no invented0, no added mapping and no source order with IT99.
Limits	This guard tests exact mapping cardinality, not real purchasing authority or semantic correctness of a supplied price.
```

### Handover Issues A1:C7 - actual findings and repair

```text
Issue / observation	State	Evidence and disposition
K01 - IT99 mapping	Open - unresolved	Key Handover B3=0/C3=Unresolved rate. Hold numeric amount; obtain authoritative mapping evidence before any real use. No Rates changes made.
R01 - pivot commit instruction	Runbook repaired v2	Version1 said extend pivots but omitted explicit confirmation. Added Select data range -> Orders!A1:K26 -> OK, then reopen and verify both pivots. Count25 and amount3248 prove saved coverage.
R02 - historical practice coverage	Scope clarified	Validation Practice rules apply only there, not Orders. Historical snapshots/tests/old Lab9 prediction rows/old Dashboard Contract remain fixed evidence; release manifest identifies active scenario tabs.
R03 - independently expected controls	Added release gate	Stale Dashboard initially showed All checks pass at24/3158. Require predicted count25/all3248 plus independent source deltas and pivot reconciliation, not only internal zeros.
Automation note	Corrected before release	Typing a range into sidebar and pressing Enter did not persist in this attempt. Uncommitted captures excluded. Explicit picker + OK used and totals rechecked. This is not evidence of a learner error.
Independent checks	Pending	Real partner/reviewer, independent PO026 update, spoken handover and50-minute learner pilot have not been performed.
```

### Runbook A17:B20 - version 2 repair after testing

```text
Exact pivot update	Click inside Pivot Review -> pencil/Edit pivot table -> Select data range -> Orders!A1:K26 -> OK. Repeat for Pivot Counts. Reopen each editor to verify saved bounds. Expected totals3248 and25.
Chart check	Dashboard Chart editor Setup must still show A5:B8; data now1070/1204/974. Sparkline source Dashboard Data B16:E16 must now include916 at week4.
Independent release gate	Compare against predicted25/3248/2028/1568 before accepting zero differences. Old mutually stale summaries may show All checks pass while omitting the added row.
Version2 repair record	Added explicit range-picker confirmation, separate count-pivot check, accepted-input/manual-validation scope and historical-tab boundaries after the author extension test. No partner review or PO026 test is implied.
```

### Runbook A1:B3 - final version/accepted inputs clarification

```text
Runbook v2 - tested PO025 procedure	Use Release Manifest to distinguish the preserved24-order baseline from the25-order extension test. Never append the scenario to the baseline.
Source and grain	Orders A1:K25: one fictional order line per unique OrderID. Rates A1:D7: one authoritative row per ItemCode. RM amounts; numeric practice weeks1-4.
Accepted inputs	Projects PJ-A/PJ-B/PJ-C; Teams Planning/Procurement/Site Coordination; ItemCode must match exactly one Rates key; Quantity whole numeric >=0; Status Delivered/Pending/Cancelled; Week numeric1-4. Orders inputs require manual checks; validation practice is a separate fixed lab.
```

### Release Summary A1:D12 - fixed columnB with live comparisons C:D

```text
FIXED SNAPSHOT - PO025 test	46322	B fixed; C:D live checks	Regenerate snapshot B after update
Population	25 fictional Orders A1:K26	All includes Cancelled	Source baseline preserved separately
Metric	Snapshot value	Checked live value	Difference
Order count	25	=Dashboard!B19	=B4-C4
All Amount (RM)	3248	=Dashboard!B20	=B5-C5
Active Amount (RM)	2028	=Dashboard!B21	=B6-C6
Delivered Amount (RM)	1568	=Dashboard!B22	=B7-C7
PJ-A all Amount (RM)	1070	=Dashboard!B6	=B8-C8
Delivered leader	PJ-A	=Dashboard!B25	=IF(B9=C9,"Match","Review")
Delivered leader Amount (RM)	646	=Dashboard!C25	=B10-C10
Peak practice week	4	=Dashboard!B27	=IF(B11=C11,"Match","Review")
Peak week Amount (RM)	916	=Dashboard!C27	=B12-C12
```

### Release Manifest A1:B11 - retained role manifest

```text
Release manifest - training handover	27 October2026; author-checked PO025 extension. No real project approval or external handover is implied.
Maintained recovery baseline	GW - Sheets Advanced - Handover Baseline: Orders24/all3158/active1938/Delivered1478; Runbook v2 and Range Inventory. Original GW - Sheets Advanced - Analysis remains unchanged.
Scenario test	GW - Sheets Advanced - PO025 Extension Test: Orders25/all3248/active2028/Delivered1568. PO025 included exactly once; no PO026. Keep separate from recovery baseline.
Active refresh path	Orders -> Analysis / Database Analysis / Pivot Review / Pivot Counts -> Dashboard Data -> Dashboard. Extension Checks independently compares predictions, source deltas and pivot totals.
Current fixed summary	In GW - Sheets Advanced - PO025 Extension Test, Release Summary columnB holds fixed values dated27October2026; C:D are live comparison checks. Regenerate the snapshot after later updates. It is not a new live data source.
Range contract	Active source ends row26; database header rectangle A1:J26; both pivots Orders!A1:K26 confirmed with picker+OK. Chart remains Dashboard A5:B8; weekly sparkline follows Dashboard Data B16:E16.
Open issue	K01 IT99 stays Unresolved rate/Open-unmapped/Hold. It is a separate fixture, excluded from Orders and totals. Rates six-key mapping is unchanged.
Historical evidence	All other practice/test tabs including Source Snapshot, drill-through Detail1, Dashboard Contract and Dashboard Data rows22:28 remain fixed earlier-lab evidence. They are not refreshed scenario outputs.
Review state	Author walkthrough and fresh runbook read-through only. Independent PO026, actual partner/reviewer, spoken handover and50-minute classroom pilot remain pending.
Repair record	Handover Issues records the explicit pivot confirmation repair, stale-control release gate and manual-validation boundary. Baseline/scenario count and exact source names must be checked before reuse.
Next class recovery	Open Handover Baseline and confirm24/3158/1938/1478 with inactive named views. Do not merge PO025 or unresolved keys into that baseline.
```

### Native objects - do not replace pivots with pasted output

In BOTH native Pivot Review and Pivot Counts: click inside the pivot, use the pencil/Edit pivot table, choose Select data range, type **Orders!A1:K26**, then **OK**. Reopen to confirm saved bounds. The amount pivot keeps SUM Amount; count pivot keeps COUNTA OrderID. Both retain Project rows and Status columns. Do not include the copied total rows 27:28. Merely typing a different sidebar value did not persist in the author attempt; the picker+OK path was verified.

Chart Setup stays Dashboard A5:B8. Verify the bars change980/1204/974 ->1070/1204/974. Weekly source Dashboard Data B16:E16 changes728/754/850/826 ->728/754/850/916; Dashboard B15 SPARKLINE follows it. Update source/formula/pivot coverage, not the fixed three-project chart shape.

Before adding PO025, Extension Checks B2:B9 uses original rows 2:25 and D is blank. Keep that original-bound column after adding the record. Predictions inC are25/3248/2028/1568/646/916/0/25. After refresh paste D2:E9, label E1 Difference. In the recorded stale state Dashboard was green at24/3158 despite PO025 already existing at row 26. Require independently expected counts and totals as well as zero differences.

Quantity must be a whole nonnegative number; validate Orders inputs manually. Native Quantity/Status rules and conditional formatting on Validation Practice belong to that fixed practice tab and do not protect Orders. Existing historical test/snapshot tabs stay outside the current scenario refresh path. Keep this boundary in the manifest.

Release Summary B4:B12 contains literals forming a dated fixed snapshot; C:D are live comparisons. That sheet is in the PO025 Extension Test workbook. The recovery copy contains the same role manifest, not a second scenario source. Keep K01 open until authoritative key/rate evidence is provided. No external sharing or owner contact was performed.

The fresh-view runbook navigation was an author read-through after closing the previous extension working browser tab. It does not establish independent partner success. The separate PO026 challenge remains unperformed; do not combine PO026 with PO025 without defining and reconciling another scenario.
