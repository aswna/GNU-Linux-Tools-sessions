# Notes
## Scripting exercise
### Are you ready?
Write a script (`script.sh`), which prints out the following upon execution:

    Hello, <USER>!

where `<USER>` is replaced by the (Linux) username of the user, who started the script.

The next line should be prompt-like, which asks for input:

    Are you ready or not? [y/n] 

Note: there is a single space character at the end of this line, and it does
not contain newline character at the end of line!

The next line kind of echos back the provided answer:

    Your answer was '<ANSWER>'

where `<ANSWER>` is replaced by the provided answer of the user.

Finally, if the answer is a single 'y' (yes), then it should print:

    OK. You are ready!

otherwise, it should print:

    Fine. Then take your time, check back later...

You can download the test script [test_script.exp](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/11/test_script.exp), which will test your small program.

The team started to implement the script (see the preliminary results here: [script.sh](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/11/script.sh)).
