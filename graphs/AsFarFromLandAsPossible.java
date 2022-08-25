class Point{
    
    public  int x;
    public int y;
    
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public int maxDistance(int[][] grid) {
        
        Queue<Point> queue = new LinkedList<>();
        int[][] dir = {
            {-1,0},{0,1},{1,0},{0,-1}
        };
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1) { 
                    queue.add(new Point(i,j));
                    visited[i][j] = true;
                }
            }
        }
        
        int ans = 0;
        int l = queue.size();
        
        if(l== ( grid.length)*(grid[0].length)) return -1;
        
        while(!queue.isEmpty()){
            
            Point cur = queue.poll();
            l--;
            
            for(int i=0;i<4;i++){
                int[] k = dir[i];
                int newRow = cur.x + k[0];
                int newCol = cur.y + k[1];
                if(newRow>=0 && newCol>=0 && newRow<grid.length && newCol< grid[0].length &&   !visited[newRow][newCol]){
                    queue.add(new Point(newRow, newCol));
                    visited[newRow][newCol] = true;
                }
            }
            
            if(l==0) {
                ans++;
                l = queue.size();
            }
            
        }
        return ans-1;
    }
}
