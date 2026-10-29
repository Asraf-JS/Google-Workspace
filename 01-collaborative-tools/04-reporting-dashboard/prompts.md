# 04 - Clean, Calculate and Stress-Test a Reporting Dashboard: Prompts

## Part 1: Guided Formulas
```text
Tasks!I2: =H2-G2
Summary!B2: =COUNTIF(Tasks!$F$2:$F$13,A2)
Summary!B6: =SUM(B2:B4)
Summary!E2: =SUMIF(Tasks!$B$2:$B$13,D2,Tasks!$G$2:$G$13)
Summary!F2: =SUMIF(Tasks!$B$2:$B$13,D2,Tasks!$H$2:$H$13)
Summary!G2: =F2-E2
```
Enter formulas in the named cells without the `Tasks!I2:` labels. The fixed ranges are intentional: diagnose and repair them during the new-record challenge.
## Part 2: Labels
```text
Team | Planned | Actual | Variance
Planning
Procurement
Site Coordination
Pilot task status
```
## Part 3: Status Intake Headings
```text
Record | Raw status | Normalised status | Reason
```
Copy the inputs from masterclass-challenges.txt. Do not paste them into the original Tasks statuses.
