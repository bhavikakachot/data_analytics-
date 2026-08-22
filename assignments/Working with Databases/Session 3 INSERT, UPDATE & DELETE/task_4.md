## Deleting a Short Song

Delete one specific playlist entry only when its duration is less than 120 seconds:

```sql
DELETE FROM Playlist
WHERE id = 5
	AND duration < 120;
```

The `id = 5` condition identifies the exact song, while `duration < 120` ensures that it is deleted only if it meets the duration requirement. Using both conditions prevents all short songs, or all rows, from being deleted accidentally.
