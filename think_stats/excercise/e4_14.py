import math
import random
import distribution_test as dt

def weibullvariate(scale,shape):
    return pow(math.e, math.log(scale) +                \
        1.0/shape *                                     \
        math.log( math.log(1.0/(1-random.random())) )   \
        )

def main():
    scale, shape =0.5, 2.0
    n = 20000
    xs = [ weibullvariate(scale,shape) for i in xrange(n)]
    xs.sort()
    dt.rankit_figure('weibull', xs)

if __name__ == '__main__':
        main()  
