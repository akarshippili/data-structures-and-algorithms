class Solution {
    
    boolean isInBoundary = false;
    
    public int numEnclaves(int[][] grid) {
        int ans = 0;
        
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1){
                    int cur = dfs(grid, i, j, visited);
                    
                    // System.out.println(i +" " + j + " "+ cur + isInBoundary);
                    
                    if(!isInBoundary) ans+=cur;
                    isInBoundary=false;
                }
            }
        }
        return ans;
    }
        
    public int dfs(int[][] grid, int sr, int sc, boolean[][] visited){
        if(sr>=0 && sc >=0 && sr<grid.length && sc<grid[0].length && grid[sr][sc] == 1 && !visited[sr][sc]){
            if(sr==0 || sc ==0 || sr == grid.length-1 || sc==grid[0].length-1) isInBoundary = true;
            visited[sr][sc] = true;
            return 1 + dfs(grid,sr-1,sc,visited) + dfs(grid,sr,sc+1,visited) + dfs(grid,sr+1,sc,visited) + dfs(grid,sr,sc-1,visited);
        } else {
            return 0;
        }
    }
}
