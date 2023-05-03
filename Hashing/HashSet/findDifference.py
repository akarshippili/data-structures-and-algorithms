class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_a = set(nums1)
        set_b = set(nums2)
        
        return [[num for num in set_a if(num not in set_b)], [num for num in set_b if(num not in set_a)]]
