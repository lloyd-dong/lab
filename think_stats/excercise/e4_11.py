"""This program runs about 1 min, the log scatter looks a very good stright line
"""

import math
import sys
sys.path.append('..')
import brfss
import myplot
import sample_distribution as sd

def get_sorted_weights():
    resp = brfss.Respondents()
    resp.ReadRecords('..')
    l = [r.weight2 for r in resp.records if r.weight2 != 'NA']
    l.sort()
    return l, len(l)

def main():
    weights, n = get_sorted_weights()
    xs = sd.samples('normal', n) 
    myplot.scatter(xs, weights, label='normal')

    log_w = [math.log(w) for w in weights]
    myplot.scatter(xs, log_w, color='red', label='log normal')

    myplot.show()

if __name__ == '__main__':
    main()