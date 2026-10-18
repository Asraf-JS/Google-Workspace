# 05 - Match Records and Handle Errors: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
LookupRate
```

```text
=VLOOKUP(D2,Rates!$A$2:$D$7,3,FALSE)
```

```text
=INDEX(Rates!$C$2:$C$7,MATCH(D2,Rates!$A$2:$A$7,0))
```

```text
=HLOOKUP(F4,$G$1:$L$2,2,FALSE)
```

```text
=IFNA(VLOOKUP("IT99",Rates!$A$2:$D$7,3,FALSE),"Unmapped item")
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Lookup challenge: Known IT01 and IT06; unknown IT99; blank; space-padded IT03. Duplicate-test mapping adds IT03 with UnitCost 99 only on a disposable copy. Baseline IT03 remains 30. Keep the supplied six-key Rates source intact.
```
