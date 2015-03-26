import random
import sys 
sys.path.append("..")
import Cdf, myplot


def CDFPareto(alpha, Xm=1.0,point_n=1000,name='CDF Pareto',max_x=None ):
    #max_x is to avoid a very long line
    xs = x0 = sorted([random.paretovariate(alpha)*Xm for i in xrange(point_n)])
    if max_x is not None:
        xs = [i for i in x0 if i < max_x]
    ys = [1.0- pow(Xm/x, alpha) for x in xs]
    return Cdf.Cdf(xs,ys,name)

def main():
    xm = 2
    alpha = [0.1,1.0]
    cdfs=[]
    for a in alpha:
        cdfs.append(CDFPareto(a,xm, 100,name=str(a),max_x=100))

    myplot.Cdfs(cdfs, complement=True) 
    myplot.Config(xscale = 'log', yscale='log')    
    myplot.show()

if __name__ == '__main__':    
    main()

