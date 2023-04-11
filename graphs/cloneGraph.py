"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(not node): return

        mapper = {}
        def dfs(node):
            if(node.val in mapper): return mapper[node.val]

            new_node = Node(node.val, [])
            mapper[new_node.val] = new_node
            for neigh in node.neighbors: new_node.neighbors.append(dfs(neigh))
            return mapper[new_node.val] 
        
        dfs(node)
        return mapper[node.val]
