#!/bin/sh

if [ $# -gt 2 ]; then
    echo "Usage: $0 <file/gold file> [<more files>+]"
    #echo "Usage: $0 <gold standard> <automatically parsed> "
    exit -1
fi

gold=$1
eval=$2

echo $gold
echo $eval
echo $#

if [ $# -eq 2 ]; then
    java -Xmx5000m -jar ~/software/MaltEval-20081119/lib/MaltEval.jar -g $gold -s $eval -v 1
else
    java -Xmx5000m -jar ~/software/MaltEval-20081119/lib/MaltEval.jar -s $gold -v 1
fi
