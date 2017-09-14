# GNU/Linux Tools


# GNU/Linux Tools I.

• Introduction (history)
{~• Tool of the week
• Request of the week~}


# GNU/Linux Tools I.

{~• Introduction (history)~}
• Tool of the week
{~• Request of the week~}


# GNU/Linux Tools I.

{~• Introduction (history)
• Tool of the week~}
• Request of the week


# Introduction
## Operating Systems

An operating system (OS) is system software that
• manages computer hardware and software resources,
• provides common services for computer programs.

All computer programs (excluding firmware) require
an OS to function.

```markdown
{~Reference:
• https://en.wikipedia.org/wiki/Operating_system~}
```


# Operating Systems
## OS common features

┌──────────────────┐
│       User       │
└──────────────────┘
      ↓      ↑
┌──────────────────┐
│   Application    │
└──────────────────┘
      ↓      ↑
┌──────────────────┐
│ Operating System │
└──────────────────┘
      ↓      ↑
┌──────────────────┐
│     Hardware     │
└──────────────────┘

```markdown
{~Reference:
• https://goo.gl/soMFop (OS common features)~}
```


# Operating Systems
## OS Components

• Kernel
{~• Networking
• Security
• User interface (shell)~}


# OS Components
## Kernel

The kernel is a computer program that is the core
of a computer's operating system, with complete
control over everything in the system.

• monolithic kernel {~(speed)~}
• microkernel {~(modularity)~}
• hybrid kernels
{~• nanokernel ≅ picokernel
• exokernel~}


# Operating Systems
## Examples

• Unix and Unix-like OSes
 ･ BSD and its descendants
 ･ macOS
 ･ Linux
• Microsoft Windows
• Other

```markdown
{~Reference:
• https://goo.gl/3Q9fQk (Examples of OSes)~}
```


# Operating Systems
## Timeline

• 1950s: basic OS features (monitoring)
• 1960s: modern and more complex features
  ･ runtime libraries
  ･ interrupts
  ･ parallel processing
• 1980s: personal computers

```markdown
{~Reference:
• https://en.wikipedia.org/wiki/Operating_system#History
• https://en.wikipedia.org/wiki/Timeline_of_operating_systems
• https://en.wikipedia.org/wiki/History_of_operating_systems~}
```


# Operating Systems
## "Unix" history

Some Unix and Unix-like operating systems

• 1964: Multics {~(novel and valuable ideas)~}
• 1969: Ken Thompson {~(Space Travel, PDP-7)~}
• 1970: Unics {~(+ Dennis Ritchie & Brian Kernighan)~}
• 1971: Unix {~- philosophy~}
{~• 1972: Unix is rewritten in C (portability)
• 1983: GNU Project (Richard Stallman)
• 1987: Minix (Andrew S. Tanenbaum)
• 1991: Linux (Linus Torvalds, v0.01, 10,239 LoC)
• 1992: GNU/Linux (released under GNU GPLv2)
• 1994: GNU/Linux (v1.0.0, 176,250 LoC)
• 2017: GNU/Linux (v4.13) [4.12 = 24,170,860 LoC]~}

```markdown
{~References:
• https://en.wikipedia.org/wiki/Multics
• https://en.wikipedia.org/wiki/Unix
• https://goo.gl/x6N9dU (Unix history)
• http://simh.trailing-edge.com/photos.html
• https://www.bell-labs.com/usr/dmr/www/1stEdman.html~}
```


# Operating Systems
## Unix philosophy

"minimalist, modular software development"
{~"simple, short, clear, modular, and extensible code"~}

Write programs
• that do one thing and do it well,
• to work together,
• to handle text streams (universal interface).
{~Peter H. Salus, 1994~}

┌──────────────────────────────────────────────────────┐
│ Unix is simple.                                      │
│ It just takes a genius to understand its simplicity. │
│ {~Dennis Ritchie~}                                       │
└──────────────────────────────────────────────────────┘
☺

```markdown
{~Reference:
• https://en.wikipedia.org/wiki/Unix_philosophy~}
```


# Operating Systems
## "Unix" history cont'd

Some Unix and Unix-like operating systems

