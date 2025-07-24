from collections import defaultdict
from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        
        N = len(nums)
        parentMap = {}
        xor = {}
        edgesMap = [set() for _ in range(N)]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def traverse(node, parent):
            xor[node] = nums[node]
            parentMap[node] = parent

            for child in graph[node]:
                if child == parent: continue

                traverse(child, node)
                xor[node] ^= xor[child]
                edgesMap[node].add((node, child))
                for edge in edgesMap[child]: edgesMap[node].add(edge)

        traverse(0, None)
        total = xor[0]
        directedEdges = list(edgesMap[0])
        L = len(directedEdges)

        """
        11 --- 1011
        4 ---- 0100
        5 -----0101
        xor ---1010 -- 10
        """

        ans = 10 ** 10
        for index1 in range(L):
            for index2 in range(index1+1, L):
                edge1, edge2 = directedEdges[index1], directedEdges[index2]
                u1, v1 = edge1
                u2, v2 = edge2

                if edge2 in edgesMap[v1]: 
                    one, two = xor[v1], xor[v2]
                    rem = total ^ one 
                    one ^= two
                elif edge1 in edgesMap[v2]:
                    one, two = xor[v1], xor[v2]
                    rem = total ^ two 
                    two ^= one
                else:
                    one, two = xor[v1], xor[v2]
                    rem = total ^ one ^ two
                
                mx, mn = max(one, two, rem), min(one, two, rem)
                ans = min(ans, mx - mn)

        return ans