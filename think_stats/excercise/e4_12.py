import math
import sys
sys.path.append('..')
import populations
import myplot
import Cdf
import sample_distribution as sd

def main():
    pops = populations.ReadData('../populations.csv')
    n = len(pops)
    print 'city num is ',  n
    cdf = Cdf.MakeCdfFromList(pops, 'popluation')
    xs, ys = cdf.Render()

    xs_normal = sd.samples('normal', n)
    #myplot.scatter(xs, xs_normal, label='sample normal')
   
    xs_log = [math.log(x) for x in pops]
    xs_log.sort()
    myplot.scatter(xs_normal, xs_log, color='red', label='sample log normal')

    myplot.Show()
    myplot.Clf()

    try:
        ccdf_log_ys = [ math.log(1.00000001-y) for y in ys]
        # myplot.Cdf(cdf, complement=True)
        myplot.plot(xs, ys, label=cdf.name)
        myplot.Config(yscale='log',xscale='log')
        myplot.Show()    
    except:
        print 'exception', y

if __name__ == '__main__':
    main()
