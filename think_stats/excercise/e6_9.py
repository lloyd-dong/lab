import sample_distribution as sd

import math
import sys
sys.path.append('..')
import Pmf
import Cdf
import myplot

def convolution(pmf_a, pmf_b):
    pmf_z = Pmf.Pmf()
    pmf_z.name = pmf_a.name + ' + ' + pmf_b.name
    for x1, y1 in pmf_a.Items():
        for x2, y2 in pmf_b.Items():
            #k = (x1, x2)
            #if x1 > x2: k = (x2,x1)
            k = x1+x2
            pmf_z.Incr(k, y1+y2)
    print pmf_z.Mean()
    pmf_z.Normalize()
    print pmf_z.Mean()
    return pmf_z

def factorial(k):
    result = 1
    for i in xrange(k):
        result *= i+1
    return result

def pmf_erlan(k,lam,x):
    denominator = factorial(k-1)    
    return (lam**k) * (x**(k-1)) * math.e ** (-lam*x)/denominator

def main():
    lam = 0.5
    x_a, x_b = sd.samples('expo',1000),sd.samples('expo',1000)
    pmf_a = Pmf.MakePmfFromList(x_a, 'a')
    pmf_b = Pmf.MakePmfFromList(x_b, 'b')
    pmf_z = convolution(pmf_a,pmf_b)

    cdf_a = Cdf.MakeCdfFromList(x_a,'a')
    cdf_b = Cdf.MakeCdfFromList(x_b, 'b')
    cdf_z = Cdf.MakeCdfFromPmf(pmf_z)
    myplot.Cdfs([cdf_a,cdf_b,cdf_z])
    myplot.Show()
    #print pmf_z.Mean()

if __name__ == '__main__':
    main()