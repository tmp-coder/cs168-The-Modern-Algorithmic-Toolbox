import pandas as pd
import numpy as np

from similarity import cosSimilarity,JaccardSimilarity,L2Similarity
from utils import read_data

arts,groupedArts,groups,label = read_data()

NO_ARTS = 1000
NO_GROUPS = 20

def stupidNN(docId,metricFunc):
    bestArts = -1
    metricVal = -np.inf

    for (i,e) in enumerate(arts):
        if i == docId:
            continue
        v = metricFunc(e,arts[docId])
        if v > metricVal:
            metricVal = v
            bestArts = i
    
    return bestArts

def get_allNN(metric = cosSimilarity):
    """
    compute a vec : (1000,),nn[i] : the nn of ith article 
    """
    noArts = 1000

    nn = [stupidNN(docV,metric) for docV in arts]

    return np.array(nn)

def base_classfier(nn=None):
    """
    for problem a,compute a matrix : 20x20,(A,B), # articles in A that has there nn in B
    """
    if nn is None:
        nn = get_allNN()
    noGroups = len(groupedArts)
    mat = np.array((noGroups,noGroups),dtype=np.int)

    noMisClassfications = 0
    for i in range(noGroups):
        for j in range(noGroups):
            mat[i,j] = sum([label[nn[e]] == j for e in groupedArts[i]])
            if i != j:
                noMisClassfications += mat[i,j]
    return mat, noMisClassfications / NO_ARTS

def randomProjection(mat,noBais):
    n,k = mat.shape
    baseMat = np.random.randn(k,noBais)

    return mat.dot(baseMat)