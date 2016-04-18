#!python

import gzip
import sys

max_length = 100
ctl_filename = sys.argv[1]

def shorten_nbest(filename):
    assert (filename.endswith('.gz'))
    new_filename = "%s.%d.gz"%(filename[:-3], max_length)
    file = gzip.open(filename)
    new_file = gzip.open(new_filename, 'wb')
    counter = 0
    for line in file:
        new_file.write(line)
        if not (line.startswith('#') or line.startswith('End')):
            counter = counter + 1
            if counter == max_length:
                break
    file.close()
    new_file.close()

counter = 0

for line in open(ctl_filename):
    counter += 1
    if counter % 1000 == 0:
        print "Shortened %d files."%counter
    line = line[:-1]
    shorten_nbest(line)
