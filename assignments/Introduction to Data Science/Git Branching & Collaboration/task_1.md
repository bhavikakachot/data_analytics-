# Create a Feature Branch for a Playlist


Git branches allow developers to work on features separately from the main project branch. A feature branch keeps changes isolated until they are reviewed and ready to merge.

## Steps

1. Open PowerShell and move into any existing local Git project:

	```powershell
	Set-Location path\to\existing-project
	```

2. Create a new branch named `feature-playlist` and switch to it:

	```powershell
	git switch -c feature-playlist
	```

	The older equivalent command is `git checkout -b feature-playlist`.

3. Create a file named `playlist.md` with the following content:

	```markdown
	# My Top 3 Spotify Playlists

	## 1. Today's Top Hits
	A playlist for discovering current popular songs and new releases.

	## 2. Peaceful Piano
	A calm collection for studying, reading, or focusing.

	## 3. RapCaviar
	A playlist featuring popular hip-hop and rap tracks.
	```

4. Check that the new branch and file are present:

	```powershell
	git branch --show-current
	git status
	```

	The first command should display `feature-playlist`, and `playlist.md` should appear as an untracked file in the status output.

This workflow keeps the playlist change separate from the main branch and provides a safe basis for review before merging.
