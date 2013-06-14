#!/bin/sh

if [ $# -ne 2 ]; then
    echo "Usage: $0 <gold standard> <automatically parsed> "
    exit -1
fi

gold=$1
eval=$2

java -Xmx2000mb -jar ~/software/MaltEval-20081119/lib/MaltEval.jar -g $gold -s $eval
