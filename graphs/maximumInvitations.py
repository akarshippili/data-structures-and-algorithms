class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        
        N = len(favorite)
        visited = set()
        stack = {}
        ans = 0
        non_loops = 0

        
        graph = defaultdict(set)
        for index, favor in enumerate(favorite): graph[favor].add(index)

        def height(node):
            if(len(graph[node]) == 0): return 1
            return 1 + max(height(child) for child in graph[node])
        
        def dfs(node, depth):
            if(node in stack):
                # found a cycle
                nonlocal ans, non_loops
                
                sub_ans = depth - stack[node]
                if(sub_ans == 2):
                    graph[node].remove(favorite[node])
                    graph[favorite[node]].remove(node)

                    val = height(node)-1 + height(favorite[node])-1 
                    sub_ans += val
                    non_loops += (2 + val)

                    graph[node].add(favorite[node])
                    graph[favorite[node]].add(node)

                ans = max(ans, sub_ans)
                return
            
            if(node in visited): return

            visited.add(node)
            stack[node] = depth
            dfs(favorite[node], depth + 1)
            del stack[node]
        
        for node in range(N): dfs(node, 0)
        ans = max(ans, (non_loops))

        return ans
