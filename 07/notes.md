# Notes
## GNU parallel

GNU parallel builds and executes shell command lines in parallel.

### Testing with sleep

Running six sleep command with a single job slot.

    > time parallel -j 1 sleep ::: 1 2 3 4 5 10
    parallel -j 1 sleep ::: 1 2 3 4 5 10  0.08s user 0.05s system 0% cpu 27.528 total

Running six sleep command with three job slots.

    > time parallel -j 3 sleep ::: 1 2 3 4 5 10
    parallel -j 3 sleep ::: 1 2 3 4 5 10  0.09s user 0.04s system 0% cpu 13.344 total

Running six sleep command with a hundred job slots.

    > time parallel -j 100 sleep ::: 1 2 3 4 5 10
    parallel -j 100 sleep ::: 1 2 3 4 5 10  0.10s user 0.04s system 1% cpu 10.647 total

### Testing with ssh

Running four ssh command with the default number of job slots to print out the hostnames.

*Note: the output order can be different for below executions.*

    > parallel ssh -l user {} hostname ::: host1 host2 host3 host4
    host1
    host2
    host3
    host4

Snippet from the manual about the *-j* option:

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
parallel-ssh is a program for executing ssh in parallel on a number of hosts.

Running parallel-ssh on four hosts to print out the hostname of each host.

    > parallel-ssh -l user --host="host1 host2 host3 host4" 'hostname'
    [1] 15:23:26 [SUCCESS] host1
    [2] 15:23:26 [SUCCESS] host2
    [3] 15:23:26 [SUCCESS] host4
    [4] 15:23:26 [SUCCESS] host3

Running parallel-ssh on four hosts to print out the hostname of each host.
Below option displays the output as each host completes.

    > parallel-ssh -l user --host="host1 host2 host3 host4" --inline-stdout 'hostname'
    [1] 15:24:27 [SUCCESS] host2
    host2
    [2] 15:24:27 [SUCCESS] host1
    host1
    [3] 15:24:27 [SUCCESS] host3
    host3
    [4] 15:24:27 [SUCCESS] host4
    host4

Running parallel-ssh on four hosts to print out the hostname of each host.
Below option displays the output as it arrives (outputs can be interleaved).

    > parallel-ssh -l user --host="host1 host2 host3 host4" --print 'hostname'
    host1: host1
    [1] 15:25:28 [SUCCESS] host1
    host3: host3
    [2] 15:25:28 [SUCCESS] host3
    host4: host4
    [3] 15:25:28 [SUCCESS] host4
    host2: host2
    [4] 15:25:28 [SUCCESS] host2
