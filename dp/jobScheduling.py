class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        arr = []
        N = len(startTime)
        for index, start in enumerate(startTime):
            arr.append([start, index])
        
        arr.sort(key=lambda x:x[0])

        def getNext(startIndex, val):
            low = startIndex
            high = len(startTime)

            while(low < high):
                mid = low + (high - low)//2
                if(arr[mid][0] >= val):
                    high = mid
                else:
                    low = mid + 1
            
            return low

        @cache
        def helper(index):
            if(index == N): return 0

            ans = 0
            
            # take
            nextIndex = getNext(index, endTime[arr[index][-1]])
            ans = max(ans, profit[arr[index][-1]] + helper(nextIndex))

            # not take
            ans = max(ans, helper(index+1))
            
            return ans
        
        return helper(0)
