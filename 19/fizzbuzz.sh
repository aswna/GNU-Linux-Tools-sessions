#!/bin/bash

input_number=${1}

if [ $((input_number % 15)) -eq 0 ]; then
    echo "fizzbuzz"
elif [ $((input_number % 3)) -eq 0 ]; then
    echo "fizz"
elif [ $((input_number % 5)) -eq 0 ]; then
    echo "buzz"
else
    echo "${input_number}"
fi
