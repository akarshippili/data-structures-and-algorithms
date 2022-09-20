class Solution {

	public int[] shortestPath(int N,int M, int[][] edges) {
		//Code here
		int[] ans = new int[N];
		for(int i=0;i<N;i++) ans[i] = -1;
		
		ArrayList<ArrayList<Edge>> graph = new ArrayList<>();
		
		for(int i=0; i<N;i++) graph.add(new ArrayList<>());
		
		for(int[] edge:edges){
		    graph.get(edge[0]).add(new Edge(edge[0], edge[1], edge[2]));
		}
		
// 		System.out.println(graph);
		
		boolean[] visited = new boolean[N];
		PriorityQueue<Node> queue = new PriorityQueue<>();
		queue.add(new Node(0, 0));
		
		while(!queue.isEmpty()){
		    Node cur = queue.poll();
		    if(visited[cur.val]) continue;
		    
		    visited[cur.val] = true;
		    ans[cur.val] = cur.distance;
		    
		    for(Edge e: graph.get(cur.val)){
		        if(visited[e.dest]) continue;
		        queue.add(new Node(e.dest, cur.distance + e.distance));
		    }
		}
		
		return ans;
	}
}


class Edge {
    int source;
    int dest;
    int distance;
    
    
    public Edge(int source, int dest, int distance){
        this.source = source;
        this.dest = dest;
        this.distance = distance;
    }
    
    public String toString() {
        return this.source  + " " + this.dest + " " + this.distance;
    }
    
}


class Node implements Comparable<Node> {
    int val;
    int distance;
    
    public Node(int val, int distance) {
        this.val = val;
        this.distance = distance;
    }
    
    
    public int compareTo(Node o){
        return this.distance - o.distance;
    }
}
