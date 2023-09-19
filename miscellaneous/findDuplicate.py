class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        index = 0
        N = len(nums)

        while(index < N):
            val = nums[index]
            if(nums[val-1] != val): nums[val-1], nums[index] = nums[index], nums[val-1]
            else: index += 1
        
        print(nums)
        return nums[-1]
