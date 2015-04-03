import e_babies as eb

import random
import sys
sys.path.append('..')
import thinkstats
import Cdf

def mean_diff_and_whole_samples():
	''' wl[0] is weight list of 1st, wl[1] is rest, wl[2] is all
	'''
	wl = [eb.get_wight_list(baby) for baby in eb.partition_babies()]	
	means = [thinkstats.Mean(li) for li in wl] 	
	return means, wl[2]

def means_by_resampling(wl, sample_times=100, point_n=1000):	
	means = []
	for i in xrange(sample_times):
		l = []
		for j in xrange(point_n):
			l.append(random.choice(wl))
		means.append(thinkstats.Mean(l))
	return means

def main():	
	means, wl = mean_diff_and_whole_samples()	
	mean_diff = abs(means[0]-means[1])
	print 'mean diff: %4.2f oz' % (mean_diff)

	sample_times = 1000
	mean_sample = means_by_resampling(wl, sample_times)
	mean_sample = [abs(m-means[1]) for m in mean_sample]
	cdf_means = Cdf.MakeCdfFromList(mean_sample, 'sample means')
	p_value = cdf_means.Prob(mean_diff)
	print 'p value: %4.2f%%' % (p_value*100) 

if __name__ == '__main__':
	main()