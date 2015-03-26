import random
import sys
sys.path.append('..')
import myplot
import relay

def sample_normal_xs(n=1000):
    return sorted([random.normalvariate(0.0, 1.0) for i in xrange(n)])

def get_sorted_relay_data():
	l = relay.GetSpeeds(relay.ReadResults())
	return sorted(l)

def main():
    l = get_sorted_relay_data()	
    n = len(l)
    xs = sample_normal_xs(n)
    print n, len(xs)

    myplot.scatter(xs, l,  label='relay')
    myplot.Show()

if __name__ == '__main__':
	main()