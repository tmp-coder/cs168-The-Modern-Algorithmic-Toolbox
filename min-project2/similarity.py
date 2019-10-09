import numpy as np

def JaccardSimilarity(y1,y2):
    
    mi = np.min([y1,y2],axis=0)
    ma = np.max([y1,y2],axis=0)

    return np.sum(mi)/np.sum(ma)

def L2Similarity(y1,y2):
    return -np.linalg.norm(y1-y2)

def cosSimilarity(y1,y2):
    return y1.dot(y2) / (np.linalg.norm(y1) * np.linalg.norm(y2))
