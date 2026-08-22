## Cumulative Transaction Total per User

```sql
SELECT
	user_id,
	id,
	transaction_date,
	amount,
	SUM(amount) OVER (
		PARTITION BY user_id
		ORDER BY transaction_date, id
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
	) AS running_total
FROM transactions
ORDER BY user_id, transaction_date, id;
```
