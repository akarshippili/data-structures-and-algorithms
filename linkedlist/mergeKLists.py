# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        heapify(heap)
        counter = 0

        for node in lists: 
            if(node): 
                heappush(heap, [node.val, counter, node])
                counter += 1

        
        head = ListNode(-10**10)
        temp = head

        while(heap):
            _, _, node = heappop(heap)
            next_node = node.next
            if(next_node): 
                heappush(heap, [next_node.val, counter, next_node])
                counter += 1

            node.next = None
            temp.next = node
            temp = temp.next
        return head.next

