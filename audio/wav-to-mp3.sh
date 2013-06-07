#!/bin/sh

i=0
print_interval=100

wav_files=`find ./wsj-wav -name *.wav`
#total_count=`wc -l $wav_files`


for wav_file in $wav_files; do

    mp3_file=`dirname $wav_file`/`basename $wav_file .wav`.mp3

    #echo $mp3_file
    
    if [ ! -f $mp3_file ]; then
        ../../software/bin/lame $wav_file $mp3_file &> /dev/null
	#../../software/bin/lame $wav_file $mp3_file
    fi
     
    i=$((i+1))
    modulo=$((i%$print_interval))

    if [[ $modulo == 0 ]]; then
	echo "Processed: $i"
    fi
done