class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        sub_tree = [0 for i in range(n)]
        distances = [0 for i in range(n)]

        def helper(node, parent):
            ans = 0
            cnt = 1

            for child in graph[node]:
                if(child == parent): continue
                sub_ans, sub_cnt = helper(child, node)
                ans += sub_ans + sub_cnt
                cnt += sub_cnt
            
            distances[node] = ans
            sub_tree[node] = cnt
            return ans, cnt
        
        helper(0, None)
        # print(sub_tree, distances)
        
        ans = [0 for _ in range(n)]
        ans[0] = distances[0]

        def helper2(node, parent):
            if(parent != None):
                # print(f"parent {parent}, node {node} -> ans[parent]: {ans[parent]}, ans[node]: {ans[parent] + (n - sub_tree[node]) - sub_tree[node]}") 
                ans[node] = ans[parent] + (n - sub_tree[node]) - sub_tree[node]
            
            for child in graph[node]:
                if(child == parent): continue
                helper2(child, node)

        helper2(0, None)
        return ans
        # return [list(helper(i, None))[0] for i in range(n)]
