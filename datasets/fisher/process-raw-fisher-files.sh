#!/usr/bin/python


## fe_03_00001.sph
## Transcribed at the LDC
#3.76 5.54 A: and i generally prefer 
#
#5.82 6.48 A: eating at home 
#
#7.92 9.52 B: hi my name is andy 
#
#10.05 10.88 A: hello andy 

import sys
import subprocess
import os


#ctl_file = True
ctl_file = False

folder=sys.argv[1]
command = ['ls', folder]
result = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
filenames = result.split()
filenames = map(lambda x: folder + "/" + x, filenames)

for filename in filenames:
    file_base_name = os.path.basename(filename).lower()
    file_base_name = file_base_name[:-4]
    lines = open(filename).readlines()
    for line in lines:
        line = line[:-1]
        if len(line) > 0 and line[0] != '#':
            tokens = line.split()
            start=float(tokens[0])*100
            end=float(tokens[1])*100
            speaker=tokens[2]
            line = tokens[3:]
            line = ' '.join(line)
            line = line.upper()
            if speaker == "A:":
                file = file_base_name + ".ch1"
            elif speaker == "B:":
                file = file_base_name + ".ch2"
            else:
                error("Invalid speaker ID: %s"%speaker)
            #print line
            #CTL file looks like this:
            #a960521 3810 4037 a960521_3810_4037_Ted_Koppel_Male_Native_Planned_High_Music_Faint
            #a960521 4035 4403 a960521_4035_4403_Ted_Koppel_Male_Native_Planned_High_Music_Faint
            id = "%s_%d_%d"%(file, start, end)
            if ctl_file:
                print "%s %d %d %s"%(file, start, end, id)
            else:
                print "%s (%s)"%(line, id)
            
