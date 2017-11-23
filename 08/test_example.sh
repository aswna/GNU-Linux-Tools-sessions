#!/bin/bash

set -u
set -e

GLOBAL_VARIABLE_WITH_ALL_CAPITAL_LETTERS=999

main() {
    delete_something
    create_something_because_it_is_needed
    create_something_just_for_fun "${@}"
}

delete_something() {
    local sleep_time
    sleep_time=$((GLOBAL_VARIABLE_WITH_ALL_CAPITAL_LETTERS / 999))
    echo "Now deleting..."
    sleep "${sleep_time}"
}

create_something_because_it_is_needed() {
    create "needed"
}

create_something_just_for_fun() {
    create "fun" "${@}"
}

create() {
    local name="${1}"
    shift
    echo "creating, because it is ${name}"
    for arg in "${@}"; do
        echo "  arg = ${arg}"
    done
}

main "${@}"
