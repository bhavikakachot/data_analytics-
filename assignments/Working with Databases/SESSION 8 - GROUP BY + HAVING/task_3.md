## Calculate Total Spend by User

```sql
SELECT user_id, SUM(amount) AS total_spend
FROM Orders
GROUP BY user_id;
```
