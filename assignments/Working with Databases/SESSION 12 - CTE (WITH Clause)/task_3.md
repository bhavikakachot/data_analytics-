## Top Users and Posts

```sql
WITH top_users AS (
	SELECT user_id, username, followers
	FROM Users
	ORDER BY followers DESC
	LIMIT 3
),
top_posts AS (
	SELECT post_id, content, likes
	FROM Posts
	ORDER BY likes DESC
	LIMIT 3
)
SELECT
	'Top User' AS item_type,
	user_id AS item_id,
	username AS item_name,
	followers AS engagement_count
FROM top_users

UNION ALL

SELECT
	'Top Post' AS item_type,
	post_id AS item_id,
	content AS item_name,
	likes AS engagement_count
FROM top_posts;
```
