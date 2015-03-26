import sys
sys.path.append('..')
import erf

def main():
    IQs = [100, 115, 130, 145]
    mu, delta = 100, 15
    for iq in IQs:
        print "IQ> %d prob is %f%% " % (iq, (1-erf.NormalCdf(iq, mu, delta))*100) 
    people=6*1000*1000*1000* (1-erf.NormalCdf(mu + 6*delta, mu, delta))
    print 'high IQ is %d' % (people)  #5 people

if __name__ == '__main__':
	main()