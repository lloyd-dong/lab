import math
import sys
sys.path.append('..')
import Cdf
import Pmf
import myplot
import sample_distribution as sd
import exceptions

def rankit_figure(function_name, xs,name=None):
    xs_expo = sd.samples(function_name, len(xs))
    if name is None: 
        name = function_name
    myplot.scatter(xs_expo,xs, label='rankit '+ name)
    myplot.Show()

def convert_to_Cdf(p):
    cdf = Cdf.Cdf()
    if isinstance(p, Cdf.Cdf):
        return p
    elif isinstance(p,list):
        cdf = Cdf.MakeCdfFromList(p)
    elif isinstance(p, Pmf.Pmf):
        cdf = cdf.MakeCdfFromPmf(p)
    else:
        raise Exception('unknow type of input parameter')
    return cdf

def is_expo(p):    
    cdf = convert_to_Cdf(p)
    myplot.Cdf(cdf, complement=True, color='blue', label='is expo')
    myplot.Show(yscale='log')

    rankit_figure('expo', cdf.Values())    

def is_pareto(p):
    cdf = convert_to_Cdf(p)    
    myplot.Cdf(cdf, complement=True, color='green',label='is pareto')
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
    #xs_log = [math.log(x) for x in xs if x >0]
    #rankit_figure('normal',xs_log,'log normal'
    rankit_figure('log_normal',xs,'log normal')

