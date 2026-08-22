## Users With More Than 1,000 Followers

```sql
WITH popular_users AS (
	SELECT *
	FROM Users
	WHERE followers > 1000
)
SELECT *
FROM popular_users;
```
