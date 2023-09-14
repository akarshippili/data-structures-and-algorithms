class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        nodes = set()
        graph = {}
        
        for src, dest in tickets:
          if(src not in graph):graph[src] = {}
          if(dest not in graph[src]): graph[src][dest] = 0
          
          graph[src][dest] += 1
          nodes.add(src)
          nodes.add(dest)
        
        nodes = list(nodes)
        nodes.sort()

        print(graph)

        stack = []
        def helper(node):
          stack.append(node)
          
          for neigh in nodes:
            if node not in graph or neigh not in graph[node]: continue
            graph[node][neigh] -= 1
            if(graph[node][neigh] == 0): del graph[node][neigh]
            if(len(graph[node]) == 0): del graph[node]

            if(helper(neigh)): return True

            if(node not in graph): graph[node] = {}
            if(neigh not in graph[node]): graph[node][neigh] = 0
            graph[node][neigh] += 1
          
          if(len(graph) == 0): return True

          stack.pop()
          return False


        helper("JFK")
        return stack
