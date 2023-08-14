class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        N = len(grid)
        M = len(grid[0])

        start = None
        k = 0

        for row_index in range(N):
            for col_index in range(M):
                if(grid[row_index][col_index] == '@'):
                    start = (row_index, col_index)
                elif(grid[row_index][col_index] == '.' or grid[row_index][col_index] == '#' or ord(grid[row_index][col_index]) < 97):
                    continue
                elif('a' <= grid[row_index][col_index] <= 'z'):
                    k += 1
        
        INF = 10**10
        dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]    
        stack = set()
        keys = set()
        best = [INF for _ in range(6)]

        def dfs(node):
            x, y = node
            if(x < 0 or x >= N or y < 0 or y >= M): return [INF for _ in range(6)]
            if(node in stack or grid[x][y] == '#'): return [INF for _ in range(6)]
            if(65 <= ord(grid[x][y]) <= 90 and grid[x][y].lower() not in keys): 
                return [INF for _ in range(6)]
            
            if(97 <= ord(grid[x][y]) <= 122): 
                keys.add(grid[x][y])
            

            ans = [INF for _ in range(6)]
            stack.add(node)
            for dx, dy in dir:
                newx, newy = x + dx, y + dy
                if((newx, newy) in stack): continue
                
                d = dfs((newx, newy))
                for index in range(6): ans[index] = min(ans[index], d[index] + 1) 

            if(97 <= ord(grid[x][y]) <= 122): 
                keys.remove(grid[x][y])
                ans[ord(grid[x][y]) - 97] = 0
            
            stack.remove(node)
            return ans

        ans = sum(dfs(start))
        print(dfs(start))
        return -1 if(ans >= INF) else ans


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        N = len(grid)
        M = len(grid[0])

        start = None
        k = 0

        for row_index in range(N):
            for col_index in range(M):
                if(grid[row_index][col_index] == '@'):
                    start = (row_index, col_index)
                elif(grid[row_index][col_index] == '.' or grid[row_index][col_index] == '#' or ord(grid[row_index][col_index]) < 97):
                    continue
                elif('a' <= grid[row_index][col_index] <= 'z'):
                    k += 1
        
        INF = 10**10
        dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]    
        stack = set()
        keys = set()

        def dfs(node):
            x, y = node
            if(x < 0 or x >= N or y < 0 or y >= M): return {}
            if(node in stack or grid[x][y] == '#'): return {}
            if(65 <= ord(grid[x][y]) <= 90 and grid[x][y].lower() not in keys): return {}
            if(97 <= ord(grid[x][y]) <= 122): keys.add(grid[x][y])
            

            ans = {}
            stack.add(node)
            for dx, dy in dir:
                newx, newy = x + dx, y + dy
                if((newx, newy) in stack): continue
                
                d = dfs((newx, newy))
                for index in d: 
                    if(index in ans):
                        ans[index] = min(ans[index], d[index] + 1)
                    else:
                        ans[index] = d[index] + 1 

            if(97 <= ord(grid[x][y]) <= 122): 
                keys.remove(grid[x][y])
                ans[ord(grid[x][y]) - 97] = 0
            
            stack.remove(node)
            return ans

        ans = sum(dfs(start).values())
        print(dfs(start))
        return -1 if(ans >= INF) else ans