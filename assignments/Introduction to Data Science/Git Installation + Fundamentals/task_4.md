# Clone and Check a Public Repository

## Steps

1. Open PowerShell in the folder where you want to store the repository.

2. Clone the public GitHub repository:

	```powershell
	git clone https://github.com/public-apis/public-apis.git
	```

	This downloads the repository into a new folder named `public-apis` and automatically configures its remote repository as `origin`.

3. Enter the cloned repository:

	```powershell
	Set-Location public-apis
	```

4. Check the repository status:

	```powershell
	git status
	```

## Expected Result

Because a newly cloned repository starts with no local changes, Git should display a message similar to:

```text
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

The branch may be named `main` instead of `master`, depending on the repository's default branch. The message `working tree clean` means the local files match the latest committed version.
