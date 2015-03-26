class WrongCase:
	""" this is a wrong case, it doesn't retrieve score by percentile, 
	instead it retrieves percentileRank by score. 
	I didn't pay close attention to the requirement carefully
	"""
	d = {}

	def MakePercentileRank(scores):
		count=pre_score=0
		total_n = len(scores)
		scores.sort()
		for score in scores:
			count +=1
			d[score] = float(count)/total_n * 100
			# 100.0 * count/total_n, then float() is unneccesary
	def Percentile(scores, percentile_rank):
		if len(d) ==0:
			MakePercentileRank(scores)
		return d[percentile_rank]

import math
def PercentileSelect(scores, percentile_rank):
	right_pos = int(math.ceil(len(scores) * percentile_rank))-1
	for i in range(right_pos):
		min_pos=i		
		for j in range(i+1, len(scores)):			
			if scores[j] < scores[min_pos]:
				min_pos = j
		if min_pos != i:
			scores[i],scores[min_pos] = scores[min_pos],scores[i]
	return scores[right_pos]


scores = [55, 66, 77, 88, 99]
score_rank = 0.84
print PercentileSelect(scores,score_rank)
