class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if(not root): 
            return 0
        
        ans = 0
        val = root.val

        if(low<=val<=high): 
            ans += val
        if(low<=val):
            ans += self.rangeSumBST(root.left, low, high)
        if(val<=high):
            ans += self.rangeSumBST(root.right, low, high)
        
        return ans
