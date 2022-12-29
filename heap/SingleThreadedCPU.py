class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        def scheduleTask(heap, t, ans):
            taskProcesstingTime, index = heappop(heap)
            t += taskProcesstingTime
            ans.append(index)
            return t

        new = []
        for index,task in enumerate(tasks):
            task.append(index)
            new.append(task)
        tasks = new
    
        tasks.sort(key=lambda x:(x[0]))
        index = 0
        N = len(tasks)

        t = 1
        heap = []
        heapify(heap)
        ans = []

        while(index<N):
            # tasks whose enqueue time is less than equal to t 
            # add them to pq
            while(index<N and tasks[index][0]<=t):
                heappush(heap, [tasks[index][1], tasks[index][2]])
                index += 1
            
            if(heap): t = scheduleTask(heap, t, ans)
            else: t = tasks[index][0]
        
        while(heap): t = scheduleTask(heap, t, ans)

        return ans



