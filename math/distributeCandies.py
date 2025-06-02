class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        ans = 0
        
        for x in range(0, min(limit, n) + 1):
            x_left = n - x
            if x_left <= limit:
                """
                    x_left  | 0
                    0 | x_left
                    allvalid
                """
                ans += x_left + 1
            else:
                """
                x_left > limit
                0       | x_left
                1       | x_left - 1
                2       | x_left - 2
                ... (no valid)
                
                x | x_left - x ==== x_left - limit == y
                x + 1 | x_left - x -1
                ...

                limit | x_left - limit
                """

                ans += max((2 * limit) - x_left + 1, 0)
             
        return ans