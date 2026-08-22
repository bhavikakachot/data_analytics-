## Running Total of Orders per User

```sql
SELECT
	user_id,
	order_id,
	order_date,
	total_amount,
	SUM(total_amount) OVER (
		PARTITION BY user_id
		ORDER BY order_date, order_id
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
	) AS running_total
FROM Orders
ORDER BY user_id, order_date, order_id;
```
