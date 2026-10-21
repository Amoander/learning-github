# Learning Progress

A running log of what I've learned about Git, GitHub, and coding.

## September 26, 2026

* Created my GitHub account
* Created my first repository with a README
* Edited the README with Markdown and made my first commit
* Viewed the commit history and read a diff

## September 27, 2026

* Created my first branch (add-goals) and saw how branches keep separate versions
* Opened my first pull request, reviewed the changes, and merged it into main
* Built a learning roadmap with Claude and uploaded it to this repo
* Started this progress log
* Log 2FA setup
* Installed GitHub Desktop and cloned my repo to my computer
* Edited a file locally and pushed it to GitHub
* Install Git and checked repo with git status and git log
- Made my first commit and push from the command line
- Git case-sensitive fix: always check git status before and after each step

## September 28, 2026
- Practiced git pull, git branch, and git switch
- Ran the full branch and pull request cycle from the command line
- Fixed a Markdown formatting bug caught during pull request review
- Installed VS Code and committed and pushed from it

## October 7, 2026
- Installed Python 3.14 and the VS Code Python extension
- Wrote and ran my first Python script (hello.py)
- Learned the difference between the editor (code) and the terminal (commands)
- Read my first Python error message: file, line number, and the problem line
- Built a number guessing game (guess.py) with import, while loops, and if/elif
- Broke it on purpose: ValueError, IndentationError, NameError
- Built it on a branch, reopened a closed pull request, and merged it
- Lesson: read the commit message before pressing Enter. 

## October 10, 2026

- Built a to-do list script (todo.py) with lists, a function, and a menu loop
- Learned that lists count from 0, and saw an IndexError when asking for a position that doesn't exist
- Shipped it on a branch with a pull request
- Built a tip calculator (tip.py) with float, math operators, and f-string formatting
- Saw a ZeroDivisionError when splitting a bill among 0 people
- Completed the Phase 1 milestone: 4 Python scripts, each shipped with a pull request

## October 12, 2026

- Added error handling to tip.py, guess.py and todo.py with try/except
- Learned to CATCH errors (try/except) and PREVENT them (if checks)
- New Python: function parameters, return, continue, or
- Built one feature as 3 commits on one branch, merged with a single pull request

## October 14, 2026

- todo.py now saves tasks to tasks.txt and loads them on startup
- Learned open(), with, read/write modes, "\n", .strip(), pass, FileNotFoundError
- Added a .gitignore so personal data never goes to GitHub
- Created a merge conflict on purpose with two branches editing the same README line
- Resolved it in VS Code, finished the merge, and viewed it with git log --graph
- Learned git merge, git merge --abort, and git rm

## October 15, 2026

- Created a virtual environment (.venv) and installed rich with pip
- Saw ModuleNotFoundError when the venv was off; learned to check for (.venv)
- Saved packages to requirements.txt and added .venv/ to .gitignore

## October 16, 2026

- Created a separate repo, tally-fitness, for my Tally Fitness tracker
- Fixed a folder that wasn't a Git repo by cloning fresh and copying files in
- Added .nojekyll and deployed the tracker live with GitHub Pages
- Installed it on my phone with Add to Home Screen
- Tally is now my Phase 2 milestone project

## October 18, 2026

- Wrote a README for tally-fitness with a description, live link, and screenshot
- Shipped it with a branch and pull request in the tally-fitness repo
- Learned about VS Code's Restricted Mode (Workspace Trust) and trusted my own folder
- Learned VS Code auto-activates my .venv in learning-github
- Installed the Claude Code extension; keeping it disabled until its own lesson
- Found a bug while testing Tally on my phone: the barcode scanner was a placeholder
- Reported it as GitHub Issue #1 with steps, expected result, and device info
- Shipped the Tally chat's fix on a branch with 2 commits (code + README privacy update)
- Merged the PR, the site redeployed, and the scanner works on my phone
- Learned PRs need "Fixes #1" before merging to auto-close; closed the issue by hand with a link
- Learned slashes in branch names make folders, so I'll use hyphens with OneDrive

## October 19, 2026

- Planned Tally improvements as GitHub Issues (#2-#5) with labels: enhancement, bug, question
- Wrote "Done when" checklists so each feature is testable on my phone
- Decided to remove the unreliable step counter and recorded the reasoning on the Issue
- Shipped backup/restore (#2) and step counter removal (#3) as separate PRs, in order
- Reviewed the Tally chat's output before shipping: caught a combined download and a README overwrite
- Learned the > prompt means an unclosed quote; Ctrl + C cancels safely
- Completed the Phase 2 milestone and Phase 2

## October 20-21, 2026

- Installed pytest and wrote 5 tests for tip.py (assert, pytest.approx, pytest.raises)
- Refactored tip.py: math in calculate_tip(), input in main(), if __name__ == "__main__"
- Added pytest.ini and ignored .pytest_cache/ and __pycache__/
- Debugged: test vs tests folder, stray text in a file, a stale editor tab
- Broke tip.py on purpose and watched 3+ tests fail; undid it with git restore
- Learned why several test cases matter: a 0% tip test missed the bug
- Added a GitHub Actions workflow (.github/workflows/tests.yml) to run pytest on every push and PR
- First run failed: copied the "yaml" label into the file, and an extra dash split a step in two
- Fixed it on a fix-ci branch and waited for green before merging (rule: never merge on red)
- Added a Tests badge to the README