#!/bin/bash
echo "Hello, $USER!"
echo -n "Are you ready or not? [y/n] "
read valasz
#if [ "$valasz" = "y" ];then
#    echo "OK"
#fi
[ "$valasz" = "y" ] && echo "OK"
