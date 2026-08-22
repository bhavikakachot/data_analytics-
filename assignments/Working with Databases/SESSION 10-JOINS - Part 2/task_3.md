## Display Users, Orders, and Payments

```sql
SELECT
	u.username,
	o.order_date,
	p.amount AS payment_amount
FROM Users AS u
LEFT JOIN Orders AS o
	ON u.id = o.user_id
LEFT JOIN Payments AS p
	ON o.id = p.order_id;
```

The `LEFT JOIN`s keep all users in the results. Users without orders or payments show `NULL` for the related columns.
