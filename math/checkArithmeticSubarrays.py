class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        

        def isit(left, right):
            s = set()
            min1, min2 = min(nums[left], nums[left+1]), max(nums[left], nums[left+1]) 
            
            s.add(min1)
            s.add(min2)
            for num in nums[left+2:right+1]:
                if(num < min1): min1, min2 = num, min1
                elif(num == min1 or min1 < num < min2): min2 = num
                s.add(num)

            start = min1 
            d = min2-min1
            count = 0

            if(d == 0 and len(s) == 1): return True
            
            while(s):
                if(start in s):
                    s.remove(start)
                    start += d
                    count += 1
                else: 
                    return False

            return count == (right - left + 1)

        
        return [isit(left, right) for left, right in zip(l, r)]
