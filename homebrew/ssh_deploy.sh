if [ -z $1 ]; then
	echo "provide file name to deploy"
	exit -1
fi 
scp $1 arches-repo:/home/bo_dong/
ssh arches-repo /home/bo_dong/update-repo.sh