import e_babies as eb

import random
import sys
sys.path.append('..')
import thinkstats
import Cdf


def resample(pool, n):
    return [random.choice(pool) for i in xrange(n)]

def mean_diff(l1, l2):
    return thinkstats.Mean(l1) - thinkstats.Mean(l2)

def generate_diff_list(pool, len1,len2, iter_times=1000):
    md_l = []
    for i in xrange(iter_times):
        sample_1 = resample(pool, len1)
        sample_2 =resample(pool,len2)
        md = mean_diff(sample_1, sample_2)
        md_l.append(md)
    return md_l

def p_value(first, others, pool):
    md_1_others = abs(mean_diff(first, others))
    print 'mean diff 1st and others: %4.2f' % (md_1_others)
    
    md_l = generate_diff_list(pool,len(first), len(others))     
    cdf_md = Cdf.MakeCdfFromList(md_l, 'sample mean diff')    
    p_value = cdf_md.Prob(-md_1_others) + (1 - cdf_md.Prob(md_1_others))
    return p_value

def p_value_weigtht(babies):
    w_l = [eb.get_wight_list(baby) for baby in babies]
    p = p_value(w_l[0],w_l[1],w_l[2])
    print 'wight p value: %4.2f%%' % (p*100)

def length_p_value(babies):
    length_l = [eb.get_pregnacy_list(baby) for baby in babies] 
    p = p_value(length_l[0],length_l[1],length_l[2])
    print 'length p value: %4.2f%%' % (p*100)

def reduced_sample(babies):
    print '7 - 2'
    reduce_rates = [2,4]
    for r in reduce_rates:
        reduced = [random.sample(babies[0], len(babies[0])/r), \
                   random.sample(babies[1], len(babies[1])/r)]
        reduced.append(reduced[0]+reduced[1])
        print r,': ', 
        p_value_weigtht(reduced)    
def bayes(s1, s2, pool, cross_validation=False):
    if cross_validation:
        p1_1, p1_2 = partition(s1)
        p2_1, p2_2 = partition(s2)
        pool = p1_2 + p2_2
    

def main(): 
    ''' [0]list of 1st, [1] is others, [2] is all'''
    babies = eb.partition_babies()
    p_value_weigtht(babies)
    #length_p_value(babies)
    #reduced_sample(babies)
       
if __name__ == '__main__':
    main()