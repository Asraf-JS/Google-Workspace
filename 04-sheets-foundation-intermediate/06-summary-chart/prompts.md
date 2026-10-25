# 06 - Summarise and Visualise: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
=COUNTIF(Tasks!$F$2:$F$13,A2)
```

```text
=SUM(B2:B4)
```

```text
Task count by status
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Troubleshooting card: A status chart shows Complete, In Progress, Not Started and Total. Another summary says 4, 4 and 0 even though 12 task rows remain. Investigate source range and exact criterion spelling before altering the chart design.
```


## Captured Conditional Summary Reference

```text
=SUMIF(Tasks!$B$2:$B$13,D2,Tasks!$G$2:$G$13)
```

Gemini prompt (panel explanation only):

```text
Explain this formula in the panel only: =COUNTIF(Tasks!$F$2:$F$13,A2). Explain the anchored range and the relative criterion cell, including what changes when filled to B3. Use only this formula and this fictional workbook. Do not edit cells, create charts, or apply changes.
```

Baseline: status4/4/4, total12; team planned2800/4000/3600, grand total10400. Summary B2:B4 uses COUNTIF with fixed Tasks F2:F13 and relative A2/A3/A4; E2:E4 uses SUMIF with fixed Tasks B2:B13 and G2:G13 and relative D2/D3/D4.

Summary Checks G2:J4: Task count H3=B5, I3=COUNTA(Tasks!A2:A13), J3=H3-I3; Planned cost (RM) H4=SUM(E2:E4), I4=SUM(Tasks!G2:G13), J4=H4-I4. Both differences zero.

Chart titles: Task count by status (A1:B4), Planned cost by team (RM) (D1:E4). On Chart Range Tests, A1:B5 deliberately plots Total12 as a fourth category; repair to A1:B4 using Select data range and OK. Misspell A4 Not Startd: COUNTIF0, total8, difference-4; repair label to Not Started, retaining the formula.

Temporary source tests: Tasks F4 Not Started→Complete gives5/4/3, then restore Not Started. Tasks G4 500→600 gives I4-600, Planning2900 and both planned totals10500; restore500 gives I4-500, Planning2800 and10400. Source values/formulas restored. Summary Test Log retains observations. Independent dashboard/reviewer and learner timing pending.
