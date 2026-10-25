# 03 - Validate Entries and Flag Exceptions: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
=AND($G2="Pending",$J2>=200)
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Synthetic coverage record, test copy only: PO-TEST | PJ-A | Planning | IT01 | Quantity 5 | UnitCost 45 | Pending | week 4 | Coverage test. Quantity candidates: 0, 2, -1, 1.5, text “two”, blank and numeric text imported from a CSV.
```

## Captured Validation Reference

Use the separate Validation Practice tab. G2:G25: single-choice Delivered/Pending/Cancelled, strict Reject input. E2:E25: Custom formula is **=AND(ISNUMBER(E2),E2>=0,MOD(E2,1)=0)**, explicitly select Reject input (the custom editor defaulted to warning). Conditional format A2:K25: **=AND($G2="Pending",$J2>=200)**, light fill#b7e1cd. L2 uses that same formula, filled to25.

### Input expectations — Validation Tests A1:H11

Observed columns F:H start empty. Each entry test uses cell-edit mode, not a bulk-range paste. Restore E3=4 or G3=Pending after each accepted test; rejected input retains the original value. Test clearing separately with Delete and restore4 afterward.

```text
Case	Target	Input	Expected value rule	Expected UI	Observed UI	Result	Saved test value
V01	Quantity E3	0	Valid nonnegative whole zero	Accept
V02	Quantity E3	2	Valid positive whole number	Accept
V03	Quantity E3	-1	Invalid negative	Reject
V04	Quantity E3	1.5	Invalid fractional	Reject
V05	Quantity E3	two	Invalid text	Reject
V06	Status G3	Delivered	Allowed status	Accept
V07	Status G3	Pending	Allowed status	Accept
V08	Status G3	Cancelled	Allowed status	Accept
V09	Status G3	Ready	Not an allowed status	Reject
V10	Quantity E3	Clear cell	Blank is not numeric for a completed row	Observe clearing behavior
```

Nine ordinary cases matched accept/reject expectations. Delete cleared E3 without a blocking dialog while the custom rule remained. A blank is not a completed numeric Quantity: record the completeness limit rather than claiming requiredness is enforced. Bulk-range paste and CSV-imported numeric text remain untested.

### Exception expectations — Validation Tests A15:H20

Use temporary practice PO002 (row3), Quantity1 and the listed UnitCost/Amount; restore4/12/Pending after all five cases. Observed columns E:H start empty.

```text
Case	Status	Amount	Expected flag	Observed flag	Observed highlight	Qualifying OrderID	Result
X01	Pending	199	FALSE
X02	Pending	200	TRUE
X03	Pending	201	TRUE
X04	Delivered	200	FALSE
X05	Cancelled	200	FALSE
```

Actual flags/highlights were FALSE/none, TRUE/PO002, TRUE/PO002, FALSE/none, FALSE/none. The two positive rows in the report are sequential tests of one record. Delivered/Cancelled fail the status condition even at200.

### First/final-row coverage check

On the practice copy only, set row2 PO001 to Quantity1/UnitCost200/Pending and row25 PO024 to Quantity1/UnitCost201/Pending. Flags L2/L25 and row highlights are TRUE. Filter A1:L25 on PendingHigh TRUE:2of24 records, PO001 and PO024. Remove the filter; restore row2 to2/45/Delivered and row25 to8/8/Delivered. Leave row3 at4/12/Pending. Original24IDs and J/K formulas remain, totals3158/1938 and24FALSE flags.

### Handover notes — Validation Tests J1:K9

```text
Validation handover	Author-run guided and casework evidence
Restoration	Practice E3/F3/G3 restored to4/12/Pending. First row restored2/45/Delivered; final row restored8/8/Delivered. Filter removed.
Validation coverage	Validation Practice G2:G25: Delivered/Pending/Cancelled, single choice, Reject input. E2:E25 custom formula =AND(ISNUMBER(E2),E2>=0,MOD(E2,1)=0), Reject input.
Exception coverage	Conditional format A2:K25 uses =AND($G2="Pending",$J2>=200). Explicit flags L2:L25 use the same row logic.
Boundary reconciliation	First and final rows tested positive as PO001/Pending200 and PO024/Pending201; flags TRUE, both highlighted, filter showed2of24 matching IDs. All values now restored; baseline flags0.
Blank limit	Delete cleared E3 without a blocking dialog, while the custom rule remained. A complete row still needs numeric Quantity; do not claim requiredness is enforced by this input rule.
Input method limit	Tests used cell-edit mode with text pasted into the editor and Enter. Bulk range paste and CSV-imported numeric text were not tested.
Independent work pending	No PO-TEST row was appended. New-row rule/formula/format coverage diagnosis and repair, independent report, reviewer and learner timing remain pending.
Source boundary	Maintained Orders/Analysis/Rates and original Source Snapshot were not altered. Practice copy restored with24 original IDs and no current exceptions.
```

No PO-TEST row was appended. Independent new-row validation/formula/format coverage repair, bulk paste, CSV numeric text, reviewer and learner timing remain pending. Maintained Orders/Analysis/Rates and Source Snapshot were unchanged.
