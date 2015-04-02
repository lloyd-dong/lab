'''this is the public lib for pregnancy, periods and weights
'''
import sys
sys.path.append('..')
import survey

def partition_babies():
	baby_1st, baby_rest, babies = [],[],[]
	table= survey.Pregnancies() 
	table.ReadRecords('../data')
	
	for baby in table.records:
		if baby.outcome != 1:
			continue		
		data = (baby.prglength, baby.totalwgt_oz)
		babies.append(data)
		if baby.birthord == 1:
			baby_1st.append(data)
		else:
			baby_rest.append(data)
	print 'dgb: pregancies: %d, live baby: %d, live rate: %4.2f%%' % \
	    (len(table.records), len(babies), 100.0*len(babies)/len(table.records))
	return baby_1st, baby_rest, babies

def get_wight_list(babies):
	return [x[1] for x in babies if x[1] != 'NA'] 	

def get_pregnacy_list(babies):
	return [x[0] for x in babies if x[0] != 'NA']
