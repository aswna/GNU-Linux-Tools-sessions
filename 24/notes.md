# Git and Gerrit basics
## Basic commands
Clone the repository

    git clone ssh://$USER@${GERRIT_SERVER}:${PORT}/${PROJECT}

Copy hook for inserting "Change-Id" in commit message automatically

    scp -p -P ${PORT} ${USER}@${GERRIT_SERVER}:hooks/commit-msg .git/hooks/

Set username and email if necessary

    git config user.email <your.email@address>
    git config user.name <your_user_name>

Use *.gitignore* to avoid committing directories, files by accident

Some basic commands

    git status
    git add tools/new_tool.sh
    git reset HEAD tools/new_tool.sh
    git reset --hard origin/master

See changes

    git diff
    git diff --cached

    git show
    git show --oneline --name-only

    git log <file or directory>
    git log -p <file or directory>
    git blame <file>

Commit your change

    git commit
    git commit --amend
    git commit --amend --no-edit

Push your changes to Gerrit

 * As draft (kind of private change)

    git push origin HEAD:refs/drafts/master

 * As a public change

    git push origin HEAD:refs/for/master

Rebase, squash (non published) changes

    git rebase --interactive HEAD~2

