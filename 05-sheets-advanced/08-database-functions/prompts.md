# 08 - Query Structured Criteria: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Delivered amount
```

```text
=DSUM(Orders!A1:J25,"Amount",A10:A11)
```

```text
Delivered numeric quantity records
```

```text
=DCOUNT(Orders!A1:J25,"Quantity",A10:A11)
```

```text
Average delivered unit cost
```

```text
=DAVERAGE(Orders!A1:J25,"UnitCost",A10:A11)
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Criteria cases: Status=Delivered AND Project=PJ-A; Status=Delivered OR Status=Pending; Status=Delivered OR Project=PJ-A. The last case overlaps. DCOUNT uses numeric Quantity; OrderID is text and must not be treated as a numeric record count.
```
