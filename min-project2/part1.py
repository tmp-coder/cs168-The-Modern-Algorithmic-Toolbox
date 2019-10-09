import pandas as pd
import numpy as np

from makeHeatMap import makeHeatMap
from similarity import JaccardSimilarity,L2Similarity,cosSimilarity
from utils import read_data

arts,groupedArts,groups,_ = read_data()

def similarityMatrix(similarityFun):
    mat = np.zeros((len(groupedArts),len(groupedArts)))

    for gid1,groupedVal1 in enumerate(groupedArts):
        for gid2,groupedVal2 in enumerate(groupedArts):
            if gid2 <gid1:
                mat[gid1][gid2] = mat[gid2][gid1]
                continue
            ans = [similarityFun(arts[y1],arts[y2]) for y1 in groupedVal1 for y2 in groupedVal2]
            mat[gid1][gid2] = np.mean(ans)

    return mat

def problemB():
    print("JacardSimilarity:")

    similarityFuns = [JaccardSimilarity,L2Similarity,cosSimilarity]
    
    idx =0
    for fun in similarityFuns:
        mat = similarityMatrix(fun)
        makeHeatMap(mat,groups.values,'heatMap'+str(idx)+'.png' )
        idx += 1

if __name__ == "__main__":
    
    problemB()