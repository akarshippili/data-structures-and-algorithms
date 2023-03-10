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
    
    def print(self, forward = True):
        if(forward): print(str(self.head))
        else:
            temp = self.tail
            while(temp):
                print(str(temp.val) + " -> ", end="")
                temp = temp.prev
            print(temp)

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.dll = DoubllyLinkedList()
        self.count = 0
        self.timeToLive = timeToLive
        self.map = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.cleanup(currentTime)
        node = DoubllyLinkedListNode([currentTime+self.timeToLive, tokenId])
        self.map[tokenId] = node
        self.dll.addNodeToTail(node)
        # self.dll.print()
        self.count += 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.cleanup(currentTime)

        if(tokenId not in self.map): return
        node = self.map[tokenId]
        self.dll.delete(node)
        node.val[0] = currentTime+self.timeToLive
        self.dll.addNodeToTail(node)
        # self.dll.print()


    def cleanup(self, currentTime):
        temp = self.dll.head
        while(temp and temp.val[0]<=currentTime):
            tokenId = temp.val[1]

            del self.map[tokenId]
            self.dll.delete(temp)
            
            temp = temp.next
            self.count -= 1

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.cleanup(currentTime)
        return self.count   


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
