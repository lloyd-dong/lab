# exercise 2-4
import Pmf
def RemainingLifetime(pmf, t):
	r = {}
	for k, v in pmf.Items():
		if (k <t):
			continue
		r[k] = v
	result=Pmf.MakePmfFromDict(r)
	#d = {30:0.8, 40:0.2}
	return result

p = [5,5,10,20,20,30,30,30,30,40]
all_people_pmf = Pmf.MakePmfFromList(p)


r= RemainingLifetime(all_people_pmf,25)

expected={30:0.8, 40:0.2}
for k,v in r.Items():
	assert v== expected[k]
