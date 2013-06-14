#!/bin/bash

memory='14000m'
alg="nivreeager"
#alg="2planar"

if [ $# -lt 1 -o $# -gt 2 ]; then
    echo "Usage: $0 train_file [test_file]"
    exit 1
fi

train_file=$1
if [ $# -eq 2 ]; then
    test_file=$2
fi

train_model_p=true
#train_model_p=false

#model=swb-basic-linear-$alg
model=swb-basic-linear-$alg-all
echo "Training model: $model"

if $train_model_p ; then
    # Train the model
    java -Xmx$memory -jar ~/software/maltparser/maltparser-1.7.1.jar -c $model -i $train_file -m learn -l liblinear -a $alg -grl "root" -nr false
fi

# Run the resulting parser on the training data
parsed_file=$train_file.parsed
eval_file=$parsed_file.eval
java -Xmx$memory -jar ~/software/maltparser/maltparser-1.7.1.jar -c $model -i $train_file -m parse -o $parsed_file 2>> error.log
java -Xmx$memory -jar ~/software/MaltEval-20081119/lib/MaltEval.jar -g $train_file -s $parsed_file > $eval_file
echo "Performance on training data:"
grep "Row mean" $eval_file

 # Run the resulting parser on the test data
if [[ -n "$test_file" ]] ; then
    parsed_file=$model.test.conll.parsed
    eval_file=$parsed_file.eval
    java -Xmx$memory -jar ~/software/maltparser/maltparser-1.7.1.jar -c $model -i $test_file -m parse -o $parsed_file 2>> error.log
    java -Xmx$memory -jar ~/software/MaltEval-20081119/lib/MaltEval.jar -g $test_file -s $parsed_file > $eval_file
    echo "Performance on test data:"
    grep "Row mean" $eval_file
fi
 