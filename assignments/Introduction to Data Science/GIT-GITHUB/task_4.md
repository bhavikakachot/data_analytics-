# Simulating Team Collaboration with GitHub


Git and GitHub help team members collaborate on a shared project. Git records changes locally in commits, while GitHub stores the repository online so that team members can view and share the latest version. GitHub Issues are used to suggest features, report problems, and track project tasks.

## Edit README.md

1. Open PowerShell and enter the local repository folder:

	```powershell
	cd path\to\music-recommendation
	```

2. Open `README.md` in a text editor and add the following section:

	```markdown
	## Top 3 Music Apps

	1. Spotify
	2. YouTube Music
	3. Wynk
	```

3. Save the file and review the changes:

	```powershell
	git status
	```

## Commit and Push

4. Stage the modified README file:

	```powershell
	git add README.md
	```

5. Create a commit describing the update:

	```powershell
	git commit -m "Add top 3 music apps to README"
	```

6. Push the commit to the connected GitHub repository:

	```powershell
	git push
	```

	If the local `main` branch has not been connected to its upstream branch, use:

	```powershell
	git push -u origin main
	```

7. Refresh the repository page on GitHub and confirm that the README update and commit are visible.

## Create a GitHub Issue

8. Open the project repository on the GitHub website and select the **Issues** tab.

9. Select **New issue**.

10. Enter the title:

	 ```text
	 Add playlist sharing
	 ```

11. Add a description such as:

	 ```text
	 Add playlist sharing so users can share their favorite playlists with friends using a public link.
	 ```

12. Select **Submit new issue**. The feature request is now available for team discussion, assignment, and tracking.
