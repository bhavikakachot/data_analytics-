## Finding the Top Three Trending Songs

Assuming the `songs` table stores the date a song was added in a column named `date_added`:

```sql
SELECT *
FROM songs
ORDER BY play_count DESC, date_added DESC
LIMIT 3;
```
