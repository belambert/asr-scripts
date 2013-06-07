#!/bin/sh

ngram -lm ../../lm/gigaword-1m-wsj-vocab.lm -unk -gen 1000000 > ../gigaword/gigaword-random-1m.txt

