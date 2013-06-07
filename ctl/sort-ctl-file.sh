#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print """Sorts by filename, then by begin time"""
    print "Usage: %s <ctl file>"%sys.argv[0]
    exit(-1)

remove_channel_number = True

ctl_file = sys.argv[1]
ctl_entries = []

for line in open(ctl_file):
    line = line[:-1]
    tokens = line.split()
    if remove_channel_number:
        # Remove the channel number from the filename
        tokens[0] = tokens[0][:-1]
    # Convert the begin and end times to ints so they sort correctly
    tokens[1] = int(tokens[1])
    tokens[2] = int(tokens[2])
    # Add the raw line to the tokens, because that's what we want to print
    tokens.append(line)
    # Save the whole thing in a list
    ctl_entries.append(tokens)

# First sort by the begin time
ctl_entries.sort(key=lambda x: x[1])
# Then sort by the filename
ctl_entries.sort(key=lambda x: x[0])

# Print only the last field (the raw line) of the sorted list
for entry in ctl_entries:
    print entry[-1]


    
