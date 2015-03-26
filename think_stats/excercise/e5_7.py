import sys
sys.path.append('..')
import brfss

def main():	
	resp = brfss.Respondents()
    resp.ReadRecords('../data')
    heights = resp.SummarizeHeight()
