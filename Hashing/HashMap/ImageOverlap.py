class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        def mapper(arr):
            ans = 0
            for i in arr:
                ans = (ans<<1) | i
            return ans
        
        N = len(img1)
        
        img1 = [mapper(i) for i in img1]
        img2 = [mapper(i) for i in img2]
                
        visited = {}
        
        self.helper(img1, img2, 0, 0, visited)
                 
        return max(visited[i] for i in visited)
    
    # ~O(1)
    def numOfOnes(self,num):
        count = 0
        while(num>0): 
            num = num&(num-1)
            count+=1
        return count
    
    O(4*(N**2)) ~ O(N**2)
    def helper(self, img1, img2, row, col, visited):
        
        key = (row, col)
        
        if(row<=len(img1)*-1 or row>=len(img1) or col<=len(img1)*-1 or col>=len(img1) or key in visited): 
            return
        
        ans = 0
        
        O(N)
        if(row>=0):
            for index in range(0, len(img1)-row):
                val1 = img1[index] >> col if(col>=0) else img1[index] << (-1*col)
                val2 = img2[index+row]
                ans += self.numOfOnes(val1 & val2)
        else:
            for index in range(0, len(img1)+row):
                val1 = img1[index-row] >> col if(col>=0) else img1[index-row] << (-1*col)
                val2 = img2[index]
                ans += self.numOfOnes(val1 & val2)
        
        visited[key] = ans
        # print(key, ans)
         
        self.helper(img1, img2, row-1, col, visited)
        self.helper(img1, img2, row, col+1, visited)
        self.helper(img1, img2, row+1, col, visited)
        self.helper(img1, img2, row, col-1, visited)
