#!/bin/bash

# Script for making 3 files that are common: notest.txt, example_data.py, input_data.py

files=("notes.txt" "example_data.py" "input_data.py")

for file in ${files[@]}; do
    touch $file
done

echo $(date +'%m/%d/%Y') >> notes.txt