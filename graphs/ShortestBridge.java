class Point{
    int x;
    int y;
    
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
    
    public String toString(){
        return x + " " + y;
    }
}


class Solution {
    
    boolean[][] visited;
    Queue<Point> queue = new LinkedList<>();
        
    
    public int shortestBridge(int[][] grid) {
        
        this.visited = new boolean[grid.length][grid[0].length];
            
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j] == 1){
                    dfs(grid,i,j);
                    i = grid.length;
                    j = grid[0].length;
                }
            }
        }
        
        // System.out.println(queue);
        
        int ans = 0;
        int l = queue.size();
        int[][] dir = {
            {-1,0},{0,1},{1,0},{0,-1}
        };
        
        while(!queue.isEmpty()){
            Point cur = queue.poll();
            l--;
            
            for(int i=0;i<4;i++){
                int sr = cur.x + dir[i][0];
                int sc = cur.y + dir[i][1];
                
                if(sr>=0 && sc>=0 && sr<grid.length && sc<grid[0].length && !visited[sr][sc]){
                    if(grid[sr][sc]==1) return ans;
                    else{
                        visited[sr][sc] = true;
                        queue.add(new Point(sr,sc));
                    }
                }
                
            }
            
            
            if(l==0){
                l=queue.size();
                ans++;
            }
        }
        
        return ans;
        
    }
    
    
    public void dfs(int[][] grid, int sr, int sc){
        if(sr>=0 && sc>=0 && sr<grid.length && sc<grid[0].length && !visited[sr][sc] && grid[sr][sc]==1){
            
            queue.add(new Point(sr,sc));
            visited[sr][sc] = true;
            
            dfs(grid, sr-1, sc);
            dfs(grid, sr, sc+1);
            dfs(grid, sr+1, sc);
            dfs(grid, sr, sc-1);
            
        }
    }
    
    
}
