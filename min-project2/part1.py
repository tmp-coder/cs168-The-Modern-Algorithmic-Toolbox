import pandas as pd
import numpy as np

from makeHeatMap import makeHeatMap

dataPath = 'p2_data/'


def read_data():
    groupFilePath = dataPath + 'groups.csv'
    dataFilePath = dataPath + 'data50.csv'
    labelFilePath = dataPath +'label.csv'
    
    group = pd.read_csv(groupFilePath,header=None)
    rawData = pd.read_csv(dataFilePath,header=None).values
    labels = pd.read_csv(labelFilePath,header=None)

    artMat = np.zeros((rawData[:,0].max(),rawData[:,1].max()))
    groupedArticles = [ values for values in labels.groupby(0).groups.values()]

    for artId,wordId,count in rawData:
        artMat[artId - 1][wordId -1] = count


    return artMat,groupedArticles,group



def JaccardSimilarity(y1,y2):
    
    mi = np.min([y1,y2],axis=0)
    ma = np.max([y1,y2],axis=0)

    return np.sum(mi)/np.sum(ma)

def L2Similarity(y1,y2):
    return -np.linalg.norm(y1-y2)

def cosSimilarity(y1,y2):
    return y1.dot(y2) / (np.linalg.norm(y1) * np.linalg.norm(y2))


arts,groupedArts,groups = read_data()

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