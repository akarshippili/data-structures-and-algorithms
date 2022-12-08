class Solution:
    def getLeaves(self, root):
        if(not root): return []


        left = []
        right = []

        if(not root.left and not root.right): return [root.val]
        if(root.left): left = self.getLeaves(root.left)
        if(root.right): right = self.getLeaves(root.right)

        return left + right


    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        a = self.getLeaves(root1)
        b = self.getLeaves(root2)

        if(len(a)!=len(b)): return False

        return all(i == j for i, j in zip(a,b))
