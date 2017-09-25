# GNU/Linux Tools


# GNU/Linux Tools II.

• Tool of the week
{~• Request of the week
• Homework~}


# Tool of the week

+- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
|^ ^ ^ ^ ^ ^ ^ # % ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |
  
|^ ^ ^ ^ ^ ^ ^ # M ^ ^ ^ ^ ^ ^ ^ ^ ^ % % ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |
  
|^ ^ ^ ^ ^ ^ ^ ^ ^ @ M M # % @ @ @ # $ $ M M $ ^ ^ ^ ^ ^ ^ ^ ^ |
  
|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ M M M M M M $ @ $ $ @ ^ ^ ^ ^ ^ ^ ^ ^ |
  
|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ M M M M M M M M @ # ^ ^ ^ ^ ^ ^ ^ ^ ^ |
  
|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ M M $ # % M M # # % ^ ^ ^ ^ ^ ^ ^ ^ ^ |
  
|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ % $ % # ^ ^ M # M $ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |
  
|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ @ # ^ % ^ @ % % # ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |
  
|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ % ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |
+- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +


# Tool of the week

+--------------------------------------------------------------+
|^^^^^^^^^^^^^^#$%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|
  
|^^^^^^^^^^^^^^#MM%^^^^^^^^^^^^^^^^^^%#%^^^^^^%^^^^^^^^^^^^^^^^|
  
|^^^^^^^^^^^^^^^^^#@MMMM@#%%#@@@@@@##$$$MMMMM$#^^^^^^^^^^^^^^^^|
  
|^^^^^^^^^^^^^^^^^^^^^^^MMMMMMMMMMMMM$@@$$$$@@%^^^^^^^^^^^^^^^^|
  
|^^^^^^^^^^^^^^^^^^^^^^^@MMMMMMMMMMMMMMM@@###^^^^^^^^^^^^^^^^^^|
  
|^^^^^^^^^^^^^^^^^^^^^^^@MMMM$@#^%MMMM@####%^^^^^^^^^^^^^^^^^^^|
  
|^^^^^^^^^^^^^^^^^^^^^^%$$#%@#%^^^#M$#%MM$^^^^^^^^^^^^^^^^^^^^^|
  
|^^^^^^^^^^^^^^^^^^^^^^^^@@#%^%%^^%@$%^%##^^^^^^^^^^^^^^^^^^^^^|
  
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^%%%^^^^^^^^^^^^^^^^^^^^|
+--------------------------------------------------------------+


# Tool of the week

+--------------------------------------------------------------+
|^^^^^^^^^^^^^^#$%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^MM#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^#MM%^^^^^^^^^^^^^^^^^^%#%^^^^^^%^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^#MMM@%%^^^^^^^^^^^^^^#$@@######%^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^#@MMMM@#%%#@@@@@@##$$$MMMMM$#^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^%#@MMMMMMMMMMMMM$$$$@$$@@#^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^^MMMMMMMMMMMMM$@@$$$$@@%^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^%MMMMMMMMMMMMMM$#####@%^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^^@MMMMMMMMMMMMMMM@@###^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^^%MMMM$#$$$MMM$$$$$$@%^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^^@MMMM$@#^%MMMM@####%^^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^%MMM$$$@%^^@M$@#$$@#^^^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^%$$#%@#%^^^#M$#%MM$^^^^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^^#M#^%@%%^^%$@^^%##^^^^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^^^@@#%^%%^^%@$%^%##^^^^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^^^^^%^^^^^^^@$%^%$@%^^^^^^^^^^^^^^^^^^^^|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^%%%^^^^^^^^^^^^^^^^^^^^|
+--------------------------------------------------------------+


# Tool of the week
## cat

cat - concatenate files and print on the standard output

```markdown
> cat example.txt
This is the first line with three spaces at the end.   
This is the second line containing      TAB     characters.
This line contains some garbage.
 
There are some empty lines around this one.
 
 
 
Finally, this is the last line.
```


# Tool of the week
## cat

-n, --number
  number all output lines

```markdown
> cat --number example.txt
     1  This is the first line with three spaces at the end.   
     2  This is the second line containing      TAB     characters.
     3  This line contains some garbage.
     4  
     5  There are some empty lines around this one.
     6  
     7  
     8  
     9  Finally, this is the last line.
```


# Tool of the week
## cat

-b, --number-nonblank
  number nonempty output lines{~, overrides -n~}

```markdown
> cat --number-nonblank example.txt
     1  This is the first line with three spaces at the end.   
     2  This is the second line containing      TAB     characters.
     3  This line contains some garbage.
 
     4  There are some empty lines around this one.
 
 
 
     5  Finally, this is the last line.
```


# Tool of the week
## cat

-s, --squeeze-blank
  suppress repeated empty output lines

