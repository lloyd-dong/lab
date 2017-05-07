/bin/bash -e util.sh

if [ ! $# == 1 ]; then
        echo need input file name
        exit
fi

INPUT=$1

echo "...................................................................."
echo "（4）Align samples to reference genome with bwa mem ${INPUT}"
echo "...................................................................."

bwa mem -M -t 24 -R '@RG\tID:001\tSM:dm01\tLB:seq01' ${WDR}${REF_FA} \
   "$WDR"/rawData/2016006L-1-2"$INPUT"_R1.fq.gz "$WDR"/rawData/2016006L-1-2"$INPUT"_R2.fq.gz \
   2> "$OUTPUT"/"$INPUT"_out.log \
   | samtools view -1 -@ 23 - > "$OUTPUT"/"$INPUT"_out.aln.bam
# -@ 23, additional 23 threads

echo "...................................................................."
echo "(5) Fix Mate Information ${INPUT}"
echo "...................................................................."

samtools fixmate -O bam --output-fmt-option nthreads=24 ./output/$INPUT_out.aln.bam  ./output/$INPUT_out.fixmate.bam

echo "...................................................................."
echo "6 Sort BAM ${INPUT}"
echo "...................................................................."

#samtools sort -T /tmp/Sample_name_lib_num.sorted -o Sample_name_lib_num.sorted.bam Sample_name_lib_num.fixmate.bam
samtools sort -@ 24 -O bam -T tmp -o output/"$INPUT"_sorted.bam output/"$INPUT"_out.fixmate.bam
