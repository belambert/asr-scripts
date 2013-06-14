#!/bin/sh

pos_script_location="/home/belamber/thesis/scripts/parser"

############ PARAMETERS ################################

# How many files per part?
#files_per_part=100
files_per_part=500
#files_per_part=5000

#nbest_folder='/home/belamber/workhorse4/decode/nbest/fisher-2013-03-19-decode-5_15-dev-lw_9.5-f2lm.DMP-f1-5_15-clean-dev.ctl-copy'
#nbest_folder='/home/belamber/workhorse4/decode/nbest/fisher-2013-03-19-decode-lw_9.5-f2lm.DMP-f1-0_40wer.ctl'

nbest_folder='/home/belamber/workhorse4/decode/nbest/fisher-2013-03-20-decode-lw_9.5-f2lm.DMP-f1-5_15-clean.ctl'

############ SCRIPT #####################################

# Get a list of files that we want to tag
ctl_file=ctl-$$
if [ -e $ctl_file ]; then
    echo "ctl file already exists... try again."
    exit -1;
fi

# Build a ctl file
find $nbest_folder -name *.nbest.gz | sort > $ctl_file

#ctl_file='/home/belamber/workhorse4/decode/nbest/fisher-2013-03-20-decode-lw_9.5-f2lm.DMP-f1-5_15-clean.ctl.ctl-10'
#ctl_file='test.ctl'

# and split that into lots of pieces
split -a 5 -d -l $files_per_part $ctl_file $ctl_file-part.

#to_do="53 57 60 67 68"

for file_list in `ls $ctl_file-part.*`; do
#for file_list in `ls $ctl_file-part.00047`; do
#for part in $to_do; do
#for part in {0..9}; do
    #file_list=$ctl_file-part.0000$part
    tmpscript=$file_list.sh
    echo "#$ -S /bin/sh" > $tmpscript
    echo "source ~/.bashrc" >> $tmpscript
    echo "cd $pos_script_location" >> $tmpscript
    echo "./nbest-syntax-processing.sh $file_list" >> $tmpscript
    #qsub -q default -d $pos_script_location -j oe -l walltime=3:00:00,mem=4g $tmpscript
    qsub -q hplong -d $pos_script_location -j oe -l walltime=24:00:00,mem=4g $tmpscript
    rm $tmpscript
done
