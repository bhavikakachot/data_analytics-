## Ranking Each User's Playlists

```sql
SELECT
	playlist_name,
	user_id,
	total_likes,
	DENSE_RANK() OVER (
		PARTITION BY user_id
		ORDER BY total_likes DESC
	) AS dense_rank
FROM Playlists
ORDER BY user_id, total_likes DESC;
```
