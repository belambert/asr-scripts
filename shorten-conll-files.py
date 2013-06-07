#!python

import sys
import gzip

ctl_filename = sys.argv[1]

max_length = 100

def shorten_conll_file(filename):
    assert (filename.endswith('.gz'))
    new_filename = "%s.%d.gz"%(filename[:-3], max_length)
    file = gzip.open(filename)
    new_file = gzip.open(new_filename, 'wb')
    count = 0
    for line in file:
        if line == "\n":
            count += 1
        if count == max_length:
            break
        new_file.write(line)

counter = 0

for line in open(ctl_filename):
    counter += 1
    if counter % 1000 == 0:
        print "Shortened %d files."%counter
    line = line[:-1]
    shorten_conll_file(line)
