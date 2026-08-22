## Correcting an Artist Name

Suppose an artist was entered as `Arjit Singh` by mistake. Use an `UPDATE` statement with a `WHERE` clause to correct only the affected playlist entries:

```sql
UPDATE Playlist
SET artist = 'Arijit Singh'
WHERE artist = 'Arjit Singh';
```

The `WHERE` clause prevents the names of other artists from being changed.
