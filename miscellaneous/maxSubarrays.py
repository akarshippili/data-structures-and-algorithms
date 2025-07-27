class Node:
    def __init__(self, val):
        self.val = val
        self.count = 0
        self.next = None

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
        
        index = 0

        """
            [A B] [C D]
            -----------A--------B-----C---D-->
                val            ^
                        val              ^ 
            
            [A C] [B D]
            -----------A--------B-----C---D-->
            -----------A             ^
                        ^                ^

            [A C] [B D]
            -----------A--------B-----D---C-->
            -----------A             ^
                        ^                ^

        """
        
        lookup = defaultdict(int)
        seMapping = defaultdict(set)
        esMapping = {}
        start, end = [], []
        for s, e in conflictingPairs:
            s, e = min(s, e), max(s, e)
            start.append([s, e])
            end.append(e)
            lookup[e] += 1
            seMapping[s].add(e)
            esMapping[e] = e
        
        start.sort()
        end.sort()


        def updateEND():
            if not end: return
            while(end and lookup[end[0]] == 0):
                end.pop(0)

        done = set()
        all_  = 0

        val = 1
        index = 0

        while(val < n + 1):
            if start and val == start[0][0]:
                
                if val not in done: all_ += end[0] - val
                #print(val, start, end, end[0] - val)
                
                done.add(val)
                _, end_ = start.pop(0)
                lookup[end_] -= 1
                updateEND()

                val += 1
                if start: val = min(start[0][0], val)
                continue

            if end:
                #print(val, start, end, end[0] - val)
                all_ += end[0] - val
            else:
                #print(val, start, end, n - val + 1)
                all_ += n - val + 1
            
            val += 1
            if start: val = min(start[0][0], val)
        
        #print(all_)
        #print("-"*100)


        ans = all_
        done = set()
        lookup = defaultdict(int)
        seMapping = defaultdict(set)
        esMapping = {}
        start, end = [], []
        for s, e in conflictingPairs:
            s, e = min(s, e), max(s, e)
            start.append([s, e])
            end.append(e)
            lookup[e] += 1
            seMapping[s].add(e)

            if e in esMapping: esMapping[e] = max(s, esMapping[e])
            else: esMapping[e] = s
        
        start.sort()
        end.sort()

        buffer = defaultdict(int)
        val = 1

        list_ = Node(1)
        temp = list_
        cur = 2
        while(cur < n+1):
            temp.next = Node(cur)
            cur += 1
            temp = temp.next


        while(val < n + 1):
            if start and val == start[0][0]:
                
                #print(start, end)
                
                if val not in done:

                    end_ = end[0]
                    edge = (esMapping[end_], end_)

                    nextEnd = n+1
                    index = 1

                    while(index < len(end)):
                        # if lookup[end[index]] == 0 or end[index] == end[0]:
                        if lookup[end[index]] <= 0 or (lookup[end[index]] == 1 and end[0] == end[index]):
                            index += 1
                        else:
                            nextEnd = end[index]
                            break 
                        
                    buffer[edge] += nextEnd - end_
                    #print(val, edge, nextEnd, buffer[edge], lookup)


                done.add(val)
                _, end_ = start.pop(0)
                lookup[end_] -= 1
                updateEND()

                
                # done.add(val)
                # for x in seMapping[val]: lookup[x] -= 1
                # start_ = start.pop(0)
                # updateEND()
                val += 1
                if start: val = min(start[0][0], val)
                continue

            if end and lookup[end[0]] == 1:
                #print(start, end)
                nextEnd = n+1
                index = 1

                while(index < len(end)):
                    if lookup[end[index]] <= 0 or (lookup[end[index]] == 1 and end[0] == end[index]):
                        index += 1
                    else:
                        nextEnd = end[index]
                        break

                edge = (esMapping[end[0]], end[0])
                buffer[edge] += nextEnd - end[0]
                #print(val, edge, nextEnd, buffer[edge], lookup)

            val += 1
            if start: val = min(start[0][0], val)

        #print(start, end)         
        return ans + max(buffer.values())
        



