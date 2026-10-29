# 07 - Share and Prepare Output: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

This chapter uses the supplied files and visible controls. No additional prompt or typed code is required.

## Part 1: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Output brief: Sponsor wants a readable summary of the 12-task baseline and planned costs. Contributor needs all task rows and labels. Exclude Entry Practice, temporary rule tests and unrelated helper notes from the sponsor handout.
```

## Part 2: Captured Output Reference

Actual access display: Restricted, one listed owner; no additional people/groups or inherited group access displayed. Roles are proposed only; no invitation or recipient access test. Publish to the web says not published and was closed without Publish.

Register logical scope: Tasks A1:I13, twelve records/nine fields. Register Output is a separate layout copy bounded by removing J:Z and rows 14:1000. Current sheet PDF, A3 landscape, custom break after row 7 at 100%, repeated frozen row 1: page 1 T001–T006, page 2 T007–T012. GW-Task-Listing-r1.pdf has 2 pages.

Sponsor logical scope: Summary A1:N28. Initial A1:J28 clips the cost chart. A3 landscape / Fit to width; all counts 4/4/4, total 12, team planned 2800/4000/3600, total 10400, zero differences, two complete charts. Native Download as PDF opens Export; Print's Next opens a browser dialog. Recheck Selected cells after each opening.

Revision test: GW-Sponsor-Summary-r1.pdf, 1 page, heading Status; temporarily change Summary A1 to Task status; export GW-Sponsor-Summary-r2.pdf, 1 page, changed heading/same numeric controls. Original r1 SHA256 unchanged. Restore source A1 Status. Latest fixed demonstration r2 retains its changed heading; restored live source and fixed copy are documented separately in Output Plan.

Native exports and JSON manifest are linked in the lesson. All four pages were rendered and checked at approximately 10.7 pt on A3. Page-number option did not produce visible footers in the downloaded PDFs; repeated header was verified. Independent outputs/reviewer and learner timing remain pending.

## Part 3: Output Plan Labels

Section 7.4. Put the plan in A1:B10 and the export manifest from A12 down. Write your own entry for each row in column B.

Output Plan, A1:A10 (step 1), with `Output brief and actual access record` in B1:

```text
Item
Maintained source
Contributor proposal
Sponsor proposal
Actual access inspected
Role explanation
Publication check
Register scope
Sponsor scope
Revision plan
```

Export manifest, A12:A22 (step 22), with `Scope, settings and verified revision` in B12:

```text
Export manifest
GW-Sponsor-Summary-r1.pdf
GW-Sponsor-Summary-r2.pdf
GW-Task-Listing-r1.pdf
Source restored
Summary r1 SHA256
Summary r2 SHA256
Register SHA256
Access and publication
PDF check boundary
Remaining learner checks
```

The SHA256 rows are optional on Windows: `certutil -hashfile GW-Sponsor-Summary-r1.pdf SHA256` in Command Prompt prints the hash. If you can't run it, record each file's size and modified time instead.
