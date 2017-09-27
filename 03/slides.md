# GNU/Linux Tools


# GNU/Linux Tools III.

• Homework check
{~• Request of the week (continued)~}


# Homework check
## cat

{~• What does the -A option do?~}
Displays non-printing characters,
 - uses ^ and M- notation{~, except for line-feed and TAB~}
 - displays $ at end of each line
 - displays TAB characters as ^I

{~• What is the long name of the -A option?~}
 --show-all


# Homework check
## cat

{~• What will be the output of the below command?~}
```markdown
> cat -A example.txt
This is the first line with three spaces at the end.   $
This is the second line^Icontaining^ITAB^Icharacters.$
This line contains some ^[[3~^?^[[2~^[O^[O^[O^?garbage.$
$
There are some empty lines around this one.$
$
$
$
Finally, this is the last line.$
```


# Homework check
## ASCII animations

{~• What other tools could have been used instead of pv?~}
Some examples:
 - while read -r line; do echo "$line"; sleep 0.03; done
 - awk '{print $0; system("sleep 0.03")}'
 - perl -MTime::HiRes=usleep -pe '$|=1a; usleep(30000)'
 - perl -pe 'select(undef, undef, undef, 0.03)'
 - https://grox.net/software/mine/slowcat/slowcat.c
 ...

{~• Show us your favorite ASCII art!~}


# Homework check
## screen

{~• How can you start a new screen in screen (nested session)?~}
 - start screen with the -m option (enforced creation of new shell)
   {~screen -m~}
 - clear the $STY environment variable, then start screen
   {~unset STY~}
   {~screen~}
 - within the running screen session start a new named screen session
   {~screen -S foobar~}
 - within the running screen session ssh to localhost, then start a
   new screen session
   {~ssh localhost~}
   {~screen~}

{~• How can you detach from that inner screen?~}
 - Use "C-a a" as the command character for issuing commands for the
   inner screen session
   {~C-a a d~} or
   {~C-a a :detach~}
 - Use different control characters for the different screen sessions
   {~F.i. start nested screen as: screen -ea~}


# Sidenote
## foobar

Placeholder name like foo, bar, baz, and qux.
Foobar probably relates to FUBAR {~(Fucked Up Beyond All Recognition / Any
Repair / All Reason)~} military slang, which dates from World War II.

The word foo on its own was used earlier in the comic Smokey Stover as
"good luck". This may be related to the Chinese word fu ("福", sometimes
transliterated foo), which can mean happiness.

```markdown
{~References:
• https://en.wikipedia.org/wiki/Foobar
• https://en.wikipedia.org/wiki/List_of_military_slang_terms#FUBAR~}
```


# GNU/Linux Tools III.

{~• Homework check~}
• Request of the week (continued)


# screen
## Regions (splits)

Display more than one window on the user's display. This is done by
splitting the screen in regions, which can contain different windows.

• split display horizontally    C-a S
• split display vertically      C-a | {~(since v4.1)~}

• jump to next display region   C-a <Tab>

• remove current region         C-a X
• remove all regions but the current one        C-a Q

• change window size to fit the current region  C-a F
  {~(if the window is displayed more than once screen does not adapt the
  window size automatically)~}

{~[demo]~}

```markdown
{~References:
• https://www.gnu.org/software/screen/manual/screen.html#Regions
• http://aperiodic.net/screen/quick_reference#split_screen~}
```


# screen
## Monitoring

Monitoring for activity

• monitor [state]               C-a M
  {~Toggles monitoring of the current window.~}

• activity <message>
  {~Example: activity 'Activity in window %n %t'~}

```markdown
{~Reference:
• https://www.gnu.org/software/screen/manual/screen.html#Monitor~}
```


# screen
## Monitoring

Monitoring for silence

• silence [state|sec]           C-a _
  {~Toggles silence monitoring of the current window.~}
  {~state: on|off~}

• silencewait seconds
  {~Default is 30 seconds.~}

```markdown
{~Reference:
• https://www.gnu.org/software/screen/manual/screen.html#Silence~}
```


# screen
## Logging

```markdown
• hardcopy                      C-a h {~or~} C-a C-h

• log                           C-a H
  {~turn on logging               screen -L~}
• logfile
  · logfile [filename]
  · logfile [flush secs] {~(default value is 10 seconds)~}
  
```

{~[demo]~}

```markdown
{~References:
• https://www.gnu.org/software/screen/manual/screen.html#Hardcopy
• https://www.gnu.org/software/screen/manual/screen.html#Logging~}
```


