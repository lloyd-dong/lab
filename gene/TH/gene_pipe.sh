#!/bin/bash


module load bwa/0.7.12 
module load samtools/1.2
module load GATK/3.7 
module load picard/1.129
module load bcftools/1.3.1


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


yhbatch -N 1 -c 24 4_5_6.sh a &
yhbatch -N 1 -c 24 4_5_6.sh b &
yhbatch -N 1 -c 24 4_5_6.sh c &
yhbatch -N 1 -c 24 4_5_6.sh d &

wait

yhbatch  -N 1 -c 24 wrapper.sh 7-13.sh a b c d

wait

yhbatch  -N 1 -c 24 14.sh a &
yhbatch  -N 1 -c 24 14.sh b &
yhbatch  -N 1 -c 24 14.sh c &
yhbatch  -N 1 -c 24 14.sh d &

wait 

yhbatch  -N 1 -c 24 wrapper.sh 15-18.sh a b c d