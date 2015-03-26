import math
import sys
sys.path.append('..')
import Cdf
import thinkstats
import myplot
import survey
import erf
import e4_9


def main():
    preg = survey.Pregnancies()
    preg.ReadRecords('..')
    preg_lengths = sorted([ r.prglength for r in preg.records if r.outcome==1])
    baby_n =len(preg_lengths)
    cdf_list = Cdf.MakeCdfFromList(preg_lengths, 'preg length')
    print 'how many preg?', baby_n

    mu = thinkstats.Mean(preg_lengths) # mu 38.560560,
    sigma = math.sqrt(thinkstats.Var(preg_lengths)) #  v 7.30186    
    ys_calc = [erf.NormalCdf(x, mu, sigma) for x in preg_lengths]
    cdf_calc = Cdf.Cdf(preg_lengths,ys_calc, 'cdf calc')
    print 'mean is %f, v is %f' % (mu, sigma)

    sample_xs = e4_9.sample(mu,sigma, baby_n)
    sample_ys = [erf.NormalCdf(x, mu, sigma) for x in sample_xs]
    cdf_sample = Cdf.Cdf(sample_xs,sample_ys, 'cdf sample')

    myplot.Cdfs([cdf_list, cdf_sample]) # cdf_calc    
    myplot.Show()

if __name__ == '__main__':
	main()