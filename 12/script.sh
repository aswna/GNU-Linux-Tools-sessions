#!/bin/bash
echo "Hello, ${USER}!"
echo -n "Are you ready or not? [y/n] "
read answer
echo "Your answer was '${answer}'"
if [ "${answer}" = "y" ]; then
    echo "OK. You are ready!"
else
    echo "Fine. Then take your time, check back later..."
fi
