import sample_distribution as sd
import distribution_test as dt
import math
import sys
sys.path.append('..')
import thinkstats
import Cdf
import myplot
import erf
import pdb

def get_max_loaf(n):
    mu, sigma = 950, 50
    l = sd.samples('normal', n, mu=mu, sigma=sigma)
    return max(l)

def analysis(l):   
    cdf = Cdf.MakeCdfFromList(l,'loaf')
    myplot.Cdf(cdf)

    l.sort()
    m,v = thinkstats.MeanVar(l)
    sigma = math.sqrt(v)
    print 'mu is %5.3f, sigma is %5.3f' % ( m, sigma)    
    xs_samples = sd.samples('normal',n=len(l),mu=m,sigma=sigma)
    ys_samples = [erf.NormalCdf(x,m,sigma) for x in xs_samples]
    #pdb.set_trace()

    myplot.scatter(xs_samples,ys_samples, color='red',label='sample normal')

    #myplot.plot(xs_samples,l,label='cmp with calculate')
    myplot.Show()

    #dt.is_normal(l)
    #dt.is_log_normal(l)


def main():
    days, max_n = 365, 100
    criteria = 1000

    for n in xrange(1,max_n):
        loafs = []
        for d in xrange(days):
            loafs.append(get_max_loaf(n))
        mean = thinkstats.Mean(loafs)
        if mean >= criteria:
            print n, mean
            analysis(loafs)
            break
            
if __name__ == '__main__':
    main()


    
    




