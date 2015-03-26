import e4_3  # use the CDFPareto function
import sys
sys.path.append('..')


def main():
    xm, alpha = 100.0, 1.7
    median = xm*pow(2,1/alpha)
    cdf = e4_3.CDFPareto(alpha, xm,point_n=100000,name='6 billion')
    mean = cdf.Mean()
    median_cdf = cdf.Value(0.5)
    tallest = cdf.Value(0.999)
    percentage_lower_than_mean = cdf.Prob(mean)

    print 'calculated median is %f, cdf mean(avg) %f, \
           cdf median %f, tallest is %f, shorter %f' % \
           (median, mean, median_cdf, tallest, percentage_lower_than_mean)

if __name__ == '__main__':
	main()