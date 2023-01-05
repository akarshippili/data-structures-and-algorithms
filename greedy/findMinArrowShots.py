class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda x:x[1])
        # print(points)

        ans = 0
        index = 0
        N = len(points)

        while(index<N):
            _,end = points[index]
            while(index<N and points[index][0]<=end):
                index+=1
            ans+=1
        
        return ans