```markdown
> cat --squeeze-blank example.txt
This is the first line with three spaces at the end.
This is the second line containing      TAB     characters.
This line contains some garbage.

There are some empty lines around this one.

Finally, this is the last line.
```


# Tool of the week
## cat

--squeeze-blank
--number

```markdown
> cat --squeeze-blank --number example.txt
     1  This is the first line with three spaces at the end.
     2  This is the second line containing      TAB     characters.
     3  This line contains some garbage.
     4
     5  There are some empty lines around this one.
     6
     7  Finally, this is the last line.
```

```markdown
{~Following the Unix-philosophy this should look something like this:~}
> cat example.txt | sqz | nbr
{~☺~}
```


# Tool of the week
## cat

cat f - g
  Output f's contents, then standard input, then g's contents.


# Sidenotes
## Redirection

Redirection {~allows commands' file handles to be duplicated, opened,
closed, made to refer to different files, and~} can change the files
the command reads from and writes to.

Redirecting Output: [n]>word
  word to be opened for writing on file descriptor n{~, or the standard
  output (filedescriptor 1) if n is not specified. If the file does not
  exist it is created; if it does exist it is truncated to zero size.~}
  {~Note the noclobber option.~}

{~[demo]~}

```markdown
{~Reference:
• man bash~}
```


# Sidenotes
## Here strings

A variant of here documents, the format is:
<<<word

{~The word undergoes ... expansions, then the~} result is supplied as
a single string to the command on its standard input.


# Tool of the week
## cat

{~cat f - g
  Output f's contents, then standard input, then g's contents.~}

```markdown
> cat first.txt
This
  is the
   content of the
       first file.
> cat second.txt
This is
    the content of
    the second file.

> cat first.txt - second.txt > result.txt <<< "{~This is something in between.~}"
```


# Tool of the week
## cat

{~cat f - g
  Output f's contents, then standard input, then g's contents.~}

```markdown
> cat result.txt
This
  is the
   content of the
       first file.
{~This is something in between.~}
This is
    the content of
    the second file.
```


# GNU/Linux Tools II.

{~• Tool of the week~}
• Request of the week
{~• Homework~}


# Request of the week
## screen

screen - screen manager with VT100/ANSI terminal emulation

{~[GNU screen]~}

```markdown
{~References:
• man screen or
• https://www.gnu.org/software/screen/manual/screen.html~}
```


# Request of the week
## screen

{~screen - screen manager with VT100/ANSI~} terminal {~emulation~}


# Sidenotes
## Computer terminal

A computer terminal is an electronic or electromechanical hardware
device that is used for entering data into, and displaying data from,
a computer or a computing system.

{~The term terminal covers all remote terminals, including graphical interfaces.~}

{~[DEC VT100]~}

```markdown
{~Reference:
• https://en.wikipedia.org/wiki/Computer_terminal~}
```


# Request of the week
## screen

{~screen - screen manager with VT100/ANSI~} terminal emulation


# Sidenotes
## Terminal emulator

emulates a video terminal within some other display architecture

{~terminal window ≅ terminal emulator inside a GUI~}

Some character-oriented terminal emulators:
  • Linux
    · Linux terminal {~(text mode, framebuffer) [VT subsystem of the Linux kernel]~}

  • X Window terminals {~(1984, MIT)~}
    · xterm {~(1984, emulates VT220 and Tektronix 4010)~}
    · xvt {~(1992, emulates VT100 for the X window system)~}
    · rxvt {~(1997?, emulates VT102, ouR XVT)~}
    · konsole {~(1998?, KDE Project)~}
    · gnome-terminal {~(1999?, emulates xterm, GNOME Project)~}

```markdown
                            ⤷
```


# Sidenotes
## Terminal emulator

{~emulates a video terminal within some other display architecture

terminal window ≅ terminal emulator inside a GUI~}

Some character-oriented terminal emulators (continued):
  • Command-line interface
    · GNU screen {~(1987, terminal multiplexer)~}
    · tmux {~(2007, includes most features of GNU screen)~}

  {~• Others (for MS-DOS, Microsoft Windows, macOS, etc.)~}

{~There are block-oriented terminal emulators, too.~}

```markdown
{~References:
• https://en.wikipedia.org/wiki/Terminal_emulator
• https://en.wikipedia.org/wiki/List_of_terminal_emulators~}
```


# Request of the week
## screen

{~screen - screen manager with~} VT100/ANSI {~terminal emulation~}


# Sidenotes
## VT100 / ANSI

