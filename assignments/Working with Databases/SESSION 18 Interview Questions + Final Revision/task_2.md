## Total Order Amount per User

```sql
SELECT
	u.username,
	SUM(o.amount) AS total_order_amount
FROM users AS u
JOIN orders AS o
	ON o.user_id = u.user_id
GROUP BY u.user_id, u.username
ORDER BY total_order_amount DESC;
```
