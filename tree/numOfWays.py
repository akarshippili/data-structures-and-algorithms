class Node:
    def  __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"{{val: {self.val}, left: {self.left}, right: {self.right}}}"
    
class BST:

    def __init__(self):
        self.root = None
    
    def add(self, val):
        if(not self.root): 
            self.root = Node(val)
            return 
        
        parent = None
        temp = self.root
        while(temp):
            if(temp.val < val): parent, temp = temp, temp.right
            else: parent, temp = temp, temp.left
        
        if(parent.val < val): parent.right = Node(val)
        else: parent.left = Node(val)
    
    def __str__(self):
        return str(self.root)

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        bst = BST()
        for num in nums: bst.add(num)

        mod = 10**9 + 7

        @cache
        def getPossiblePermutations(num1, num2):
            # num in slots (num1, slots)
            if(num1 == 0): return 1
            if(num2 == 0): return 1

            return getPossiblePermutations(num1-1, num2) + getPossiblePermutations(num1, num2-1)


        def helper(node):
            if(not node): return 0, 1

            left, lp = helper(node.left)
            right, rp = helper(node.right)
            
            curp = (getPossiblePermutations(left, right)%mod * lp%mod * rp%mod)%mod
            return (left + 1 + right, curp)
        
        _, ans = helper(bst.root)
        return ans-1
