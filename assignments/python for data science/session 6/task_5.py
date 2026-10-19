def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

spotify_playlist1 = {"artist_a", "artist_b", "artist_c"}
spotify_playlist2 = {"artist_b", "artist_d"}

unique_artists = get_unique_artists(spotify_playlist1, spotify_playlist2)
print(unique_artists)