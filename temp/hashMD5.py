
import sys
import hashlib
 
for line in sys.stdin:
    line = line.strip()
    print(line)
    arr = line.split()
    md5_arr = []
    for a in arr:
        md5_arr.append(hashlib.md5(a).hexdigest())
    print "\t".join(md5_arr)