{~• 1964: Multics (novel and valuable ideas)
• 1969: Ken Thompson (Space Travel, PDP-7)
• 1970: Unics (+ Dennis Ritchie & Brian Kernighan)
• 1971: Unix - philosophy~}
• 1972: Unix is rewritten in C {~(portability)~}
• 1983: GNU Project {~(Richard Stallman)~}
• 1987: Minix {~(Andrew S. Tanenbaum)~}
• 1991: Linux {~(Linus Torvalds, v0.01, 10,239 LoC) [listen the pronunciations]~}
• 1992: GNU/Linux {~(released under GNU GPLv2)~}
• 1994: GNU/Linux {~(v1.0.0, 176,250 LoC)~}
• 2017: GNU/Linux {~(v4.13) [4.12 = 24,170,860 LoC]~}

```markdown
{~LoC ≝ lines of code

References:
• https://en.wikipedia.org/wiki/GNU_Project
• https://en.wikipedia.org/wiki/MINIX
• https://en.wikipedia.org/wiki/Linux_kernel
• ftp://ftp.funet.fi/pub/Linux/PEOPLE/Linus/SillySounds/~}
```


# Operating Systems
## GNU/Linux

The Linux kernel is a monolithic kernel, supporting
• true preemptive multitasking,
• virtual memory,
• shared libraries,
• demand loading,
• shared copy-on-write executables,
• memory management,
• the Internet protocol suite and
• threading.

```markdown
{~Reference:
• https://en.wikipedia.org/wiki/Linux_kernel~}
```


# Operating Systems
## OS Components

{~• Kernel
• Networking
• Security~}
• User interface (shell)


# OS Components
## Shell

In computing, a shell is a user interface for
interacting with an OS.
• CLI
{~• TUI
• GUI~}

[demo]

It is named a shell because it is a layer around
the operating system kernel.


# Unix shells
## History

{~• 1964: Multics RUNCOM (Louis Pouzin) (executing command scripts)
• 1965: Multics shell (Glenda Schroeder) (ordinary user code)~}
• 1971: Thompson shell [sh] {~(Ken Thompson) (simple command interpreter)~}
• 1975: PWB (Mashey) shell [sh] {~(John Mashey) (programming)~}
• 1977: Bourne shell [sh] {~(Stephen Bourne) (scripting)~}
• 1978: C shell [csh] {~(Bill Joy) (more interactive, C-like)~}
• 1983: TENEX C shell [tcsh] {~(Ken Greer) (backward compatible with the C shell)~}
• 1983: Korn shell [ksh] {~(David Korn) (between the Bourne shell and the C shell)~}
• 1989: Almquist shell [ash] {~(Kenneth Almquist, BSD) (lightweight Bourne shell clone)~}
• 1989: Bourne-again shell [bash] {~(Brian Fox, GNU)
          free shell that could run existing shell scripts~}
• 1990: Z shell [zsh] {~(Paul Falstad) (extended Bourne shell, Oh My Zsh)~}
• 1997: Debian Almquist shell [dash] {~(Herbert Xu, Debian)~}

```markdown
{~Reference:
• https://en.wikipedia.org/wiki/Command-line_interface#History
• https://en.wikipedia.org/wiki/Unix_shell
• https://en.wikipedia.org/wiki/Comparison_of_command_shells~}
```


# Unix shells
## Fun

┌─────────────────────────────────────────────────────────┐
│ Nobody really knows what the Bourne shell's grammar is. │
│ Even examination of the source code is little help.     │
│ {~Tom Duff (rc shell, Version 10 Unix and Plan 9)~}         │
└─────────────────────────────────────────────────────────┘
☺


# GNU/Linux Tools I.

{~• Introduction~}
• Tool of the week
{~• Request of the week~}


# Tool of the week
## script

make typescript of terminal session
{~hardcopy record of an interactive session~}


# Tool of the week
## script

[demo]


# Tool of the week
## script

-t, --timing
  Output timing data to standard error,
  or to file when given.

[demo]
{~see scriptreplay, too~}


# Tool of the week
## script

-f, --flush
  Flush output after each write.
  {~Useful for telecooperation.~}

[demo]


# GNU/Linux Tools I.

{~• Introduction
• Tool of the week~}
• Request of the week


# Request of the week
## Performance &
## limitations

When to use and not to use shell scripts?

• low barrier of entry
• usability
• task automation
• speed
• low level operations
• dependencies
• data types
• debugging
• security
