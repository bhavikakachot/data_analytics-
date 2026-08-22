## Display All Playlists and Their Songs

Use a `LEFT JOIN` because it keeps every row from the `playlists` table, even when no matching song exists. An `INNER JOIN` would remove empty playlists, while a `RIGHT JOIN` would preserve every song instead.

Assuming the songs are stored in a `songs` table with a `playlist_id` foreign key:

```sql
SELECT
	p.name AS playlist_name,
	s.song_name
FROM playlists AS p
LEFT JOIN songs AS s
	ON p.playlist_id = s.playlist_id;
```

Empty playlists appear with `NULL` for `song_name`.
