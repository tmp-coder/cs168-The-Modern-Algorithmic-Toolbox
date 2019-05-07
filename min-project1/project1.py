"""
code for http://web.stanford.edu/class/cs168/p1.pdf

author : Zhitao Zou
"""

import numpy as np


from histgram import plot_histogram

def choice1(n):
    ret = np.zeros(n,dtype=int)

    for _ in range(n):
        rnd = np.random.randint(n)
        ret[rnd]+=1
    
    return ret

def choice2(n):
    ret = np.zeros(n,dtype=int)

    for _ in range(n):
        
        r1 = np.random.randint(n)
        r2 = np.random.randint(n)
        if ret[r1] > ret[r2]:
            r1 = r2
        ret[r1] +=1
    
    return ret

def choice3(n):
    ret = np.zeros(n,dtype=int)

    for _ in range(n):
        
        r1 = np.random.randint(n)
        r2 = np.random.randint(n)
        r3 = np.random.randint(n)

        idx=  [r1,r2,r3]
        val = [ret[r1],ret[r2],ret[r3]]
        r = np.argmin(val)
        ret[idx[r]] +=1
    
    return ret


def choice4(n):
    ret = np.zeros(n,dtype=int)

    for _ in range(n):
        
        r1 = np.random.randint(n//2)
        r2 = np.random.randint(n//2) + n//2
        if ret[r1] > ret[r2]:
            r1 = r2
        ret[r1] +=1
    
    return ret

strategies = [
    lambda n: choice1(n),
    lambda n: choice2(n),
    lambda n: choice3(n),
    lambda n: choice4(n),
]

def problemA(n):
    print("problem A,N = {}".format(n))
    for choice in strategies[1:]:
        bins = choice(n)
        max_num = np.max(bins)
        print(max_num)



def problemB(times):
    N = 200000
    no_choice = 4
    ret = np.zeros((N,4),dtype=int)

    for _ in range(times):
        for i in range(4):
            ans = np.max(strategies[i](N))
            ret[ans - 1,i] +=1 

    return ret

if __name__ == "__main__":
    
    ans = problemB(30)
    print(np.sum(ans, axis = 0))
    plot_histogram(ans)