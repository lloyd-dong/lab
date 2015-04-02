import skewness as sk
import e_babies as eb

def main():
	baby_1st, baby_rest, babies = eb.partition_babies()

	l_wt = eb.get_wight_list(babies)
	sk.show_skewness(l_wt,'weight')

	l_preg = eb.get_pregnacy_list(babies)
	sk.show_skewness(l_preg,'pregnancy')
	

if __name__ == '__main__':
	main()