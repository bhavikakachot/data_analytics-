from pathlib import Path

import pandas as pd


csv_path = Path(__file__).with_name("spotify_mini.csv")
spotify_data = pd.read_csv(csv_path)

song_count_by_genre = spotify_data.groupby("genre")["song_name"].count()
print(song_count_by_genre)
