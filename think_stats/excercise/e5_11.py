import random
import sys
sys.path.append('..')
import thinkstats

def match(criteria, matches=1):
	member = 10 
	k, p = 15*matches, 0.5

	results = 0
	for m in xrange(member):
		successive = 0
		for i in xrange(k):
			shoot = (random.random() >= 0.5)
			if shoot:
				successive += 1
				if successive == criteria:
					return 1
			else:
				successive = 0
	return 0		

def main():
	n = 1000
	criteria = 10
	matches = [1,82]
	results, prob = [], []
	for m in matches:
		results = [match(criteria,m) for i in xrange(n)]
		prob = thinkstats.Mean(results) * 100
		print 'matches %d, prob is %4.2f%%' % (m,prob)
		

if __name__ == '__main__':
		main()	
