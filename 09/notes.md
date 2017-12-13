# Notes
## Some vim commands
### Pasting text
The following command is useful if you want to paste some text into Vim
in terminal. Since Vim cannot distinguish between typed text and pasted
text, this will help to avoid unexpected effects.

    :set paste

To disable this mode use to following command:

    :set nopaste

See the *pastetoggle* command, too.

    :help pastetoggle

## Shell script programming tips
### Retry a given command aka. error handling continued
The main idea is that we need to turn off the *errexit* option (`set +e` or `set +o errexit`)
right before the command, which could fail (and what we want to retry)
and turn on *errexit* again (`set -e` or `set -o errexit`) after the command.

We also want to store the return code (*rc* in the following script) to check
whether the last execution was successful. If not, then we could not
execute the command successfully even after the given number of retries.

Find the detailed example here:
[error_handling_demo.sh](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/09/error_handling_demo.sh).
