
def get_stu_num_of_each_class(dst):
	pmf={}		
	for i in dst:
		for j in i:
#			if pmf.has_key(j):
#				pmf[j] += 1	
#			else:
#				pmf[j]=1
			pmf[j] = pmf.get(j,0) +1
	return pmf


def get_avg_stu(pmf):
	class_num = len(pmf) 
	avg= float(sum(pmf.values())) /class_num
	return avg

def list_dict(pmf):
	for k,v in pmf.iteritems():
		print k, v


student_dst = [('Eng','Chi','Art','Music'),('Eng','Art','Music'),('Music','Art'),('Chi','Eng')]
class_pmf= get_stu_num_of_each_class(student_dst)
avg_stu= get_avg_stu(class_pmf)

list_dict(class_pmf)
print('on average, each class has %f'%(avg_stu)) 

course_dst = [(7,8),(12,8),(17,14),(22,4),(27,6),(32,12),(37,8),(42,3),(47,2)]
sum_stu, sum_course = 0,0
for i in course_dst:
	sum_stu += i[0]*i[1]
	sum_course += i[1]

avg= float(sum_stu) /sum_course
print "avg of class on book", avg