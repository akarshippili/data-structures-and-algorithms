class Group:
  def __init__(self):
    self.members = set()
  
  def __str__(self):
    return 'Group: { ' + str(self.members) + " }"

class Solution:
    def __init__(self):
      self.stack = []

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

      groupMap = {}
      nodeToGrp = [None for _ in range(n)]
      grpcnt = m

      for node, grp in enumerate(group):
        if(grp == -1): 
          grp = grpcnt
          grpcnt += 1
        
        if grp not in groupMap: groupMap[grp] = Group()
        groupMap[grp].members.add(node)
        nodeToGrp[node] = grp
      
      def build(grp_id):
        graph = {}
        members = groupMap[grp_id].members
        for mem in members: graph[mem] = set()

        for node in members:
          for dep in beforeItems[node]:
            if(dep not in members): continue
            graph[dep].add(node)
        
        return graph

      # for grp in groupMap: print(grp, groupMap[grp])

      graph = defaultdict(set)
      for grp in groupMap:
          for node in groupMap[grp].members:
              for dep_items in beforeItems[node]:
                if(nodeToGrp[dep_items] == grp): continue
                graph[nodeToGrp[dep_items]].add(grp)
          
          if(grp not in graph): graph[grp] = set()
      
      # print(graph)
      if(not self.topologicalsort(graph)): return []
      topo_sorted_grp = self.stack[::-1]
      # print(topo_sorted_grp)

      ans = []
      for grp in topo_sorted_grp:
        grh = build(grp)
        if(not self.topologicalsort(grh)): return []
        ans += self.stack[::-1]

      return ans

    
    def topologicalsort(self, graph):
      self.stack = []
      visited = set()
      instack = set()

      def dfs(node):
        if(node in instack): return False
        if(node in visited): return True

        # print(node)

        visited.add(node)
        instack.add(node)

        for neigh in graph[node]:
          if(not dfs(neigh)):
            instack.remove(node) 
            return False
        
        self.stack.append(node)
        instack.remove(node)         
        return True
      
      for node in graph: 
        if(not dfs(node)): return False

      return True
