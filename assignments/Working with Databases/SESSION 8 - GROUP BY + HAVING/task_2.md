## Count Orders by Payment Method

```sql
SELECT payment_method, COUNT(*) AS order_count
FROM Orders
GROUP BY payment_method;
```
