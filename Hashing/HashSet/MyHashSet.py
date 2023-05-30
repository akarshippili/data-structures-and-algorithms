class DoubllyLinkedListNode:

    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def __str__(self) -> str:
        return str(self.val) + " -> " + str(self.next)

class DoubllyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    

    def addNodeToHead(self, node: DoubllyLinkedListNode):
        # linked list is empty 
        if(not self.head and not self.tail):
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    

    def addNodeToTail(self, node: DoubllyLinkedListNode):
        # linked list is empty 
        if(not self.head and not self.tail):
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    

    def delete(self, node):
        if(node.next and node.prev):
            node.prev.next, node.next.prev = node.next, node.prev
        elif(node == self.head and node.next):
            self.head = node.next
            self.head.prev = None
        elif(node == self.tail and node.prev):
            self.tail = node.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
    
    def contains(self, val):
        temp = self.tail
        while(temp):
            if(temp.val == val): return True
            temp = temp.prev
        
        return False

    def getNode(self, val):
        temp = self.tail
        while(temp):
            if(temp.val == val): return temp
            temp = temp.prev
        
        return None
    
    

    
    def print(self, forward = True):
        if(forward): print(str(self.head))
        else:
            temp = self.tail
            while(temp):
                print(str(temp.val) + " -> ", end="")
                temp = temp.prev
            print(temp)
    
    def __str__(self) -> str:
        return str(self.head)

class MyHashSet:

    def __init__(self):
        self.cap = 101
        self.bucket = [DoubllyLinkedList() for i in range(self.cap)]
        

    def getBucketId(self, num):
        return hash(num)%self.cap

    def add(self, key: int) -> None:
        if(self.contains(key)): return
        id = self.getBucketId(key)
        print(id, key)
        self.bucket[id].addNodeToTail(DoubllyLinkedListNode(key))
        

    def remove(self, key: int) -> None:
        id = self.getBucketId(key)
        node = self.bucket[id].getNode(key)
        if(not node): return
        self.bucket[id].delete(node) 

    def contains(self, key: int) -> bool:
        id = self.getBucketId(key)
        print(id, key)
        return self.bucket[id].contains(key)  


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
s = MyHashSet()
s.add(1)
s.add(2)
print(s.contains(1), s.contains(2))
s.remove(1)
print(s.contains(1), s.contains(2))



