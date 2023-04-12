class Solution:
    def simplifyPath(self, path: str) -> str:

        arr = path.split('/')
        stack = []

        for op in arr:
            if(op == '' or op == '.'): continue
            elif(op == ".."):
                if(stack): stack.pop()
            else:
                stack.append(op)

        return '/' + "/".join(stack)
