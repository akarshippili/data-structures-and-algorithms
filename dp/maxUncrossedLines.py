class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def helper(index1, index2):
            if(index1 >= len(nums1) or index2>=len(nums2)): return 0

            if(nums1[index1] == nums2[index2]): return 1+helper(index1+1, index2+1)
            
            ans = -1 * 10**10
            ans = max(ans, helper(index1+1, index2))
            ans = max(ans, helper(index1, index2+1))
            return ans

        return helper(0, 0)
