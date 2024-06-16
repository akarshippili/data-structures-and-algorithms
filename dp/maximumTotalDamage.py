class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        power.sort()
        power = [[l, len(list(g))] for l, g in groupby(power)]
        N = len(power)

        index = N-1
        dp = [0 for _ in range(N)]
        best = 0
        
        def search(index):
            val = power[index][0]
            val += 2
            
            low = index
            high = N-1
            
            while(low < high):
                mid = low + (high - low)//2
                # print(low, high, mid)
                
                if(power[mid][0] <= (val)):
                    low = mid + 1
                else:
                    high = mid
            
            if(power[low][0] > val):
                return low
            
            return -1
        
        while(index >= 0):
            idx = search(index)

            if(idx != -1): dp[index] = power[index][0] * power[index][-1] + dp[idx]
            else: dp[index] = power[index][0] * power[index][-1]

            if(index+1 < N): dp[index] = max(dp[index], dp[index+1])    
            index -= 1
        
        return dp[0]
        
        
