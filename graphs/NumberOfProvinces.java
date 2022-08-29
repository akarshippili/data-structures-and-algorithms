class Solution {
    public int findCircleNum(int[][] isConnected) {
        boolean[] visited = new boolean[isConnected.length];
        int ans = 0;
        for(int i=0; i<isConnected.length;i++){
            if(!visited[i]){
                ans++;
                dfs(isConnected, i, visited);
            }
        }
        
        return ans;
    }
    
    
    
    public void dfs(int[][] isConnected, int cur, boolean[] visited){
        if(visited[cur]) return;
        visited[cur] = true;
        for(int i=0;i<isConnected.length;i++){
            if(isConnected[cur][i]==1){
                dfs(isConnected, i, visited);
               }
        }
    }
}
