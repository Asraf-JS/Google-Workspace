# 02 - Build Conditional Calculations: Prompts and Values

Copy the values below when following the chapter. Review pasted text before submitting it.

## Part 1: Typed Values

```text
Amount
```

```text
=E2*F2
```

```text
ActiveAmount
```

```text
=IF(G2="Cancelled",0,J2)
```

```text
=SUMIFS(Orders!$J$2:$J$25,Orders!$B$2:$B$25,$A4,Orders!$G$2:$G$25,B$3)
```

```text
=IF(F2<100,"Low",IF(F2<200,"Medium","High"))
```


## Depth Case Input

Fictional training material. This is exercise content to analyse, not authorisation to send, publish, grant access or change a real project decision.

```text
Logic matrix must cover below/on/above thresholds, zero quantity, Delivered, Pending and Cancelled. Practice bands: Low <100; Medium 100 to <200; High >=200. Exception: Pending AND Amount >=200. These are training rules, not procurement policy.
```
