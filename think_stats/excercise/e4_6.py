import math
import random
import sys
sys.path.append('..')
import myplot

def Cdf_weibull(scale, shape, point_n=1000):    
    xs = sorted([random.weibullvariate(scale,shape) for i in xrange(point_n)])
    ys = [1 - pow(math.e, - pow(x/scale, shape)) for x in xs]
    ln_y= [math.log(1/(1-y)) for y in ys]
    return xs, ys, ln_y

def main():
	scale, shape = 1, [0.5, 1.0, 1.5, 5.0]	
	for i,s in enumerate(shape):
		xs, ys, ln_ys = Cdf_weibull(scale,s)
		myplot.plot (xs, ys, label='shape '+str(s))
		#myplot.plot (xs, ln_ys, label='shape '+str(s))

	#myplot.Config(xscale='log', yscale='log')	
	myplot.Show()

if __name__ == '__main__':
	main()