class Solution
{
    //Function to find sum of weights of edges of the Minimum Spanning Tree.
    static int spanningTree(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj) 
    {
        // Add your code here
        
        boolean[] visited = new boolean[V];
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) ->  o1.distance - o2.distance);
        
        pq.add(new Node(0,0));
        int ans = 0;
        
        while(!pq.isEmpty()){
            Node cur = pq.poll();
            if(visited[cur.val]) continue;
            
            visited[cur.val] = true;
            ans += cur.distance;
            
            for(ArrayList<Integer> neighbour: adj.get(cur.val)){
                if(visited[neighbour.get(0)]) continue;
                pq.add(new Node(neighbour.get(0), neighbour.get(1)));
            }
        }
        
        
        return ans;
        
    }
}


class Node{
    int val;
    int distance;
    
    Node(int val, int distance){
         this.val = val;
         this.distance = distance;
    }
    
    
}
