# Notes
## Some static code checkers for shell scripts
### built-in
`bash -n <your script>` checks `<your script>` for syntax errors (dry-run).

Example:

    > cat foo.sh
    echo "something
    > bash -n foo.sh
    foo.sh: line 1: unexpected EOF while looking for matching `"'
    foo.sh: line 2: syntax error: unexpected end of file

Note: see the missing end quote.


### bashate
`bashate` is a bash script style checker.

Example:

    > cat foo.sh
    #!/bin/sh

    function foo() {
        echo "bar"
    }
    > bashate foo.sh
    E020: Function declaration not in format "^function name {$":
    'function foo() {'
     - foo.sh : L3
    1 bashate error(s) found

Note: the standard usage of functions are in the below to formats:

    function foo {
        :
    }

or

    foo() {
        :
    }

Note: the `:` is the `no operation` operator in the shell (similar to
`pass` in the Python language).


### checkbashisms
`checkbashisms` performs basic checks for the presence of bashisms
in `/bin/sh` scripts and the lack of bashisms in `/bin/bash` ones.

Example (for the above script):

    > checkbashisms foo.sh
    possible bashism in foo.sh line 3 ('function' is useless):
    function foo() {

Another example (`/bin/sh` is changed to `/bin/bash`):

    > cat foo.sh
    #!/bin/bash

    function foo() {
        echo ${*}
    }

    foo
    > checkbashisms foo.sh
    [no output]


### shellcheck
`shellcheck` is an advanced shell script analysis tool.

Example (for the above script):

    > shellcheck foo.sh
    
    In foo.sh line 3:
    function foo() {
    ^-- SC2120: foo references arguments, but none are ever passed.
    
    
    In foo.sh line 4:
        echo ${*}
             ^-- SC2048: Use "$@" (with quotes) to prevent whitespace problems.
             ^-- SC2086: Double quote to prevent globbing and word splitting.
    
    
    In foo.sh line 7:
    foo
    ^-- SC2119: Use foo "$@" if function's $1 should mean script's $1.

## VIM and Syntastic
All of the [above checkers](https://github.com/vim-syntastic/syntastic/tree/master/syntax_checkers/sh)
can be integrated to your [VIM](https://www.vim.org) environment using the plugin
[Syntastic](https://github.com/vim-syntastic/syntastic).
