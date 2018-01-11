# Notes
## Patching
### Example with plain files
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

To check the changes, you can use the `vimdiff` command as well.

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

### Example with files residing in subdirectories

Let's see the directory structures and the differences!

    > find reference_directory
    reference_directory
    reference_directory/a
    reference_directory/a/b
    reference_directory/a/b/c
    reference_directory/a/b/c/a.txt
    reference_directory/a/b/c/c.txt
    
    > find directory_on_server_1
    directory_on_server_1
    directory_on_server_1/a
    directory_on_server_1/a/b
    directory_on_server_1/a/b/c
    directory_on_server_1/a/b/c/a.txt
    directory_on_server_1/a/b/c/c.txt

    > diff -ru reference_directory directory_on_server_1
    diff -ru reference_directory/a/b/c/a.txt directory_on_server_1/a/b/c/a.txt
    --- reference_directory/a/b/c/a.txt     2018-01-10 14:18:58.434658357 +0100
    +++ directory_on_server_1/a/b/c/a.txt   2018-01-10 15:14:21.584069078 +0100
    @@ -3,6 +3,9 @@
     3
     4444444444444
     AAAA
    +CCCC
    +CCCC
    +CCCC
     BBBB
     8888888888888
     9

Now we create the patch file (*directory_patch*).

    > diff -ru reference_directory directory_on_server_1 >directory_patch

Apply the patch on an other directory with the same structure.

    > cp -r reference_directory directory_on_server_2
    > patch --dry-run --verbose directory_on_server_2 directory_patch
    Hmm...  Looks like a unified diff to me...
    The text leading up to this was:
    --------------------------
    |diff -ru reference_directory/a/b/c/a.txt
    directory_on_server_1/a/b/c/a.txt
    |--- reference_directory/a/b/c/a.txt    2018-01-10
    14:18:58.434658357 +0100
    |+++ directory_on_server_1/a/b/c/a.txt  2018-01-10
    15:14:21.584069078 +0100
    --------------------------
    File directory_on_server_2 is not a regular file -- refusing to
    patch
    Hunk #1 ignored at 3.
    1 out of 1 hunk ignored
    done

As you can see, the previous method does not work for directories, only
for files. We can work with that using the other method for invoking
`patch` command with the *--strip* option.

    > cd directory_on_server_2
    > patch --dry-run --verbose --strip 1 < ../directory_patch
    Hmm...  Looks like a unified diff to me...
    The text leading up to this was:
    --------------------------
    |diff -ru reference_directory/a/b/c/a.txt
    directory_on_server_1/a/b/c/a.txt
    |--- reference_directory/a/b/c/a.txt    2018-01-10
    14:18:58.434658357 +0100
    |+++ directory_on_server_1/a/b/c/a.txt  2018-01-10
    15:14:21.584069078 +0100
    --------------------------
    checking file a/b/c/a.txt
    Using Plan A...
    Hunk #1 succeeded at 3.
    done
    
    > patch --backup --strip 1 < ../directory_patch
    patching file a/b/c/a.txt
    
    > diff -r directory_on_server_1 directory_on_server_2
    Only in directory_on_server_2/a/b/c: a.txt.orig

The patch has been applied successfully, the backup has been created as
well.
