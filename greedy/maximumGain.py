class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        ans = 0
        stack = []

        if(x > y):
            for ch in s:
                if(stack and stack[-1] == 'a' and ch == 'b'):
                    ans += x
                    stack.pop()
                else:
                    stack.append(ch)
            
            s = "".join(stack)
            stack = []
            for ch in s:
                if(stack and stack[-1] == 'b' and ch == 'a'):
                    ans += y
                    stack.pop()
                else:
                    stack.append(ch)
        else:
            for ch in s:
                if(stack and stack[-1] == 'b' and ch == 'a'):
                    ans += y
                    stack.pop()
                else:
                    stack.append(ch)
            
            s = "".join(stack)
            stack = []
            for ch in s:
                if(stack and stack[-1] == 'a' and ch == 'b'):
                    ans += x
                    stack.pop()
                else:
                    stack.append(ch)

        return ans
