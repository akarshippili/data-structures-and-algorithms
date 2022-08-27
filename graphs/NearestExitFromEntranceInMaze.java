class Point{
    int x;
    int y;
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}



class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        Queue<Point> queue = new LinkedList<>();
       
        visited[entrance[0]][entrance[1]] = true;
        queue.add(new Point(entrance[0],entrance[1]));
        
        
        int ans = 0;
        int l = queue.size();
        int[][] dir = {
            {-1,0},{0,1},{1,0},{0,-1}
        };
        
        while(!queue.isEmpty()){
            Point cur = queue.poll();
            l--;
            
            if(ans==0){}
            else if(cur.x==0 || cur.y ==0 || cur.x == maze.length-1 || cur.y== maze[0].length-1) return ans;
            
            for(int index = 0;index<4;index++){
                int newx = cur.x + dir[index][0];
                int newy = cur.y + dir[index][1];
                
                if(newx>=0 && newy>=0 && newx<maze.length && newy<maze[0].length && !visited[newx][newy] && maze[newx][newy]=='.'){
                        visited[newx][newy] = true;
                        queue.add(new Point(newx, newy));
                }
                
            }
            
            
            if(l==0){
                l = queue.size();
                ans++;
            }
        }
        
        
        return -1;
    }
}
