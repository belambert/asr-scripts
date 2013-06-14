#!/bin/sh

memory='2000m'

file=$1

model_file=$HOME/final_models/swb-basic-linear-nivreeager-all.mco

model=`basename $model_file .mco`
model_dir=`dirname $model_file`

basename=`basename $file .tagged.conll`
basename=`basename $basename .tagged`
parsed_file=`dirname $file`/$basename.parsed

java -Xmx$memory -jar ~/software/maltparser/maltparser-1.7.1.jar -w $model_dir -c $model -i $file -m parse -o $parsed_file

