# 10 - Use Gemini as an Analysis Partner: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 2: Propose a Delivered Total

**Session:** new chat | **Grounding:** explicit Orders schema

```text
Goal: Propose a formula for delivered order amount.
Context: Fictional Google Sheets analysis.
Source: Orders rows 2 to 25; Status is G and Amount is J. Header row is 1.
Expectations: Reply with a formula and explanation only. Do not edit cells. Include only Status equal to Delivered. Use bounded ranges. I will test the formula against the source.
```

Replace bracketed source placeholders before submitting. Keep a human check between an AI proposal and the final output.


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Flawed formula proposals to audit if AI is unavailable: `=SUM(Orders!J2:J24)` described as all 24 rows; `=IFERROR(VLOOKUP("IT99",Rates!A2:D7,3,FALSE),0)` described as a confirmed zero rate; `=SUMIFS(Orders!J2:J25,Orders!G2:G25,"Delivered")` described as active amount excluding only Cancelled.
```
