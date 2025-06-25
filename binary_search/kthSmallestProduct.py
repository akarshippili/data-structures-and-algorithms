class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count(target):

            cnt = 0
            for x in nums1:
                if x == 0:
                    if target >= 0:
                        cnt += len(nums2)
                    else:
                        cnt += 0
                elif x > 0:
                    cnt += bisect.bisect_right(nums2, target / x)
                else:
                    index = bisect.bisect_left(nums2, (target) / x)
                    cnt += len(nums2) - index
            
            return cnt


        low = -10 ** 10
        high = 10 ** 10

        while(low < high):
            mid = low + (high - low) //2
            val = count(mid)
            
            # print(mid, val)
            
            if val >= k:
                high = mid
            else:
                low = mid + 1
        
        return low