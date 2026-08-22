## Numbering Playlists by Total Likes

```sql
SELECT
	ROW_NUMBER() OVER (ORDER BY total_likes DESC, id ASC) AS row_number,
	id,
	user_id,
	playlist_name,
	total_likes
FROM Playlists;
```
