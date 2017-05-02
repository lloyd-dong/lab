#!/bin/bash

if [ ! $# == 1 ]; then
	echo need input file name
	exit
fi 
	
export WDR=/HOME/pp191/WORKSPACE/gene
export INPUT=$1
export OUTPUT=output
mkdir -p $OUTPUT

echo "...................................................................."
echo "processing fq.gz  =>  bam,  "
echo "...................................................................."

bwa mem -t 24 "$WDR"/ref/GRCh38_full_analysis_set_plus_decoy_hla.fa "$WDR"/rawData/2016006L-1-2"$INPUT"_R1.fq.gz "$WDR"/rawData/2016006L-1-2"$INPUT"_R2.fq.gz  2> "$OUTPUT"/"$INPUT"_out.log\
   | samtools view -1 - > "$OUTPUT"/"$INPUT"_out.aln.bam;

