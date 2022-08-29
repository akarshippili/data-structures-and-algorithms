class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];
        
        dfs(rooms, 0, visited);
        
        for(boolean x: visited){
            if(!x) return x;
        }
        
        return true;
    }
    
    
    public void dfs(List<List<Integer>> rooms, int cur, boolean[] visited){
        if(visited[cur]) return;
        visited[cur] = true;
        for(int key: rooms.get(cur)){
            dfs(rooms, key, visited);
        }
    }
}
