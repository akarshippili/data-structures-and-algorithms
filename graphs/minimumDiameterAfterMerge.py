class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def tree(edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            
            return tree

        tree1 = tree(edges1)
        tree2 = tree(edges2)

        def diameter1(node, parent):
            best1, best2 = 0, 0
            best_diameter = 0

            for next_ in tree1[node]:
                if next_ == parent: continue

                height, diameter = diameter1(next_, node)
                if height >= best1: best1, best2 = height, best1
                elif height > best2: best2 = height
                best_diameter = max(best_diameter, diameter)
            
            return best1 + 1, max(best_diameter, best1 + best2)
        
        def diameter2(node, parent):
            best1, best2 = 0, 0
            best_diameter = 0

            for next_ in tree2[node]:
                if next_ == parent: continue

                height, diameter = diameter2(next_, node)
                if height >= best1: best1, best2 = height, best1
                elif height > best2: best2 = height
                best_diameter = max(best_diameter, diameter)
            
            return best1 + 1, max(best_diameter, best1 + best2)

        _, dia1 = diameter1(0, None)
        _, dia2 = diameter2(0, None)
        return max(dia1, dia2, (dia1 + 1)//2 + (dia2 + 1)//2 + 1)
