#!/bin/sh

file=$1

~/thesis/scripts/lowercase-conll-words.sh $file > $file.lc
mv $file.lc $file

