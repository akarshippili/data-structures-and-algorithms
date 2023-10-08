class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        N = len(s)
        prev = [0]*N
        prev[-1] = 1

        start = N-2
        while(start >= 0):
            cur = [0] * N
            cur[start] = 1
            col = start+1

            while(col < N):
                cur[col] = max(
                    cur[col-1],
                    prev[col],
                    2 + prev[col-1] if(s[col] == s[start]) else 0
                )
                
                col += 1
            
            prev = cur
            start -= 1
       
        return prev[-1]
