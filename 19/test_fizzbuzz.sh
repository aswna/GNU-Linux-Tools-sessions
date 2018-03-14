#!/bin/bash

set -e
set -u

main_test() {
    local -a test_data=(1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz)
    local test_data_lenght=${#test_data[@]}

    local i
    for i in $(seq 0 $((test_data_lenght - 1))); do
        test_fizzbuzz $((i+1)) "${test_data[${i}]}"
    done
}

test_fizzbuzz() {
    local input_number="${1}"
    local expected_value="${2}"

    local return_value
    return_value=$(./fizzbuzz.sh "${input_number}")
    if [ "${return_value}" != "${expected_value}" ]; then
        echo "test failed: return value (${return_value}) does not match expected value (${expected_value}) for input number (${input_number})."
        exit 1
    fi
}

main_test
