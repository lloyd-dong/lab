import e_babies as eb

import random
import sys
sys.path.append('..')
import myplot
import Cdf


def e3_6_WightCDF():	
	baby_1st, baby_rest, babies = eb.partition_babies()
	c_1_wt = Cdf.MakeCdfFromList(eb.get_wight_list(baby_1st), '1st')
	c_2_wt = Cdf.MakeCdfFromList (eb.get_wight_list(baby_rest),'others')
	my_wt=123.45886682
	print 'my wight in 1st:%4.2f%%, in others:%4.2f%%' % \
	       (100*c_1_wt.Prob(my_wt), 100*c_2_wt.Prob(my_wt))
	
	myplot.Cdfs([c_1_wt,c_2_wt])
	myplot.Show()

def e3_9_WightCDF():
	baby_1st, baby_rest, babies = eb.partition_babies()
	l_wt = eb.get_wight_list(babies)
	slice_wt = random.sample(l_wt, 100)
	c_s = Cdf.MakeCdfFromList(slice_wt,'slice')
	c_l = Cdf.MakeCdfFromList(l_wt, 'whole')
	myplot.Cdfs([c_s,c_l])
	myplot.Show()
	
def main():
	e3_9_WightCDF()
	e3_6_WightCDF()

if __name__ == '__main__':
	main()