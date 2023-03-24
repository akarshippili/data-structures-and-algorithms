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

dll = DoubllyLinkedList()
node1 = DoubllyLinkedListNode(1)
dll.addNodeToTail(node1)
dll.delete(node1)
dll.addNodeToTail(DoubllyLinkedListNode(2))
dll.addNodeToTail(DoubllyLinkedListNode(3))
node4 = DoubllyLinkedListNode(4)
dll.addNodeToTail(node4)
dll.addNodeToTail(DoubllyLinkedListNode(5))

dll.print()
dll.print(forward=False)

dll.delete(node4)
dll.print()
dll.print(forward=False)