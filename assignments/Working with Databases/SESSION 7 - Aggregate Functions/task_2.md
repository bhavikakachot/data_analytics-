## Count Orders by User

```sql
SELECT user_name, COUNT(*) AS order_count
FROM Orders
GROUP BY user_name;
```
