#!/bin/bash

if [[ $1 == "hard" ]]
then
    python3 main_hard.py
else
    python3 main.py
fi

