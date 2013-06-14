#!/bin/sh


memory='2000m'

#test_file=swb-ptb-4-22-13.lc.test.conll
#test_file=swb-ptb-4-22-13-basic.lc.test.conll
#test_file=swb-ptb-4-22-13-collapsed.lc.test.conll
#test_file=swb-ptb-4-22-13-collapsed.lc.test.conll
#prefix=default
#prefix=basic
#prefix=collapsed

test_file=$1

#for model in `ls *.mco`; do 
#for model in `ls engmalt*.mco`; do 
for model in `ls engmalt.linear-1.7.mco`; do 
    model=`basename $model .mco`    
    echo $model
    #parsed_file=$prefix-$model.conll.parsed
    parsed_file=$test_file.parsedXXX
    eval_file=$parsed_file.eval
    java -Xmx$memory -jar ~/software/maltparser/maltparser-1.7.1.jar -c $model -i $test_file -m parse -o $parsed_file 2> /dev/null
    java -Xmx$memory -jar ~/software/MaltEval-20081119/lib/MaltEval.jar -g $test_file -s $parsed_file > $eval_file
    grep "Row mean" $eval_file
done