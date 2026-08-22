## Top 2 Playlists per User

```sql
WITH ranked_playlists AS (
	SELECT
		playlist_name,
		user_id,
		total_likes,
		ROW_NUMBER() OVER (
			PARTITION BY user_id
			ORDER BY total_likes DESC, id ASC
		) AS playlist_rank
	FROM Playlists
)
SELECT
	playlist_name,
	user_id,
	total_likes,
	playlist_rank
FROM ranked_playlists
WHERE playlist_rank <= 2
ORDER BY user_id, playlist_rank;
```
