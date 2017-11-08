# Notes
## GNU parallel
GNU parallel builds and executes shell command lines in parallel.

### Testing with sleep
    > time parallel -j 1 sleep ::: 1 2 3 4 5 10
    parallel -j 1 sleep ::: 1 2 3 4 5 10  0.08s user 0.05s system 0% cpu 27.528 total

    > time parallel -j 3 sleep ::: 1 2 3 4 5 10
    parallel -j 3 sleep ::: 1 2 3 4 5 10  0.09s user 0.04s system 0% cpu 13.344 total

    > time parallel -j 100 sleep ::: 1 2 3 4 5 10
    parallel -j 100 sleep ::: 1 2 3 4 5 10  0.10s user 0.04s system 1% cpu 10.647 total

### Testing with ssh
    > parallel ssh -l user {} hostname ::: host1 host2 host3 host4
    host1
    host2
    host3
    host4
    *[output order can be different]*

    > man parallel
    ...
    -j N
    --jobs N
    --max-procs N
    -P N
        Number of jobslots. 0 means as many as possible. Default is 100%
        which will run one job per CPU core.
    ...

## parallel-ssh
    > parallel-ssh -l user --host="host1 host2 host3 host4" 'hostname'
    [1] 15:23:26 [SUCCESS] host1
    [2] 15:23:26 [SUCCESS] host2
    [3] 15:23:26 [SUCCESS] host4
    [4] 15:23:26 [SUCCESS] host3
    *[output order can be different]*

    > parallel-ssh -l user --host="host1 host2 host3 host4" --inline-stdout 'hostname'
    [1] 15:24:27 [SUCCESS] host2
    host2
    [2] 15:24:27 [SUCCESS] host1
    host1
    [3] 15:24:27 [SUCCESS] host3
    host3
    [4] 15:24:27 [SUCCESS] host4
    host4
    *[output order can be different]*

    > parallel-ssh -l user --host="host1 host2 host3 host4" --print 'hostname'
    host1: host1
    [1] 15:25:28 [SUCCESS] host1
    host3: host3
    [2] 15:25:28 [SUCCESS] host3
    host4: host4
    [3] 15:25:28 [SUCCESS] host4
    host2: host2
    [4] 15:25:28 [SUCCESS] host2
    *[output order can be different]*
