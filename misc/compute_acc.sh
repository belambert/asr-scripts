#!/bin/bash

if [ $# != 2 ]; then
   echo "usage: $0 <hyp> <corr>"
   exit 1
fi

hyp=$1
corr=$2

#MACHINE=`~/bin/machine_type.csh`
#align=/homes/bhiksha/bin/linux/align
#align=/usr3/rsingh/bin/linux/align
#align=/net/bigbird/usr3/rsingh/bin/linux/align
#align=/net/katsura/work/belamber/hg/blambert-util/scripts/align
align=/usr0/home/belamber/thesis/scripts/align
align=~/thesis/scripts/align

#$align -def $corr -hyp $hyp >&! $hyp.align
# Once to print to the screen
#$align -def $corr -hyp $hyp
# Second time to print to a file.
$align -def $corr -hyp $hyp > $hyp.align
#$align -def $corr -hyp $hyp

grep -i accuracy $hyp.align

exit 0
