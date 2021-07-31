#!/bin/sh -l

time=$(date)
echo "::set-output name=time::$time"
python action.py || exit 1