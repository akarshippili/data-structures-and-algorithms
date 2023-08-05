# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def helper(low, high):
            if(low > high): return []
            if(low == high): return [TreeNode(low)]

            ans = []
            for cur in range(low, high+1):
                left = helper(low, cur-1)
                right = helper(cur+1, high)

                if(not left):
                    for r in right:
                        node = TreeNode(cur)
                        node.right = r
                        ans.append(node)
                
                if(not right):
                    for l in left:
                        node = TreeNode(cur)
                        node.left = l
                        ans.append(node)
                    
                
                for l in left:
                    for r in right:
                        node = TreeNode(cur)
                        node.left, node.right = l, r
                        ans.append(node)
            
            return ans
        
        return helper(1, n)
