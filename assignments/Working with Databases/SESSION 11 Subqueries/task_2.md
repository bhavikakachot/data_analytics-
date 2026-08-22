## Count Orders for Each User

```sql
SELECT
	u.username,
	(
		SELECT COUNT(*)
		FROM Orders AS o
		WHERE o.user_id = u.id
	) AS order_count
FROM Users AS u;
```
