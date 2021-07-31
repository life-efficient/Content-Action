#!/bin/sh -l

python action.py
time=$(date)
echo "::set-output name=time::$time"