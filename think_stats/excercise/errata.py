import Cdf, myplot
import math, random

def CDFExpo(lam, point_n=1000, name='CDF Expo'):
	xs= sorted([random.expovariate(lam) for i in xrange(point_n)])
	ys= [1- pow(math.e, -lam * x) for x in xs]
	return Cdf.Cdf(xs,ys,name)	

lam = math.log(2)
mean, percentile = 0.5, 0.95
cdf = CDFExpo(lam)
print 'expo mean is %f, percentile 95%% is %f' % (cdf.Value(mean), cdf.Value(percentile))
