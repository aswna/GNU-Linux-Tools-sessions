#!/bin/bash

return_value=$(./fizzbuzz.sh 1)
if [ "${return_value}" -ne 1 ]; then
    echo "test failed"
    exit 1
fi

return_value=$(./fizzbuzz.sh 2)
if [ "${return_value}" -ne 2 ]; then
    echo "test failed"
    exit 2
fi
