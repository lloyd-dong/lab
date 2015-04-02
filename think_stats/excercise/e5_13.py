import random
import math
import sys
sys.path.append('..')
import thinkstats
import Cdf

import distribution_test as dt

def patients_per_year(people_n, prob):
    patients = 0
    for i in xrange(people_n):
        if random.random() <= prob:
            patients += 1
    return patients

def process(prob, people, year):    
    patients = 0
    for y in xrange(year):
        patients += patients_per_year(people,prob) 
    return patients

def q1(prob, year, people, n):
    
    results = []
    for i in xrange(n):
        results.append(process(prob,people,year))

    mean,var = thinkstats.MeanVar(results)
    sigma = math.sqrt(var)
    print '''in %d years, in %d people, patients mean %4.2f, 
            percent is %4.2f%%, sigma is %4.2f, cv is %4.3f''' \
            % (year,people,mean, mean/(people*year)*100, sigma, sigma/mean)
    #results.sort()
    #dt.is_expo(results)
    #dt.is_pareto(results)
    #dt.is_normal(results)
    #dt.is_log_normal(results)
    return results

def q2(results):    
    results.sort()
    print results
    cdf = Cdf.MakeCdfFromList(results)
    p = [0.95, 0.99]
    for i in p:
        significant_v = cdf.Value(i)
        print 'p: %4.2f%%, significant case is %d,' % (i, significant_v ),
        #question 3        
        print '%4.2f%% is higher than significant ' %  \
                ((1-cdf.Prob(significant_v))*100)
        
def q4(prob,year):
    row,col =100,100
    patients = [[0]*col for i in xrange(row)]

    def init_partients():
        for i in xrange(row):
            for j in xrange(col):
                patients[i][j] = process(prob,1,year)    
 
    def find_in_block(r,c,block,significant_v):        
        block_p = 0
        for i in xrange(block):            
            block_p += sum(patients[r+i][c:c+block])
            if block_p >= significant_v:
                print r,c
                for ii in range(i+1):
                    print patients[r+ii][c:c+block], i, ii, sum(patients[r+ii][c:c+block])
                print block_p
                return True
        #print block_p
        return False

    def find_sig(significant_v):
        block = 10
        for r in xrange(row-block):
            print 'patients %d in 100 people, 10 years' % (sum(patients[r]))
            for c in xrange(col-block):
                if find_in_block(r,c,block,significant_v):                    
                    return 1
        return 0

    test_n = 1
    results = []
    significant_v = 4
    for n in xrange(test_n):
        init_partients()
        results.append(find_sig(significant_v))
    print results
    print '%4.2f%% prob to find a significat cluster' % (100.0*sum(results)/test_n)


def main():
    prob, year,  = 0.001, 10
    people = 100
    n = 100
    #results = q1(prob, year,people,n)
    #q2(results)
    q4(prob,year)

    
    

if __name__ == '__main__':
    main()