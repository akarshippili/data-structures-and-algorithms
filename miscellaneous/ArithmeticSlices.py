class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        def getVal(num):
            num+=1
            if(num<3): return 0
            else: return (num * num)//2 - (3*num)//2 + 1
        
        N = len(nums)
        if(N<3): return 0
        
        prevdiff = nums[1] - nums[0]
        curCount = 1
        ans = 0
        
        for index in range(2, N):
            diff  = nums[index] - nums[index-1]
            if(diff == prevdiff): 
                curCount += 1
            else:
                # print(curCount)
                ans += getVal(curCount) #something with cur count
                curCount = 1
            
            prevdiff = diff
        
        # print(curCount)
        ans += getVal(curCount)
        return ans
