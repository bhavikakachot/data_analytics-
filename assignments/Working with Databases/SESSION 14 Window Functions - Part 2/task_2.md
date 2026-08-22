## Previous Order Amount for Each User

```sql
SELECT
	user_id,
	order_id,
	order_date,
	LAG(total_amount) OVER (
		PARTITION BY user_id
		ORDER BY order_date, order_id
	) AS previous_order_amount
FROM Orders
ORDER BY user_id, order_date, order_id;
```
