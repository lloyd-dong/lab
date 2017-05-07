/bin/bash -e util.sh

if [ ! $# == 1 ]; then
        echo need input file name
        exit
fi

INPUT=$1

echo "...................................................................."
echo "############# Improvement ##############"
echo "...................................................................."

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
 -nt 6
# --interval_padding , -ip Amount of padding (in bp) to add to each interval

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

#? -nt -nct?
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

# ? parallle ?

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
#? nt nct?

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

# ?nt nct ?
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
# ? parallle ?