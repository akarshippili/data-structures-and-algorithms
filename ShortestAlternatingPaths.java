class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        
        ArrayList<Edge>[] graph = new ArrayList[n];
        int[] ans = new int[n];
        Queue<Node> queue = new LinkedList<>();
        
        for(int i=0;i<n;i++) {
            ans[i] = -1;
            graph[i] = new ArrayList<>();
        }

        
        
        for(int i=0;i<redEdges.length;i++){
            graph[redEdges[i][0]].add(new Edge(redEdges[i][0], redEdges[i][1], 0));
        }
        
        for(int i=0;i<blueEdges.length;i++){
            graph[blueEdges[i][0]].add(new Edge(blueEdges[i][0], blueEdges[i][1], 1));
        }
        
        // System.out.println(Arrays.toString(graph));
        
        
        queue.add(new Node(0,-1));
        int l = queue.size();
        int level = 0;
        
        while(!queue.isEmpty()){
            
            Node cur = queue.poll();
            l--;
            if(ans[cur.vtx]==-1) ans[cur.vtx] = level;
            
            for(Edge edge : graph[cur.vtx]){
                if(edge.visited==true) continue;
                
                if(cur.pathColor == 1 && edge.color==0){ queue.add(new Node(edge.end, 0)); edge.visited = true;}
                if(cur.pathColor == 0 && edge.color==1){ queue.add(new Node(edge.end, 1)); edge.visited = true;}
                if(cur.pathColor==-1){ queue.add(new Node(edge.end, edge.color)); edge.visited = true;}
            }
            
            if(l==0){
                // System.out.println(Arrays.toString(graph));
                // System.out.println(queue);
                l = queue.size();
                level++;
            }
        }
        
        return ans;
    }
}

class Node{
    int vtx;
    int pathColor;
    
    Node(int vtx, int pathColor){
        this.vtx = vtx;
        this.pathColor = pathColor;
    }
    
    public String toString(){
        return this.vtx + " " + this.pathColor;
    }
    
}

class Edge{
    
    int start;
    int end;
    int color;
    boolean visited;
    
    Edge(int start, int end, int color){
        this.start = start;
        this.end = end;
        this.color = color;
        this.visited = false;
    }
    
    
    public String toString(){
        return this.start + " " + this.end + " " +this.color + " "+ this.visited;
    }
}
