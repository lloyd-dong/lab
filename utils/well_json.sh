set -ex
mkdir ../well_json
for i in $(ls) ; do cat $i|python -mjson.tool >../well_json/$i ; done 
