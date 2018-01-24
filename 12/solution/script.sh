#!/bin/bash

echo "Hello, ${USER}!"
read -p "Are you ready or not? [y/n] " answer
echo "Your answer was '${answer}'"

if [[ "${answer}" =~ ^y$ ]]; then
    echo "OK. You are ready!"
else
    echo "Fine. Then take your time, check back later..."
fi
