class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
      
        n = len(isConnected)
        uf = UnionFind(n)
        for index1 in range(n):
            for index2 in range(index1+1, n):
                if(isConnected[index1][index2]==1):
                    uf.merge(index1, index2)
        
        return uf.getNumberOfComponents()
