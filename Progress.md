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

## October 23, 2026 — Claude Code + issue housekeeping

**Did**
- Used Claude Code (VS Code) in Plan mode, then "ask before edits"
- Plan mode found Issue #4 was already built (PR #8): closed #4 as completed
- Fixed wrong cross-references: #2 ↔ PR #3, commit 22fa1a7 → #4
- Opened #10, built backup validation on branch validate-backup
- Tested locally with 11 test files + a real round trip; merged PR #11 (Fixes #10)

**Learned**
- Issues and PRs share one number counter (#1 PR, #2 issue, #3 PR...)
- Pick #numbers from GitHub's dropdown; never copy numbers from another chat
- Read AI plans and diffs before accepting; approve one edit at a time
- Judge a bash command: where does it write, any rm, git, or network?
- git diff | clip copies output to the Windows clipboard
- Defense in depth: file picker filter + validation check
- git fetch --prune clears branches already deleted on GitHub
- "git branch status" creates a branch named status; git status ≠ git branch

**Next**
- Build something that calls an API

## October 24, 2026 — GH-900 prep: Projects and milestones

**Did**
- Created the Tally Roadmap project (Kanban template), imported open issues #6 and #7
- Added closed #10; a built-in workflow put it straight in Done
- Moved #6 to Ready and confirmed the issue sidebar shows the same status
- Created milestone v1.1 Live Sessions and assigned #6 and #7
- Set #6 priority to P0

**Learned**
- Label = type, Milestone = goal + due date + % done, Project = status board
- Projects belong to my account, not a repo, so one board can span repos
- Board, Table and Roadmap are views of the same items
- WIP limits (0 / 3) cap work in progress
- "Up to date with origin/main" only means since the last fetch

**Next**
- GH-900 prep: Dependabot, permissions and security settings

## October 25, 2026 — Tally #12: delete and clear weigh-ins

**Did**
- Opened #12 (delete weigh-ins) and #13 (add my own food); auto-add put both on the board
- Planned #12 in Claude Code (Plan mode); it found hard-coded Apr–Jun sample weights and a crash on an empty log
- Approved edits one at a time; checked `nW` existed with grep before testing
- Tested 10 cases locally; merged PR #14; #12 closed and moved to Done automatically
- Opened #15 to store real weigh-in dates (found during planning)

**Learned**
- Claude design canvas ≠ Claude Code in VS Code; only one Claude session should edit files at a time
- Plan mode questions: pick the answer, or type in "Tell Claude what to do instead"
- `git commit -m "title" -m "body"` gives a commit a title and a body
- Don't rewrite pushed commits for small typos
- grep matches letters anywhere (nW matched openWeight)
- Press F5 when GitHub pages disagree with the timeline

**Next**
- Issue #13: add my own food

## October 25, 2026 (evening) — Tally #13: add my own food

**Did**
- Found text search only uses 18 built-in foods (#17); README was wrong
- Opened #16 (real calorie history), #17 (search question), #18 (edit/delete saved foods)
- Transferred #16 from learning-github to tally-fitness
- Built #13 with Claude Code: 8 edits, two approval layers each
- Tested 10 cases; merged PR #19 with a Co-Authored-By line

**Learned**
- Order matters: git add → git commit → git push
- "no changes added to commit" = commit failed; push "Total 0" = nothing sent
- Transfer issue moves an Issue between repos (new number, history kept)
- "Fixes #N" closes on merge; "Related to #N" only links
- My Desktop is ~/OneDrive/Desktop, not ~/Desktop

**Next**
- Decide on online text search (#17) using the missed-foods list
- #16 + #15: plan real dates and daily history