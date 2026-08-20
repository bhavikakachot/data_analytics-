from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


csv_path = Path(__file__).with_name("movies.csv")
movies = pd.read_csv(csv_path)
movies_per_genre = movies["genre"].value_counts().sort_index()

movies_per_genre.plot(kind="bar", color="steelblue")
plt.title("Number of Movies per Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()