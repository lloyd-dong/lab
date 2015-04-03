import random
import sys
sys.path.append('..')
import myplot
import relay
import sample_distribution as sd


def get_sorted_relay_data():
	l = relay.GetSpeeds(relay.ReadResults())
	return sorted(l)

def main():
    l = get_sorted_relay_data()	
    n = len(l)
    xs = sd.samples('normal', n) 
    print n, len(xs)

    myplot.scatter(xs, l,  label='relay')
    myplot.Show()

if __name__ == '__main__':
	main()