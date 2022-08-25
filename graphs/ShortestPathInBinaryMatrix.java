class Point{
    public int x;
    public int y;
    
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
    
    public String toString(){
        return x+" "+y;
    }
}


class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
     
        Queue<Point> queue = new LinkedList<Point>();
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int[][] dir = {
            {-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}
        }; 
        int ans = 1;        
        
        if(grid[0][0]==1) return -1;
        queue.add(new Point(0,0));
        visited[0][0] = true;
        
        int l = queue.size();
        while(!queue.isEmpty()){
            
            // System.out.println(queue);
            
            Point cur = queue.poll();
            l--;
            
            if(cur.x == grid.length-1 && cur.y==grid[0].length-1){
                return ans;
            }
            
            for(int i=0;i<8;i++){
                int newRow = cur.x + dir[i][0];
                int newCol = cur.y + dir[i][1];
                
                if(newRow>=0 && newCol>=0 && newRow<grid.length && newCol<grid[0].length && !visited[newRow][newCol] && grid[newRow][newCol]==0){
                    queue.add(new Point(newRow, newCol));
                    visited[newRow][newCol] = true;
                }
                
            }
            
            if(l==0){
                ans++;
                l = queue.size();
            }
        }
        
        
        return -1;        
    }
}
