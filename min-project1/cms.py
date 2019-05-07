import numpy as np

from hashlib import md5

class CMS(object):
    
    def __init__(self,trails):
        self.no_counter = 256
        self.no_table = 4
        self.magic = str(trails)

        self.cms = np.zeros((self.no_table,self.no_counter),dtype = int)
    

    def generate_hash(self,element):
        element = str(element) + str(self.magic)
        hashCode = md5(element.encode('utf-8')).hexdigest()

        ret = [int(hashCode[i*2:i*2+2],16) for i in range(self.no_table)]
        return ret
    def add_element(self, element,frq=1):
        
        hash_values = self.generate_hash(element)

        self.add_forhash(hash_values,frq)

        return self.frq_forhash(hash_values)

    def frq_forhash(self,hash_values):
        
        ret = self.cms[0][hash_values[0]]
        for i in range(1,self.no_table):
            ret = min(ret,self.cms[i][hash_values[i]])

        return ret
    
    def frq(self,element):
        
        hash_table = self.generate_hash(element)
        return self.frq_forhash(hash_table)

    def initWithSteam(self,streams):
        for e in streams:
            self.add_element(e)

    def add_forhash(self,hash_values,frq = 1):
        """
        compare diff implementation
        """
        raise NotImplementedError

class SimpleUpdateCMS(CMS):
    
    def add_forhash(self,hash_values,frq = 1):
        for i,e in enumerate(hash_values):
            self.cms[i][e] += frq

class ConservativeUpdateCMS(CMS):
    
    def add_forhash(self,hash_values,frq = 1):
        
        upper= self.frq_forhash(hash_values) + frq

        # just update the counters with lowest count
        for i, e in enumerate(hash_values):
            if self.cms[i][e] + frq <= upper:
                self.cms[i][e] = upper
