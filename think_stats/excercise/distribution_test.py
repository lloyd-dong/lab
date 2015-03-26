import math
import sys
sys.path.append('..')
import myplot
import sample_distribution as sd

def rankit_figure(function_name, xs,name=None):
    xs_expo = sd.samples(function_name, len(xs))
    if name is None: 
        name = function_name
    myplot.scatter(xs_expo,xs, label='rankit '+ name)
    myplot.Show()

def is_expo(cdf):
    cdf.name = 'is expo'
    myplot.Cdf(cdf, complement=True, color='blue')
    myplot.Show(yscale='log')

    rankit_figure('expo', cdf.Values())    

def is_pareto(cdf):
    cdf.name = 'is pareto'
    myplot.Cdf(cdf, complement=True, color='green')
    myplot.Show(xscale='log',yscale='log')

    rankit_figure('pareto', cdf.Values())
    
def is_weibull(pmf):
    xs, ys = pmf.Render()
    ys_log = [math.log(1-y) for y in ys]
    myplot.plot(xs,ys, label='is weibull')
    myplot.Show(xscale='log',yscale='log')

    rankit_figure('weibull', xs)

def is_normal(xs):
    rankit_figure('normal',xs)

def is_log_normal(xs):    
    xs_log = [math.log(x) for x in xs if x >0]
    rankit_figure('normal',xs_log,'log normal')

