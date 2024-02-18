from sortedcontainers import SortedSet

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        N = len(meetings)
        meetings.sort()
        counter = [0 for _ in range(n)]
        s = SortedSet([index for index in range(n)])
        # print(s[0])
        heap = []


        index = 0
        while(index < N):

            start, _ = meetings[index]
            while(heap and heap[0][0] <= start): 
                _, room = heappop(heap)
                s.add(room)


            if(len(heap) < n):
                counter[s[0]] += 1
                val = s.pop(index = 0) 
                heappush(heap, [meetings[index][-1], val])
                index += 1
                continue
            
            end, room = heappop(heap)
            counter[room] += 1
            diff = meetings[index][-1] - meetings[index][0]
            heappush(heap, [end + diff, room])
            index += 1
        

        best = counter[0]
        bestIndex = 0
        for index in range(n):
            if(counter[index] > best):
                best = counter[index]
                bestIndex = index

        # print(counter)
        return bestIndex



class SolutionV2:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        N = len(meetings)
        meetings.sort()
        counter = [0 for _ in range(n)]
        heap = []
        
        # no need for sorted set we can do with heap
        s = [index for index in range(n)]
        heapify(s)


        index = 0
        while(index < N):

            start, _ = meetings[index]
            while(heap and heap[0][0] <= start): 
                _, room = heappop(heap)
                heappush(s, room)


            if(len(heap) < n):
                counter[s[0]] += 1
                val = heappop(s) 
                heappush(heap, [meetings[index][-1], val])
                index += 1
                continue
            
            end, room = heappop(heap)
            counter[room] += 1
            diff = meetings[index][-1] - meetings[index][0]
            heappush(heap, [end + diff, room])
            index += 1
        

        best = counter[0]
        bestIndex = 0
        for index in range(n):
            if(counter[index] > best):
                best = counter[index]
                bestIndex = index

        return bestIndex
