#!/bin/bash

global_variable=999

# delete something
sleep_time=$((global_variable / 999))
echo "Now deleting..."
sleep "${sleep_time}"

# create something because it is needed
echo "creating, because it is needed"

# create something just for fun
echo "creating, because it is fun"
for arg in "${@}"; do
    echo "  arg = ${arg}"
done
