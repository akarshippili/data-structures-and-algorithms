class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        hashset = set()
        prefix = nums[0] % k
        hashset.add(prefix)
        hashset.add(0)
        
        
        count = 0
        for i in nums:
            if((i % k)  == 0): 
                count += 1
            else:
                count = 0
            
            if(count>1): return True
        
        for i in range(1, len(nums)):
            if(nums[i]%k == 0): continue
            prefix = (prefix + nums[i])%k
            if(prefix in hashset):
                return True
            else:
                hashset.add(prefix)
        
        return False
        
        
        
