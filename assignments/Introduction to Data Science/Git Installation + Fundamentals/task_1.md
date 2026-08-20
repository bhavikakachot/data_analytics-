# Installing and Verifying Git

## Steps

1. On Windows, open PowerShell or Command Prompt.

2. Install Git with Windows Package Manager:

	```powershell
	winget install --id Git.Git -e
	```

	Git can also be installed using the official installer from [git-scm.com](https://git-scm.com/downloads).

3. Close and reopen the terminal so that the updated system `PATH` is loaded.

4. Confirm that Git is installed by running:

	```powershell
	git --version
	```

5. Successful installation produces output similar to:

	```text
	git version 2.46.0.windows.1
	```

The version output confirms that Git is installed and can be used from the command line.
