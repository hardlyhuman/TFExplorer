# Contribution Guidelines
---
Welcome to TFExplorer. Before you send any Pull requests, make sure to read the full contribution guidelines. If you have any doubts, feel free to raise an issue or contact the maintainers.


### Issues

- If you are opening a new issue, mark it with an appropriate tag like bug/feature-request etc. 

- Please wait for maintainers to respond before working on the raised issue.

- If you want to work on an issue, request to be assigned to that issue. Please do not work on issues assigned to others. 

### Pull Requests

- If you want to submit PR for an issue, link your PR to the issue. [Ref. Linking PR to an Issue](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue)

- If your PR is a work in progress, or you want someone's review before continuing, start the title of your PR with **WIP:** This tells github and the maintainers that your PR is not yet complete and should not be merged.

- Feel free to mark your PR with appropriate tags. 

### Code

- Please comment and document your code whereever necessary

- If you take a large snippet of code from somewhere else (say StackOverflow), please add a comment with reference to where you have taken from

- We will use [Travis CI](https://travis-ci.org/) to automatically check the PRs

- Make sure all the tests are passing. (PRs likely won't be merged until travis build passes)

- PEP8 Guidelines for code style will be enforced using Travis

- We will use [black](https://pypi.org/project/black/), [flake](https://pypi.org/project/flake8/) and [pylint](https://www.pylint.org/) to enforce code styles. You may wish to configure your editors to use them

### Git

- Make sure you are writing relevant commit messages

- All the changes that you have made should be captured in your commit message. 

- In the commit messages, focus on "What" rather than "Why"

- Use full editor mode `git commit` instead of using the shorthand `git commit -m` . 

- There is commit template included in `.github` directory.  
  Enable it in your git using `git config commit.template .github/commit-template.txt`

- If you have multiple commits that do the same task, please squash them in a single commit.

- Please don't apply new commits for minor changes to your last commit. Use `git commit --amend` to update your last commit instead

- Don't use rebase or amend to edit the commits that have already been merged. Edit only the commits still awaiting in PR in your fork. And most importantly, edit only **your** commits.

- You make wish to use GPG keys to verify your commits. This is not a must. ([Ref. Siging Commits in Git](https://blog.nemit.fi/verify-your-github-commits-2fb42bff6048))

---

If you have any queries, feel free to reach out to the maintainers anytime.