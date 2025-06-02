class Solution:
    def candy(self, rating) -> int:
        
        N = len(rating)
        if N == 1: return 1


        ans = [1 for _ in range(N)]
        start_nodes = []

        for index in range(N):
            if index == 0 and rating[index] <= rating[index + 1]:
                start_nodes.append(index)
                continue

            if index == N-1 and rating[index - 1] >= rating[index]:
                start_nodes.append(index)
                continue

            if rating[index - 1] >= rating[index] and rating[index] <= rating[index + 1]:
                start_nodes.append(index)


        if len(start_nodes) == N: return N

        for index in start_nodes:
            
            dx = index - 1
            x = 2
            while(dx >= 0 and rating[dx] >= rating[dx + 1]):
                if rating[dx] == rating[dx + 1]:
                    x = 1
                    dx -= 1
                    continue

                ans[dx] = max(ans[dx], x)
                dx -= 1
                x += 1
            
            dx = index + 1
            x = 2
            while(dx < N and rating[dx] >= rating[dx - 1]):
                if rating[dx] == rating[dx - 1]:
                    x = 1
                    dx += 1
                    continue

                ans[dx] = max(ans[dx], x)
                dx += 1
                x += 1
            
            # print(index, ans)

        return sum(ans)