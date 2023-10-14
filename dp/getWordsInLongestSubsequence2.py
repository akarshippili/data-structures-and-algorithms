class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        
        cache = {}

        def hamming_dis(s1, s2):
            a = [s1, s2]
            a.sort()
            key = (a[0], a[1])
            if(key in cache): return cache[key]
            ans = sum(1 if(ch1 != ch2) else 0 for ch1, ch2 in zip(s1,s2))
            cache[key] = ans
            return ans
        
        
        
        dp = [1] * (n+1)
        parent = [-1] * (n+1)

        dp[-1] = 0
        dp[1] = 1
        
        for index in range(n, -1, -1):
            for index2 in range(index, n):
                if(
                    len(words[index]) != len(words[index2]) or 
                    groups[index2] == groups[index] or 
                    hamming_dis(words[index], words[index2]) != 1
                ): continue

                if(dp[index] < dp[index2] + 1):
                    dp[index] = 1 + dp[index2]
                    parent[index] = index2 
        
        start_index = dp.index(max(dp))
        
        ans = []
        while(start_index != -1):
            ans.append(start_index)
            start_index = parent[start_index]

        return [words[index] for index in ans]
        
