class Solution:
    def maxScore(self, arr: List[int]) -> int:
        arr.sort(reverse = True)
        
        count = 0
        running_sum = 0
        
        for i in arr:
            running_sum += i
            if(running_sum>0): count+=1
        
        return count
