# Add and Commit an Initial Playlist

1. Create `playlist.txt` inside the `InstaCloneRepo` folder and add three song names:

	```text
	Blinding Lights - The Weeknd
	Shape of You - Ed Sheeran
	Levitating - Dua Lipa
	```

2. Open PowerShell in the repository folder:

	```powershell
	Set-Location path\to\InstaCloneRepo
	```

3. Stage the new file:

	```powershell
	git add playlist.txt
	```

4. Commit the staged file with a clear, concise message that describes the change:

	```powershell
	git commit -m "Add initial playlist with 3 songs"
	```

5. Confirm that the commit was successful:

	```powershell
	git status
	git log --oneline -1
	```

The commit message follows Git best practices because it uses an imperative verb, identifies the change, and states the number of songs added.
