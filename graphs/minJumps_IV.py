class Solution:
    def minJumps(self, arr: List[int]) -> int:

        graph = collections.defaultdict(list)
        for index, val in enumerate(arr):
            graph[val].append(index)

        queue = [0]
        size = len(queue)
        depth = 0
        visited = [False for i in range(len(arr))]

        while(queue):
            cur = queue.pop(0)
            size -= 1

            if(cur == len(arr)-1): return depth

            if(cur+1<len(arr) and not visited[cur+1]): 
                queue.append(cur+1)
                visited[cur+1] = True

            if(cur-1>=0 and not visited[cur-1]): 
                queue.append(cur-1)
                visited[cur+1] = True

            for idx in graph[arr[cur]]: 
                if(not visited[idx]):
                    queue.append(idx)
                    visited[idx] = True
            
            graph[arr[cur]] = []



            if(size == 0):
                size = len(queue)
                depth += 1
