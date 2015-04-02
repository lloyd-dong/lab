import math
import random
import sys

"""
simple way
sys.append('..')
import myplot, Pmf

much more robust code
import sys; 
if not "/home/a/" in sys.path:
    sys.path.append("/home/a/") 
if not 'b' in sys.modules:
    b = __import__('b')
else:
    eval('import b')
    b = eval('reload(b)')
"""
import sys 
if not ".." in sys.path:
    sys.path.append("..") 
if not 'Pmf' in sys.modules:
    Pmf = __import__('Pmf')
else:
    eval('import Pmf')
    Pmf = eval('reload(Pmf)')

if not 'myplot' in sys.modules:
    myplot = __import__('myplot')
else:
    eval('import myplot')
    myplot = eval('reload(myplot)')

def main():
	lam=2.0
	x=range(999)
	bin = 10

	x_rand=sorted([random.expovariate(lam) for i in x])
	cdf_by_rand_x = [1-pow(math.e, -lam *i) for i in x_rand]
	bin_cdf_by_rand_x = [ math.floor(y * bin)/bin for y in cdf_by_rand_x]
	pmf_y_by_rand_x = Pmf.MakePmfFromList(bin_cdf_by_rand_x, 'cdf by expovariate')

	bin_x_rand = [ math.floor(y * bin)/bin for y in x_rand]
	pmf_x_rand = Pmf.MakePmfFromList(bin_x_rand, 'x by expovariate')


	cdf_rand = sorted([random.random() for i in x])
	x_by_rand_cdf= sorted([ math.log(1-cy)/(-lam) for cy in cdf_rand])
	#bin_cdf_rand = [ math.floor(y * bin) for y in cdf_rand]
	#pmf_by_rand_cdf = Pmf.MakePmfFromList(bin_cdf_rand, 'cdf by random CDF')

	bin_x_by_rand_cdf = [ math.floor(y * bin)/bin for y in x_by_rand_cdf]
	pmf_x_by_rand_cdf = Pmf.MakePmfFromList(bin_x_by_rand_cdf, 'x by random cdf 0-1')

	arbitary_x = 10
	x_rand2=sorted([random.uniform(0.0,arbitary_x) for i in x])
	cdf_by_rand_x2 = [1-pow(math.e, -lam *i) for i in x_rand2]
	bin_cdf_by_rand_x2 = [ math.floor(y * bin)/bin for y in cdf_by_rand_x2]
	pmf_y_by_rand_x2 = Pmf.MakePmfFromList(bin_cdf_by_rand_x2, 'cdf by randome x 0-10')


	myplot.Pmfs([pmf_y_by_rand_x,pmf_y_by_rand_x2])
	myplot.show()

	myplot.Pmfs([pmf_x_rand,pmf_x_by_rand_cdf])
	myplot.show()

if __name__ == '__main__':
	main()