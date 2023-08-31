class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
      map = {}
      for index, rng in enumerate(ranges): 
        start, end = max(index-rng, 0), index + rng
        if(start in map): map[start] = max(map[start], end)
        else: map[start] = end

      inf = 10**10

      @cache
      def count(index):
        if(index >= n): return 0
        if(index not in map): return inf

        val = map[index]
        ans = inf
        for nxt in range(index+1, val+1):  ans = min(ans, 1 + count(nxt))
        return ans
      
      num = count(0)
      return num if(num != inf) else -1
