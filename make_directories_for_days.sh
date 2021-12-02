#!/bin/bash

# loop from 3 to 25
# mkdir day_{loop_number}

max=25
for i in `seq 3 $max`
do
    mkdir -p "day_$i"
done