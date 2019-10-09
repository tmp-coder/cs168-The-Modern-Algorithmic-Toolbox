import pandas as pd
import numpy as np

dataPath = 'p2_data/'


def read_data():
    """
    return:

    artMat : np.array []x[], art_i is feature vector of art_i
    grouped_arts : grouped[i]: articles in grouped_i
    group: i -> name, (20,)
    label : articleId -> group,shape(1000,)
    """
    groupFilePath = dataPath + 'groups.csv'
    dataFilePath = dataPath + 'data50.csv'
    labelFilePath = dataPath +'label.csv'
    
    group = pd.read_csv(groupFilePath,header=None)
    rawData = pd.read_csv(dataFilePath,header=None).values
    labels = pd.read_csv(labelFilePath,header=None)

    artMat = np.zeros((rawData[:,0].max(),rawData[:,1].max()))
    groupedArticles = [ values for values in labels.groupby(0).groups.values()]
    labels = labels.values.squeeze() -1
    for artId,wordId,count in rawData:
        artMat[artId - 1][wordId -1] = count

    assert max(labels) < len(groupedArticles),"index should based on 0"
    return artMat,groupedArticles,group,labels
