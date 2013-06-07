

print_interval=500

files=`find . -iname "*.WV[12]"`
total_count=`echo $files | wc -w`
count=1
for wv_file in $files; do

    sph_file=$wv_file.sph 
    sph_file2=$wv_file.sph2
    wav_file=`dirname $wv_file`/`basename $wv_file .sph`.wav

    /archive/bigbird/usr3/rsingh/bin/shorten -x $wv_file $sph_file
    sed "s/pcm,embedded-shorten-v1.1/pcm                      /" < $sph_file  > $sph_file2
    mv $sph_file2 $sph_file
    sed "s/pcm,embedded-shorten-v1.09/pcm                       /" < $sph_file  > $sph_file2
    mv $sph_file2 $sph_file
    sox -t .sph $sph_file -t .wav $wav_file
    
    count=$((count+1))
    modulo=$((count%$print_interval))

    if [[ $modulo == 0 ]]; then
        echo "$count of $total_count"
    fi

done
