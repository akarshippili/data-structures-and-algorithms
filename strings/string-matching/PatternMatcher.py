class PatternMatcher:

    def __init__(self):
        self.mod = 10**9 + 9
        self.p = 31
        self.pow_p = []

        self.pattern = None
        self.s = None

        self.n = None
        self.m = None
        self.strHash = {}
    
    def fill_pow_p(self, num):
        cur = 1

        while(num>=0):
            self.pow_p.append(cur)
            cur *= self.p
            num -= 1
    
    def getStrHash(self, index):
        if(index == 0):
            ans = 0
            for index, ch in enumerate(self.s[:self.m]):
                ans = (ans%self.mod +  ((ord(ch) - 96) * self.pow_p[self.m-1-index])%self.mod) % self.mod 
        
            self.strHash[0] = ans
            return ans

        if(index in self.strHash): return  self.strHash[index]
        
        prevHash = self.getStrHash(index-1)
        ans = (
            (prevHash * self.p) 
            - ( (ord(self.s[index-1]) - 96) * self.pow_p[self.m]) 
            + (ord(self.s[index+self.m-1]) - 96)
            ) % self.mod
        self.strHash[index] = ans
        return ans

    def patternMatching(self, s, pattern):
        ans = []

        self.pattern = pattern
        self.s = s
        self.m = len(pattern)
        self.n = len(s)
        self.fill_pow_p(self.m)

        patternHash = 0
        for pi, pc in enumerate(self.pattern):
            patternHash = (patternHash%self.mod +  ((ord(pc) - 96) * self.pow_p[self.m-1-pi])%self.mod) % self.mod
    
        strHash = None

        endIndex = (self.n-self.m+1)
        index = 0
        while(index < endIndex):
            strHash = self.getStrHash(index)
            if(patternHash == strHash): ans.append(index)
            index += 1

        return ans


sol = PatternMatcher()
print(sol.patternMatching("hellohello", "llo"))
print(sol.strHash)
print(sol.pow_p)
