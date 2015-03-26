# exercies  2-3
import Pmf
from operator import itemgetter
import matplotlib.pyplot as pyplot

def Mode(h):
	max_freq, max_freq_val = 0.0, 0.0
	for val, freq in h.Items():
		if freq > max_freq:
			max_freq = freq
			max_freq_val = val
	return max_freq_val, max_freq

def AllModes(h):
	r=[]
	for val, freq in h.Items():
		r.append((val, freq))

	r2=sorted(r, key=itemgetter(1), reverse=1)
	return [ k for (k,v) in r2 ]
	#return [6,4,1]

list1 = [1,6,4,4,6,6]

h = Pmf.MakeHistFromList(list1)

mode, freq = Mode(h)
allModes = AllModes(h)


assert mode==6 and freq == 3
assert allModes == [6,4,1]
vals, freqs = h.Render()
rectoangles = pyplot.bar(vals, freqs)
pyplot.show()
