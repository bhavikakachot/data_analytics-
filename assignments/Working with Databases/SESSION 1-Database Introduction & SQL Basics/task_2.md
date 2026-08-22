## Creating the `playlists` Table

First, connect to the `music_streaming_app` database:

```sql
\c music_streaming_app
```

Create the `playlists` table with `playlist_id` as the primary key:

```sql
CREATE TABLE playlists (
	playlist_id INTEGER PRIMARY KEY,
	name VARCHAR,
	created_by VARCHAR
);
```
