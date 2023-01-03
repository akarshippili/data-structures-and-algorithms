class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length = 0
        temp = head
        while(temp):
            temp = temp.next
            length+=1
        
        rounds = length//k

        def helper(head, k, offset, rounds):
            if(not head or offset>rounds): 
                return head

            prev = None
            nextNode = None
            cur = head
            count = k

            while(cur and count>0):
                nextNode = cur.next 
                cur.next = prev

                prev = cur
                cur = nextNode
                count-=1

            head.next = helper(nextNode, k, offset+1, rounds)
            return prev
        
        return helper(head, k, 1, rounds)
