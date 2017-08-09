CMD=$1
shift
for i in $*; do 
	/bin/bash $CMD $i &
	#echo $CMD $i
done 
wait