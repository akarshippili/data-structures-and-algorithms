# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root):
        if(not root): return [0, 0]
        left, right = self.helper(root.left), self.helper(root.right)
        cur = [1 + left[1], 1 + right[0]]
        self.ans = max(self.ans, left[0], right[1], max(cur))
        return cur



    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans -1
        

