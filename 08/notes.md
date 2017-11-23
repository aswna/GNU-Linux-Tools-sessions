# Notes
## Some vim commands
### Left-right motions
 - `f{char}` To `[count]`'th occurrence of `{char}` to the right.
 - `F{char}` To the `[count]`'th occurrence of `{char}` to the left.
 - `t{char}` Till before `[count]`'th occurrence of `{char}` to the right.
 - `T{char}` Till after `[count]`'th occurrence of `{char}` to the left.
 - `;` Repeat latest f, t, F or T `[count]` times.
 - `,` Repeat latest f, t, F or T in opposite direction `[count]` times.

### Delete and insert
 - `["x]c{motion}` Delete {motion} text [into register x] and start insert.

### Simple changes
 - `r{char}` Replace the character under the cursor with `{char}`.
 - `gU{motion}` Make `{motion}` text uppercase.
 - `gu{motion}` Make `{motion}` text lowercase.

## Shell script programming tips
### Error handling
It can be very useful to add the following settings to you shell scripts:

    # Treat unset variables and parameters other than the special
    # parameters "@" and "*" as an error when performing parameter
    # expansion.
    # same as 'set -o errexit'
    set -u
    
    # Exit immediately if a pipeline (even a single command), a list,
    # or a compound command exits with a non-zero status.
    # same as 'set -o nounset'
    set -e

Homework is to check the effects of:

    # If set, the return value of a pipeline is the value of the last
    # (rightmost) command to exit with a non-zero status, or zero if all
    # commands in the pipeline exit successfully.
    set -o pipefail

You can turn these settings off (and on again) for small portions of the
script, too, with `set +u`, etc.

### Use more functions
 - Instead of comments, use functions. Sometimes, you can turn a short
   comment into a function name.
 - Try to make the functions short. To be more readable, comprehensible.
 - Try to make the functions reusable. Use parameter lists.
 - In the functions, where appropriate, use the `local` keyword for the
   variables to not let them propagate outside of the functions.

See [example.sh](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/08/example.sh).
