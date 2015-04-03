import sys
sys.path.append('..')
import Cdf
import brfss

def main():
    resp = brfss.Respondents()
    resp.ReadRecords('../data')     
    l_height = [r.htm3 for r in resp.records if r.htm3 != 'NA' and r.sex==1]
    cdf = Cdf.MakeCdfFromList(l_height)
    #p_178, p_185 = cdf.Prob(178), cdf.Prob(185)
    print p_185, p_178
    print '%4.2f%% men are qualified' % ((p_185 - p_178)*100)

if __name__ == '__main__':
    main()