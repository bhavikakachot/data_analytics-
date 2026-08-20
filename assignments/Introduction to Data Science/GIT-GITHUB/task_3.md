# Connecting the Local Repository to GitHub


A GitHub repository is a remote copy of a local Git repository hosted online. Connecting the local `music-recommendation` repository to GitHub makes it possible to store the project remotely, back up commits, and collaborate with other developers.

## Steps

1. Sign in to GitHub and create a new repository named `foodie-favorites`.

	When creating the repository, do not add an extra README, `.gitignore`, or license if the local repository already contains its own files. This avoids unnecessary merge conflicts during the first push.

2. Open PowerShell and move into the existing local repository:

	```powershell
	Set-Location path\to\music-recommendation
	```

3. Rename the current local branch to `main`:

	```powershell
	git branch -M main
	```

4. Connect the local repository to the new GitHub repository. Replace `YOUR-USERNAME` with your GitHub username:

	```powershell
	git remote add origin https://github.com/YOUR-USERNAME/foodie-favorites.git
	```

	The name `origin` is the conventional alias for the main remote repository.

5. Confirm that the remote URL was added correctly:

	```powershell
	git remote -v
	```

6. Push the local commits to GitHub and set `origin/main` as the upstream branch:

	```powershell
	git push -u origin main
	```

	The `-u` option records the upstream relationship, so later pushes can usually be made with only `git push`.

7. Refresh the GitHub repository page to confirm that the files and commit history are visible online.

The local repository is now connected to the GitHub repository and its commits have been uploaded. The local project is named `music-recommendation`, while the remote GitHub repository is named `foodie-favorites`.
