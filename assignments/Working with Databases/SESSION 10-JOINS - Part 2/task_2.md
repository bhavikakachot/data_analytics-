## Display Playlists with Parent Names

```sql
SELECT
	child.playlist_name,
	child.user_id,
	parent.playlist_name AS parent_playlist_name
FROM Playlists AS child
LEFT JOIN Playlists AS parent
	ON child.parent_playlist_id = parent.id;
```

The `LEFT JOIN` keeps top-level playlists, which have no parent, with `NULL` for `parent_playlist_name`.
