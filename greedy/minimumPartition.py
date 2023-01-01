class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        
        ans = 0
        
        index = 0
        while(index<len(s)):
            cur = 0
            prev = index
            
            while(index<len(s) and (cur*10 + int(s[index])) <= k):
                cur = cur*10 + int(s[index])
                index += 1
            
            if(prev == index): return -1
            else: ans += 1
        
        return ans
            
                
        
