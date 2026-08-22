## Creating the `Playlist` Table

```sql
CREATE TABLE Playlist (
	id INT PRIMARY KEY,
	song_name VARCHAR(255),
	artist VARCHAR(255),
	duration INT
);
```

Insert one sample favorite song. The duration is stored in seconds:

```sql
INSERT INTO Playlist (id, song_name, artist, duration)
VALUES (1, 'Blinding Lights', 'The Weeknd', 200);
```
