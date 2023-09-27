class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        N = len(s)
        cur_len = 0
        start = 0
        stack = []

        while(start < N):

            cur_index = start
            while(cur_index < N and not s[cur_index].isdigit()): 
                cur_index += 1
                cur_len += 1

            # start:cur_index sub-string
            if(start != cur_index): 
                stack.append([s[start:cur_index], cur_len])
            
            if(cur_index < N): 
                cur_len *= int(s[cur_index])
                stack.append([(s[cur_index]), cur_len])
                cur_index += 1
            
            start = cur_index
        
        
        while(len(stack) > 1): 
            
            if(stack[-1][0].isdigit()):
                prev_len = stack[-2][-1]
                k = (k-1) % prev_len + 1
            else:
                prev_len = stack[-2][-1]
                if(k > prev_len): return stack[-1][0][k-prev_len-1]
            
            stack.pop()
        
        return stack[-1][0][k-1]
