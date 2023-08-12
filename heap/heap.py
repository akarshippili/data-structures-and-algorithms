from math import inf


class  Heap:

    def __init__(self, capacity = 8):
        self.capacity = capacity # number of elements it can hold/store currently
        self.size = 0 # number of elements it's actually storing/present currently
        self.heap = [None for _ in range(self.capacity)]

    # main heap operations
    def add(self, value): 
        # ran out of memory in heap, so double it!
        if(self.size == self.capacity): 
            for _ in range(self.capacity): self.heap.append(None)
            self.capacity *= 2
        
        # we add the new element to the end og the array
        self.heap[self.size] = value
        self.size += 1

        # heapify up
        self.heapifyUp(self.size-1)

    def peek(self): 
        # simpliest operation in heap
        if(self.size == 0): raise Exception("index out of bound")
        return self.heap[0]
    
    def pop(self): 
        if(self.size == 0): raise Exception("index out of bound")

        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
        self.size -= 1
        self.heapifyDown(0)
        return self.heap[self.size]

    def decreaseKey(self, index):
        if(index >= self.size): raise Exception("index out of bound")

        self.heap[index] = -10**10
        self.heapifyUp(index)
        self.pop()

    # heap helper functions
    def heapifyUp(self, index): 
        while(index > 0):
            parentIndex = Heap.parentIndex(index)
            if(self.heap[parentIndex] <= self.heap[index]): break

            self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
            index = parentIndex 

    def heapifyDown(self, index):

        while(index < self.size):
            leftChildIndex = Heap.leftIndex(index)
            rightChildIndex = Heap.rightIndex(index)
            
            smallestIndex = index
            if(leftChildIndex < self.size and self.heap[smallestIndex] > self.heap[leftChildIndex]): smallestIndex =  leftChildIndex
            if(rightChildIndex < self.size and self.heap[smallestIndex] > self.heap[rightChildIndex]): smallestIndex = rightChildIndex

            if(index == smallestIndex): break
            self.heap[smallestIndex], self.heap[index] = self.heap[index], self.heap[smallestIndex]
            index = smallestIndex

    # index calculation helper functions
    @staticmethod
    def leftIndex(index): 
        return 2 * index + 1

    @staticmethod
    def rightIndex(index): 
        return 2 * index + 2

    @staticmethod
    def parentIndex(index): 
        return (index -1)//2

    def isIndexInRange(self, index): 
        return index < self.capacity

    def hasLeftChild(self, index): 
        return self.isIndexInRange(Heap.leftIndex(index))

    def hasRightChild(self, index): 
        return self.isIndexInRange(Heap.rightIndex(index))

    def hasParent(self, index): 
        return index != 0


heap = Heap()
for i in range(10, -1, -1): 
    heap.add(i)
    print(heap.peek())

heap.decreaseKey(5)
while(heap.size > 0): print(heap.peek(), heap.pop())
