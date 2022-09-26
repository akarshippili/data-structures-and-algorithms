class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        passedIndexs = []
        
        for index,equation in enumerate(equations):
            
            if(equation[1] == '!'):
                passedIndexs.append(index)
                continue
                
            char1 = ord(equation[0]) -97
            char2 = ord(equation[-1]) -97
            uf.merge(char1, char2)
        
        for index in passedIndexs:
            char1 = ord(equations[index][0]) -97
            char2 = ord(equations[index][-1]) -97
            
            if(uf.connected(char1, char2)): 
                return False
        
        return True
            

        
        
        
        
class UnionFind:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.idx = [i for i in range(self.capacity)]
        self.sz = [1 for i in range(self.capacity)]
        self.numComponents = self.capacity
        
    def find(self, index):
        rootIndex = index
        while(self.idx[rootIndex]!=rootIndex):
            rootIndex = self.idx[rootIndex]
            
        while(index!=rootIndex):
            curParent = self.idx[index]
            self.idx[index] = rootIndex
            index = curParent
        return rootIndex
    
    def connected(self, index1, index2):
        return self.find(index1) == self.find(index2)
    
    def componentSize(self, index):
        return self.sz[self.find(index)]

    def getNumberOfComponents(self):
        return self.numComponents
    
    def merge(self, index1, index2):
        
        root1 = self.find(index1)
        root2 = self.find(index2)        
        
        if(root1 == root2): return
        
        if(self.componentSize(root1) <= self.componentSize(root2)):
            self.idx[root1] = root2
            self.sz[root2] += self.sz[root1]
        else:
            self.idx[root2] = root1
            self.sz[root1] += self.sz[root2]
            
        self.numComponents -= 1

            
