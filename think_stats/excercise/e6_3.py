import skewness as sk

import sys
sys.path.append('..')
import Cdf
import irs



def main():
    data = irs.ReadIncomeFile('../data/08in11si.csv')
    hist, pmf, cdf = irs.MakeIncomeDist(data)

    mean, median = cdf.Mean(), cdf.Percentile(50)
    print 'mean: %4.2f, median:%4.2f' % (mean, median)
    low_income_percent = cdf.Prob(mean)*100
    print '%4.2f%% people are lower then mean' % (low_income_percent)
    
    sk.show_skewness(pmf, 'income')

if __name__ == '__main__':
    main()