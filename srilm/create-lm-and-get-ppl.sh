#!/bin/sh

ngram_count_flags="-vocab hua-yoo.vocab -unk -gt3min 2"
ngram_flags="-vocab hua-yoo.vocab -unk"

#ngram_flags="-unk"
#ngram_count_flags="-unk"

train_file=../../kb-asr/data/transcripts/swb/sentence-bounded/swb1-train.txt
test_file=../../kb-asr/data/transcripts/swb/sentence-bounded/swb1-test.txt

#train_file=../../kb-asr/data/transcripts/swb/sentence-bounded/swb1-train-1k.txt
#test_file=../../kb-asr/data/transcripts/swb/sentence-bounded/swb1-test-1k.txt

lm1gram=./1gram.lm
lm2gram=./2gram.lm
lm3gram=./3gram.lm
lm4gram=./4gram.lm

#lm1gram=./1gram-1k.lm
#lm2gram=./2gram-1k.lm
#lm3gram=./3gram-1k.lm
#lm4gram=./4gram-1k.lm

echo "1-GRAM:"
rm -f $lm1gram
ngram-count -order 1 -lm $lm1gram -text $train_file $ngram_count_flags
ngram -lm $lm1gram -ppl $train_file $ngram_flags
ngram -lm $lm1gram -ppl $test_file $ngram_flags

echo "2-GRAM:"
rm -f $lm2gram
ngram-count -order 2 -lm $lm2gram -text $train_file $ngram_count_flags
ngram -lm $lm2gram -ppl $train_file $ngram_flags
ngram -lm $lm2gram -ppl $test_file $ngram_flags

echo "3-GRAM:"
rm -f $lm3gram
ngram-count -order 3 -lm $lm3gram -text $train_file $ngram_count_flags
ngram -lm $lm3gram -ppl $train_file $ngram_flags
ngram -lm $lm3gram -ppl $test_file $ngram_flags

echo "4-GRAM:"
rm -f $lm4gram
ngram-count -order 4 -lm $lm4gram -text $train_file $ngram_count_flags
ngram -order 4 -lm $lm4gram -ppl $train_file $ngram_flags
ngram -order 4 -lm $lm4gram -ppl $test_file $ngram_flags

