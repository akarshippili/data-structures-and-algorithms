class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if(low>high): return 0
        if(low%2 == 1): return 1 + self.countOdds(low+1, high)
        if(high%2 == 1): return 1 + self.countOdds(low, high-1)
        return (high-low)//2
