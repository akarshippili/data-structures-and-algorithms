class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if(source == target): return 0

        # node to in_routes map
        graph = collections.defaultdict(set)
        for index, route in enumerate(routes):
            for node in route:
                graph[node].add(index) 
                
        route_graph = collections.defaultdict(set)
        for index in range(len(routes)):
            for node in routes[index]:
                for route in graph[node]:
                    route_graph[index].add(route)
            route_graph[index].remove(index)
        
        
        queue = []
        visited = set()
        depth = 1

        for route in graph[source]:
            queue.append(route)
            visited.add(route)

        l = len(queue)

        while(queue):
            cur_route = queue.pop(0)
            l -= 1

            if(cur_route in graph[target]): return depth
    
            for neigh_route in route_graph[cur_route]:
                if(neigh_route in visited): continue

                visited.add(neigh_route)
                queue.append(neigh_route)
            
            if(l == 0):
                depth += 1
                l = len(queue)

        return -1

class Solution:
  def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
      if S==T:
          return 0
      l = len(routes)
      routes = list(map(set,routes))
      graph = collections.defaultdict(set)
      
      
      
      for index,r1 in enumerate(routes):
          for j in range(index+1,l):
              
              if any(r in routes[j] for r in r1):             
                  graph[index].add(j)
                  graph[j].add(index)
      
      
      target = set()
      start = set()
      for index,route in enumerate(routes):
          if T in route:
              target.add(index) 
          if S in route:
              start.add(index)
  
      #ans = 0
      
      queue = [(i,1) for i in start]
      
      while(len(queue)>0):
          bus,dis = queue.pop(0)
          
          #print(bus,dis)
          
          start.add(bus)
          if bus in target:
              return dis
          for nextBus in graph[bus]:
              if nextBus not in start:
                  queue.append((nextBus,dis+1))
      
      return -1
