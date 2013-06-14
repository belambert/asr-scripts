#!/bin/sh

if [ $# -eq 0 -o $# -gt 2 ]; then
    echo "Usage: $0 <mrg filename> [-basic(default), -collapsed, -CCprocessed]"
    exit -1
fi

mrg_file=$1

if [ $# -eq 2 ]; then
    type=$2
else
    type='-basic'
fi

java -Xmx2000m -cp ~/software/stanford-parser/stanford-parser.jar edu.stanford.nlp.trees.EnglishGrammaticalStructure -conllx $type -treeFile $mrg_file
