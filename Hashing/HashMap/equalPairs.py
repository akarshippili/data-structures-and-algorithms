class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        map = defaultdict(int)
        for row in range(N): map[tuple(grid[row])] += 1

        ans = 0    
        for row_index in range(N):
            for col_index in range(row_index+1, N):
                grid[row_index][col_index], grid[col_index][row_index] = grid[col_index][row_index], grid[row_index][col_index]
            ans += map[tuple(grid[row_index])]
        
        return ans
