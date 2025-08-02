from sortedcontainers import SortedDict

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        
        counter = Counter(basket1) + Counter(basket2)
        for k in counter:
            if counter[k] % 2 == 1:
                return -1

        sd1 = SortedDict() #.sort()
        sd2 = SortedDict() # basket2.sort()

        for num in basket1: 
            if num not in sd1: sd1[num] = 0
            sd1[num] += 1

        for num in basket2: 
            if num not in sd2: sd2[num] = 0
            sd2[num] += 1
        
        for k in sd1:
            if k in sd1 and k in sd2:
                val = min(sd1[k], sd2[k])

                sd1[k] -= val
                sd2[k] -= val
        
        keys = list(sd1.keys())
        for k in keys:  
            if k in sd1 and k in sd2:
                if sd1[k] == 0:
                    del sd1[k]
        
                if sd2[k] == 0:
                    del sd2[k]

        N = len(basket1)

        """

            ......XYYYYYYYY
            ......YZZZZ

            2000 1 1 1000 1000 1000 
            1 1 1000 2000 20000 2000


            12234
            12234

        """

        min_ = min(min(basket1), min(basket2))
        ans = 0

        # print(sum(list(sd1.values())), sum(list(sd2.values())))
        while(sd1):
            # print(sd1, sd2)
            # assert(len(sd1) == len(sd2))
            (val1 , _), (val2, _) = sd1.peekitem(0), sd2.peekitem(0)
            if val1 < val2: sd1, sd2 = sd2, sd1
                

            (val1 , _), (val2, _) = sd1.peekitem(0), sd2.peekitem()
            ans += min(2 * min_, min(val1, val2))

            # print(val1, val2,  min(2 * min_, min(val1, val2)))
            sd1[val1] -= 2
            sd2[val2] -= 2

            if sd1[val1] == 0: del sd1[val1]
            if sd2[val2] == 0: del sd2[val2]
        
        return ans