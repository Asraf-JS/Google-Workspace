# 05 - Link and Explain Project Data: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
=COUNTIF(Tasks!$F$2:$F$13,A2)
```

```text
Pilot task status
```

## Part 2: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
New-record challenge: T013 | Planning | Check the handover | Aina Rahman | 4 | Not Started | 200 | 0. This belongs only in the challenge copy. A copied presentation may keep links to its original source; prove the source identity.
```

## Part 3: Source and Destination for the Captured Setup

```text
GW - Slides - Linked Data Source
Summary!A1:B4
Tasks!F2:F13
Summary!B2: =COUNTIF(Tasks!$F$2:$F$13,A2)
Summary!B3: =COUNTIF(Tasks!$F$2:$F$13,A3)
Summary!B4: =COUNTIF(Tasks!$F$2:$F$13,A4)
Pilot task status
12-task snapshot
4 tasks per status
Not evidence of pilot success
```

The native source is a separate conversion of the original supplied Excel starter. Keep the absolute task range and relative criterion when filling down. Baseline counts are Complete 4, In Progress 4, Not Started 4. At the setup stage, the source/chart identity is checked. The guided reference then tests refresh/restoration and the extended comparison in 5.3 to 5.4. Independent new-row repair remains pending.

## Part 4: Proposed Status Definitions for Notes

```text
Not Started: work on the task has not begun.
In Progress: work has begun but the owner has not confirmed completion.
Complete: the task owner has confirmed that the agreed task output is ready for review.
```

These are proposed training definitions from reporting guidance v1, not approved company policy. Counts do not prove on-time final-two-weeks submissions or efficiency savings.

## Part 5: Team Costs Summary

Create a sheet named **Team Costs** and paste into A1. The total row reconciles the data; chart only A1:B4.

```text
Team	Planned cost (RM)
Planning	=SUMIF(Tasks!$B$2:$B$13,A2,Tasks!$G$2:$G$13)
Procurement	=SUMIF(Tasks!$B$2:$B$13,A3,Tasks!$G$2:$G$13)
Site Coordination	=SUMIF(Tasks!$B$2:$B$13,A4,Tasks!$G$2:$G$13)
Total	=SUM(B2:B4)
```

Expected: Planning 2800, Procurement 4000, Site Coordination 3600, total 10400. These supplied row-level planned costs are separate from the unapproved RM 12000 proposed budget ceiling.

## Part 6: Comparison and Restoration Log

```text
Source: GW - Slides - Linked Data Source
Status range: Summary!A1:B4; COUNTIF over Tasks!F2:F13
Cost range: Team Costs!A1:B4; SUMIF over Tasks!B2:B13 and Tasks!G2:G13
Baseline: 12 tasks; Complete 4; In Progress 4; Not Started 4
Temporary input: T003, Tasks!F4, Complete
Changed status counts: 5 / 4 / 3
Linked chart: changes after Update; surrounding text needs a separate check
Static comparison only: Paste unlinked; remains 4 / 4 / 4; no Update
Costs during status-only test: 2800 / 4000 / 3600; total RM 10400
Restore T003: Not Started; source and linked status return to 4 / 4 / 4
Refresh both linked objects; retain labelled static comparison in a skipped slide
```

Privately record the actual source and destination URLs before testing. Do not infer pilot success, approved spending or savings from these charts. The independent 13-record challenge is not part of the guided baseline.
