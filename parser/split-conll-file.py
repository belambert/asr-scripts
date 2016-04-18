#!/usr/bin/python

import sys
import math

if len(sys.argv) != 2:
    print "Usage: %s <CONLL file>"%os.path.basename(sys.argv[0])
    exit(1)

file = sys.argv[1]

sentence = []
sentences = []

with open(file) as f:
    for line in f:
        if line == "\n":
            sentences.append(sentence)
            sentence = []
        else:
            sentence.append(line)
total_count = len(sentences)
print "Sentences in CONLL file: %d"%total_count

split_point = int(math.ceil(total_count / 2.0))

print split_point

set1 = sentences[0:split_point]
set2 = sentences[split_point:]

print len(set1)
print len(set2)

with open(file+".set1", 'w') as f:
    for sentence in set1:
        for word in sentence:
            f.write(word)
        f.write('\n')

with open(file+".set2", 'w') as f:
    for sentence in set2:
        for word in sentence:
            f.write(word)
        f.write('\n')
