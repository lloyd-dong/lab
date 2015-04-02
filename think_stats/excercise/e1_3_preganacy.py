import random
import math

import sys
sys.path.append('..')
import Pmf
import thinkstats
import myplot
import Cdf

import e_babies as eb

def e1_3_DateRelated():
	baby_1st, baby_rest, babies = eb.partition_babies()
	b_1_date, b_2_date=[x[0] for x in baby_1st], [x[0] for x in baby_rest]
	
	first_avg, first_var = thinkstats.MeanVar(b_1_date)
	non_first_avg, non_first_var = thinkstats.MeanVar(b_2_date)
	first_sd, non_first_sd = math.sqrt(first_var), math.sqrt(non_first_var)

	late_first = [x for  x in b_1_date if x >40 ]
	late_non_first = [x for x in b_2_date if x > 40]
	late_first_ratio = float(len(late_first)) / len(b_1_date) * 100
	late_non_first_ratio = float(len(late_non_first)) / len(b_2_date) * 100
	relative_risk_of_late = (late_first_ratio - late_non_first_ratio)/late_non_first_ratio * 100

	early_first = [x for  x in b_1_date if x <38 ]
	early_non_first = [x for x in b_2_date if x < 38]
	early_first_ratio = float(len(early_first)) / len(b_1_date) * 100
	early_non_first_ratio = float(len(early_non_first)) / len(b_2_date) * 100
	relative_risk_of_early = (early_first_ratio - early_non_first_ratio)/early_non_first_ratio *100

	print('early ratio of first %f, early ratio of non_first %f' % (early_first_ratio,early_non_first_ratio))
	print('late ratio of first %f, late ratio of non_first %f' % (late_first_ratio,late_non_first_ratio))
	print('risk of late is %f, risk of early is %f' %(relative_risk_of_late, relative_risk_of_early))

	pmf_first = Pmf.MakePmfFromList(b_1_date,'first')
	pmf_non_first = Pmf.MakePmfFromList(b_2_date,'non_first')

	myplot.Pmfs([pmf_first, pmf_non_first])
	myplot.Show(xlabel='pregancy weeks',ylabel='number')

	print '================'
	#print('b_1_date # %d, b_2_date # %d' % (len(b_1_date), len(b_2_date)))
	print 'first baby is ', len(b_1_date), " b_2_date # is ", len(b_2_date)
	print('avg first is %f , avg non first is %f ' %( first_avg, non_first_avg)  )
	print 'standard deviation first ', first_sd, ", standard deviation non first ", non_first_sd
	print('avg difference in days is %f, stand deviation difference in days is %f ' % \
		((first_avg - non_first_avg) *7, ( first_sd - non_first_sd) *7 ))


def main():
	pass
if __name__ == '__main__':
	main()