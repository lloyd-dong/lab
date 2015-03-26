"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import urllib

import myplot
import Pmf
import Cdf

results = 'http://www.coolrunning.com/results/10/ma/Apr25_27thAn_set1.shtml'

"""
Sample line.

Place Div/Tot  Div   Guntime Nettime  Pace  Name                   Ag S Race# City/state              
===== ======== ===== ======= =======  ===== ====================== == = ===== ======================= 
    1   1/362  M2039   30:43   30:42   4:57 Brian Harvey           22 M  1422 Allston MA              
"""

def ConvertPaceToSpeed(pace):
    """Converts pace in MM:SS per mile to MPH."""
    m, s = [int(x) for x in pace.split(':')]
    secs = m*60 + s
    mph  = 1.0 / secs * 60 * 60 
    return mph


def CleanLine(line):
    """Converts a line from coolrunning results to a tuple of values."""
    t = line.split()
    if len(t) < 6:
        return None
    
    place, divtot, div, gun, net, pace = t[0:6]

    if not '/' in divtot:
        return None

    for time in [gun, net, pace]:
        if ':' not in time:
            return None

    return place, divtot, div, gun, net, pace


def ReadResults(url=results):
    """Read results from coolrunning and return a list of tuples."""
    results = []
    conn = urllib.urlopen(url)
    for line in conn.fp:
        t = CleanLine(line)
        if t:
            results.append(t)
    return results


def GetSpeeds(results, column=5):
    """Extract the pace column and return a list of speeds in MPH."""
    speeds = []
    for t in results:
        pace = t[column]
        speed = ConvertPaceToSpeed(pace)
        speeds.append(speed)
    return speeds


def e3_8(results):
    m5059 = [x for x in results if x[2] == 'M5059']
    speeds_m50 = GetSpeeds(m5059) 
    f2039 = [x for x in results if x[2] == 'F2039']
    speeds_f20 = GetSpeeds(f2039)

    my_cdf = 1- float(26)/256
    my_speed_in_50 = Cdf.MakeCdfFromList(speeds_m50).Value(my_cdf)
    her_speed_in_20 = Cdf.MakeCdfFromList(speeds_f20).Value(my_cdf)
    print '50 speed is %f, her speed should be faster than %f' % (my_speed_in_50,her_speed_in_20)

def relay(results):

    speeds = GetSpeeds(results)
    pmf = Pmf.MakePmfFromList(speeds, 'speeds')
    myplot.Pmf(pmf)

    c= Cdf.MakeCdfFromList(speeds) 
    myplot.Cdf(c)

    myplot.Show(title='PMF of running speed',
               xlabel='speed (mph)',
               ylabel='probability')

def main():
    results = ReadResults()
    e3_8(results)


if __name__ == '__main__':
    main()
