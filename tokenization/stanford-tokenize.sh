#!/bin/bash

file=$1

java -Xmx1000m -cp ~/software/stanford-parser/stanford-parser.jar edu.stanford.nlp.process.PTBTokenizer -preserveLines -options "americanize=false" $file


