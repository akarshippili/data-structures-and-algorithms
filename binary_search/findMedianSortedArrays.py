def getMedian(arr):
    n = len(arr)
    if(n%2 == 1): return arr[n//2]
    return (arr[(n-1)//2] + arr[n//2])/2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        N, M = len(nums1), len(nums2)
        total = N + M
        if(N == 0): return getMedian(nums2)
        elif(M == 0): return getMedian(nums1)


        low = 0
        high = N
        while(low <= high):
            left1 = low + (high - low)//2
            right1 = N - left1            
            left2 = (total+1)//2 - left1
            right2 = M - left2


            if(left2 < 0):
                high = left1-1
                continue
            elif(left2 > M):
                low = left1 + 1
                continue

            if(
                (left1 <= 0 or left1 > N  or left2 < 0 or left2 >= M or nums1[left1-1] <= nums2[left2]) 
                and 
                (left1 < 0 or left1 >= N  or left2 <= 0 or left2 > M or nums1[left1] >= nums2[left2-1] )
            ): 
                if(total%2 == 1): return max(nums1[left1-1] if(0 <= left1-1 < N) else -10**10, nums2[left2-1] if(0 <= left2-1 < M) else -10**10)
                return (
                    max(nums1[left1-1] if(0 <= left1-1 < N) else -10**10, nums2[left2-1] if(0 <= left2-1 < M) else -10**10) + 
                    min(nums1[left1] if(0 <= left1 < N) else 10**10, nums2[left2] if(0 <= left2 < M) else 10**10)
                ) / 2

            elif(left1-1 >= 0 and left2 < M and nums1[left1-1] > nums2[left2]): high = left1-1
            elif(left2-1>=0 and left1 < N and nums2[left2-1] > nums1[left1]): low = left1+1
        
        return -1
