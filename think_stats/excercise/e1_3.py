import survey
import Pmf
import thinkstats, math
import myplot
import Cdf
import random

first_baby, non_first_baby = [],[]

def PartitionBabies():
	table= survey.Pregnancies() 
	table.ReadRecords()
	print "number of pregancies ", len(table.records)

	live_baby=0
	for baby in table.records:
		if baby.outcome ==1 :
			live_baby +=1

	print "live_baby ", live_baby	

	for baby in table.records:
		if baby.outcome !=1 :
			continue
		if baby.birthord ==1:
			first_baby.append((baby.prglength, baby.totalwgt_oz))
		else:
			non_first_baby.append((baby.prglength,baby.totalwgt_oz))

def DateRelated():
	b_1_date, b_2_date=[x[0] for x in first_baby], [x[0] for x in non_first_baby]
	
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

def WightCDF_3_6():	
	""" excise 3-6
	"""
	c_1_wt = Cdf.MakeCdfFromList([x[1] for x in first_baby if x[1] != 'NA'],'first')
	c_2_wt = Cdf.MakeCdfFromList ([x[1] for x in non_first_baby if x[1] != 'NA'],'non first')
	my_wt=123.45886682
	print 'my wight at 1 is %f and at non 1 is %f' %(c_1_wt.Prob(my_wt), c_2_wt.Prob(my_wt))
	
	myplot.Cdfs([c_1_wt,c_2_wt])
	myplot.Show()

def GetToalWightList():
	return [x[1] for x in first_baby if x[1] != 'NA'] + \
		[x[1] for x in non_first_baby if x[1] != 'NA']
	
def WightCDF_3_9():
	l_wt = GetToalWightList()
	slice_wt = random.sample(l_wt, 100)
	c_s = Cdf.MakeCdfFromList(slice_wt,'slice')
	c_l = Cdf.MakeCdfFromList(l_wt, 'whole')
	myplot.Cdfs([c_s,c_l])
	myplot.Show()


def Interquartile_Mean(l):
	c_l = Cdf.MakeCdfFromList(l, 'whole')
	v_25, v_mean, v_75 = c_l.Value(0.25),c_l.Value(0.50),c_l.Value(0.75)

	print v_75, v_25,v_mean

	myplot.Cdf(c_l)
	myplot.Show()
	pmf = Pmf.MakePmfFromList(l,'pmf')
	print 'len of values ',len(pmf.Values())
	myplot.Pmf(pmf)
	myplot.Show()
	
	return v_75 - v_25, v_mean
	
def e_3_11():
	l_wt = GetToalWightList()
	print 'len of wt is ', len(l_wt)
	interquartile, mean = Interquartile_Mean(l_wt)
	print 'Interquartile is %d, mean is %f' % (interquartile, mean)

PartitionBabies()
# DateRelated()
e_3_11()	