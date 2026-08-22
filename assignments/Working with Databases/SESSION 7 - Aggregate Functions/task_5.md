## Calculate Total Sales

```sql
SELECT SUM(total_amount) AS total_sales
FROM Orders
WHERE total_amount IS NOT NULL;
```
