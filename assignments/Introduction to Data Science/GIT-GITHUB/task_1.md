# Installing and Verifying Git



Git is a distributed version control system used to track changes in files and source code. It allows developers to save different versions of a project, work on separate branches, and collaborate with others.

Git can be installed on Windows using the official Git installer or Windows Package Manager. The following command installs Git through PowerShell:

```powershell
winget install --id Git.Git -e
```

After the installation finishes, open a new terminal or command prompt. Opening a new terminal ensures that the Git installation has been added to the system `PATH`.

To verify the installation, run:

```powershell
git --version
```

If Git is installed correctly, the terminal displays its version, for example:

```text
git version 2.46.0.windows.1
```

This output confirms that Git is installed and can be accessed from the command line.
