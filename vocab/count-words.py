#!/usr/bin/python

import sys
import collections

argc = len(sys.argv)

if argc != 3 and argc != 4:
    print "Usage: %s text_file <print_counts: y/n> [num of words]"%sys.argv[0]
    exit(-1)

count_word_classes = False

print_counts = True if sys.argv[2] == "y" else False
if argc == 4:
    n=int(sys.argv[3])
else:
    n = 0

f = open(sys.argv[1])
lines = f.readlines()
counts = collections.defaultdict(int)

total_count = 0

characters_to_count = ["'", '-','+', '.', '?', ',', '!', '"']

dis = ('um',
       'uh',
       'mm',
       'ah',
       'er',
       'eh',
       'mhm',
       'hm',
       'ha',
       'huh',
       'uhuh',
       'uh-uh',
       'uh-huh',
       'huh-',
       'huh-huh',
       'uh-oh',
       'um-hum',
       'uh-hum',
       'ahah',
       'heh',
       'hmm',
       'aha',
       'aw',
       'mh-',
       # Do these count?
       #'ooh',
       #'oh',
       )

for line in lines:
    tokens = line.split()
    for token in tokens:
        counts[token]+= 1
        total_count += 1
        if count_word_classes:
            if token in dis:
                counts['DISFLUENCY'] += 1
            if token.startswith('-') or token.endswith('-'):
                counts['PARTIAL_WORD'] += 1
            if token.endswith('s\''):
                counts['ES_APOSTROPHE'] += 1
            for char in characters_to_count:
                if char in token:
                    counts['HAS_%s'%char] += 1

counts = counts.items()
counts = sorted(counts, key=lambda x: x[1], reverse=True)

if n != 0:
    counts = counts[0:n]

counter = 0
for word, count in counts:
    counter += 1
    if print_counts:
        print "%10d   %30s  %10d  %5f"%(counter,word,count, count * 100.0 / total_count)
    else:
        print "%s"%word

