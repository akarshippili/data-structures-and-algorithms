from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.arr = SortedList()
        self.cnt = 0
        

    def add(self, left: int, right: int) -> None:
        new = [left, right]
        index = self.arr.bisect_left(new)
        # print(new, index)

        if(0 <= index-1 and self.arr[index-1][-1] >= left):
            self.cnt -= self.arr[index-1][-1] - self.arr[index-1][0] + 1
            self.arr[index-1][-1] = max(self.arr[index-1][-1], right)

            temp = []
            temp_index = index
            while(temp_index < len(self.arr) and self.arr[index-1][-1] >= self.arr[temp_index][0]):
                temp.append(self.arr[temp_index])
                self.cnt -= self.arr[temp_index][-1] - self.arr[temp_index][0] + 1
                temp_index += 1
            
            if(temp): self.arr[index-1][-1] = max(self.arr[index-1][-1], temp[-1][-1])
            self.cnt += self.arr[index-1][-1] - self.arr[index-1][0] + 1
            index = 0
            while(index < len(temp)):
                self.arr.discard(temp[index])
                index += 1
        
        else:
            self.arr.add(new)

            temp = []
            temp_index = index + 1
            while(temp_index < len(self.arr) and self.arr[index][-1] >= self.arr[temp_index][0]):
                temp.append(self.arr[temp_index])
                self.cnt -= self.arr[temp_index][-1] - self.arr[temp_index][0] + 1
                temp_index += 1

            if(temp): self.arr[index][-1] = max(self.arr[index][-1], temp[-1][-1])
            self.cnt += self.arr[index][-1] - self.arr[index][0] + 1

            index = 0
            while(index < len(temp)):
                self.arr.discard(temp[index])
                index += 1


        # print(self.arr, self.cnt)        

    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
