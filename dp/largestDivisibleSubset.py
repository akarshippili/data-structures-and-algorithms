class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        N = len(nums)

        dp = {index: [nums[index]] for index in range(N)}
        best_comp = dp[0] 
        best = len(best_comp)

        for index in range(N-1, -1, -1):
            for num_index in range(index+1, N):
                if(nums[num_index] % nums[index] == 0 and len(dp[num_index]) + 1 > len(dp[index])):
                    comp = dp[num_index]
                    new_comp = comp[::]
                    new_comp.append(nums[index])
                    dp[index] = new_comp
            

            if(len(dp[index]) > best): best, best_comp = len(dp[index]), dp[index]

        return best_comp
