/bin/bash -e util.sh

if [ ! $# == 1 ]; then
        echo need input file name
        exit
fi

INPUT=$1


echo "...................................................................."
echo "(14) index BAM using samtools ${INPUT}"
echo "...................................................................."

samtools index -@ 24 output/"$INPUT"_out.improvement.bam
