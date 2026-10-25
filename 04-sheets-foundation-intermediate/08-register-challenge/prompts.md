# 08 - Complete the Register Challenge: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Check the handover
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Corrections and extension: T013 ActualCost becomes 150. Further-copy T014: Procurement | Verify submission checklist | Bala Kumar | week 4 | In Progress | planned 300 | actual 100. Keep all three states separate: original baseline, 13-record corrected challenge, 14-record extension.
```


## Captured Challenge Reference

T013 TSV for Tasks A14:H14:

```text
T013	Planning	Check the handover	Aina Rahman	4	Not Started	200	0
```

I14 =H14-G14. Live source totals/average/count and COUNTIF/SUMIF bounds include row14. PlannedCosts in this challenge is Tasks!G2:G14, retargeted from historical Sorting Practice!G2:G13. Status range Tasks F2:F14 (plus retained spare N2), strict canonical choices Complete/In Progress/Not Started. Commit through range picker and actually test the new cell; first compact text edit did not persist in the author run.

Before correction:13unique records,planned10600,actual6800,variance-3800,status4/4/5;Planning planned3000. Deliberate I14=H14-G13 gives-700 and total-4300 (mismatch-500), repaired to own-row H14-G14. After H14=150:rowvariance-50,actual6950,variance-3650,planned10600 and status4/4/5 unchanged. No extra sort was performed; all13variance formulas were inspected in the grid and metadata.

Summary actual check:

```text
=SUMIF(Tasks!B2:B14,"Planning",Tasks!H2:H14)+SUMIF(Tasks!B2:B14,"Procurement",Tasks!H2:H14)+SUMIF(Tasks!B2:B14,"Site Coordination",Tasks!H2:H14)
```

Change Log controls compare count/unique IDs, planned and actual team totals, variance sum versus actual-minus-planned, status population and named range. All differences0. Both saved views reopened with A1:I14:incomplete9IDs T002,T003,T005,T006,T008,T009,T011,T012,T013;Planning incomplete3IDs T002,T003,T013. No manual view-range edit needed in this session; both closed with13source rows visible.

Current PDF:GW-Register-Challenge-Corrected-r1.pdf,Summary A1:N28,one A3landscape page,13-record corrected state. Current native workbook's Tasks/Summary/Change Log are authoritative; inherited practice tabs and old outputs are history. Original12-record baseline unchanged at10400/6800/-3600/status4/4/4. Independent T014 and partner/timing checks pending.
