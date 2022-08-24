class Solution {
    
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int ans = 0;
        boolean[][] visited = new boolean[grid1.length][grid1[0].length];
        
        for(int i=0;i<grid2.length;i++){
            for(int j=0;j<grid2[0].length;j++){
                if(grid2[i][j]==1 && !visited[i][j] && dfs(grid1, grid2, i, j, visited)) {
                    ans += 1;
                }
            }
        }
        
        return ans;
    }
    
    public boolean dfs(int[][] grid1, int[][] grid2, int sr, int sc, boolean[][] visited){
        if(sr>=0 && sc>=0 && sr<grid1.length && sc<grid1[0].length && grid2[sr][sc]==1 && !visited[sr][sc]){
            visited[sr][sc] = true;
            
            boolean isSubIsland = true;
            if(grid1[sr][sc]==0) isSubIsland = false;
            
            isSubIsland =  dfs(grid1, grid2, sr-1, sc, visited) && isSubIsland;
            isSubIsland =  dfs(grid1, grid2, sr, sc+1, visited) && isSubIsland;
            isSubIsland =  dfs(grid1, grid2, sr+1, sc, visited) && isSubIsland;
            isSubIsland =  dfs(grid1, grid2, sr, sc-1, visited) && isSubIsland;
            
            return isSubIsland;
        } else {
            return true;
        }
    }
    
}
