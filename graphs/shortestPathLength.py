class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        INF = 10 ** 10
        N = len(graph)
        dp = [[INF]*N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 0
            for neigh in graph[i]:
                dp[i][neigh] = dp[neigh][i] = 1
        

        # floyd-warshall algo
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


        @cache
        def helper(node, visited):
            if(visited == (2**N)-1): return 0
            if(visited & (1 << node)): return INF

            
            cost = INF
            visited = visited | (1 << node) 
            for next in range(N): cost = min(cost, helper(next, visited) + dp[node][next]) 
            visited = visited ^ (1 << node)

            return cost 


        ans = INF
        for src in range(N):ans = min(ans,  helper(src, 0))
        return ans
