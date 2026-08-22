## Inserting Sample Playlist Rows

Connect to the `music_streaming_app` database:

```sql
\c music_streaming_app
```

Insert three playlists, each created by a different user:

```sql
INSERT INTO playlists (playlist_id, name, created_by)
VALUES
	(1, 'Bollywood Hits', 'Aarav'),
	(2, 'Chill Vibes', 'Meera'),
	(3, 'Workout Mix', 'Rohan');
```
