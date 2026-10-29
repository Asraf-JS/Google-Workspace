# 03 - Calculate and Copy Formulas: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Variance
```

```text
=H2-G2
```

```text
=SUM(G2:G13)
```

```text
=SUM(H2:H13)
```

```text
=SUM(I2:I13)
```

```text
=AVERAGE(G2:G13)
```

```text
=COUNT(G2:G13)
```

```text
Practice multiplier
```

```text
=G2*$L$9
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Calculation pairs Planned/Actual: 100/80; 100/120; 100/0; 100/blank. The final blank means “not supplied” for this test, not a confirmed zero. Use this to distinguish calculation mechanics from data meaning.
```


## Captured Reference Ranges

Tasks: I1 Variance; I2 **=H2-G2**, fill I2:I13. Summary K1:L7: L2 **=SUM(G2:G13)** →10400; L3 **=SUM(H2:H13)** →6800; L4 **=SUM(I2:I13)** →-3600; L6 **=AVERAGE(G2:G13)** →866.666… (display RM866.67); L7 **=COUNT(G2:G13)** →12.

Navigation Practice: clear prior Lab 2 examples J2:K6 and reset J2:J13 to Number. K9 Practice multiplier; L9 1.1; J2 `=G2*$L$9`, fill to J13. Change 1.1→1.2→1.1; first/final results 660/770→720/840→660/770.

Calculation Tests: A1:D5 four pairs and interpretation, C2:C4 **=B2-A2** filled down gives -20,20,-100; B5/C5 stay empty. A8:D11 zero/blank/text tests give COUNT 1/0/0 and SUM 0/0/0. C2 deliberately wrong **=B3-A2** gives 20, repaired **=B2-A2** gives-20. A14:D16 retains the observed test history. F2:F5 are 100, G2 `=F2*K2`, H2 `=F2*$K$2`, fill G2:H5. K2 1.1→1.2→1.1; G3/G5 drift to empty K3/K5 while H3/H5 stay anchored. A19:D20 records restoration. B24 **=SUM(Tasks!I2:I13)** and B25 **=SUM(Tasks!H2:H13)-SUM(Tasks!G2:G13)** both give-3600; B26 **=B24-B25** gives 0.

The source twelve records remain unchanged. Independent estimate/omitted-range challenge and classroom timing are pending. Lab 2 values-only target-format preservation remains a separate unresolved check.
