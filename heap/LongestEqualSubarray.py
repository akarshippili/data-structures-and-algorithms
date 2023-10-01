class Heap:

    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.arr = [None for _ in range(self.capacity)]
        self.size = 0
    
    def __str__(self):
        ans = [str(node) for node in self.arr]
        return " ".join(ans)

    def doubleTheCapacity(self):
        self.arr += [None  for _ in range(self.capacity)]
        self.capacity *= 2

    def add(self, node): 
        if(self.capacity == self.size): self.doubleTheCapacity()
        
        self.arr[self.size] = node
        node.index = self.size
        self.size += 1

        self.heapifyUp(self.size-1)
    
    def peek(self):
        if(self.size == 0): raise Exception("index out of bound")
        return self.arr[0]
    
    def pop(self): 
        if(self.size == 0): raise Exception("index out of bound")

        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.arr[0].index = 0
        self.arr[self.size-1].index = self.size-1
        self.size -= 1
        self.heapifyDown(0)
        return self.arr[self.size]
    
    def increaseKey(self, index, newVal):
        if(index < 0 and index >= self.size): raise Exception("index out of bound")

        self.arr[index].val = newVal
        self.heapifyUp(index)
    
    def decreaseKey(self, index, newVal):
        if(index < 0 and index >= self.size): raise Exception("index out of bound")

        self.arr[index].val = newVal
        self.heapifyDown(index)

    def heapifyUp(self, index): 
        if(index >= self.size): raise Exception("index out of bound")

        while(Heap.hasParent(index) and self.arr[Heap.getParentIndex(index)] < self.arr[index]):
            parentIndex = Heap.getParentIndex(index)
            self.arr[index], self.arr[parentIndex] = self.arr[parentIndex], self.arr[index]
            self.arr[index].index = index
            self.arr[parentIndex].index = parentIndex
            index = parentIndex

    def heapifyDown(self, index): 
        if(self.size == 0): return
        if(index < 0 or index >= self.size): raise Exception("index out of bound")

        greatestIndex = index
        while True:
            leftIndex = Heap.getLeftChildIndex(index)
            rightIndex = Heap.getRightChildIndex(index)
            if(leftIndex < self.size and self.arr[greatestIndex] < self.arr[leftIndex]): greatestIndex = leftIndex
            if(rightIndex < self.size and self.arr[greatestIndex] < self.arr[rightIndex]): greatestIndex = rightIndex

            if(greatestIndex == index): return
            self.arr[index], self.arr[greatestIndex] = self.arr[greatestIndex], self.arr[index]
            self.arr[index].index = index
            self.arr[greatestIndex].index = greatestIndex
            index = greatestIndex

            

    @staticmethod
    def hasParent(index): return index != 0

    @staticmethod
    def getParentIndex(index): return (index-1)//2
    
    @staticmethod
    def getLeftChildIndex(index): return 2*index +1
    
    @staticmethod
    def getRightChildIndex(index): return 2*index +2


class HeapNode:
    def __init__(self, val):
        self.val = val
        self.index = None
    
    def __eq__(self, value):
        return self.val == value.val
    
    def __lt__(self, value):
        return self.val < value.val

    def __str__(self):
        return f'val: {self.val} index: {self.index}'

class Solution:
    
    def longestEqualSubarray(self, nums, K):
        # [)
        
        ans = -10 ** 10
        N = len(nums)
        start = 0
        end = 0
        k = 0
        nodeMap = {}
        heap = Heap()

        while(end < N):
            while(end < N and k <= K):
                print(start, end, k)
                if(nums[end] not in nodeMap): 
                    nodeMap[nums[end]] = HeapNode(0)
                    heap.add(nodeMap[nums[end]])
                
                node = nodeMap[nums[end]]
                heap.increaseKey(node.index, node.val +1)
                end += 1

                l = end - start
                maxFreq = heap.peek().val
                k = l - maxFreq
                
                if(k <= K): ans = max(ans, maxFreq)
            
            print('-'*10)

            while(k > K and start < end):
                print(start, end, heap)
                node = nodeMap[nums[start]]
                heap.decreaseKey(node.index, node.val-1)
                start += 1

                k = (end - start) - heap.peek().val
            
            print('-'*10)
            
            if(heap.size > 0):
              print(start, end) 
              ans = max(ans, heap.peek().val)
        
        return ans

sol = Solution()
nums = [1,1,2,2,1,1]
ans = sol.longestEqualSubarray(nums, 1)
print(ans)

# heap = Heap()
# heap.add(HeapNode(1))
# heap.add(HeapNode(2))
# heap.add(HeapNode(3))
# heap.add(HeapNode(4))
# heap.add(HeapNode(6))
# heap.add(HeapNode(5))

# while(heap.size > 0):
#     print(heap.pop())
