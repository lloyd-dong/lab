'''
5-8:
	1/6 + 1/6 - 1/6*1/6 = 11/36

	first time: 1      2      3      4      5      6
	second time:123456 123456 123456 123456 123456 123456
	= (5 + 6)/36 

5_9:
	P(A or B) = P(A) + P(B)

5_10: as the following
'''

def main():
	numerators = xrange(51,100,2)
	denominator = [i * 8 for i in xrange(1,26)]

	fraction = 1.0
	for i,v in enumerate(numerators):
		fraction *= float(v)/denominator[i]

	print fraction * 100  #7.96%

if __name__ == '__main__':
	main()