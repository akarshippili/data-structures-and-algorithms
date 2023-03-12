# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def getMiddleNode(self, head):
        slow = head
        fast = head
        prev = None

        while(slow and fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev


    def sortedListToBST(self, head):
        if(not head):return 
        if(not head.next): return TreeNode(head.val)  
        
        prev = self.getMiddleNode(head)
        middlenode = prev.next
        nextnode = middlenode.next
        prev.next = None

        root = TreeNode(middlenode.val)

        root.left =  self.sortedListToBST(head)
        root.right = self.sortedListToBST(nextnode)

        return root
    
    def inorder(self, node):
        if(not node): return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

node = ListNode(-10)
node.next  = ListNode(-2)
node.next.next  = ListNode(3)
node.next.next.next  = ListNode(5)
node.next.next.next.next  = ListNode(10)
node.next.next.next.next.next  = ListNode(12)

Solution = Solution()
root = Solution.sortedListToBST(node)
Solution.inorder(root)