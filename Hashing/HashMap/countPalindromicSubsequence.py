class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        N = len(s)

        left = defaultdict(int)
        right = defaultdict(int)

        for index in range(1, N): right[s[index]] += 1
        
        ans = set()
        for index in range(N):
            for ch in left:
                if(left[ch] > 0 and right[ch] > 0):
                    ans.add((ch, s[index]))
            
            left[s[index]] += 1
            if(index+1 < N): right[s[index+1]] -= 1
        
        return len(ans)
