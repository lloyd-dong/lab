#coding=utf-8
from pymongo import MongoClient
from pymongo.collection import ReturnDocument
import sys

if len(sys.argv) < 2:
	print 'usage: %s input_file_name' % sys.argv[0]
	sys.exit(-1)

fileName=sys.argv[1]
	
client = MongoClient('localhost', 27017)   #we could have just done MongoClient() too
cl_raw=client.gene.seq_raw
cl_10=client.gene.seq_gt_10

with open(fileName) as f:
	i,j=0,0
	n_1,n_2=4e+4,50 #every n_1 print a ., print n_2 times, then print next line
	for line in f:
		i +=1
		if i%4==0:
			if i%n_1==0: print '.',
			if i==n_1*n_2: 
				j +=1
				print ' %d m' % (i/(4e+6)*j)
				i=0
			continue
		if i%2!=0:
			continue	
		line = line[:-1] #remove the last \n 
		cnt=cl_raw.find_one_and_update(
			{'_id':line},
			{'$inc':{'cnt':1}},
			projection={'cnt': True, '_id': False},
			upsert=True,
			return_document=ReturnDocument.AFTER)['cnt']
		if  cnt>20: #put most  frequent records in a separate collection
			cl_10.update_one({'_id':line},{'$set':{'cnt': cnt }}, True)

for item in cl_10.find().sort([('cnt',-1)]).limit(20):
		print item
client.close()