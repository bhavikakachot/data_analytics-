## Ranking Playlists by Total Likes

```sql
SELECT
	playlist_name,
	user_id,
	total_likes,
	RANK() OVER (ORDER BY total_likes DESC) AS playlist_rank
FROM Playlists
ORDER BY total_likes DESC;
```
