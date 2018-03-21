#!/bin/bash

set -e
set -u

main_test() {
    local -A test_data=(
        [1]=1
        [2]=2
        [3]=fizz
        [4]=4
        [5]=buzz
        [6]=fizz
        [7]=7
        [8]=8
        [9]=fizz
        [10]=buzz
        [11]=11
        [12]=fizz
        [13]=13
        [14]=14
        [15]=fizzbuzz
        [666]=fizz
        [945]=fizzbuzz
    )

    local keys=${!test_data[@]}
    for key in ${keys}; do
        test_fizzbuzz "${key}" "${test_data[${key}]}"
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
