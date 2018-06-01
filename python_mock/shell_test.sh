tgz_filer="/Users/bodong/Git/maps-services-library/Users/bodong/tmp/data/pakckaged_mirror/"

for f in $(ls $tgz_filer) 
do
	f_name=${f%%.*}
	echo $f_name
	folder_name="/Users/bodong/tmp/data/mirror_lastest_run_52_0826/"${f_name}

	mkdir -p $folder_name
	tar -xzf "$tgz_filer""$f" -C $folder_name
	ls $folder_name
done