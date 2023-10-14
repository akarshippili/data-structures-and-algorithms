class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        N = len(cost)
        cache = {}

        def minCost(index, rem_count):
            if(rem_count <= 0): return 0
            if(index == N): return 10**10

            key = (index, rem_count)
            if(key in cache): return cache[key]
            
            cache[key] = min(cost[index] + minCost(index+1, rem_count - 1 -time[index]), minCost(index+1, rem_count))
            return cache[key]
        
        return minCost(0, N)
        # print(cache)
        # return ans
