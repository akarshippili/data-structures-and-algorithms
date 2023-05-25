import collections


class Solution:

    def __init__(self):
        self.stack = set()
        self.ans = 0
        self.cycleDetected = False
        self.graph = None
        self.colors = None
        self.cache = None


    def dfs(self, node):

        if(node in self.stack):
            self.cycleDetected = True 
            return [0 for i in range(26)]

        if(node in self.visited): return self.cache[node]
        
        self.visited.add(node)
        self.stack.add(node)
        nodeVal = ord(self.colors[node]) - 97

        path = [0 for i in range(26)]
        for neigh in self.graph[node]: 
            response = self.dfs(neigh)
            path = self.maxArr(path, response)

        path[nodeVal] += 1
        self.cache[node] = path
        self.ans = max(self.ans, path[nodeVal])                
        self.stack.remove(node)
        return self.cache[node]
    

    def maxArr(self, arr1, arr2):
        for i in range(26):
            arr1[i] = max(arr2[i], arr1[1])
        return arr1

    def largestPathValue(self, colors, edges):

        N = len(colors)

        self.ans = 0
        self.cache = collections.defaultdict(list)
        self.stack = set()
        self.cycleDetected = False
        self.graph = collections.defaultdict(list)
        self.colors = colors
        self.visited = set()

        for source, destination in edges: self.graph[source].append(destination)
        def maximumFrequency(arr): return max(arr)

        for node in range(N):
            if(node not in self.visited):
                self.dfs(node)
                if(self.cycleDetected): return -1
        
        # print(self.cache)
        return self.ans

sol = Solution()
# ans =  sol.largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]])
ans =  sol.largestPathValue("a", [[0,0]])
print(ans)