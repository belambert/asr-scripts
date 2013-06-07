#!/bin/bash

for folder in $@; do
    echo "Concatenating match files in folder: $folder"
    cd $folder
    #cat *-?.match *-??.match *-???.match > ALL.match
    cat *-?.match *-??.match > ALL.match
    cd -
done
