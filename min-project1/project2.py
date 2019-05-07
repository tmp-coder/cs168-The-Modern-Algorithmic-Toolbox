import numpy as np

import math

from cms import SimpleUpdateCMS,ConservativeUpdateCMS

# problem contants

max_value = 9050
ratio = .01


def generate_seq():
    
    for i in range(9050):

        t = i // 1000
        e = i +1
        if t >=9:

            t = e % 9000
            t *= t
            while t >0:
                yield e
                t -=1
        else:
            while t >=0:
                yield e
                t -= 1

data = list(generate_seq())



def haevy_hitters(streams):
    """
    exact ans for heavy_hitter problem
    """
    min_frq = math.ceil(len(streams) * ratio)

    counters = np.zeros(max_value+5,dtype=int)

    for e in streams:
        counters[e] +=1

    return np.sum(counters >= min_frq
    )



def epsilon_heavy_hitters(streams,cms_generator,trails):
    
    """

    a fake method for e-heavy hitter problem, know the length ,not use min-heap, not same as lecture note

    only for test cms

    return: number of heavy hitters
    cms_generator: test for different update stratage
    """

    cms_counter = cms_generator(trails)

    min_frq = math.ceil(ratio * len(streams))
    # print("min frq :",min_frq)
    heavy_set = set()

    for e in streams:
        if e in heavy_set:
            # print("{0} : {1}".format(e,cms_counter.frq(e)))
            continue
        cnt = cms_counter.add_element(e)
        if cnt >= min_frq:
            heavy_set.add(e)
    
    # print("heavy hitters: {0}".format(heavy_set))
    # print("9050 : {0}".format(cms_counter.frq(9050)))
    return len(heavy_set)


def testC(streams,cms_generator,trails=10):
    
    ret = 0

    cnt9050 =0
    for i in range(trails):
        number= epsilon_heavy_hitters(streams,cms_generator,i)
        ret += number

        mycms = cms_generator(i)
        mycms.initWithSteam(streams)
        cnt9050 += mycms.frq(9050)

    print("avg hitters :{0}, 9050 frq :{1}".format(ret /trails,cnt9050/trails))

def problemC(cmsgenerator):

    

    print("Forward: non-decreasing")
    testC(data,cmsgenerator)

    x = data
    x.reverse()
    print("Reverse: non-increasing")
    testC(x,cmsgenerator)

    print("random")
    tmp = data
    np.random.shuffle(tmp)
    testC(tmp,cmsgenerator)




if __name__ == "__main__":
    
    # print("problem b : {0}".format(haevy_hitters(data))) # 21, 9030,...,9050

    print("problem c :")

    problemC(SimpleUpdateCMS)

    """
    output : 

    Forward: non-decreasing
    avg hitters :22.0, 9050 frq :2577.2
    Reverse: non-increasing
    avg hitters :21.2, 9050 frq :2500.0
    random
    avg hitters :21.2, 9050 frq :2500.0
    """