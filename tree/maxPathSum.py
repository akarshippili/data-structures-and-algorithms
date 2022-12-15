class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if(not root): return -10001,-10001

            leftx, leftmax  = helper(root.left)
            rightx, rightmax = helper(root.right)
            val = root.val

            ansx = max(val, val+leftx, val+rightx)
            ans = max(ansx, val + leftx + rightx, leftmax, rightmax) 
            return (ansx, ans)

        
        return max(helper(root))
