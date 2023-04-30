class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        a_set = set()
        b_set = set()
        
        ans = []
        prev_ans = 0
        
        for a, b in zip(A, B):
            if(a == b): prev_ans += 1
            if(a in b_set): prev_ans +=1
            if(b in a_set): prev_ans +=1
            
            a_set.add(a)
            b_set.add(b)
            ans.append(prev_ans)
        
        return ans
