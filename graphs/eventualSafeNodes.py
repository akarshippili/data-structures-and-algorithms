class Solution:
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        N = len(graph)
        visited = [False for _ in range(N)]
        isSafe = [None for _ in range(N)]
        stack = set()

        def dfs(node):
            if(node >= N): return False
            
            if(len(graph[node]) == 0):
                visited[node] = True
                isSafe[node] = True
                return True
            
            if(visited[node]):
                if(node in stack): return False 
                return isSafe[node]

            stack.add(node)
            visited[node] = True
            ans = True
            
            for neigh in graph[node]: 
                ans = ans and dfs(neigh)
            
            isSafe[node] = ans
            stack.remove(node)
            return ans
        
        for index in range(N):
            if(not visited[index]): dfs(index)
        
        # print(isSafe)
        return [i for i in range(N) if(isSafe[i])]


