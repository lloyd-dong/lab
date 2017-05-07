#!/bin/bash

if [ ! $# == 1 ]; then
	echo need input file name
	exit
fi 
	
export WDR=/HOME/pp191/WORKSPACE/gene
export INPUT=$1


echo "...................................................................."
echo "genate vcf"
echo "...................................................................."

java -jar /WORK/app/GATK/3.3.0/GenomeAnalysisTK.jar -T UnifiedGenotyper \
 -R ref/GRCh38_full_analysis_set_plus_decoy_hla.fa \
 -I output/"$INPUT"_out.aln.bam -o output/"$INPUT"_out.vcf -glm BOTH