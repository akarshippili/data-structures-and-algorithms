class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        N = len(key)
        M = len(ring)

        mapper = defaultdict(list)
        for index, ch in enumerate(ring): mapper[ch].append(index)

        @cache
        def helper(key_index, ring_index):
            if(key_index == N): return 0

            if(key[key_index] == ring[ring_index]): 
                return 1 + helper(key_index+1, ring_index)
            
            ans = 10**10
            for next_index in mapper[key[key_index]]:
                moves = abs(ring_index - next_index)
                moves = min(moves, M - moves)
                ans = min(ans, moves + helper(key_index, next_index))
            
            return ans        
        
        return helper(0, 0)
