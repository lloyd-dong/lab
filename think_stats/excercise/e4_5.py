""" alpha is about 0.77 (1/1.3) - 1.7
"""
import sys
sys.path.append('..')
import Cdf
import myplot

def read_word_count():
	path = '/Users/bodong/Documents/lab/aws/AWS_word_count_output/'
	file_name = ['part-00000','part-00001','part-00002']
	l = []
	for n in file_name:
		f = file(path+n,'r')
		for i, line in enumerate(f):
			l.append(int(line.split()[1]))
		f.close()	
	return l

def main():
	l = read_word_count()
	cdf = Cdf.MakeCdfFromList(l)
	myplot.Cdf(cdf, complement=True, label='word count')
	myplot.Config(yscale='log', xscale='log')
	myplot.Show()

if __name__ == '__main__':
	main()