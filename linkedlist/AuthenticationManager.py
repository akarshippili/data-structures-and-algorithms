from linkedlist.DoubllyLinkedList import DoubllyLinkedList, DoubllyLinkedListNode

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
