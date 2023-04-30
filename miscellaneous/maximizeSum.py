class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        def sumOfn(num): return (num * (num+1))//2
        
        m = max(nums)
        return sumOfn(m+k-1) - sumOfn(m-1)
