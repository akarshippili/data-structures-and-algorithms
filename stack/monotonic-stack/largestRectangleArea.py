class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0

        stack = []
        for index, height in enumerate(heights):
            prev = index

            while(stack and stack[-1][-1] > height):
                ans = max(ans, stack[-1][-1] * ( index - stack[-1][0]))
                prev, _ = stack.pop()

            stack.append([prev, height])
        
        while(stack):
            index, height = stack.pop()
            ans = max(ans, height * (len(heights) - index))
        
        return ans
