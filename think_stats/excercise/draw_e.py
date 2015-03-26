""" draw a line of exponential function
"""
from math import e
import Pmf, Cdf
import myplot

la=[0.5,1.0,2.0]
Interval,MAX=0.1,10
step = int(MAX/Interval)

xs=[float(i)*Interval for i in xrange(step)]
ys,p,cys=[],[],[]

for i in xrange(len(la)):
	ys.append([la[i]*e**(-la[i] * x ) for x in xs])
	#cy.append([1 - e**(-la[i] * x ) for x in xs])	
	p.append(Pmf.MakePmfFromList(ys[i]))

	print 'sum ys[%d] is %f' % (i,sum(ys[i]))
	print 'la[%d] is %f, 1/la[i] is %f, p[%d].average is %f, 1/(la^2) is %f, var is %f,' \
		 % (i,la[i],1/la[i],i,p[i].Mean(), 1/(la[i]**2), p[i].Var())
	print 'ys[%d].mean[%d] is %f'  % (i, step/2,ys[i][step/2])
	#myplot.plot(xs, ys[i],label=la[i])


#myplot.plot(x, cy1,label=la2)
#myplot.plot(x, cy2,label=la2)
#myplot.Show()