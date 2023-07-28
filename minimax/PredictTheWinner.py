class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def helper(startIndex, endIndex):
            if(startIndex > endIndex): return 0

            return max(
                nums[startIndex] - helper(startIndex+1, endIndex), 
                nums[endIndex] - helper(startIndex, endIndex-1)
                )

        
        return helper(0, len(nums)-1) >= 0
