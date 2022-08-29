class Solution {
    List<List<Integer>> list = new ArrayList<List<Integer>>();
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {    
        dfs(graph, 0, new ArrayList());
        return list;
    }
    
    public void dfs(int[][] graph, int cur, ArrayList<Integer> path){
        path.add(cur);
        if(cur==graph.length-1){
            list.add((ArrayList<Integer>) path.clone());
        }
        for(int i=0;i<graph[cur].length;i++){
            dfs(graph, graph[cur][i], path);
        }
        path.remove(path.size()-1);
    }
    
}
