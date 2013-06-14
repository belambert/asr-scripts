#!/bin/sh

if [ $# -eq 0 -o $# -gt 2 ]; then
    echo "Usage: $0 <conll filename> [-basic, -collapsed, -CCprocessed(default)]"
    exit -1
fi

conll_file=$1

if [ $# -eq 2 ]; then
    type=$2
fi

java -Xmx4000m -cp ~/software/stanford-parser/stanford-parser.jar edu.stanford.nlp.trees.EnglishGrammaticalStructure -conllx $type -conllxFile $conll_file
