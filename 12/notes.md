# Notes
## Scripting exercise continued
### You are ready!

For the exercise, see the [description](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/11/notes.md).

Our dedicated small-but-hard-core team finished the implementation of the script ([script.sh](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/12/script.sh)).

You can download the test script [test_script.exp](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/12/test_script.exp), which will test your small program.

My initial solution can be found at [script.sh](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/12/solution/script.sh).

## Miscellaneous Vim tricks

How could we change `valasz` to `answer`?

    Select the word with '*', then
    use 'cw' to change the word, then
    use 'n' to find next match, then
    repeat the last change with '.'.
    
    help *
    help .

How did we finally change `valasz` to `answer`?

    %s/\<valasz\>/answer/gc
    
    The syntax is similar to 'sed'.
    The flag 'g' means apply replace all occurrences in the line.
    The flag 'c' means confirm each substitution.
    
    help :substitute

How did we insert `\<valasz\` as the search pattern?

    We selected the word 'valasz' with the '*' key, then
    entered command mode and used 'CTRL-r /' to insert the last search pattern.
    
    help i_CTRL-R

How can you easily indent some text?

    Use >> and << in normal mode.
    
    help shift-left-right

How can you check your active mappings in vim?

    Use the 'map' command.

How can you make trailing spaces more visible?

    Check out the 'listchars' string setting
    to be able to customize the view of the TAB character, trailing spaces, etc.
    
    help listchars

Where did my deleted text go?

    You can use register names to delete / paste text to / from.
    Example:
    "udw  : delete word under cursor and save it to register named 'u'
    "uP   : put the content of register named 'u' before the cursor position
    
    help :reg
