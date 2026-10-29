# 02 - Enter and Format Reliable Data: Prompts

Copy the values below when following the chapter. Review pasted text before submitting it.

Use the supplied source and the explicit practice values below. Keep dates and type tests outside the original register.

## Part 1: Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Formatting intake: PlannedCost “RM 600” supplied as text; DueWeek “next Monday” with no agreed calendar start; a long Task description clipped in a narrow column. Treat type, missing date evidence and presentation as three different issues.
```

## Part 2: Exact Practice Values

- Source costs: Tasks!G2:H13, custom Malaysian Ringgit **RM1,000** without decimals.
- Source week indices: Tasks!E2:E13, custom number format **0**.
- Practice date: **2026-10-24**, displayed **24/10/2026** in the reference locale; not a confirmed project start.
- Navigation Practice: J2 date; J4:K4 Numeric cost / Text cost; J5 numeric 600, K5 text RM 600.

Entry Practice type block: A7:B12, labelled numeric 600 / text RM 600 / week 2 / practice date. B14 **=SUM(B9:B10)** gives 600; B15 **=COUNT(B9:B10)** gives 1. Both formulas reference the cells as a range; the observed result does not establish behaviour for every possible way of passing text to a function.

Paste comparison: D9 normal paste from B9 gives numeric 600 with currency format; F9 format-only retains 123 and displays RM123. **Values-only target-format preservation remains unverified**: both shortcut and menu carried the RM format in this controlled session after setting E9 to number format 0. Repeat manually and compare formats as well as values. Do not claim this property-transfer check passed.

Source controls: **=COUNT(Tasks!G2:H13)** gives 24; **=COUNT(Tasks!E2:E13)** gives 12. All twelve source records retain their original underlying values. The source header already had readable contrast and its widths were retained; wrapping and Fit to data were applied. Entry Practice header/widths/wrapping were improved. Independent intake repair, partner test and classroom timing remain pending.
