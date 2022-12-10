from heapq import heappush,heappop,heapify

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        N = len(vals)
        graph = [[] for i in range(N)]
        
        for edge in edges:
            heappush(graph[edge[0]], -1 * vals[edge[1]])
            heappush(graph[edge[1]], -1 * vals[edge[0]])
        
        
        ans = -10 ** 10
        for i in range(N):
            temp = k
            curSum = vals[i]
            heap = graph[i]
            ans = max(ans, curSum)
            
            
            while(temp>0 and len(heap)>0):
                curSum += -1 * heappop(heap)
                ans = max(ans, curSum)
                temp-=1
        
        return ans
