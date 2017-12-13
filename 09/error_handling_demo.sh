#!/bin/bash

set -e
set -u

main() {
    local param1="1"
    local param2="11"

    retry "cmd ${param1} ${param2}" 3
    retry "cmd $((param1 + 1)) $((param2 - 1))" 3
}

retry() {
    local cmd="${1}"
    local max_tries="${2}"

    local rc=1
    local i
    for i in $(seq "${max_tries}"); do
        echo "Trying to execute cmd = ${cmd} (retry = ${i})"
        set +e
        ${cmd}
        rc=${?}
        set -e
        echo "rc = ${rc}"
        if [ ${rc} -eq 0 ]; then
            break
        fi
    done
    if [ "${rc}" -ne 0 ]; then
        echo "Failed to execute command (${cmd}) successfully after ${max_tries} tries."
        return 1
    fi
    echo "Successfully executed command (${cmd}) after ${i} tries."
    echo
}

cmd() {
    echo "  Executing command... (args = ${*})"
    if [ $((RANDOM % 2)) -ne 0 ]; then
        echo "  (successful execution)"
        return 0
    else
        echo "  (failed execution)"
        return 1
    fi
}

main
