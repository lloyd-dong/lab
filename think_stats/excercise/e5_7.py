import random
import sys
sys.path.append('..')
import brfss
import thinkstats

def main(): 
    resp = brfss.Respondents()
    resp.ReadRecords('../data')
    heights = resp.SummarizeHeight()

    n_pairs, result = 1000, []
    man_n, lady_n = len(heights[1]), len(heights[2])
    for i in xrange(n_pairs):
        man_h = heights[1][random.randint(0,man_n)]
        lady_h = heights[2][random.randint(0,lady_n)]
        result.append(lady_h > man_h)

    expect = thinkstats.Mean(result)*100
    print 'lady higher than man is %4.2f%%' % (expect)

if __name__ == '__main__':
        main()    


