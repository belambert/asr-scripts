#!/usr/bin/python

import sys, re

file = sys.argv[1]

in_header= True

this_line = ""

with open(file) as f:
    string = f.read()


#string = re.sub('x.*===\s', '', string, count=1)
#string = re.sub('x.*\=\=\=\s', '', string, count=1, flags=re.DOTALL)
#string = re.sub('x.*\=\=\=\s', '', string, re.DOTALL)

# First remove the header
header_re = re.compile('\*x.*\=\=\=\s', re.DOTALL)
string = re.sub(header_re, '', string)
# Then remove the speaker identifier, and replace it with a forward slash which delimits each 'turn'
string = re.sub('[AB]\.\d+: *', '/', string)
string = re.sub('[AB]: *', '/', string)
# Replace all the newline characters with a space
string = re.sub('\n', ' ', string)


# Remove the tokens that designate various types of disfluencies
string = re.sub('{F', '', string)
string = re.sub('{E', '', string)
string = re.sub('{D', '', string)
string = re.sub('{C', '', string)
string = re.sub('{A', '', string)
# Replace the 'unfinished' -/ with a regular forward slash
string = re.sub('-/', '/', string)
# Remove the double dash: --
string = re.sub('--', ' ', string)
# Remove various punctuation marks
#string = re.sub('[{},\+\?\[\]\.@\(\)#]\"', ' ', string)
string = re.sub('[{},\+\?\[\]\.@\(\)#]', ' ', string)
string = string.replace('"', ' ')
# Remove comments which are between <>
# Non-greedily remove everything between two brackets...
string = re.sub('<.*?>+', ' ', string)

# And condense all the sequences of spaces to single spaces
string = re.sub(' +', ' ', string)

string = string.lower()

lines = string.split('/')

# Remove any lines that are empty or are all spaces
lines = filter(lambda x: not re.match(' *$', x), lines)

for line in lines:
    line = line.strip()
    print line


