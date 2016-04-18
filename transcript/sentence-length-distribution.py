#!/opt/local/bin/python 

import argparse
parser = argparse.ArgumentParser(description='Compute the distribution of sentence lengths')
parser.add_argument("filename", help="Name of the file with sentences - one per line.")
args = parser.parse_args()


filename = args.filename

maxlength = 50

counters = [0] * (maxlength + 2)
total_count = 0

for line in open(filename):
    total_count += 1
    tokens = line.split()
    token_count = len(tokens)
    if token_count > maxlength:
         token_count = maxlength + 1
    counters[token_count] += 1


print "Total number of lines: %d"%total_count


cumulative = 0
 
for i in range(maxlength+2):

    cumulative += counters[i]

    if i == maxlength+1:
         print "%10d+ %10d %10d"%(i, counters[i], cumulative)
    else:
         print "%10d  %10d %10d"%(i, counters[i], cumulative)
