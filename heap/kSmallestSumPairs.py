class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        N = len(nums1)
        M = len(nums2)
        
        row_index = 0
        col_index = 0

        ans = []
        visited = set()
        visited.add((0, 0))
        heap = [(nums1[row_index]+nums2[col_index], row_index, col_index)]
        heapify(heap)

        while(k and heap):
            _, x, y = heappop(heap)
            ans.append([nums1[x], nums2[y]])
            k -= 1
            if(k == 0): return ans

            if(x+1 < N and (x+1, y) not in visited): 
                heappush(heap, (nums1[x+1]+nums2[y], x+1, y))
                visited.add((x+1, y))
            if(y+1 < M and (x, y+1) not in visited): 
                heappush(heap, (nums1[x]+nums2[y+1], x, y+1))
                visited.add((x, y+1))
        
        return ans


