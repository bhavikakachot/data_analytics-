# Fork and Extend a Data Science Repository


1. Sign in to GitHub and open the public data repository:

	```text
	https://github.com/mwaskom/seaborn-data
	```

2. Select **Fork**, choose your GitHub account, and create the fork. A fork is your personal copy of another user's repository, where you can make changes independently.

3. Clone your fork. Replace `YOUR-USERNAME` with your GitHub username:

	```powershell
	git clone https://github.com/YOUR-USERNAME/seaborn-data.git
	Set-Location seaborn-data
	```

4. Create and switch to the required feature branch:

	```powershell
	git switch -c feature-zomato-analysis
	```

5. Create a file named `zomato_analysis.txt` with this one-line description:

	```text
	I would clean Zomato order data, summarize orders by restaurant and cuisine, and analyze delivery time, ratings, and revenue trends with pandas and visualizations.
	```

6. Stage and commit the new file:

	```powershell
	git add zomato_analysis.txt
	git commit -m "Add Zomato analysis plan"
	```

7. Push the new branch to your fork:

	```powershell
	git push -u origin feature-zomato-analysis
	```

8. On GitHub, open your fork and confirm that the `feature-zomato-analysis` branch contains `zomato_analysis.txt`.

This workflow demonstrates how a data scientist can start from a public project, create an independent fork, isolate new work on a feature branch, and publish the change without modifying the original repository.
