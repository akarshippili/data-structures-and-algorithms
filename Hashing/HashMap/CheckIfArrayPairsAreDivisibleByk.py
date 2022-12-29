class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        table = {}
        for i in arr:
            if(i%k not in table):
                table[i%k] = 0
            table[i%k] += 1
        

        for i in table:
            if(i==0): 
                if(table[0]%2 == 1): return False
            elif( ((i in table) ^ ((k-i) in table)) or table[i]!=table[k-i]): return False 
        return True
