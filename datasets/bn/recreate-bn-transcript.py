#!/usr/bin/python

import sys
import re
import string

sphinx_file=sys.argv[1]
ldc_file=sys.argv[2]

f = open(ldc_file)
lines = f.readlines()

filename=None
start_time=None
end_time=None
transcript=None

transcript_lines = []

ldc_lines = []
ldc_table = {}
sphinx_lines = []

def read_attribute (str):
    tokens = str.split("=")
    return tokens[1]    

def get_token_num(str, n):
    tokens = str.split()
    return tokens[n]

def get_time_attribute(str):
    tokens = str.split()
    time_tokens = filter(lambda x: x.startswith("Time=") or x.startswith("startTime=") or x.startswith("sec="), tokens)
    if not len(time_tokens) == 1:
        print time_tokens
    assert len(time_tokens) == 1
    time_tokens = time_tokens[0]
    time_tokens = time_tokens.split("=")
    assert time_tokens[0] == "Time" or time_tokens[0] == "startTime" or time_tokens[0] == "sec"
    time = time_tokens[1]
    return time

def print_transcript():
    global transcript_lines, ldc_lines
    if len(transcript_lines) > 0:
        #transcript_lines = reverse(transcript_lines)
        transcript = ' '.join(transcript_lines)
        if start_time:
            #print "%10s  %s"%(start_time, transcript)
            time = start_time[:-1]
            time = string.replace(time, ".", "")
            time = int(time)
            ldc_lines.append([filename, time, transcript])
            if not ldc_table.get(filename):
                ldc_table[filename] = []
            ldc_table[filename].append([filename, time, transcript])
        transcript_lines = []

for line in lines:
    if "<Episode" in line or "<episode" in line:
        print_transcript()
        filename = read_attribute(get_token_num(line, 1))
        #filename = filename[:-4]
        filename = filename.replace(".rtg.sph", "")
        filename = filename.replace(".sph", "")
        filename = filename.replace("\"", "")
        
    if "<Segment" in line or "<Sync" in line:
        print_transcript()
        #end_time = start_time
        start_time = read_attribute(get_token_num(line, 1))
        #start_time = get_time_attribute(line)
    elif "Time=" in line:
        print_transcript()
        #end_time = start_time
        start_time = get_time_attribute(line)
    else:
        if not line[0] == "<":
            transcript = line[:-1]
            #print "%10s  %10s  %s"%(start_time, end_time, transcript)
            #print "%10s  %s"%(start_time, transcript)
            transcript_lines.append(transcript)
        
            
f = open(sphinx_file)
lines = f.readlines()

for line in lines:
    m = re.match("(.*)\((.+)\)", line)
    trans = m.group(1)
    id = m.group(2)
    #print id
    id_tokens = id.split("_")
    id_tokens[1] = int(id_tokens[1])
    id_tokens[2] = int(id_tokens[2])

    trans = trans.replace("<s> ", "")
    trans = trans.replace("<sil> ", "")
    trans = trans.replace(" </s>", "")
        
    id_tokens.append(trans)
    sphinx_lines.append(id_tokens)
    #return {"A": m.group(1), "B": m.group(2), "TS": m.group(3)}
    #sphinx_lines=lines

sphinx_lines.sort(key=lambda x: x[1])
sphinx_lines.sort(key=lambda x: x[0])

ldc_lines.sort(key=lambda x: x[1])
ldc_lines.sort(key=lambda x: x[0])

for line in sphinx_lines[0:10]:
    print line

for line in ldc_lines[0:10]:
    print line

print "Sphinx line count: %d"%len(sphinx_lines)
print "LDC line count:    %d"%len(ldc_lines)


def find_ldc_transcript_prev(filename, start_time):
    for line in ldc_lines:
        if filename == line[0] and abs(start_time - line[1]) < 5:
            return line
    return None


total_count = 0

def find_ldc_transcript(filename, start_time):
    global total_count
    #for line in ldc_table[filename]:
    lines = ldc_table.get(filename)
    if not lines: print "Don't have transcript table for filename: %s"%filename
    if lines:
        total_count += 1
        for line in ldc_table.get(filename):
            if filename == line[0] and abs(start_time - line[1]) < 100:
                return line
    return None


not_found_count = 0

for sphinx_line in sphinx_lines:
    filename = sphinx_line[0]
    start_time = sphinx_line[1]
    ldc_line = find_ldc_transcript(filename, start_time)
    if not ldc_line:
        not_found_count += 1

for i in range(len(sphinx_lines)):
    print "%3d (ldc) %10s %10s %s"%(i, ldc_lines[i][0], ldc_lines[i][1], ldc_lines[i][2].upper())
    print "%3d (sph) %10s %10s %s"%(i, sphinx_lines[i][0], sphinx_lines[i][1], sphinx_lines[i][-1].upper())

for i in range(len(sphinx_lines) - 10, len(sphinx_lines)):
    print "%3d (sph) %10s %10s %s"%(i, sphinx_lines[i][0], sphinx_lines[i][1], sphinx_lines[i][-1].upper())

for i in range(len(ldc_lines) - 10, len(ldc_lines)):
    print "%3d (ldc) %10s %10s %s"%(i, ldc_lines[i][0], ldc_lines[i][1], ldc_lines[i][2].upper())

print "Transcripts not found: %s"%not_found_count


