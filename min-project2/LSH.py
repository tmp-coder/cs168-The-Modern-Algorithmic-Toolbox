from collections import defaultdict
from hash_function import RandomHyperplanHash
from multiprocessing import Pool

hashs = {
    "rhp":RandomHyperplanHash,
}

class LSH(object):
    
    def __init__(self,dataDim,b,r,hash_function="rhp"):
        
        self.hashs = [hashs[hash_function](dataDim,b) for _ in range(r)]
        self.hashTables = [defaultdict(list) for _ in range(r)]
        self.__b__ = b
        self.__r__ = r

    def putVector(self,vec,id):
        """
        Args:
            id : index of vec
            vec: np.array, a sample vector
        """
        for i in range(self.__r__):
            hashv = self.hashs[i].hash(vec)
            self.hashTables[i][hashv].append(id)
    
    def putMat(self,mat):
        def subTask(i):
            hashvs = self.hashs[i].hash(mat)
            for j,e in enumerate(hashvs):
                assert hashvs[j] is not None,"j"
                self.hashTables[i][hashvs[j]].append(j)
        pool = Pool(16)
        pool.map(subTask,range(self.__r__))

    
    def get(self,vec):
        """
        return:
            the n baket that vec map to
        """
        return [self.hashTables[i].get(self.hashs[i].hash(vec)) for i in range(self.__r__)]