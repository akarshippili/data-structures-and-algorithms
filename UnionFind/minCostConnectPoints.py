class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        def distance(p1, p2):
          x1, y1 = p1
          x2, y2 = p2

          return abs(x1 - x2) + abs(y1 - y2)

        N = len(points)
        edges = []

        for index1 in range(N):
          for index2 in range(index1+1, N):
            if(index1 == index2): continue
            edges.append([distance(points[index1], points[index2]), index1, index2])
        
        edges.sort(key = lambda x: x[0])
        
        ans = 0
        uf = UnionFind(N)
        for dis, p1, p2 in edges:
          if(not uf.connected(p1, p2)):
            ans += dis
            uf.merge(p1, p2)
        
        return ans
