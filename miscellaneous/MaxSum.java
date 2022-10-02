class Solution {
    public int maxSum(int[][] grid) {
        int ans = 0;
        for(int i=0; i<grid.length-2; i++){
            for(int j=0; j<grid[0].length-2;j++){
                ans = Math.max(ans, getValue(grid, i, j));
            }
        }
        return ans;
    }
    
    public int getValue(int[][] grid, int index1, int index2){
        return grid[index1][index2] + grid[index1][index2+1] + grid[index1][index2+2] + 
            grid[index1+1][index2+1] + 
            grid[index1+2][index2] + grid[index1+2][index2+1] + grid[index1+2][index2+2];
    }
}
