class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        N = len(bombs)
        def inRange(index1, index2):
            x1, y1, r1 = bombs[index1]
            x2, y2, r2 = bombs[index2]
            dis = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
            return dis <= r1
        
        graph = defaultdict(list)
        for index1 in range(N):
            for index2 in range(N):
                if(index1 != index2 and inRange(index1, index2)): 
                    graph[index1].append(index2)
        
        
        stack = set()
        def dfs(index):
            if(index in stack): return
            stack.add(index)
            for child in graph[index]: dfs(child)


        ans = 0
        for index1 in range(N):
            stack = set()
            dfs(index1)
            ans = max(ans, len(stack))
        
        return ans
