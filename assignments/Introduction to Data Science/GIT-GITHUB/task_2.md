# Creating the Music Recommendation Repository

## Steps

1. Open PowerShell or a command prompt and move to the folder where you want to create the project.

2. Create the project folder and enter it:

	```powershell
	New-Item -ItemType Directory -Name music-recommendation
	Set-Location music-recommendation
	```

3. Initialize the folder as a new local Git repository:

	```powershell
	git init
	```

4. Create a `README.md` file inside the repository:

	```powershell
	New-Item README.md -ItemType File
	```

5. Add the README file to Git's staging area:

	```powershell
	git add README.md
	```

6. Create the first commit with the required message:

	```powershell
	git commit -m "Initial commit for music-recommendation project"
	```

7. Confirm that the commit was created:

	```powershell
	git log --oneline
	```

The repository should contain the following structure:

```text
music-recommendation/
└── README.md
```

The first commit records the initial state of the project and provides a starting point for tracking future changes.
