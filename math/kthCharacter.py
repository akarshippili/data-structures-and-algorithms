class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        

        def count(k, N):
            if N == 0: return 0

            """
                N + 1 // 2

                0       N-1//2 | N+1//2       N

            """

            # print(k, N, 0 <= k <= ((N-1) // 2), ops[-1])

            op = ops.pop()
            if 0 <= k <= ((N-1) // 2): return count(k, (N-1) // 2)
            else: return count(k - (N+1)//2, (N-1)//2) + op
        
        N = 1
        ops = []
        index = 0
        while(k > N):
            N *= 2
            ops.append(operations[index])
            index += 1
        
        # print(k-1, N-1, ops)
        steps = count(k-1, N-1)
        return chr(steps % 26 + ord('a'))