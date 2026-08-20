# Merge Conflict Resolution Workflow


A merge conflict occurs when two branches change the same line of the same file in different ways. Git cannot decide which version to keep, so the developer must review both changes and resolve the conflict manually. A merge commit records the point where the two lines of development are combined.

## Create Different Changes on Both Branches

1. Open PowerShell in the local repository that contains `playlist.md` and confirm the starting branch:

	```powershell
	Set-Location path\to\existing-project
	git status
	```

2. Switch to the feature branch and edit the same playlist line. For example, change the first playlist line to:

	```markdown
	## 1. Today's Top Hits - Feature Selection
	```

	Save the file and commit the feature-branch version:

	```powershell
	git switch feature-playlist
	git add playlist.md
	git commit -m "Update playlist selection on feature branch"
	```

3. Switch to `main`, edit that exact same line differently, and commit the main-branch version:

	```powershell
	git switch main
	```

	Change the line to:

	```markdown
	## 1. Today's Top Hits - Main Selection
	```

	Then run:

	```powershell
	git add playlist.md
	git commit -m "Update playlist selection on main"
	```

## Merge with a Merge Commit

4. From the `main` branch, merge the feature branch with fast-forward disabled:

	```powershell
	git merge --no-ff feature-playlist -m "Merge feature-playlist into main"
	```

	Because both branches changed the same line, Git pauses and reports a conflict in `playlist.md`.

## Resolve the Conflict in VS Code

5. Open the repository in VS Code:

	```powershell
	code .
	```

6. Open `playlist.md`. The VS Code merge editor displays the **Current Change** from `main` and the **Incoming Change** from `feature-playlist`.

7. Review both versions and choose **Accept Current Change**, **Accept Incoming Change**, or combine the text into one final line. Save the resolved file.

8. Mark the conflict as resolved and complete the merge commit:

	```powershell
	git add playlist.md
	git commit -m "Resolve playlist merge conflict"
	```

9. Verify the final history and clean working tree:

	```powershell
	git status
	git log --oneline --graph --all
	```

The merge commit preserves both branch histories and records how the conflicting playlist change was resolved.
