import random
import Pmf
import Cdf
import myplot

l=[]
for i in xrange(999):
	l.append(random.random())

p = Pmf.MakePmfFromList(l, 'pmf')
c = Cdf.MakeCdfFromList(l,'cdf')

myplot.Pmf(p)
myplot.Show()
myplot.Clf()
myplot.Cdf(c)
myplot.Show()