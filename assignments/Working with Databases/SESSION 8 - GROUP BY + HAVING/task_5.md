## Difference Between `WHERE` and `HAVING`

`WHERE` filters individual rows before grouping. This query counts orders of at least 300 for each payment method:

```sql
SELECT payment_method, COUNT(*) AS order_count
FROM Orders
WHERE amount >= 300
GROUP BY payment_method;
```

`HAVING` filters groups after aggregation. This query shows payment methods whose total order amount exceeds 1,000:

```sql
SELECT payment_method, SUM(amount) AS total_amount
FROM Orders
GROUP BY payment_method
HAVING SUM(amount) > 1000;
```
