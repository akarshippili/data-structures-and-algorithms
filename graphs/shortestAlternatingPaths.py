class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        rgraph = defaultdict(list)
        bgraph = defaultdict(list)

        for src,dest in redEdges: rgraph[src].append(dest)
        for src,dest in blueEdges: bgraph[src].append(dest)
        print(rgraph, bgraph)

        heap = []
        ans = [-1 for i in range(n)]
        rvisited = [False for i in range(n)]
        bvisited = [False for i in range(n)]    
        for node in rgraph[0]: heap.append([node, 1])
        for node in bgraph[0]: heap.append([node, 0])
        dis = 1
        l = len(heap)

        rvisited[0] = True
        bvisited[0] = True
        ans[0] = 0

        # print(heap)
        while(heap):
            node, prevColor = heap.pop(0)
            l -= 1

            if(prevColor == 1):
                visited, nvisited = rvisited, bvisited
                graph = bgraph
            else:
                visited, nvisited = bvisited, rvisited
                graph = rgraph
            
            # print(node, prevColor, dis, ans)
            visited[node] = True

            if(ans[node] == -1): ans[node] = dis
            for neigh in graph[node]:
                if(nvisited[neigh]): continue
                heap.append([neigh, 1 ^ prevColor])

            if(l == 0):
                l = len(heap)
                dis += 1

        return ans

