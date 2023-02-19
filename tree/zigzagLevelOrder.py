# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root): return []

        ans = []
        cur_ans = []
        queue = [root]
        l = 1
        reverse_flag = False

        while(queue):
            # print([i.val for i in queue])
            cur = queue.pop(0)
            l -= 1
            cur_ans.append(cur.val)

            if(cur.left): queue.append(cur.left)
            if(cur.right): queue.append(cur.right)

            if(l == 0):
                ans.append(cur_ans if not reverse_flag else cur_ans[::-1])
                cur_ans = []
                l = len(queue)
                reverse_flag = True ^ reverse_flag
        
        return ans
