#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%sys.argv[0]
    exit(-1)

file = sys.argv[1]
entries = []

#begin_end_delimiter = '_'
begin_end_delimiter = '-'
filename_begin_delimiter = '_'
remove_channel_number = True

def split_id(id):
    """Split a sphinx ID into three parts:
       filename, begin time, and end time."""
    pivot1=id.rfind(begin_end_delimiter)
    # End is the end time
    end = id[pivot1+1:]
    # This is everything that comes before the end time
    rest = id[:pivot1]
    pivot2=rest.rfind(filename_begin_delimiter)
    # This is the begin time
    begin = rest[pivot2+1:]
    # This is the filename
    filename = rest[:pivot2]
    # Remove the channel number from the filename
    if remove_channel_number:
        filename = filename[:-1]        
    # Convert the begin and end times to ints
    begin=int(begin)
    end=int(end)
    return (filename, begin, end)

for line in open(file):
    line = line[:-1]
    # Extract the ID... the part between the parens
    pivot= line.rfind("(")
    id= line[pivot+1:-1]
    # Extract the pieces and put everything in a list
    filename, begin, end = split_id(id)
    entries.append([filename, begin, end, line])

# First sort by the begin time
entries.sort(key=lambda x: x[1])
# Then sort by the filename
entries.sort(key=lambda x: x[0])

# Finally print the original lines in the newly sorted order
for entry in entries:
    print entry[-1]


    
