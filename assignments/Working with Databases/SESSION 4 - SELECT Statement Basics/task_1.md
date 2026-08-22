## Creating the `MusicPlaylist` Table

```sql
CREATE TABLE MusicPlaylist (
	id INT PRIMARY KEY,
	song_name VARCHAR(255),
	artist VARCHAR(255),
	genre VARCHAR(100),
	duration INT
);
```

The duration is stored in seconds. These songs are from a favorite Spotify playlist:

```sql
INSERT INTO MusicPlaylist (id, song_name, artist, genre, duration)
VALUES
	(1, 'Blinding Lights', 'The Weeknd', 'Synth-pop', 200),
	(2, 'As It Was', 'Harry Styles', 'Pop', 167),
	(3, 'Levitating', 'Dua Lipa', 'Dance-pop', 203),
	(4, 'Good 4 U', 'Olivia Rodrigo', 'Pop rock', 178),
	(5, 'Stay', 'The Kid LAROI and Justin Bieber', 'Pop', 141);
```

Retrieve all columns for all songs:

```sql
SELECT *
FROM MusicPlaylist;
```
