#!/usr/bin/python

import sys, math


if len(sys.argv) != 2:
    print "Usage: %s <CONLL file>"%os.path.basename(sys.argv[0])
    exit(1)

file = sys.argv[1]

filter_word_list = ['mumblex', 'intj', 'intj-2', 'intj-unf', 'intj-sez', 'typo']
filter_word_table = dict([(x, None) for x in filter_word_list])

def not_corrupt_sentence (s):
    for word in s:
        word = word[1].lower()
        if word in filter_word_table:
            return False
    return True

sentence = []
sentences = []

with open(file) as f:
    for line in f:
        if line == "\n":
            sentences.append(sentence)
            sentence = []
        else:
            sentence.append(line.split())

sentences = filter(not_corrupt_sentence, sentences)

for sentence in sentences:
    for word in sentence:
        print '\t'.join(word)
    print ""

