# Notes
## Find matching lines with number of occurrences
### Using awk
Print the first to fields (date and time).

    > awk 'BEGIN{counter=0;} /some-pattern-to-be-matched/{counter++; print $1 " " $2} END{print(counter);}' *
    2017-10-21 05:03:44,717
    2017-10-21 12:50:31,013
    2017-10-21 12:52:59,174
    2017-10-21 18:18:27,884
    2017-10-21 20:09:51,316
    2017-10-21 20:37:05,144
    2017-10-21 23:02:29,962
    2017-10-22 04:47:01,219
    2017-10-22 14:19:22,560
    2017-10-07 13:04:10,659
    2017-10-07 14:00:19,203
    11

If you want to manipulate the matched lines (print the number of matches first, then the matched lines), you can try:

    > awk 'BEGIN{counter=0; matches="";} /some-pattern-to-be-matched/{counter++; matches=(matches $1 " " $2 "\n");} END{print(counter); printf(matches);}' *

### Using grep and tee (duplicating stdout to stderr)
Print the first 19 characters (date and time).

    > grep -h 'some-pattern-to-be-matched' * | cut -c -19 | tee /dev/stderr | wc -l
    2017-10-21 05:03:44
    2017-10-21 12:50:31
    2017-10-21 12:52:59
    2017-10-21 18:18:27
    2017-10-21 20:09:51
    2017-10-21 20:37:05
    2017-10-21 23:02:29
    2017-10-22 04:47:01
    2017-10-22 14:19:22
    2017-10-07 13:04:10
    2017-10-07 14:00:19
    11

## Vim line numbers
See my [line numbers toggle function](https://github.com/aswna/Environment/blob/master/.vim/functions/line_numbers_toggle.vim).
You can map this function to your preferred key, see my
[mappings](https://github.com/aswna/Environment/blob/master/.vim/config/mappings.vim).
