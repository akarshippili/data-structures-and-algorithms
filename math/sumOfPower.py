class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        
        ans = 0
        N = len(nums)
        mod = 10**9 + 7
        nums.sort() 

        def mul(a, b): return (a%mod * b%mod)%mod
        def sum(a, b): return (a%mod + b%mod)%mod

        cur = 0
        for index in range(N):
            cur = mul(cur, 2)
            if(index-1>=0): cur = sum(cur, nums[index-1])
            ans = sum(ans, nums[index] ** 3)
            ans = sum(ans, nums[index]**2 * cur)

        return ans


sol = Solution()
arr = [1 for i in range(10**5)]
ans = sol.sumOfPower(arr)
print(ans)