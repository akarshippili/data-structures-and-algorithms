class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        N = len(nums)
        counter = collections.Counter()

        ans = 0
        for index1 in range(N):
            for index2 in range(index1):

                '''
                    2, 2, 4, 6
                    (4, 2) = 2
                    (6, 2) = 2
                '''
                delta = nums[index1] - nums[index2]
                ans += counter[(index2, delta)]
                counter[(index1, delta)] += counter[(index2, delta)] + 1
        
        return ans

