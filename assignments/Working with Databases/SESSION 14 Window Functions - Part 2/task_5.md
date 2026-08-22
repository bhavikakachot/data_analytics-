## Three-Order Moving Average per User

```sql
SELECT
	user_id,
	order_id,
	order_date,
	total_amount,
	SUM(total_amount) OVER (
		PARTITION BY user_id
		ORDER BY order_date, order_id
		ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
	) / COUNT(*) OVER (
		PARTITION BY user_id
		ORDER BY order_date, order_id
		ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
	) AS moving_avg
FROM Orders
ORDER BY user_id, order_date, order_id;
```
