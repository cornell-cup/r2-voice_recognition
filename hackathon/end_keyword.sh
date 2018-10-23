#!/bin/bash

ps -allf > file.txt
line=$(grep 'speech_to_braille' file.txt) 
kill -INT $(awk '{print $4}' <<< $line)
