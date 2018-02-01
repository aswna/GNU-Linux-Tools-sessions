# Notes
## Python script for checking duplicate packets in large files
We have some large files (500 MB), which contain records describing
some IP packets in the following format:

    sequence number    timestamp    ID1    ID2    IP1    IP2


Two records are considered the same if their keys (ID1, ID2, IP1, and IP2)
are the same. The sequence numbers can be ignored.

The goal was to find same records (duplicates) that are within 2.0 seconds
based on their time-stamps.

It is obvious, that it is inefficient to collect all the keys and scan
the input file again and again for matching records (and check the time
stamps).

You can see a more efficient solution in [check_duplicates.py](https://github.com/aswna/GNU-Linux-Tools-sessions/blob/master/13/check_duplicates.py).
