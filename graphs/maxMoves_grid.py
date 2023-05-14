class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        @cache
        def helper(row_index, col_index):
            if(not (0<=row_index and row_index<len(grid) and 0<=col_index and col_index<len(grid[0]))): return 0
            
            ans = 0
            dire = [[-1, 1], [0, 1], [1,1]]
            for dx, dy in dire:
                nx, ny = row_index+dx, col_index+dy
                if(0<=nx and nx<len(grid) and 0<=ny and ny<len(grid[0]) and grid[row_index][col_index]<grid[nx][ny]):
                    sub = 1+helper(nx, ny)
                    ans = max(ans, sub)
            return ans
        
        ans = 0
        for index in range(len(grid)):
            ans = max(ans, helper(index, 0))
        
        return ans
              
