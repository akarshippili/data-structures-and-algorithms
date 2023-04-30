class UnionFind:

    def __init__(self, size):
        self.size = size
        self.componentSize = [1 for i in range(size)]
        self.id = [i for i in range(size)]
        self.numberOfComponents = size
    

    def getNumberOfComponents(self): return self.numberOfComponents
    
    def find(self, index):
        temp = index
        while(self.id[index] != index): index = self.id[index]

        
        # path compression
        while(self.id[temp] != index):
            temp = self.id[temp]
            self.id[temp] = index 
        
        return index

    def getComponentSize(self, index): return self.componentSize(self.find(index))
    def areConnected(self, index1, index2): return self.find(index1) == self.find(index2)

    def merge(self, index1, index2):
        if(self.areConnected(index1, index2)): return

        root1 = self.find(index1)
        root2 = self.find(index2)

        if(self.componentSize[root1] >= self.componentSize[root2]): 
            self.id[root2] = root1
            self.componentSize[root1] += self.componentSize[root2]
        else: 
            self.id[root1] = root2
            self.componentSize[root2] += self.componentSize[root1]
        
        self.numberOfComponents -= 1
    
    def clone(self):
        new = UnionFind(self.size)
        new.componentSize = [i for i in self.componentSize]
        new.id = [i for i in self.id]
        new.numberOfComponents = self.numberOfComponents

        return new


class Solution:
    def numSimilarGroups(self, strs):

        N = len(strs)
        uf = UnionFind(N)


        def similar(s1, s2):
            count = 0
            
            for ch1, ch2 in zip(s1, s2):
                if(ch1 != ch2): 
                    count += 1
                    if(count>2): return False
            
            return True

        for index1 in range(N):
            for index2 in range(index1+1, N):
                if(similar(strs[index1], strs[index2]) and not uf.areConnected(index1, index2)):
                    uf.merge(index1, index2) 
        
        return uf.getNumberOfComponents()