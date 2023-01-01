class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for i in range(right+1)]
        
        def SieveOfEratosthenes(prime):
            N = len(prime)
            p = 2
            while (p * p <= N-1):
                if (prime[p] == True):
                    for i in range(p * p, N, p):
                        prime[i] = False
                p += 1
        
        SieveOfEratosthenes(prime)
        
        ans = 10**10
        prev = -1
        arr = [-1, -1]
        
        for p in range(max(2, left), len(prime)):
            if prime[p]:
                if(prev != -1):
                    cur = p - prev
                    if(cur<ans):
                        ans = cur
                        arr = [prev, p]
                prev = p
        
        return arr
