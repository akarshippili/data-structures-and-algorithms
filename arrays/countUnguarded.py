class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        

        obj = {}
        obj[0] = {}
        obj[1] = {}

        arr = []
        for guard in guards: arr.append(guard)
        for wall in walls: arr.append(wall)
        for x in range(m):
            arr.append([x, -1])
            arr.append([x, n])
        
        for y in range(n):
            arr.append([-1, y])
            arr.append([m, y])

        for x,y in sorted(arr):
            if x not in obj[0]: obj[0][x] = []
            obj[0][x].append(y)

            if y not in obj[1]: obj[1][y] = []
            obj[1][y].append(x)
        

        def merge(d, key):
            arr = d[key]
            arr.sort()
            N = len(arr)
            
            end = arr[0][0]
            start_index = index = 0
            new = []

            while(start_index < N):
                
                while(index < N and end >= arr[index][0]):
                    end = max(end, arr[index][-1])
                    index += 1
                
                new.append([arr[start_index][0], end])
                start_index = index
                if start_index < N: end = arr[start_index][0]
            
            d[key] = new
            #print(new)


        fill = {}
        fill[0] = {}
        fill[1] = {}
        for guard in guards:
            x, y = guard

            #print(x, y, obj[0][x], obj[1][y])
            right = bisect.bisect_left(obj[0][x], y+1)
            left = bisect.bisect_left(obj[0][x], y-1)
            if obj[0][x][left] == y: left -= 1

            bottom = bisect.bisect_left(obj[1][y], x+1)
            top = bisect.bisect_left(obj[1][y], x-1)
            if obj[1][y][top] == x: top -= 1

            #print(left, right, top, bottom)
            #print(obj[0][x][left], obj[0][x][right], obj[1][y][top], obj[1][y][bottom])
            left, right, top, bottom = obj[0][x][left], obj[0][x][right], obj[1][y][top], obj[1][y][bottom]

            if x not in fill[0]: fill[0][x] = []
            if y not in fill[1]: fill[1][y] = []
            fill[0][x].append([left, right])
            fill[1][y].append([top, bottom])
        
        for wall in walls:
            x, y = wall
            if x not in fill[0]: fill[0][x] = []
            if y not in fill[1]: fill[1][y] = []
            fill[0][x].append([y, y])
            fill[1][y].append([x, x])

        for row in fill[0]:
            # print(row, fill[0][row])
            merge(fill[0], row)
            # print(row, fill[0][row])

        
        for col in fill[1]:
            merge(fill[1], col)
            # print(col, fill[1][col])

        
        cnt = [[0 for _ in range(n)] for _ in range(m)]
        for row in fill[0]:
            for start, end in fill[0][row]:
                for index in range(start, end+1):
                    if 0 <= index < len(cnt[row]):
                        cnt[row][index] = 1
        
        for col in fill[1]:
            for start, end in fill[1][col]:
                for index in range(start, end+1):
                    if 0 <= index < len(cnt):
                        cnt[index][col] = 1

        return (m * n) - sum(sum(row) for row in cnt)
