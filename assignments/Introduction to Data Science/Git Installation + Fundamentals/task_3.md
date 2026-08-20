# Initialize the InstaCloneRepo Git Repository

## Steps

1. Create a folder named `InstaCloneRepo` and open PowerShell in that folder:

	```powershell
	New-Item -ItemType Directory -Name InstaCloneRepo
	Set-Location InstaCloneRepo
	```

2. Initialize the folder as a Git repository:

	```powershell
	git init
	```

3. Git creates a hidden `.git` folder inside `InstaCloneRepo`. This folder contains the repository database, including commit history, branches, and configuration. It should not be edited manually.

4. Display hidden files to observe the new folder:

	```powershell
	Get-ChildItem -Force
	```

	The output should include:

	```text
	.git
	```

The `.git` folder confirms that `InstaCloneRepo` is now a local Git repository.
