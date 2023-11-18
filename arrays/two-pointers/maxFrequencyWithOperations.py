class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        nums.sort()
        
        ans = 1
        start, end = 0, 1
        cur_len = 1
        cur_cost = 0

        while(start < N):
            
            while(end < N and cur_cost + (cur_len) * (nums[end] - nums[end-1]) <= k):
                cur_cost += (cur_len) * (nums[end] - nums[end-1])
                cur_len += 1
                end += 1
                ans = max(ans, cur_len)

            cur_cost -= (nums[end-1]-nums[start])
            cur_len -= 1
            start += 1

        return ans
