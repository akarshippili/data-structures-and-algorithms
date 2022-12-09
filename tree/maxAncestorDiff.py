class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def helper(root, minVal, maxVal):
            if(not root): return -1

            a = abs(root.val - maxVal)
            b = abs(root.val - minVal)
            cur = max(a, b)

            left = helper(root.left, min(minVal, root.val), max(maxVal, root.val))
            right = helper(root.right, min(minVal, root.val), max(maxVal, root.val))

            return max(left, right, cur)
        
        return helper(root, root.val, root.val)
