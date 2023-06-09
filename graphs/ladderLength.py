class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = {}
        for index, word in enumerate(wordList): words[word] = index
        if(endWord not in words): return 0

        src = -1
        dest = words[endWord]

        if(beginWord not in words): 
            wordList.append(beginWord)
            src = len(wordList)-1
        else:
            src = wordList.index(beginWord)
        
        N = len(wordList)
        graph = {}
        for index in range(N): graph[index] = set()
        

        # O(N * L * 26) ~ O(N * 260) ~ O((1.3)*10**6)
        for wordIndex in range(N):
            word = wordList[wordIndex]
            for index in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwyz':
                    new = word[:index] + ch + word[index+1:]
                    if(new not in words): continue 
                    node = words[new]
                    graph[wordIndex].add(node)
                    graph[node].add(wordIndex)

        # Make it bidirectional bfs
        def bfs(root, dest):
            queue = [root]
            visited = set()
            visited.add(root)
            l = 1
            depth = 1

            while(queue):
                cur = queue.pop(0)
                l -= 1
                if(cur == dest): return depth 

                for neigh in graph[cur]:
                    if(neigh in visited): continue
                    if(neigh == dest): return depth+1
                    visited.add(neigh)
                    queue.append(neigh)
                
                if(l == 0):
                    l = len(queue)
                    depth += 1
            
            return -1
        
        def biDirectionalBfs(root, dest):
            queue = [(root, 0), (dest, 1)]
            visited = [{}, {}]
            l = 2
            depth = 1

            while(queue):
                cur, parent = queue.pop(0)
                l -= 1
                if(cur in visited[1^parent]): return depth + visited[1^parent][cur] 

                for neigh in graph[cur]:
                    if(neigh in visited[parent]): continue
                    visited[parent][neigh] = depth
                    queue.append((neigh, parent))
                
                if(l == 0):
                    l = len(queue)
                    depth += 1
            
            return -1

        depth = bfs(src, dest)
        if(depth == -1): return 0
        return depth
