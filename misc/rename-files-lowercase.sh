#!/bin/sh

folder=$1

for file in `ls $folder`; do
    file_lc=`echo $file | tr '[:upper:]' '[:lower:]'`
    echo $file_lc
    mv $folder/$file $folder/$file_lc
done
