class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = set()
        pop_index = 0
        push_index = 0
        N = len(pushed)
        arr = []

        while(pop_index < N):
            val = popped[pop_index]

            while(push_index<N and val not in stack):
                arr.append(pushed[push_index])
                stack.add(pushed[push_index])
                push_index += 1
            
            # print(val, stack, arr)


            if(val in stack):
                if(arr[-1] == val):
                    arr.pop()
                    stack.remove(val)
                    pop_index += 1
                else:
                    return False
        
        return True

