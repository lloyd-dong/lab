import sys
sys.path.append('..')
import irs
import distribution_test as dt

def main():
    data = irs.ReadIncomeFile('../08in11si.csv')
    hist, pmf, cdf = irs.MakeIncomeDist(data)

    dt.is_expo(cdf)
    dt.is_pareto(cdf)
    dt.is_weibull(pmf)
    dt.is_normal(hist.Values())
    dt.is_log_normal(hist.Values())

if __name__ == '__main__':
    main()