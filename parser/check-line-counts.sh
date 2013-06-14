#$ -S /bin/sh
source ~/.bashrc

#cd /home/belamber/Workspace/cxgp/

#folder_name="/usr0/belamber/Sphinx/decode/nbest/wsj-2-20-12-nbest"
folder_name=$1

for file in $( ls $folder_name/*.2tag); do
    tagged_file=`dirname $file`/`basename $file .2tag`.tagged
    orig_line_count=`wc -l $file | awk '{print $1}'`
    tagged_line_count=`wc -l $tagged_file | awk '{print $1}'`
    if [[ $orig_line_count -ne $tagged_line_count ]]; then
	echo "Line counts don't match!! $orig_line_count  $tagged_line_count ($file)"
    fi
done
        
