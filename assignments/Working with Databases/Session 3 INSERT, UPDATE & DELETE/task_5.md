## Updating AP Dhillon Song Names

Append `(Remix)` to the name of every `AP Dhillon` song longer than 180 seconds:

```sql
UPDATE Playlist
SET song_name = song_name || ' (Remix)'
WHERE artist = 'AP Dhillon'
	AND duration > 180;
```

The `WHERE` clause ensures that only songs by `AP Dhillon` with a duration greater than 180 seconds are updated.
