import random
import sys
sys.path.append('..')
import thinkstats

def ask():
    q = {0:0,1:1,2:2,3:3,4:4,5:5}
    a = guess(q)
    return q, a 

def guess(q):
    return random.choice(q.keys())

def process(method='5_4'):
    q,a= ask()
    guessed = guess(q)
    #print a, guessed ,
    is_correct = (guessed == a) 

    def open_door_5_4():  
        # change after open a wrong door, prob raise from 1/n to 1/(n-1)
        del q[guessed]  # get left iterms
        while True:
            b = random.choice(q.keys())
            if a==b: continue
            del q[b] # remove another wrong answer, i.e. open a wrong door
            break
        return random.choice(q.keys())          
    
    def open_door_5_5():
        del q[guessed]
        b = random.choice(q.keys())
        if b == a: return -1 # means you losed
        del q[b]
        return random.choice(q.keys())

    open_door=eval('open_door_'+method)
    return is_correct, open_door() == a


def main():
    n = 10000    
    methods = ['5_4', '5_5']
    for m in methods:
        change_rate, unchange_rate = [], []  
        for i in xrange(n):
            unchange_correct,change_correct = process(m)
            change_rate.append(change_correct)
            unchange_rate.append(unchange_correct)
        print '%s: change rate is %f, unchange is %f' % \
              ( m, thinkstats.Mean(change_rate), thinkstats.Mean(unchange_rate))

if __name__ == '__main__':
    main()
    

    