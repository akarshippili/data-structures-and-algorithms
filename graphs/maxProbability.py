class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        graph = defaultdict(list)
        for [src, dest], prob in zip(edges, succProb):
            graph[src].append([dest, prob])
            graph[dest].append([src, prob])

        heap = []
        heapify(heap)
        heappush(heap, (1, start))
        visited = [False for _ in range(n)]

        while(heap):
            prob, node =  heappop(heap)
            if(visited[node]): continue
            visited[node] = True
            
            if(node == end): return 1/prob
            for child, p in graph[node]:
                if(visited[child]): continue 
                heappush(heap, (prob * 1/p, child))
        
        return 0
