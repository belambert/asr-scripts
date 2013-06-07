#!/bin/sh

ngram-count -order 2 -lm swb-2gram.lm -text swb1-train-1k-train.txt 
ngram-count -order 3 -lm swb-3gram.lm -text swb1-train-1k-train.txt 
