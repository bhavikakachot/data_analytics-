# Push a Feature Branch and Open a Pull Request

## Steps

1. Open PowerShell in the cloned fork and confirm that the feature branch is active:

	```powershell
	Set-Location path\to\seaborn-data
	git switch feature-zomato-analysis
	```

2. Push the branch to your GitHub fork:

	```powershell
	git push -u origin feature-zomato-analysis
	```

	The `-u` option connects the local branch to its remote branch so future updates can use `git push`.

3. Open the original repository on GitHub:

	```text
	https://github.com/mwaskom/seaborn-data
	```

4. Select **Pull requests** and then **New pull request**. Choose **compare across forks** if necessary.

5. Set the pull request branches as follows:

	- **Base repository:** `mwaskom/seaborn-data`
	- **Base branch:** `master` (or the original repository's current default branch)
	- **Head repository:** `YOUR-USERNAME/seaborn-data`
	- **Compare branch:** `feature-zomato-analysis`

6. Select **Create pull request** and use a clear title such as:

	```text
	Add Zomato order analysis plan
	```

7. Add a description or comment explaining the change:

	```text
	This PR adds zomato_analysis.txt with a short plan for cleaning Zomato order data and analyzing restaurant, cuisine, delivery-time, rating, and revenue trends. The change is documentation only and does not modify the existing datasets.
	```

8. In the pull request's **Reviewers** section, select a classmate's GitHub username and request their review.

9. Select **Create pull request** or **Submit pull request**. The PR now shows the feature branch, changed file, explanation, and requested reviewer.

This workflow lets a contributor propose changes to the original repository without editing it directly. The repository owner or maintainers can review the change, request updates, and merge it if approved.
