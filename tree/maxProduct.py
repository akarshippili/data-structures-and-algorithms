# Approach

# Two pass
# - first pass to get the sum of the tree
# - second pass to find the max product 


# Complexity
# - Time complexity: $$O(n)$$
# - Space complexity: $$O(n)$$


# Code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        cache = {}
        mod = 10**9 + 7

        def getSumOfTree(root):
            if(root in cache): return cache[root]
            if not root: return 0

            left = getSumOfTree(root.left)
            right = getSumOfTree(root.right)
            
            ans = left + right + root.val

            cache[root] = ans
            return ans
        
        def ans(root, totalSum):
            if(not root): return -1

            sumVal = getSumOfTree(root)
            cur = (totalSum-sumVal) * (sumVal%mod)

            return max(cur, ans(root.left, totalSum), ans(root.right, totalSum))
        
        return ans(root, getSumOfTree(root))%mod
