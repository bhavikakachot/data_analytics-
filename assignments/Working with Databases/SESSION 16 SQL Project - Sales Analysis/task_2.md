## Create the `TopSongs` Table

```sql
CREATE TABLE TopSongs (
	song_id INT PRIMARY KEY,
	song_title VARCHAR(255) NOT NULL,
	artist VARCHAR(255) NOT NULL,
	streams BIGINT NOT NULL,
	release_date DATE NOT NULL
);
```

Insert popular Spotify-style tracks:

```sql
INSERT INTO TopSongs (
	song_id,
	song_title,
	artist,
	streams,
	release_date
)
VALUES
	(1, 'Blinding Lights', 'The Weeknd', 4500000000, '2019-11-29'),
	(2, 'Shape of You', 'Ed Sheeran', 3800000000, '2017-01-06'),
	(3, 'As It Was', 'Harry Styles', 2800000000, '2022-03-31'),
	(4, 'Someone You Loved', 'Lewis Capaldi', 2500000000, '2018-11-08'),
	(5, 'Dance Monkey', 'Tones and I', 2400000000, '2019-05-10');
```
