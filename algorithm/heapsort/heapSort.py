import sys
import time
import random
import pdb
"""init random 10000 to a file
cmp 2 file
once comfired the 2 file generate the same result,
================
read random 
run 10000
	copy array
	log start time
	if parameter is 1:		
		headAdjust_1(new array)
	else:
		headAdjust_2(new array)
	log end time
write adjusted list to file
"""

file_name = 'random.dat'

def generate_randome(n, file_name):
	f = file(file_name,'w')
	for i in xrange(n):
		f.write(str(random.randint(0,n)) + ',')		
	f.close()

def get_list_in_file(fileName):
	f = file(file_name,'r')
	l = []
	for i, line in enumerate(f):
		l = line.split(',')
	f.close()
	l.pop()  # remove the last empty ''
	return [int(i) for i in l]	

def heap_sort_1(l):
	for i in xrange(len(l)):
		heap_adjust_1(l, len(l)-i)		
		l[0],l[len(l)-i-1] = l[len(l)-i-1],l[0]	

def heap_adjust_1(l,nlen):	
	"""This algrithem use linear complexity to ensure the l[0] is the biggest one
	this algrithem is useless when ajust the heap from top, which is log(n) complexity
	"""
	i = nlen/2 - 1 # this is the last non-leaf node
	while i >= 0 : 
		child = i*2 + 1	
		# compare the 2 children nodes, choose the bigger one
		if child+1 < nlen and l[child] < l[child +1]: 
			child += 1
		if l[i] < l[child]:
			l[i], l[child] = l[child],l[i]		
		i -= 1 # to check the previous node

def heap_sort(l):
	last_p = len(l)-1 # pointer to the last element in l	

	#start_p = last_p/2
	#while True : 
	#	heap_adjust(l, start_p, last_p)
	#	start_p -= 1
	#	if start_p < 0: break
	# use the following 2 lines to replace the above 5 lines 

	for start_p in xrange(last_p/2, -1, -1): # biuld heap, the 1st -1 make sure l[0] is included
		heap_adjust(l, start_p, last_p)		

	while last_p > 0:		
		l[0],l[last_p] = l[last_p],l[0]	
		last_p -= 1
		heap_adjust(l, 0, last_p)

def heap_adjust(l, start, end):	
	while start < end:
		child = start*2 + 1
		if child > end: break
		if child+1 <= end and l[child] < l[child+1]: 
			child += 1  # choose the bigger children
		if l[start] < l[child]:
			l[start],l[child] = l[child], l[start]
		start = child

def check_compare(origin_l, l):		
	origin_l.sort()
	for i in xrange(len(l)):
		if origin_l[i] != l[i]:
			raise Exception('at %d %d != %d' % (i, origin_l[i], l[i]))

def log_time(spend_time):
	print spend_time	

def main(name, method=None):	
	trial_n = 11

	random_l=get_list_in_file(file_name)
	spend_time=[]
	for i in xrange(trial_n):
		l = random_l[:] 		#shallow copy array
		start_time = time.time()
		if method == '1' :		
			heap_sort_1(l)
		else:
			heap_sort(l)
		spend_time.append(time.time()-start_time)   #log spend time for further analysis
		# check_compare(random_l,l)		
	log_time(spend_time)

if __name__ == '__main__':	
	
	main(*sys.argv)
	#generate_randome(1000,file_name)
	