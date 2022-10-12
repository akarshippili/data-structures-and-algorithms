class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        
        boolean[] visited = new boolean[friends.length];
        Queue<Integer> queue = new LinkedList<>();
        
        queue.offer(id);
        visited[id] = true;
        int l = queue.size();
        
        
        while(level>0){
            int node = queue.poll();
            l--;
            
            for(int friend: friends[node]) {
                if(visited[friend]) continue;
                queue.offer(friend);
                visited[friend] = true;
            }
            
            if(l==0) {
                l = queue.size();
                level--;
            }
        }
        
        HashMap<String, Integer> map = new HashMap<>();
        for(int x: queue){
            for(String video: watchedVideos.get(x)){
                if(!map.containsKey(video)) map.put(video, 1);
                else map.put(video, map.get(video)+1);
            }
        }
        
        ArrayList<String> ans = new ArrayList<>(map.keySet());
        Collections.sort(ans, (O1, O2) -> (map.get(O1) == map.get(O2)) ? (O1.compareTo(O2)) : (map.get(O1) - map.get(O2)));
        
        return ans; 
    }
}