# screen
## Logging

```markdown
{~• hardcopy                      C-a h or C-a C-h

• log                           C-a H
  turn on logging               screen -L
• logfile
  · logfile [filename]
  · logfile [flush secs] (default value is 10 seconds)~}
    Question: how to view these logfiles?
```

{~[demo]~}

```markdown
{~References:
• https://www.gnu.org/software/screen/manual/screen.html#Hardcopy
• https://www.gnu.org/software/screen/manual/screen.html#Logging~}
```


# screen
## Logging

```markdown
{~• hardcopy                      C-a h or C-a C-h

• log                           C-a H
  turn on logging               screen -L
• logfile
  · logfile [filename]
  · logfile [flush secs] (default value is 10 seconds)~}
    Answer: pv can come in handy to redisplay the logfile
```

{~[demo]~}

```markdown
{~References:
• https://www.gnu.org/software/screen/manual/screen.html#Hardcopy
• https://www.gnu.org/software/screen/manual/screen.html#Logging~}
```


# screen
## Screen exchange

• bufferfile [exchange-file]
  {~used for reading and writing with the paste buffer~}
• readbuf [filename]            C-a <
  {~read the contents of filename into paste buffer~}
• writebuf [filename]           C-a >
  {~write the contents of paste buffer to filename~}

Example:
Paste the system's password file into the screen window
  C-a :bufferfile /etc/passwd
  C-a <
  C-a ]
  C-a :bufferfile

{~[demo]~}

```markdown
{~Reference:
• https://www.gnu.org/software/screen/manual/screen.html#Screen-Exchange~}
```


# screen
## Multiuser session

• multiuser state
  {~Switch between single-user and multi-user mode.~}

• acladd usernames {~[crypted password]~}
• addacl usernames {~[crypted password]~}
  {~Enable comma separated list of users to fully access this screen session.~}

• aclchg usernames permbits list
• chacl usernames permbits list
  {~Change permissions for a comma separated list of users.~}

```markdown
{~References:
• https://www.gnu.org/software/screen/manual/screen.html#Multiuser-Session
• http://aperiodic.net/screen/multiuser
• http://aperiodic.net/screen/commands:acladd~}
```


# screen
## Multiuser session

Try to attach to an existing session (not yet multiuser-enabled):
screen -x <user>/

Probably you will get the following error message from screen:
Must run suid root for multiuser support.

For this you need to set setuid bit on the screen binary {~(security risk)~}:
sudo chmod u+s /usr/bin/screen

Now you might get a strange error message for 'screen -ls':
Directory '/var/run/screen' must have mode 755.

To make this work you can change the permissions on the directory:
sudo chmod 755 /var/run/screen


# Sidenote
## setuid and setgid

setuid {~(set user ID upon execution)~} and
setgid {~(set group ID upon execution)~} allow users to
run an executable with the permissions of the executable's owner or group

{~(run programs with temporarily elevated privileges)~}


# screen
## Multiuser session

Trying to attach to an existing session {~(still not yet multiuser-enabled)~},
you might get something like this:
chmod /dev/pts/4: Operation not permitted

Set up (or clear) the password for the session:
• Setting up a password:
    :password
    New screen password: {~[passwd]~}
    Retype new password: {~[passwd]~}
    [ Password moved into copybuffer ] {~(This is the encrypted password.)~}
  You can paste it with below command (then you can share it):
    C-a ]
• Clearing the password:
    :password
    New screen password: {~[Enter]~}

Note: without setting up or clearing the password, you might get this during attach:
Screen password: {~[you cannot guess this]~}
crypt() failed.


# screen
## Multiuser session

Set up the multiuser session and access rights in the session:
:multiuser on
:acladd <user> {~[the shared crypted password from the copybuffer]~}

Remove all the <user>'s permissions (still can connect to the session
and view the list of windows):
:aclchg <user> -rwx "#?"

Add permission to <user> to be able to select window 0, view its content
and detach:
:aclchg <user> +rx 0,select,detach

Try to attach to the selected multiuser-enabled session:
screen -x <user>/{~[session name or ID]~}

Kick out <user>:
:acldel <user>
{~<user> removed from acl database~}

On <user>'s terminal: [remote detached from <session>]


# screen
## Multiuser session

You might want to restore the directory permissions:
sudo chmod 775 /var/run/screen

You might want to clear the setuid bit on the screen binary:
sudo chmod u-s /usr/bin/screen
