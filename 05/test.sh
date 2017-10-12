#!/bin/bash

# Try to use:
set -u
set -e

# -e
#   Exit immediately if a pipeline (which may consist of a single simple command), a list, or a compound command, exits with a non-zero status.
# -u
#   Error on unset variable or parameter. The shell prints an error message, and, if not interactive, exits with a non-zero status.


# You can disable, try to disable only for the smallest scope.
set +u
set +e
RESULT=$(echo "foo\nbar\nbaz\n" | grep foobar)
echo "rc = ${?}"
echo "RESULT = ${RESULT}"
set -u
set -e

# { list; }
#   list is simply executed in the current shell environment.
#   list must be terminated with a newline or semicolon.
#   This is known as a group command.
#   The return status is the exit status of list.
error=0
[ "${error}" -eq 1 ] && { echo "error = ${error}"; exit "${error}"; }

# same as:
if [ "${error}" -eq 1 ]; then
    echo "error = ${error}"
    exit 1
fi

VAR=0
echo "VAR = ${VAR}"

VAR=1
echo "VAR = ${VAR}"

FOO=1
echo "FOO = ${FOO}"

# ${VAR} = 2
# results in "1: command not found"
# the same as:
# 1 = 2

VAR=FOO
echo "VAR = ${VAR}"

eval ${VAR}=2
echo "FOO = ${FOO}"

let ${VAR}=3
echo "FOO = ${FOO}"

BASEDIR=/tmp
echo
echo "DIRECTORIES ONLY UNDER ${BASEDIR}"
for dir in $(find ${BASEDIR} -maxdepth 1 -type d); do
    echo "dir = ${dir}"
done

echo
echo "EVERYTHING UNDER ${BASEDIR}"
for f in "${BASEDIR}"/*; do
    if [ -f "${f}" ]; then
        echo "regular file = ${f}"
    else
        echo "not file (probably dir) = ${f}"
    fi
done

echo
echo "Using ls..."
ls ${BASEDIR}
