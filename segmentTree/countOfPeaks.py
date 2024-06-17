class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        
        arr = [0]
        for index in range(1, N-1):
            if(nums[index-1] < nums[index] > nums[index+1]): arr.append(1)
            else: arr.append(0)

        arr.append(0)
       
        segment_tree = SegmentTree(arr, operator = lambda x, y : x + y, operationIdentity = 0)

        def getNumPeaks(start, end):
            return segment_tree.query(start+1, end-1)
        

        def update(index, val):
            nums[index] = val

            for idx in [index-1, index, index+1]:
                if(idx <= 0 or idx >= N-1): continue

                if(nums[idx-1] < nums[idx] > nums[idx+1]): segment_tree.update(idx, 1)
                else: segment_tree.update(idx, 0)
            

        ans = []
        for query in queries:
            if(query[0] == 1): ans.append(getNumPeaks(query[1], query[-1]))
            else: update(query[1], query[-1])
        
        return ans
