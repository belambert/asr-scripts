#!python

import sys
import gzip

ctl_filename = sys.argv[1]

max_length = 100

def shorten_conll_file(filename):
    assert (filename.endswith('.gz'))
    new_filename = "%s.%d.gz"%(filename[:-3], max_length)
    print "Working on file: %s"%filename
    file = gzip.open(filename)
    new_file = gzip.open(new_filename, 'wb')
    counter = 0
    
    count = 0
    for line in file:
        #line = line[:-1]
        print count
        if line == "\n":
            count += 1
        if count == max_length:
            break
        new_file.write(line)


for line in open(ctl_filename):
    line = line[:-1]
    shorten_conll_file(line)