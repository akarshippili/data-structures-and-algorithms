class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if(len(trust)==0):
            return 1 if n==1 else -1


        out_graph = {}
        in_graph = {}

        for a, b in trust:
            if a not in out_graph: out_graph[a] = set()
            if(b not in in_graph): in_graph[b] = set()

            out_graph[a].add(b)
            in_graph[b].add(a)
        
        for i in range(1, n+1):
            if(i not in out_graph and (i in in_graph and len(in_graph[i])==n-1)):
                return i
        
        return -1
