class Solution {
    
    public int closedIsland(int[][] grid) {
        
        int ans = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==0 && !visited[i][j] && helper(grid,i,j,visited)==false) 
                {
                    // System.out.println(i + " " + j);
                    ans++;
                }
            }
        }
        
        return ans;
    }
    
    public boolean helper(int[][] grid, int sr, int sc, boolean[][] visited){
        if(sr>=0 && sc>=0 && sr<grid.length && sc<grid[0].length){
            if(grid[sr][sc]==1 || visited[sr][sc]) return false;
            visited[sr][sc] = true;
            boolean ans = helper(grid,sr-1,sc,visited);
            ans = helper(grid,sr,sc+1,visited) || ans;
            ans = helper(grid,sr+1,sc,visited) || ans;
            ans = helper(grid,sr,sc-1,visited) || ans;
            return ans;
        } else {
            return true;
        }
    }
    
    
}
