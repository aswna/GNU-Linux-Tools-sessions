#!/bin/bash

test_fizzbuzz() {
    local input_number="${1}"
    local expected_value="${2}"

    return_value=$(./fizzbuzz.sh "${input_number}")
    if [ "${return_value}" != "${expected_value}" ]; then
        echo "test failed: return value (${return_value}) does not match expected value (${expected_value}) for input number (${input_number})."
        exit 1
    fi
}

test_fizzbuzz 1 1
test_fizzbuzz 2 2
test_fizzbuzz 3 fizz
