class Solution:

    def getNumOfCombinations(self, mn, mx, index1, index2, start, end):
        if(index1>=len(mn) or index2>=len(mx)): return 0
        mn_idx, mx_idx = min(mn[index1], mx[index2]), max(mn[index1], mx[index2])

        left = mn_idx - start + 1
        right = end - mx_idx
        if(mn_idx == mn[index1]): ans = self.getNumOfCombinations(mn, mx, index1+1, index2, mn[index1]+1, end)
        else: ans = self.getNumOfCombinations(mn, mx, index1, index2+1, mx[index2]+1, end)

        return (left*right) + ans

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        def getSubAns(nums, start, end):
            mn = []
            mx = []
            for i in range(start, end): 
                if(nums[i] == minK): mn.append(i)
                if(nums[i] == maxK): mx.append(i)

            if((len(mn)==0 or len(mx)==0)): return 0
            
            # if we have n minK and m maxK in [start, end)
            # how to get all possible combinations
            return self.getNumOfCombinations(mn, mx, 0, 0, start, end)

        start = 0
        end = 0
        ans = 0 

        while(end<len(nums)):
            while(end<len(nums) and minK<=nums[end]<=maxK): end += 1
            ans += getSubAns(nums, start, end)
            end += 1
            start = end
        
        return ans

class Solution2:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        N = len(nums)
        start_index = end_index = 0
        queue = [[], []]
        ans = 0
        next_ = 0

        while(end_index < N):
            if(minK <= nums[end_index] <= maxK): 
                if(nums[end_index] == minK or nums[end_index] == maxK):
                    if(nums[end_index] == minK): queue[0].append(end_index)
                    if(nums[end_index] == maxK): queue[-1].append(end_index)
                end_index += 1
            else:
                """
                    [start_index, end_index)
                """
                # print(start_index, end_index, queue)
                while(queue[0] and queue[1]):
                    if(queue[0][0] < queue[-1][0]):
                        start = next_
                        while(queue[0] and queue[0][0] < queue[-1][0]): end = queue[0].pop(0)
                        ans += (end_index - queue[-1][0]) * (end - next_ + 1)
                        next_ = end + 1

                    elif(queue[0][0] > queue[-1][0]):
                        start = next_
                        while(queue[-1] and queue[0][0] > queue[-1][0]): end = queue[-1].pop(0)
                        ans += (end_index - queue[0][0]) * (end - next_ + 1)
                        next_ = end + 1

                    else:
                        ans += end_index - queue[0][0]
                        queue[-1].pop(0)
                        queue[0].pop(0)
                
               
                end_index += 1
                start_index = end_index
                next_ = start_index 
                queue = [[], []]
        
        
        while(queue[0] and queue[1]):
            if(queue[0][0] < queue[-1][0]):
                start = next_
                while(queue[0] and queue[0][0] < queue[-1][0]): end = queue[0].pop(0)
                ans += (end_index - queue[-1][0]) * (end - next_ + 1)
                next_ = end + 1

            elif(queue[0][0] > queue[-1][0]):
                start = next_
                while(queue[-1] and queue[0][0] > queue[-1][0]): end = queue[-1].pop(0)
                ans += (end_index - queue[0][0]) * (end - next_ + 1)
                next_ = end + 1

            else:
                ans += end_index - queue[0][0]
                queue[-1].pop(0)
                queue[0].pop(0)
        
        return ans
