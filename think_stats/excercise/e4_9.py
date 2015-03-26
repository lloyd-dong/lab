import random
import sys
sys.path.append('..')
#import erf
import thinkstats
import myplot

def sample(mu=0.0, sigma=1.0, n=6):	
	# return sorted([erf.NormalCdfInverse(random.random(),mu,sigma ) \
	#    for i in xrange(n)] )
	return sorted([random.normalvariate(mu,sigma) for i in xrange(n)])

def samples(mu=0.0, sigma=1.0, group=6, n=10000):
    return [ sample(mu,sigma,group) for i in xrange(n)]

def rankit_xs(group=6,n=10000): 
	return [thinkstats.Mean(i) for i in zip(*samples(group=group, n=n))]

def main():
    #means = [thinkstats.Mean(i) for i in zip(*samples())]
    #for m in means:
    #    print '%5f' % (m) ,
    l = [9,11,11,13,14,15,16,17,19,21,23,25,26,26,28,32,36,37,43,62]
    l.sort()
    n = len(l)
    print n
    xs = rankit_xs(n)

    myplot.plot(xs,l, label='rankit')
    myplot.Show()


if __name__ == '__main__':
	main()