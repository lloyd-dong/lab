"""
draw a exponetial line, mean is 1, calculate value for percentile 95%
    mean is ln2/lam. lam=ln2
draw a pareto line, mean is 1, calculate value for percentile 95%
    mean is Xm * 2^(1/alpha) alpha=1 Xm=0.5 or Xm=0.2 alpha = ln2/ln0.5
"""
import math
import random
import sys
sys.path.append('..')
import Cdf
import myplot

def CDFExpo(lam, point_n=1000, name='CDF Expo'):
    xs= sorted([random.expovariate(lam) for i in xrange(point_n)])
    ys= [1- pow(math.e, -lam * x) for x in xs]
    return Cdf.Cdf(xs,ys,name)    
    
def CDFPareto(alpha, Xm=1.0,point_n=1000,name='CDF Pareto' ):
    xs = sorted([random.paretovariate(alpha)*Xm for i in xrange(point_n)])
    ys = sorted([1- pow(Xm/x, alpha) for x in xs])
    return Cdf.Cdf(xs,ys,name)
    
def ExpoPDF(lam,max_x=10, point_n=1000):
    xs=[ float(max_x) * i /point_n for i in xrange(point_n) ] 
    ys = [lam * pow(math.e, -lam * x) for x in xs]
    return xs, ys

def DrawExpo():
    xs, ys = ExpoPDF(0.1)
    myplot.plot(xs, ys, label = 'lam 0.1')
    myplot.show()

def Mean_Percentile_95():
    
    cdf_e, cdf_p = CDFExpo(math.log(2)), CDFPareto(1, 0.5)
    
    mean, percentile = 0.5, 0.95

    print 'expo mean is %f, percentile %f is %f; pareto mean is %f, percentile %f is %f' \
        % (cdf_e.Value(mean), percentile, cdf_e.Value(percentile), \
        cdf_p.Value(mean), percentile, cdf_p.Value(percentile))
    

    myplot.Cdfs([cdf_e,cdf_p])
    myplot.Show()
def ForErrata():
    lam = math.log(2)
    mean, percentile = 0.5, 0.95
    cdf = CDFExpo(lam)
    print 'expo mean is %f, percentile 95%% is %f' % (cdf.Value(mean), cdf.Value(percentile))

def expo_mean():
    lam =2.0
    cdf = CDFExpo(lam, point_n=100000, name='CDF Expo')
    mean = 1.0/lam
    cdf_mean= cdf.Mean()
    print 'mean %f, cdf mean %f' % (mean, cdf_mean)


if __name__ == '__main__':
    expo_mean()