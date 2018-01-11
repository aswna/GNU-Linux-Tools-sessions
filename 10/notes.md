# Notes
## Patching
### Example
Let's see a small example of patching the same configuration file at
different places (on different servers). Note that the content of the
files are similar, but not identical (see later).

Check the content of our first file.

    > cat some_config_file_on_server_1.txt
    [common]
    parameter1=value1
    parameter2=value2
    
    [topic10]
    parameter1=value1
    parameter2=value2
    
    [topic20]
    parameter1=value1
    parameter2=value2
    parameter3=value3
    
    [topic30]
    parameter1=value1
    parameter2=value2

Create the backup of the original file.

    > cp some_config_file_on_server_1.txt some_config_file_on_server_1.txt.orig

Edit the file, then check the changes with the `diff` command.

    > diff some_config_file_on_server_1.txt.orig some_config_file_on_server_1.txt
    10,11c10,11
    < parameter1=value1
    < parameter2=value2
    ---
    > parameter20=value20
    > parameter21=value21

For patching we use the unified format, which includes some context, too.

    > diff -u some_config_file_on_server_1.txt.orig some_config_file_on_server_1.txt
    --- some_config_file_on_server_1.txt.orig       2018-01-11 09:05:19.374444897 +0100
    +++ some_config_file_on_server_1.txt    2018-01-11 09:06:43.120161369 +0100
    @@ -7,8 +7,8 @@
     parameter2=value2
    
     [topic20]
    -parameter1=value1
    -parameter2=value2
    +parameter20=value20
    +parameter21=value21
     parameter3=value3
    
     [topic30]

Create the patch file (*patch*) itself.

    > diff -u some_config_file_on_server_1.txt.orig some_config_file_on_server_1.txt > patch

Now, we check whether we could apply this patch on the next file (*--dry-run*).

    > patch --verbose --dry-run some_config_file_on_server_2.txt patch
    Hmm...  Looks like a unified diff to me...
    The text leading up to this was:
    --------------------------
    |--- some_config_file_on_server_1.txt.orig      2018-01-11
    09:05:19.374444897 +0100
    |+++ some_config_file_on_server_1.txt   2018-01-11
    09:06:43.120161369 +0100
    --------------------------
    checking file some_config_file_on_server_2.txt
    Using Plan A...
    Hunk #1 succeeded at 7 with fuzz 1.
    done

The content of the second file has not changed, yet.

    > cat some_config_file_on_server_2.txt
    [common]
    parameter1=value1
    parameter2=value2
    
    [topic12]
    parameter1=value1
    parameter2=value2
    
    [topic20]
    parameter1=value1
    parameter2=value2
    parameter3=value3
    
    [topic32]
    parameter1=value1
    parameter2=value2
    parameter3=value3

Now, we can apply this patch on this second file successfully, also we
are creating a backup as well (see the *.orig* postfix appended to the
original filename).

    > patch --backup some_config_file_on_server_2.txt patch
    patching file some_config_file_on_server_2.txt
    Hunk #1 succeeded at 7 with fuzz 1.

To check the changes, you can use `vimdiff` as well.

    vimdiff some_config_file_on_server_2.txt.orig some_config_file_on_server_2.txt

Now, try to apply our patch on the third file.

    > cat some_config_file_on_server_3.txt
    [common]
    parameter1=value1
    parameter2=value2

    [topic13]
    parameter1=value1
    parameter2=value2
    parameter3=value3

    [topic20]
    parameter1=value1
    parameter2=value2

    [topic33]
    parameter1=value1
    parameter2=value2

Note, that the context of the change is a bit different, so we can guess
that the patch might not work.

    > patch --verbose --dry-run some_config_file_on_server_3.txt patch
    Hmm...  Looks like a unified diff to me...
    The text leading up to this was:
    --------------------------
    |--- some_config_file_on_server_1.txt.orig      2018-01-11
    09:05:19.374444897 +0100
    |+++ some_config_file_on_server_1.txt   2018-01-11 09:06:43.120161369
    +0100
    --------------------------
    checking file some_config_file_on_server_3.txt
    Using Plan A...
    Hunk #1 FAILED at 7.
    1 out of 1 hunk FAILED
    done

As we guessed, the patch would not work. We can work around this
tweaking the fuzz factor of the `patch` command.

    > patch --fuzz 3 --verbose --dry-run some_config_file_on_server_3.txt patch
    Hmm...  Looks like a unified diff to me...
    The text leading up to this was:
    --------------------------
    |--- some_config_file_on_server_1.txt.orig      2018-01-11
    09:05:19.374444897 +0100
    |+++ some_config_file_on_server_1.txt   2018-01-11 09:06:43.120161369
    +0100
    --------------------------
    checking file some_config_file_on_server_3.txt
    Using Plan A...
    Hunk #1 succeeded at 8 with fuzz 3 (offset 1 line).
    done

Let's patch it!

    > patch --fuzz 3 --backup some_config_file_on_server_3.txt patch
    patching file some_config_file_on_server_3.txt
    Hunk #1 succeeded at 8 with fuzz 3 (offset 1 line).

We can check the changes and see that the patch was applied correctly.

    > diff -u some_config_file_on_server_3.txt.orig
    > some_config_file_on_server_3.txt
    --- some_config_file_on_server_3.txt.orig       2018-01-10
    15:52:32.669262611 +0100
    +++ some_config_file_on_server_3.txt    2018-01-11
    09:31:35.991858242 +0100
    @@ -8,8 +8,8 @@
     parameter3=value3
    
     [topic20]
    -parameter1=value1
    -parameter2=value2
    +parameter20=value20
    +parameter21=value21
    
     [topic33]
     parameter1=value1

Great!

What if we did not create a backup and realize that the patch should not
have been applied on a certain file (f.i. the second file). We can apply
the reverse of the patch and revert the change back.

    > patch --reverse --backup some_config_file_on_server_2.txt patch
    patching file some_config_file_on_server_2.txt
    Hunk #1 succeeded at 7 with fuzz 1.

Note that the previous backup file gets overwritten by `patch`, unfortunately.

    > diff some_config_file_on_server_2.txt.orig some_config_file_on_server_2.txt
    10,11c10,11
    < parameter20=value20
    < parameter21=value21
    ---
    > parameter1=value1
    > parameter2=value2

##### DELETE FROM HERE AND BELOW...
[error_handling_demo.sh](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/09/error_handling_demo.sh).
