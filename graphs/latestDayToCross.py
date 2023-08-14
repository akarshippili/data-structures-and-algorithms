from UnionFind.EquationsPossible import UnionFind


class Solution:
    def latestDayToCross(self, row, col, cells):

        lands = set()   
        tops = set()
        bottoms = set()

        uf = UnionFind(row*col)
        dir = [[-1 ,0], [0, 1], [1, 0], [0, -1]]

        def add_node(row_index, col_index):
            lands.add((row_index, col_index))
            if(row_index == 1): tops.add((row_index, col_index))
            if(row_index == row): bottoms.add((row_index, col_index))
            
            for dx, dy in dir:
                newx, newy = row_index + dx, col_index + dy
                if((newx, newy) not in lands): continue
                uf.merge((row_index-1) * col + col_index -1, (newx-1) * col + newy -1)

        def connected():
            for top_cell in tops:
                _, top = top_cell
                for bottom_cell in bottoms:
                    _, bottom = bottom_cell
                    if(uf.connected(top-1, col*(row-1) + bottom-1)): 
                        return True
            
            return False
        
        low = 0
        high = row*col -1
        # prev = row*col

        while(low < high):
            mid = low + (high - low + 1)//2
            for index in range(row*col-1, mid-1, -1): uf.add((index // col) + 1, (index % col) + 1)
            # prev = mid

            if(connected()): low = mid
            else: high = mid-1        
        return low


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        lands = set()   
        tops = set()
        bottoms = set()

        uf = UnionFind(row*col)
        dir = [[-1 ,0], [0, 1], [1, 0], [0, -1]]

        def add_node(cell):
            row_index, col_index = cell
            lands.add((row_index, col_index))
            if(row_index == 1): tops.add((row_index, col_index))
            if(row_index == row): bottoms.add((row_index, col_index))
            
            for dx, dy in dir:
                newx, newy = row_index + dx, col_index + dy
                if((newx, newy) not in lands): continue
                uf.merge((row_index-1) * col + col_index -1, (newx-1) * col + newy -1)

        def connected():
            # print(tops, bottoms)
            for top_cell in tops:
                _, top = top_cell
                for bottom_cell in bottoms:
                    _, bottom = bottom_cell
                    if(uf.connected(top-1, col*(row-1) + bottom-1)): 
                        return True
            
            return False
        
        low = 0
        high = row*col -1
        # prev = row*col

        while(low < high):
            mid = low + (high - low + 1)//2
            print(low, high, mid)

            for index in range(row*col-1, mid-1, -1):
                # print(index, ((index // col) + 1, (index % col) + 1))
                # uf.merge((index // col) + 1, (index % col) + 1)
                # uf.merge(cells[index][0], cells[index][1])
                print(index, cells[index])
                add_node(cells[index])                
                
            print(uf.idx, connected())
            if(connected()): low = mid
            else: high = mid-1        
        
        print(low, high)
        return low