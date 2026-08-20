# Configure Git Username and Email

Git stores the author identity with each commit. Configure the username and email globally so the settings apply to all repositories on the computer.

Run these commands in PowerShell or a terminal, replacing the example values with your actual details:

```powershell
git config --global user.name "Your Actual Name"
git config --global user.email "your.actual.email@example.com"
```

Verify the settings with:

```powershell
git config --global user.name
git config --global user.email
```

The terminal should display the name and email configured for your Git commits.
