import math


class SegmentTree:

    def __init__(self, arr, operator, operationIdentity) -> None:
        self.arrLength = len(arr)
        self.arr = arr
        self.modifiedNumberOfChildren = 2**(math.ceil(math.log(self.arrLength, 2)))
        self.segmentTreeLength = 2*self.modifiedNumberOfChildren - 1
        self.segmentTree = [None for i in range(self.segmentTreeLength)]
        self.operationIdentity = operationIdentity
        self.operation = operator
        self.buildSegmentTree(0,self.modifiedNumberOfChildren-1, 0)
    
    
    def buildSegmentTree(self, start, end, index):
        if(start == end): 
            self.segmentTree[index] = self.arr[start] if(start < self.arrLength) else self.operationIdentity
            return self.segmentTree[index]
          
        mid = start + (end - start)//2
        leftSegmentValue = self.buildSegmentTree(start, mid, 2*index+1)
        rightSegmentValue = self.buildSegmentTree(mid+1, end, 2*index+2)
        self.segmentTree[index] = self.operation(leftSegmentValue, rightSegmentValue)
        return self.segmentTree[index]


    def query(self, start, end):

        def queryHelper(qstart, qend, start, end, index):
            if(qstart>end or qend<start): return self.operationIdentity
            if(qstart == start and qend == end): return self.segmentTree[index]

            mid = start + (end - start)//2
            return self.operation(queryHelper(qstart, min(qend, mid), start, mid, 2*index + 1), 
                                  queryHelper(max(qstart, mid+1), qend, mid+1, end, 2*index + 2))

        return queryHelper(start, end, 0, self.modifiedNumberOfChildren-1, 0)
    
    def update(self, index, newValue):

        def updateHelper(start, end, segIndex, index, newValue):
            if(start == end == index): 
                self.segmentTree[segIndex] = newValue
                return

            mid = start + (end - start)//2
            if(start <= index <= mid): updateHelper(start, mid, 2*segIndex+1, index, newValue)
            else: updateHelper(mid+1, end, 2*segIndex+2, index, newValue)

            self.segmentTree[segIndex] = self.operation(self.segmentTree[2*segIndex+1], self.segmentTree[2*segIndex+2])



        self.arr[index] = newValue
        updateHelper(0, self.modifiedNumberOfChildren -1, 0, index, newValue)


SegmentTree = SegmentTree([1,2,3,4,5,6], operator=lambda x, y : x*y, operationIdentity=1)


print(SegmentTree.segmentTree)
print(SegmentTree.query(0,5))
print(SegmentTree.query(0,4))
print(SegmentTree.query(1,4))
print(SegmentTree.query(2,5))

SegmentTree.update(0, 6)
print(SegmentTree.segmentTree)
print(SegmentTree.query(0,5))
print(SegmentTree.query(0,4))
print(SegmentTree.query(1,4))
print(SegmentTree.query(2,5))



SegmentTree.update(0,1)
print(SegmentTree.segmentTree)
print(SegmentTree.query(0,5))
print(SegmentTree.query(0,4))
print(SegmentTree.query(1,4))
print(SegmentTree.query(2,5))



SegmentTree.update(5, 0)
print(SegmentTree.segmentTree)
print(SegmentTree.query(0,5))
print(SegmentTree.query(0,4))
print(SegmentTree.query(1,4))
print(SegmentTree.query(2,5))