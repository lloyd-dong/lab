import math, random
import Cdf, myplot
import survey

class Baby(survey.Record):
	"""Represent a baby record """

class Babies(survey.Table):
	def __init__(self):
		survey.Table.__init__(self)
		self.start_flag=False
		
	def GetFileName(self):
		return 'babyboom.dat'
	def GetFields(self):
		return [			
			('t_birth', 1, 8, int),
			('gender', 9, 16, int),
			('birthwgt_gram', 17, 24, int),
			('m_since_mn', 25, 32, int),
		 ]
	def Recode(self):
		pass
	def ReadRecords(self, data_dir='.', n=None):
		filename = self.GetFileName()
		self.ReadFile(data_dir, filename, self.GetFields(), Baby, n)
		self.Recode()
	def MakeRecord(self, line, fields, constructor):		
		
		if not self.start_flag :
			self.start_flag = (line.find('START DATA:') >-1)
			#self.start_flag = (line ==('START DATA:'))			
			return None
		
		obj = constructor()
		for (field, start, end, cast) in fields:
			try:
				s = line[start-1:end]
				val = cast(s)
			except ValueError:		  
				val = 'NA'
			setattr(obj, field, val)					
		return obj		
	def AddRecord(self, record):
		"""Adds a record to this table.

		Args:
			record: an object of one of the record types.
		"""

		if record is not None:			
			self.records.append(record)


def getInterval():
	babies = Babies()
	babies.ReadRecords()	
	last_record=0
	interval= []
	for i in babies.records:
		interval.append(i.m_since_mn - last_record)
		last_record= i.m_since_mn
	#print interval
	return interval

def main():
	lam=1/32.6
	x=xrange(43)

	eX= sorted([random.expovariate(lam) for i in x])
	cdf_fml = [1-pow(math.e, -lam * i) for i in eX]
	cdf_cal = Cdf.MakeCdfFromList(eX, 'cdf by sum expovariate')

	myplot.plot(eX, cdf_fml, label='cdf by formular')
	myplot.cdf(cdf_cal)
	myplot.show()

	x_baby_interal = getInterval()
	cdf_baby = Cdf.MakeCdfFromList(x_baby_interal, 'cdf of babies')
	myplot.Cdfs([cdf_cal,cdf_baby] , complement=True, yscale='log')

	myplot.show()

if __name__ == '__main__':
	main()