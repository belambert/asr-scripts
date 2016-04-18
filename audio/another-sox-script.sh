#!/bin/bash
# Set the field seperator to a newline
IFS="
"
# Loop through the file
for line in `cat $1`;do
    echo $line
    ~rsingh/bin/shorten -c2 -x $line /net/ayesha/usr3/fisher/audio$line
    sox -U -b -t .sph /net/ayesha/usr3/fisher/audio$line -r 8000 -t .sph -s -w -c 1 /net/ayesha/usr3/fisher/audio$line.ch1.sph avg -l
    sox -U -b -t .sph /net/ayesha/usr3/fisher/audio$line -r 8000 -t .sph -s -w -c 1 /net/ayesha/usr3/fisher/audio$line.ch2.sph avg -r
    rm /net/ayesha/usr3/fisher/audio$line
done

