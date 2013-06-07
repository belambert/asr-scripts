#!/bin/sh



folder=$1

for file in `ls $folder`; do
    
    echo $file
    cat $folder/$file

done