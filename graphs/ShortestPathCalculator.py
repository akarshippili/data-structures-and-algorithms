class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        
        self.N = n
        self.edges = edges
        self.graph = collections.defaultdict(list)

        for src, dest, weight in self.edges: self.graph[src].append([dest, weight])

    def addEdge(self, edge: List[int]) -> None:
        self.edges.append(edge)
        self.graph[edge[0]].append([edge[1], edge[-1]])

    def shortestPath(self, node1: int, node2: int) -> int:
        
        src = node1
        dest = node2
        if(src == dest): return 0

        visited = [None for _ in range(self.N)]
        heap = [[0, src]]
        heapify(heap)

        while(heap):
            weight, cur = heappop(heap)
            if(cur == dest): return weight

            visited[cur] = weight
            for neigh, dis in self.graph[cur]:
                if(visited[neigh] != None): continue
                heappush(heap, [weight + dis, neigh])
        
        return -1







# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
