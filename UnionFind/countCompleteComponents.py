class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        uf = UnionFind(n)
        for source, dest in edges: uf.merge(source, dest)
        
        def sumOfN(n): return (n*(n-1))//2
        count = 0
        for index in range(n):
            if(uf.idx[index] == index):
                ec = 0
                for ne in range(n):
                    if(uf.connected(index, ne)):
                        ec += len(graph[ne])
                
                x = uf.componentSize(index)
                if(ec//2 == sumOfN(x)): count+=1
        
        return count
        
