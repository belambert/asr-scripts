#!/usr/bin/python

import sys
import collections

argc = len(sys.argv)

if argc != 3:
    print "Usage: %s text_file vocab_file"%sys.argv[0]
    exit(-1)

text_file = sys.argv[1]
vocab_file = sys.argv[2]


f = open(text_file)
lines = f.readlines()

#counts = collections.defaultdict(int)
counts = {}

vocab = open(vocab_file).readlines()
vocab = map(lambda x: x[:-1], vocab)
for word in vocab:
    counts[word] = 0


total_count = 0
for line in lines:
    tokens = line.split()
    for token in tokens:
        if counts.get(token):
            counts[token]+= 1
            total_count += 1

counts = counts.items()
counts = sorted(counts, key=lambda x: x[1], reverse=True)

counter = 0
for word, count in counts:
    if count > 0:
        counter += 1
        print "%10d   %s\t\t%d"%(counter,word,count)
