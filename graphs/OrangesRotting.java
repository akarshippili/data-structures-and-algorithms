class Solution {
    public int orangesRotting(int[][] grid) {
        
        Queue<CoOrdinate> queue = new LinkedList<>();
        int count = 0;
        
        for(int i=0;i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j] == 2) queue.add(new CoOrdinate(i,j));
                if(grid[i][j] == 1) count++;
            }
        }
        
        
        int size = queue.size();
        int level = 0;
        int[][] dir = new int[][]{
            {-1,0},
            {0,1},
            {1,0},
            {0,-1}
        };
        
        
        while(!queue.isEmpty()){
            
            // System.out.println(queue);
            // System.out.println(level);
            
            CoOrdinate cur = queue.poll();
            size--;
            
            for(int[] x: dir){
                int dx = cur.x + x[0];
                int dy = cur.y + x[1];
                
                if(dx<0 || dy<0 || dx>=grid.length || dy>=grid[0].length || grid[dx][dy]!=1 ) continue;
                
                queue.add(new CoOrdinate(dx, dy));
                grid[dx][dy] = 2;
                count--;
            }
            
            
            if(size==0 && queue.size()>0){
                size = queue.size();
                level++;
            }
        }
        
        return count == 0 ? level : -1;
        
    }
}


class CoOrdinate{
    int x;
    int y;
    
    CoOrdinate(int x, int y){
        this.x = x;
        this.y = y;
    }
    
    
    public String toString(){
        return this.x + " " + this.y; 
    }
    
}
