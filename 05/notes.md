# Notes
## Ghost in the shell
### Simple prompt
Set a minimalist prompt:

        > export PS1='> '

### Getting file size
Probably, it is better to use the *stat* command instead of parsing the output of the *ls* command for getting the size of a file:

        > stat --printf "%s\n"

**Note: using *stat* is not portable. The portable way is to use *wc*:**

        size=$(wc -c < "${file}")

### Using the output of *ls* command
Using the output of *ls* command might be dangerous, since it could be an *alias* to something else (*/bin/rm -rf*) or some options might be set, which could change the output completely. **These are relevant when you *source* the file and does not execute it as a script.**

        > alias ls
        ls='/bin/ls $=LS_OPTIONS'

        > echo ${LS_OPTIONS}
        -N --color=auto -T 0 -p

Setting the *LS_OPTIONS *to *-1* will result in a very different output.

The really unwise thing is the use the output of *ls* for getting the filenames, since they can contains white-space, etc.

**For more details, see the dangers of [parsing ls](http://mywiki.wooledge.org/ParsingLs).**

## Miscellaneous Vim tricks
* Install the [Syntastic](https://github.com/vim-syntastic/syntastic) plugin, which makes use of external syntax checkers for a wide variety of files.

* Use the "." command more often, which repeats the last (simple) change.

* Use *retab* to replace all sequences of white-space containing a <Tab> with new strings of white-space using the new tabstop value given.

* Use *resize* to change size of the (horizontally) split current window.

* Set *listchars* to make some white-spaces more visible. Example (for UTF-8 capable terminals):

        listchars=tab:▸ ,trail:·,extends:>,precedes:<,nbsp:·

* Map ";" to ":" in normal mode to spare pressing the shift key for entering *command mode*:

        " No need to press Shift, real optimization for almost all Vim commands.
        nnoremap ; :
        " If the repetition of latest f, t, F or T move is needed use below mapping
        nnoremap <Leader>; ;