VT100: video terminal{~, introduced in 1978 by DEC~}
  • 132 columns and 24 rows
  • ANSI X3.64 standard for command codes
    ･ blinking, bolding, reverse video, and underlining
    ･ box-drawing character set
          {~Esc ( 0 switched the codes for lower-case ASCII letters to draw
          this set, and the sequence Esc ( B switched back.~}

```markdown
{~References:
• https://en.wikipedia.org/wiki/VT100~}
```


# Sidenotes
## Box-drawing characters example I.

```markdown
  {~0 1 2 3 4 5 6 7 8 9 ~}a{~ b c ~}d e{~ f
~}6{~                     ~}┘{~ ┐ ┌ ~}└ ┼{~
7   ─     ├ ┤ ┴ ┬ │~}

> printf "\x1b(0 \x6d\x6e\x6a = \x1b(B \x6d\x6e\x6a \n"
 └┼┘ = mnj 
```

```markdown
{~References:
• https://en.wikipedia.org/wiki/Box-drawing_character
• https://en.wikipedia.org/wiki/ANSI_escape_code
• https://en.wikipedia.org/wiki/ASCII_art~}
```


# Sidenotes
## Box-drawing characters example II.

```markdown
    ████████████████████████████████████████
    █▄        ┌─┬┐  ╔═╦╗  ╓─╥╖  ╒═╤╕       █░
    █▄▀       │ ││  ║ ║║  ║ ║║  │ ││       █░
    █▄▀       ├─┼┤  ╠═╬╣  ╟─╫╢  ╞═╪╡       █░
    █▄▀       └─┴┘  ╚═╩╝  ╙─╨╜  ╘═╧╛       █░
    █▄▀       ┌────────────────────┐       █░
    █▄▀       │  ╔═══╗ Box-drawing │▒      █░
    █▄▀       │  ╚═╦═╝   example   │▒      █░
    █▄▀       ╞═╤══╩══╤════════════╡▒      █░
    █▄▀       │ ├──┬──┤            │▒      █░
    █▄▀       │ └──┴──┘            │▒      █░
    █▄▀       └────────────────────┘▒      █░
    █▄▀        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      █░
    █▄▀                                    █░
    ████████████████████████████████████████░
     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```


# Sidenotes
## VT100 art and animations

http://artscene.textfiles.com/vt100/

{~[demo]~}

{~Use wget and pv to play these animations.
  wget: non-interactive network downloader
  pv: monitor the progress of data through a pipe (has rate limiting option)~}

```markdown
{~Reference:
• http://artscene.textfiles.com/vt100/~}
```


# screen
## Getting started

• screen -S <name>    {~start session with name~}
• screen -ls          {~list running sessions~}
• screen -x           {~attach to a running session~}
• screen -r <name>    {~attach to session with name~}
• screen -dRR         {~ultimate attach (reattach a session and if necessary~}
                      {~detach or create it, use the first session if~}
                      {~more than one session is available)~}

```markdown
{~Reference:
• http://aperiodic.net/screen/quick_reference~}
```


# screen
## Getting started

• screen -c file      {~use file as the configuration file~}
                      {~instead of the default $HOME/.screenrc~}
• screen -U           {~run screen in UTF-8 mode~}
• screen -T           {~set $TERM environment variable~}

```markdown
{~Example:
screen -U -dRR -c $HOME/.screenrc.test -T screen-256color~}
```


# screen
## commands

{~Customizable~} command character: each command begins with a Control-a
{~(CTRL-a, C-a, ^A or ^a)~} keystroke.

```markdown
{~Reference:
https://www.gnu.org/software/screen/manual/screen.html#Command-Character~}
```


# screen
## commands

Help

• list keybindings              C-a ?


# screen
## commands

Getting out

• exit session                  exit {~(or C-d)~} {~in all windows,
                                after closing all applications
                                in each window~}
• detach                        C-a d
• detach and logout             C-a D D
{~• exit screen                   C-a \ (not recommended)~}
{~• force-exit screen             C-a C-\ (not recommended)~}


# screen
## commands

Window management

Create
  • new window                  C-a c

{~Destroy~}
  {~• current window              C-a k (not recommended)~}
  {~• all windows                 C-a \ (not recommended)~}


# screen
## commands

Window management

Change to
  • last-visited active window  C-a C-a
  • window by number            C-a <number>
  • window by number or name    C-a '
  • next window in list         C-a n or C-a <space>
  • previous window in list     C-a p or C-a <backspace>
  • chosen window from list     C-a " {~(lists windows, then you can choose)~}

Rename current window           C-a A


# screen
## commands

```markdown
  
  
  
  If you want...
          ... we can see more
                            • commands,
                            • details,
                            • configuration settings
                                                     next time!
```


# GNU/Linux Tools II.

{~• Tool of the week
• Request of the week~}
• Homework


# Homework
## cat

• What does the -A option do?

• What is the long name of the -A option?

• What will be the output of the below command?
  {~Find example.txt in the repository!~}

```markdown
  > cat -A example.txt
```


# Homework
## ASCII animations

• What other tools could have been used instead of pv?

{~• Show us your favorite ASCII art!~}


# Homework
## screen

• How can you start a new screen in screen {~(nested session)~}?

• How can you detach from that inner screen?
