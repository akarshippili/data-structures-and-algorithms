class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        mapper = {}
        ans = []
        
        for num in nums:
            if(num in mapper): mapper[num] += 1
            else: mapper[num] = 0
            
            if(mapper[num] >= len(ans)): ans.append([])                
            ans[mapper[num]].append(num)
        
        return ans
