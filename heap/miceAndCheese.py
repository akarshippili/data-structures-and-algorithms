class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        N = len(reward1) 
        heap = []
        heapify(heap)
        visited = [False for i in range(N)]
        ans = 0
        
        for index, [rewarda, rewardb] in enumerate(zip(reward1, reward2)):
            heappush(heap, [rewardb-rewarda, index])
        
        while(k>0):
            diff, index = heappop(heap)
            visited[index] = True
            ans += reward1[index]
            k-=1
        
        for index in range(N):
            if(not visited[index]): ans += reward2[index]
        
        return ans
        
