from abc import ABC, abstractmethod

import numpy as np
import random
class Hash(ABC):
    
    def __init__(self,dataDim,numOfBasedHashFunction = 1):
        """
        Args:

            numOfBasedHashFunction : int, number of based hash function

            dataDim : the length of Vector sample 
        """
        self.numOfBasedHashFunction = numOfBasedHashFunction
        self.dataDim = dataDim
        super().__init__()

    @abstractmethod
    def hash(self,x):
        pass

class RandomHyperplanHash(Hash):
    
    def __init__(self,dataDim,numOfBasedHashFunction=1,seed=1):
        super().__init__(dataDim = dataDim,numOfBasedHashFunction=numOfBasedHashFunction)
        # random.seed(seed)
        self.randomVector = np.random.randn(self.numOfBasedHashFunction,self.dataDim)

    @staticmethod
    def sgn(val):
        hashval = 0
        for e in val:
            hashval |= (1 if e > 0 else 0)
            hashval <<=1
        return hashval


    def hash(self, x):
        if len(x.shape) == 1:
            val = self.randomVector.dot(x)

            return RandomHyperplanHash.sgn(val)
        else:
            vals = x.dot(self.randomVector.T)
            
            hashIds = [ RandomHyperplanHash.sgn(e) for e in vals]
            return hashIds