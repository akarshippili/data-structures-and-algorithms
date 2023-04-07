class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        ans = 0
        N = len(grid)
        M = len(grid[0])

        def dfs(row, col):
            if(row<0 or col<0 or row>=N or col>=M): return True, 0 
            if(grid[row][col] == -1 or grid[row][col] == 0): return False, 0

            grid[row][col] = -1

            onEdge = False
            ans = 1

            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nx, ny = row + dx, col + dy
                a, b = dfs(nx, ny)
                onEdge = onEdge or a
                ans += b
            
            return onEdge, ans

        
        ans = 0
        for row_index in range(N):
            for col_index in range(M):
                if(grid[row_index][col_index] == 1):
                    onEdge, count = dfs(row_index, col_index)
                    if(not onEdge): ans += count

        return ans 
