class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        N = len(nums)
        M = len(pattern)

        eff_num = []
        for index in range(1, N):
            diff = nums[index] - nums[index-1]
            if(diff > 0): eff_num.append(1)
            elif(diff == 0): eff_num.append(0)
            else: eff_num.append(2)
        
        for index in range(M):
            if(pattern[index] == -1):
                pattern[index] = 2

        mod = 10**9 + 7
        ans = 0
        pow_p = 5
        patternHash = 0
        curHash = 0

        for index in range(len(pattern)):
            patternHash *= pow_p
            patternHash += pattern[index]
            patternHash %= mod

            curHash *= pow_p
            curHash += eff_num[index]
            curHash %= mod

        
        if(curHash == patternHash): ans += 1


        pow_p_pow_m = pow(pow_p, M, mod)

        start_index = 0
        index = len(pattern)
        while(index < len(eff_num)):
            
            curHash *= pow_p
            curHash += eff_num[index]
            curHash -= (eff_num[start_index] * pow_p_pow_m)
            curHash %= mod
            
            if(curHash == patternHash): ans += 1
            index += 1
            start_index += 1
        
        return ans

