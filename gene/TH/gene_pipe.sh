#!/bin/bash


module load bwa/0.7.12 
module load samtools/1.2
module load GATK/3.7 
module load picard/1.129
module load bcftools/1.3.1

yhbatch -N 1 -c 24 4,5,6

########################################
############### Mapping ################
########################################

################
#(1) build index
################
# bwa index -a bwtsw -p <reference> <reference.fa>

# => *.pac, *.ann
################
#(2) Sort reference
################
# samtools faidx reference.fasta
# => *.fai
################
#(3) Create sequence dictionary
################
# java -jar CreateSequenceDictionary.jar REFERENCE=reference.fa OUTPUT=reference.dict
# => *.dict


if [ ! $# == 1 ]; then
        echo need input file name
        exit
fi

export WDR=/HOME/pp191/WORKSPACE/gene
export INPUT=$1
export OUTPUT=output
export GATK_JAR=/WORK/app/GATK/3.7/GenomeAnalysisTK.jar
export PICARD_JAR=/WORK/app/picard/1.129/picard.jar
export REF_FA=ref/GRCh38_full_analysis_set_plus_decoy_hla.fa
mkdir -p $OUTPUT

################
#(4) Align samples to reference genome with bwa mem
################

echo "...................................................................."
echo "（4）Align samples to reference genome with bwa mem ${INPUT}"
echo "...................................................................."

bwa mem -M -t 24 -R '@RG\tID:001\tSM:dm01\tLB:seq01' ${WDR}${REF_FA} \
   "$WDR"/rawData/2016006L-1-2"$INPUT"_R1.fq.gz "$WDR"/rawData/2016006L-1-2"$INPUT"_R2.fq.gz \
   2> "$OUTPUT"/"$INPUT"_out.log \
   | samtools view -1 -@ 23 - > "$OUTPUT"/"$INPUT"_out.aln.bam
# -@ 23, additional 23 threads


################
#(5) Fix Mate Information
################
echo "...................................................................."
echo "(5) Fix Mate Information ${INPUT}"
echo "...................................................................."

samtools fixmate -O bam --output-fmt-option nthreads=24 ./output/$INPUT_out.aln.bam  ./output/$INPUT_out.fixmate.bam


################
#(6) Sort BAM file
################
echo "...................................................................."
echo "6 Sort BAM ${INPUT}"
echo "...................................................................."

#samtools sort -T /tmp/Sample_name_lib_num.sorted -o Sample_name_lib_num.sorted.bam Sample_name_lib_num.fixmate.bam
samtools sort -@ 24 -O bam -T tmp -o output/"$INPUT"_sorted.bam output/"$INPUT"_out.fixmate.bam

########################################
############# Improvement ##############
########################################

###############
#(7)Splits reads with Ns in CIGAR
###############
# java –jar GenomeAnalysisTK.jar \
# –T SplitNCigarReads \
# –R reference.fa \
# –I Sample_name_lib_num.sorted.bam \
# –o Sample_name_lib_num.sorted.SplitNCigar.bam \
# –U ALLOW_N_CIGAR_READS \
# –rf ReassignOneMappingQuality \
# –RMQF 255 \
# –RMQT 60

# => split.bam split.bai
# no nt nor -nct 24

echo "...................................................................."
echo "7 Splits reads with Ns in CIGAR ${INPUT}"
echo "...................................................................."

java -jar ${GATK_JAR} -T SplitNCigarReads \
 -R ${REF_FA} \
 -I output/"$INPUT"_sorted.bam -o output/"$INPUT"_out.split.bam \
 -U ALLOW_N_CIGAR_READS \
 -rf  ReassignOneMappingQuality \
 -RMQF 255 \
 -RMQT 60


################
#(8)Identify target regions for realignment
################
echo "...................................................................."
echo "(8)Identify target regions for realignment ${INPUT}"
echo "...................................................................."
# java -Xmx2g -jar GenomeAnalysisTK.jar -T RealignerTargetCreator \
# -R reference.fa \
# -I Sample_name_lib_num.sorted.SplitNCigar.bam  \
# -ip 50 \
# -o Sample_name_lib_num.sorted.SplitNCigar.intervals

java  -jar ${GATK_JAR}  -T RealignerTargetCreator \
 -R ${REF_FA} \
 -I output/"$INPUT"_out.split.bam -o output/"$INPUT"_out.split.intervals \
 -ip 50 \
 -nt 24
# --interval_padding , -ip Amount of padding (in bp) to add to each interval

################
#(9) Perform realignment
################
echo "...................................................................."
echo "(9) Perform realignment ${INPUT}"
echo "...................................................................."

# java -Xmx4g -jar GenomeAnalysisTK.jar -T IndelRealigner \
# -R reference.fa \
# -I Sample_name_lib_num.sorted.SplitNCigar.bam  \
# -targetIntervals Sample_name_lib_num.sorted.SplitNCigar.intervals \
# -output Sample_name_lib_num.realigned.bam

java  -jar ${GATK_JAR} -T IndelRealigner \
-R ${REF_FA} \
-I output/"$INPUT"_out.split.bam  \
-targetIntervals output/"$INPUT"_out.split.intervals \
-output output/"$INPUT"_out.realigned.bam

? -nt -nct?
################
#(10) fixes mate information that may be changed during the realignment process
################
echo "...................................................................."
echo "(10) fixes mate information that may be changed during the realignment process ${INPUT}"
echo "...................................................................."
# java -Djava.io.tmpdir=/tmp/ \
# -jar picard.jar FixMateInformation \
# INPUT=Sample_name_lib_num.realigned.bam \
# OUTPUT=Sample_name_lib_num.realigned.fixed.bam \
# SO=coordinate \
# VALIDATION_STRINGENCY=LENIENT \
# CREATE_INDEX=true

java -Djava.io.tmpdir=/tmp/ \
-jar ${PICARD_JAR} FixMateInformation \
INPUT=output/"$INPUT"_out.realigned.bam \
OUTPUT=output/"$INPUT"_out.realigned.fixed.bam \
SO=coordinate \
VALIDATION_STRINGENCY=LENIENT \
CREATE_INDEX=true

? parallle ?
################
#(11) Build the recalibration model
################
echo "...................................................................."
echo "(11) Build the recalibration model ${INPUT}"
echo "...................................................................."

# java -Xmx4g -jar GenomeAnalysisTK.jar -T BaseRecalibrator \
# -R reference.fa \
# -I Sample_name_lib_num.realigned.fixed.bam \
# -ip 50 \
# -o Sample_name_lib_num_recalibration.table

java -jar ${GATK_JAR} -T BaseRecalibrator \
-R ${REF_FA} \
-I output/"$INPUT"_out.realigned.fixed.bam \
-ip 50 \
-o output/"$INPUT"_out.recalibration.table
? nt nct?
################
#(12) Apply the recalibration model
################
echo "...................................................................."
echo "(12) Apply the recalibration model ${INPUT}"
echo "...................................................................."

# java -Xmx4g -jar GenomeAnalysisTK.jar -T PrintReads \
# -R reference.fa \
# -I Sample_name_lib_num.realigned.bam \
# -BQSR Sample_name_lib_num_recalibration.table \
# -o Sample_name_lib_num.realigned.recal.bam
java -jar ${GATK_JAR} -T PrintReads \
-R ${REF_FA} \
-I output/"$INPUT"_out.realigned.bam \
-BQSR output/"$INPUT"_out.recalibration.table \
-o output/"$INPUT"_out.realigned.recal.bam

?nt nct ?
################
#(13) Mark Duplicates
################
echo "...................................................................."
echo "(13) Mark Duplicates ${INPUT}"
echo "...................................................................."

# java -jar $PICARD MarkDuplicates \
# I=Sample_name_lib_num.realigned.recal.bam \
# O=Sample_name_lib_num.improvement.bam \
# M=Sample_name_lib_num_dedup_metrics.txt \
# CREATE_INDEX=true

java -jar ${PICARD_JAR} MarkDuplicates \
I=output/"$INPUT"_out.realigned.recal.bam \
O=output/"$INPUT"_out.improvement.bam \
M=output/"$INPUT"_out.dedup_metrics.txt \
CREATE_INDEX=true
? parallle ?
################
#(14) index BAM using samtools
################
echo "...................................................................."
echo "(14) index BAM using samtools ${INPUT}"
echo "...................................................................."

samtools index -@ 24 output/"$INPUT"_out.improvement.bam

########################################
########## Variant Calling #############
########################################

###################
## (15) Call variants using HaplotypeCaller in GVCF mode.
###################
echo "...................................................................."
echo "(15) Call variants using HaplotypeCaller in GVCF mode. ${INPUT}"
echo "...................................................................."

# java -jar GenomeAnalysisTK.jar \
# -T HaplotypeCaller \
# -R reference.fa \
# -I Sample_name_lib_num.improvement.bam \
# -o Sample_name_lib_num.HaplotypeCaller.vcf \
# -ERC GVCF
java -jar ${GATK_JAR} \
-T HaplotypeCaller \
-R ${REF_FA} \
-I output/"$INPUT"_out.improvement.bam \
-o utput/"$INPUT"_out.HaplotypeCaller.vcf \
-ERC GVCF

? nt nct ?
###################
#(16) Run GenotypeGVCFs in GVCF mode.
###################
echo "...................................................................."
echo "(16) Run GenotypeGVCFs in GVCF mode.. ${INPUT}"
echo "...................................................................."

java -jar ${GATK_JAR} \
-T GenotypeGVCFs \
-R ${REF_FA} \
-V output/"$INPUT"_out.HaplotypeCaller.vcf \
-o output/"$INPUT"_out.HaplotypeCaller.gg.vcf

? nt nct ?
###################
# (17) Call variants with Samtools
###################
echo "...................................................................."
echo "(17) Call variants with Samtools ${INPUT}"
echo "...................................................................."

samtools mpileup -C 50 -uf ${REF_FA} output/"$INPUT"_out.improvement.bam | \
bcftools view -bvcg - > output/"$INPUT"_out.samtools_var.bcf
bcftools view output/"$INPUT"_out.samtools_var.bcf | vcfutils.pl varFilter -D 100 > output/"$INPUT"_out.samtools_var.vcf
? parallle ?

###################
# (18) Merge two separate callsets
###################
echo "...................................................................."
echo "(18) Merge two separate callsets ${INPUT}"
echo "...................................................................."

java -jar ${GATK_JAR} \
-T CombineVariants \
-R ${REF_FA} \
--variant output/"$INPUT"_out.samtools_var.vcf \
-o output/"$INPUT"_out.vcf \
-genotypeMergeOptions UNIQUIFY

? nt nct ?
