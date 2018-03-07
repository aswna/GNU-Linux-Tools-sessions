#!/bin/bash

# TODO:
# - check lifetime of i
# - make testdata local
# - dynamic limits for seq

set -e
set -u

declare -a testdata=(
    1
    2
    fizz
)

main_test() {
    for i in $(seq 0 2); do
        test_fizzbuzz $((i+1)) "${testdata[${i}]}"
    done
}

test_fizzbuzz() {
    local input_number="${1}"
    local expected_value="${2}"

    return_value=$(./fizzbuzz.sh "${input_number}")
    if [ "${return_value}" != "${expected_value}" ]; then
        echo "test failed: return value (${return_value}) does not match expected value (${expected_value}) for input number (${input_number})."
        exit 1
    fi
}

main_test
