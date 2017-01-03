apt-get update
cd /root

# ---------------------
# install osscmd
# wget -O osscmd.zip https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/internal/oss/0.0.4/assets/sdk/OSS_Python_API_20160419.zip?spm=5176.doc32171.2.2.cRTWFj&file=OSS_Python_API_20160419.zip
# apt-get -y install unzip
# unzip osscmd.zip
# rm *.zip

# ---------------------
# install ossfs
wget -O ossfs.deb http://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/32196/cn_zh/1481699531936/ossfs_1.80.0_ubuntu14.04_amd64.deb?spm=5176.doc32196.2.1.kxKrKX&file=ossfs_1.80.0_ubuntu14.04_amd64.deb

# -y assume yes
apt-get -y install gdebi-core

# -n --non-interactive
gdebi -n ossfs.deb

mkdir /mnt/gene
ossfs bob-backup /mnt/gene -ourl=http://vpc100-oss-cn-beijing.aliyuncs.com

# ---------------------
# run bwa mem

cd /mnt/gene/bwa
pwd

export INPUT=a
export OUTPUT=../output
mkdir -p $OUTPUT

echo "...................................................................."
echo "processing 2016006L-1-2$INPUT_R1.fq  =>  $OUTPUT/$INPUT_out.aln.bam "
echo "...................................................................."
#./seqtk mergepe ../rawData/2016006L-1-2$INPUT_R1.fq ../rawData/2016006L-1-2$INPUT_R2.fq \
#   | ./bwa mem -p ../ref/GRCh38_full_analysis_set_plus_decoy_hla.fa - 2> $OUTPUT/$INPUT_out.log.bwamem \
#   | ./samtools view -1 - > $OUTPUT/$INPUT_out.aln.bam;

export INPUT=r
./seqtk mergepe ../rawData/$INPUT1.fq ../rawData/$INPUT2.fq \
   | ./bwa mem -p ../ref/GRCh38_full_analysis_set_plus_decoy_hla.fa - 2> $OUTPUT/$INPUT_out.log.bwamem \
   | ./samtools view -1 - > $OUTPUT/$INPUT_out.aln.bam;

./htsbox samview $OUTPUT/$INPUT_out.aln.bam >$OUTPUT