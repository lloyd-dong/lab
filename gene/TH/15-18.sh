/bin/bash -e util.sh

if [ ! $# == 1 ]; then
        echo need input file name
        exit
fi

INPUT=$1

echo "...................................................................."
echo "########## Variant Calling #############"
echo "...................................................................."


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

#? nt nct ?

echo "...................................................................."
echo "(16) Run GenotypeGVCFs in GVCF mode.. ${INPUT}"
echo "...................................................................."

java -jar ${GATK_JAR} \
-T GenotypeGVCFs \
-R ${REF_FA} \
-V output/"$INPUT"_out.HaplotypeCaller.vcf \
-o output/"$INPUT"_out.HaplotypeCaller.gg.vcf

#? nt nct ?

echo "...................................................................."
echo "(17) Call variants with Samtools ${INPUT}"
echo "...................................................................."

samtools mpileup -C 50 -uf ${REF_FA} output/"$INPUT"_out.improvement.bam | \
bcftools view -bvcg - > output/"$INPUT"_out.samtools_var.bcf
bcftools view output/"$INPUT"_out.samtools_var.bcf | vcfutils.pl varFilter -D 100 > output/"$INPUT"_out.samtools_var.vcf
#? parallle ?

# echo "...................................................................."
# echo "(18) Merge two separate callsets ${INPUT}"
# echo "...................................................................."

# java -jar ${GATK_JAR} \
# -T CombineVariants \
# -R ${REF_FA} \
# --variant output/"$INPUT"_out.samtools_var.vcf \
# -o output/"$INPUT"_out.vcf \
# -genotypeMergeOptions UNIQUIFY

#? nt nct ?
