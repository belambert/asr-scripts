#!/usr/bin/python

import sys
import collections

if len(sys.argv) == 4:
    threshold = int(sys.argv[3])
else:
    threshold = 100

def count_words (file):
    counts = collections.defaultdict(int)
    with open(file) as f:
        for line in f:
            tokens = line.split()
            for token in tokens:
                counts[token]+= 1
    return counts


print "file1: %s"%sys.argv[1]
print "file2: %s"%sys.argv[2]
    
f1_counts = count_words(sys.argv[1])
f2_counts = count_words(sys.argv[2])


print '*'*40
print "Common words in file1 that aren't in file2 (and their file1 counts)"
for word, count in sorted(f1_counts.items(), key=lambda x: x[1], reverse=True):
    if count > threshold:
        #print "w: %30s c: %5d"%(word, count)
        #print f2_counts.get(word)
        if word not in f2_counts:
            print "%30s     %5d"%(word, count)

print '*'*40
print "Common words in file2 that aren't in file1 (and their file2 counts)"
for word, count in sorted(f2_counts.items(), key=lambda x: x[1], reverse=True):
    if count > threshold:
        #print "w: %30s c: %5d"%(word, count)
        #print f1_counts.get(word)
        if word not in f1_counts:
            print "%30s     %5d"%(word, count)
print '*'*40
