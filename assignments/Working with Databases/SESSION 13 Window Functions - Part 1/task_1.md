## Creating the `Playlists` Table

```sql
CREATE TABLE Playlists (
	id INT PRIMARY KEY,
	user_id INT,
	playlist_name VARCHAR(255),
	total_likes INT
);
```

Insert sample playlists. Some users have created more than one playlist:

```sql
INSERT INTO Playlists (id, user_id, playlist_name, total_likes)
VALUES
	(1, 101, 'Morning Motivation', 245),
	(2, 101, 'Late Night Chill', 189),
	(3, 102, 'Road Trip Anthems', 512),
	(4, 103, 'Focus Flow', 328),
	(5, 102, 'Weekend Party', 674),
	(6, 104, 'Acoustic Favorites', 156),
	(7, 105, 'Workout Energy', 431),
	(8, 103, 'Rainy Day Songs', 217);
```
