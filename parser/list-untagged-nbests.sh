#!/usr/bin/python

import sys
import os
from subprocess import call

folder=sys.argv[1]

files=os.listdir(folder)

#print(files[:10])

#result looks like this...
#['fe_03_00347.ch1_6952_7311.nbest.tagged.gz', 'fe_03_00289.ch2_27364_27419.nbest.tagged.gz', 'fe_03_00168.ch1_17238_17412.nbest.gz', 'fe_03_00297.ch2_52629_53200.nbest.tagged.err', 'fe_03_00210.ch1_4995_5381.nbest.gz', 'fe_03_00031.ch1_28545_28601.nbest.gz', 'fe_03_00311.ch2_23823_23928.nbest.gz', 'fe_03_00157.ch1_34494_34830.nbest.gz', 'fe_03_00484.ch2_1716_2492.nbest.tagged.err', 'fe_03_00109.ch2_36060_36119.nbest.tagged.err']


nbest_files=filter(lambda x: x.endswith(".nbest"), files)
nbestgz_files=filter(lambda x: x.endswith(".nbest.gz"), files)

tagged_files=filter(lambda x: x.endswith(".nbest.tagged"), files)
taggedgz_files=filter(lambda x: x.endswith(".nbest.tagged.gz"), files)

nbest_ids=map(lambda x: x[:-6], nbest_files)
nbestgz_ids=map(lambda x: x[:-9], nbestgz_files)
tagged_ids=map(lambda x: x[:-13], tagged_files)
taggedgz_ids=map(lambda x: x[:-16], taggedgz_files)

nbest_ids_table=dict(map(lambda x: (x, True), nbest_ids))
nbestgz_ids_table=dict(map(lambda x: (x, True), nbestgz_ids))
tagged_ids_table=dict(map(lambda x: (x, True), tagged_ids))
taggedgz_ids_table=dict(map(lambda x: (x, True), taggedgz_ids))

#print "Uncompressed N-bests:"
#for nbest_id in nbest_ids:
#    if nbest_id not in nbestgz_ids_table:
#        print nbest_id
#        call(["wc", "-l", "%s/%s.nbest"%(folder, nbest_id)])
#        call(["gzip", "%s/%s.nbest"%(folder, nbest_id)])

#print "Uncompressed N-bests:"
#for tagged_id in tagged_ids:
#    if tagged_id not in taggedgz_ids_table:
#        print tagged_id
#        call(["wc", "-l", "%s/%s.nbest.tagged"%(folder, tagged_id)])
#        #call(["gzip", "%s/%s.nbest"%(folder, nbest_id)])

#print "Uncompressed N-bests:"
#for nbest_id in nbestgz_ids:
#    if nbest_id not in taggedgz_ids_table:
#        #print nbest_id
#        print "%s%s.nbest.gz"%(folder, nbest_id)
#        #call(["wc", "-l", "%s/%s.nbest"%(folder, nbest_id)])
#        #call(["gzip", "%s/%s.nbest"%(folder, nbest_id)])


print "N best:      %d"%len(nbest_files)
print "N best(gz):  %d"%len(nbestgz_files)
print "Tagged:      %d"%len(tagged_files)
print "Tagged (gz): %d"%len(taggedgz_files)
