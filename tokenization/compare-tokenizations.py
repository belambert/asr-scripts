#!/usr/bin/python

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f:
    f1str = f.read()
with open(file2) as f:
    f2str = f.read()

f1tok = dict((x, None) for x in f1str.split())
f2tok = dict((x, None) for x in f2str.split())

print '*' * 40
for key in f1tok:
    if key not in f2tok:
        print "Token '%s' is not in %s"%(key, file2)
print '*' * 40
for key in f2tok:
    if key not in f1tok:
        print "Token '%s' is not in %s"%(key, file1)
print '*' * 40
