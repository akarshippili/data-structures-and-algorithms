class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        M = len(grid[0])
        dir_ = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ones = sum(sum(i) for i in grid)
        if(ones == 1): return 1
        if(ones == 0): return 0
        
        def connected():
            visited = set()

            def helper(x, y):
                if(0 > x or x >= N or 0 > y or y >= M): return
                if((x, y) in visited): return
                if(grid[x][y] == 0): return
                
                visited.add((x,y))
                for dx, dy in dir_:
                    helper(x + dx, y + dy)
            
            cnt = 0
            for x in range(N):
                for y in range(M):
                    if(grid[x][y] == 1 and (x, y) not in visited):
                        helper(x, y)
                        cnt += 1
                    
                    if(cnt >= 2): return False

            return cnt < 2

        if(not connected()): return 0

        for x in range(N):
            for y in range(M):
                if(grid[x][y] == 1):
                    grid[x][y] = 0
                    if(not connected()): return 1
                    grid[x][y] = 1

        return 2
