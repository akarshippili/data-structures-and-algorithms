class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        M = len(grid[0])
        visited = [[False]*M for i in range(N)]
        
        def dfs(row, col):
            if(row<0 or row>=N or col<0 or col>=M or visited[row][col] or grid[row][col] == 0): return 0
            
            visited[row][col] = True
            ans = grid[row][col]
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                newx, newy = row+dx, col+dy
                ans += dfs(newx, newy)
            
            return ans
        
        ans = 0
        for index1 in range(N):
            for index2 in range(M):
                if(not visited[index1][index2] and grid[index1][index2]!=0):
                    sub_ans = dfs(index1, index2)
                    ans = max(ans, sub_ans)
        
        return ans
        
        
