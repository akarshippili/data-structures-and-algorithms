# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        visited = collections.defaultdict(int)

        def inorder(root):
            if(not root): return ("null", "null")

            in_l, pre_l = inorder(root.left)
            in_r, pre_r = inorder(root.right)

            cur_in = in_l + str(root.val) + in_r
            cur_pre = str(root.val) + pre_l + pre_r
            cur = (cur_in, cur_pre)

            if(cur in visited and visited[cur] == 1):
                # print(cur)
                ans.append(root)
                visited[cur] += 1
            else:
                visited[cur] += 1
            return cur
        
        inorder(root)
        return ans
