## Artists With More Than 3 Songs

```sql
SELECT
	artist_name,
	COUNT(*) AS total_songs
FROM songs
GROUP BY artist_name
HAVING COUNT(*) > 3
ORDER BY total_songs DESC;
```
