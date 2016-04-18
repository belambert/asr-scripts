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
counts = collections.defaultdict(int)

vocab_list = open(vocab_file).readlines()
vocab_list = map(lambda x: x[:-1], vocab_list)
vocab = {}
for word in vocab_list:
    vocab[word] = True

oov_count = 0
token_count = 0
for line in lines:
    tokens = line.split()
    for token in tokens:
        token_count += 1
        if not vocab.get(token):
            counts[token] += 1
            oov_count += 1

counts = counts.items()
counts = sorted(counts, key=lambda x: x[1], reverse=False)

counter = 0
for word, count in counts:
    if count > 0:
        counter += 1
        print "%10d   %s\t\t%d"%(counter,word,count)

print "Total token count: %d"%token_count
print "OOV count:         %d"%oov_count
print "OOV rate:          %f"%(1.0 * oov_count/token_count)
