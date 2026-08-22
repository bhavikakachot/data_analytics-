## Find Movies with Five-Star Reviews

```sql
SELECT id, title
FROM Movies
WHERE id IN (
	SELECT movie_id
	FROM Reviews
	WHERE rating = 5
);
```
