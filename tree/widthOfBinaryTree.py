# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def appendNone(queue, count):
            while(queue and queue[-1][0] == None):
                node, sub_count = queue.pop()
                count += sub_count
            queue.append([None, count])

        if(not root): return 0

        ans = 1
        queue = [[root, 1]]
        l = 1

        while(queue):
            cur, count = queue.pop(0)
            l -= 1

            if(not cur): appendNone(queue, count*2)
            else:
                if(cur.left): queue.append([cur.left, 1])
                else: appendNone(queue, 1)
                
                if(cur.right): queue.append([cur.right, 1])
                else: appendNone(queue, 1)
            

            if(l == 0):
                while(queue and not queue[0][0]): queue.pop(0)
                while(queue and not queue[-1][0]): queue.pop()
                
                l = len(queue)
                ans = max(ans, sum([i[-1] for i in queue]))

        
        return ans


