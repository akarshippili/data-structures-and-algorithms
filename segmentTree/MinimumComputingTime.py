from SegmentTree import SegmentTree


class MinimumComputingTime:

    def findMinimumTime(self, tasks) -> int:
        timeline = SegmentTree([0 for i in range(10)], operator=lambda x, y : x+y, operationIdentity=0)
        ans = 0
        for start, end, duration in tasks:
            onTime =  timeline.query(start, end)
            if(onTime >= duration): continue

            remaining = duration - onTime
            ans += remaining
            timeline.rightfill(remaining, start, end)
        
        return ans

MinimumComputingTime = MinimumComputingTime()
MinimumComputingTime.findMinimumTime([[2,3,1],[4,5,1],[1,5,2]])