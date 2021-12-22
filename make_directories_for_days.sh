#!/bin/bash

# Make directories for each day

max=25
for i in `seq 1 $max`
do
    mkdir -p "day-$i"
done

# Below command changes all day_# directory names with underscores to hyphens
# find . -type d -name "day_*" | sed -e "p;s/_/-/g" | xargs -n2 mv