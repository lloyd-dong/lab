""" draw a line of exponential function
"""
from math import e
import sys
sys.path.append('..')
import Pmf 
import Cdf
import myplot
import thinkstats

def generate_xs(max_x, point_n=1000):
	return [float(max_x) * i /point_n for i in xrange(point_n)] 
	
def draw_gause():
	''' draw a line of exp(-t^2)
	'''
	max_x, point_n = 100,1000
	xs = generate_xs(max_x,point_n)
	ys = [pow(e, -x*x) for x in xs]
	myplot.plot(xs, ys, label='exp(-t^2)')
	myplot.Show()

def draw_expo_line():
	la=[0.5,1.0,2.0]
	MAX, point_n =100, 1000
	xs = generate_xs(MAX,point_n)
	ys,p,cys=[],[],[]

	for i in xrange(len(la)):
		ys.append([la[i]*e**(-la[i] * x ) for x in xs])
		#cy.append([1 - e**(-la[i] * x ) for x in xs])	#complement CDF
		p.append(Pmf.MakePmfFromList(ys[i]))

		'''1/lam != ys[i].mean(), because xs is not exponotial distribution
		on the line near y axis, xs should be much more intenseive to sample
		the value of ys[i], otherwise the mean() would be diluted 
		'''
		print '%d: lam %4.2f,1/lam: %4.2f, pmf mean: %4.2f,ys mean[%d]: %4.2f' % \
		        (i, la[i],1/la[i], p[i].Mean(),point_n/2,ys[i][point_n/2])
		print 'sum y is %4.2f 1/(la^2): %4.2f' \
			 % (sum(ys[i]), 1/(la[i]**2))		
		
		myplot.plot(xs, ys[i],label=la[i])
	
	myplot.Show()
def main():
	draw_gause()

if __name__ == '__main__':
		main()	